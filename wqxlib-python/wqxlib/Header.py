from datetime import datetime
from yattag import Doc, indent
from .WQXException import WQXException

class Header:
  __author: str # required
  __comment: str # optional
  __contactInfo: str # required
  __creationTime: datetime # required
  __dataService: str # optional
  __notification: str # optional
  __organization: str # required
  __sensitivity: str # optional
  __title: str # required

  def __init__(self):
    self.__comment = None
    self.__creationTime = datetime.now()
    self.__dataService = None
    self.__notification = None
    self.__sensitivity = None
    self.__title = 'WQX'

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
  def creationTime(self) -> datetime:
    return self.__creationTime
  @creationTime.setter
  def creationTime(self, val:datetime) -> None:
    if not isinstance(val, datetime):
      raise TypeError("Property 'creationTime' must be a datetime.")
    self.__creationTime = val

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
  def notification(self) -> str:
    return self.__notification
  @notification.setter
  def notification(self, val) -> None:
    if val is None or len(val) < 1:
      self.__notification = None
    if not isinstance(val, str):
      raise TypeError("Property 'notification' must be a string, if provided.")
    self.__notification = val

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
  def title(self) -> str:
    return self.__title
  @title.setter
  def title(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'title' must be a string")
    if len(val) < 1:
      raise ValueError("Property 'title' is required.")
    self.__title = val

  def generateXML(self):
    if not self.__author:
      raise WQXException("Property 'author' must be set before XML can be generated.")
    if not self.__contactInfo:
      raise WQXException("Property 'contactInfo' must be set before XML can be generated.")
    if not self.__organization:
      raise WQXException("Property 'organization' must be set before XML can be generated.")

    doc, tag, text, line = Doc().ttl()
    line('Author', self.__author)
    line('Organization', self.__organization)
    line('Title', self.__title)
    line('CreationTime', self.__creationTime.astimezone().replace(microsecond=0).isoformat())
    line('ContactInfo', self.__contactInfo)
    if self.__comment is not None:
      line('Comment', self.__comment)
    if self.__dataService is not None:
      line('DataService', self.__dataService)
    line('Notification', self.__notification)
    if self.__sensitivity is not None:
      line('Sensitivity', self.__sensitivity)
    return indent(doc.getvalue(), indentation = ' '*2)
