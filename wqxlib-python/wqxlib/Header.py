from datetime import datetime
from rfc3986 import uri_reference
from typing import List
from yattag import Doc, indent
from .common import WQXException

class Header:
  __author: str
  __organization: str
  __title: str
  __creationTime: datetime
  __comment: str
  __dataService: str
  __contactInfo: str
  __notification: List[uri_reference]
  __sensitivity: str
  __property: dict

  def __init__(self,
    author = None,
    organization = None,
    title = 'WQX',
    creationTime = None,
    comment = None,
    dataService = None,
    contactInfo = None,
    notification = [],
    sensitivity = None,
    property = {}
  ):
    self.__author = author
    self.__organization = organization
    self.__title = title
    if creationTime is None:
      self.__creationTime = datetime.now()
    else:
      self.__creationTime = creationTime
    self.__comment = comment
    self.__dataService = dataService
    self.__contactInfo = contactInfo
    self.__notification = notification
    self.__sensitivity = sensitivity
    self.__property = property

  @property
  def author(self) -> str:
    return self.__author
  @author.setter
  def author(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'author' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'author' is required.")
    self.__author = val

  @property
  def organization(self) -> str:
    return self.__organization
  @organization.setter
  def organization(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'organization' must be a string.")
    if len(val) < 1:
      raise ValueError("Property 'organization is required.")
    self.__organization = val

  @property
  def title(self) -> str:
    return self.__title
  @title.setter
  def title(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'title' must be a string")
    if len(val) < 1:
      raise ValueError("Property 'title' is required.")
    self.__title = val

  @property
  def creationTime(self) -> datetime:
    return self.__creationTime
  @creationTime.setter
  def creationTime(self, val:datetime) -> None:
    if not isinstance(val, datetime):
      raise TypeError("Property 'creationTime' must be a datetime.")
    self.__creationTime = val

  @property
  def comment(self) -> str:
    return self.__comment
  @comment.setter
  def comment(self, val) -> None:
    if val is None or len(val) < 1:
      self.__comment = None
    if not isinstance(val, str):
      raise TypeError("Property 'comment' must be a string, if provided.")
    self.__comment = val

  @property
  def dataService(self) -> str:
    return self.__dataService
  @dataService.setter
  def dataService(self, val) -> None:
    if val is None or len(val) < 1:
      self.__dataService = None
    if not isinstance(val, str):
      raise TypeError("Property 'dataService' must be a string, if provided.")
    self.__dataService = val

  @property
  def contactInfo(self) -> str:
    return self.__contactInfo
  @contactInfo.setter
  def contactInfo(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'contactInfo' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'contactInfo' is required.")
    self.__contactInfo = val

  @property
  def notification(self) -> List[str]:
    return self.__notification
  @notification.setter
  def notification(self, val:List[str]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'notification' must be a list of 0 or more URIs.")
    for x in val:
      if not isinstance(x, str) or not uri_reference(x).is_valid():
        raise TypeError("Property 'notification' must be a list of 0 or more URIs.")
    self.__notification = val

  @property
  def sensitivity(self) -> str:
    return self.__sensitivity
  @sensitivity.setter
  def sensitivity(self, val) -> None:
    if val is None or len(val) < 1:
      self.__sensitivity = None
    if not isinstance(val, str):
      raise TypeError("Property 'sensitivity' must be a string, if provided.")
    self.__sensitivity = val

  @property
  def property(self) -> dict:
    return self.__property
  @property.setter
  def property(self, val:dict) -> None:
    if not None and not isinstance(val, list):
      raise TypeError("Property 'property' must be a dict of 0 or more key/value pairs.")
    self.__property = {} if val is None else val

  def generateXML(self, name:str = 'Header') -> str:
    if self.__author is None:
      raise WQXException("Property 'author' is required.")
    if self.__contactInfo is None:
      raise WQXException("Property 'contactInfo' is required.")
    if self.__organization is None:
      raise WQXException("Property 'organization' is required.")
    if self.__creationTime is None:
      raise WQXException("Attribute 'creationTime' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(name):
      line('Author', self.__author)
      line('Organization', self.__organization)
      line('Title', self.__title)
      line('CreationTime', self.__creationTime.astimezone().replace(microsecond=0).isoformat())
      if self.__comment is not None:
        line('Comment', self.__comment)
      if self.__dataService is not None:
        line('DataService', self.__dataService)
      if self.__contactInfo is not None:
        line('ContactInfo', self.__contactInfo)
      for x in self.__notification:
        line('Notification', x)
      if self.__sensitivity is not None:
        line('Sensitivity', self.__sensitivity)
      for key in self.__property:
        with tag('Property'):
          line('name', key)
          line('value', self.__property[key])

    return doc.getvalue()
