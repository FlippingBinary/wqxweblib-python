from datetime import date
from yattag import Doc, indent
from .WQXException import WQXException

class Resource:
  __resourceCreatorName: str # optional
  __resourceDate: date # required
  __resourceIdentifier: str # required
  __resourcePublisherName: str # optional
  __resourceSubjectText: str # optional
  __resourceTitleName: str # required

  def __init__(self):
    self.__resourceCreatorName = None
    self.__resourcePublisherName = None
    self.__resourceSubjectText = None

  @property
  def resourceCreatorName(self) -> str:
    return self.__resourceCreatorName
  @resourceCreatorName.setter
  def resourceCreatorName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'resourceCreatorName' must be a string, if provided.")
    self.__resourceCreatorName = val

  @property
  def resourceDate(self) -> date:
    return self.__resourceDate
  @resourceDate.setter
  def resourceDate(self, val:date) -> None:
    if not isinstance(val, date):
      raise TypeError("Property 'resourceDate' must be a date object.")
    if len(val) < 1:
      raise TypeError("Property 'resourceDate' is required.")
    self.__resourceDate = val

  @property
  def resourceIdentifier(self) -> str:
    return self.__resourceIdentifier
  @resourceIdentifier.setter
  def resourceIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'resourceIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'resourceIdentifier' is required.")
    self.__resourceIdentifier = val

  @property
  def resourcePublisherName(self) -> str:
    return self.__resourcePublisherName
  @resourcePublisherName.setter
  def resourcePublisherName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'resourcePublisherName' must be a string, if provided.")
    self.__resourcePublisherName = val

  @property
  def resourceSubjectText(self) -> str:
    return self.__resourceSubjectText
  @resourceSubjectText.setter
  def resourceSubjectText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'resourceSubjectText' must be a string, if provided.")
    self.__resourceSubjectText = val

  @property
  def resourceTitleName(self) -> str:
    return self.__resourceTitleName
  @resourceTitleName.setter
  def resourceTitleName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'resourceTitleName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'resourceTitleName' is required.")
    self.__resourceTitleName = val

  def generateXML(self):
    if self.__resourceTitleName is None:
      raise WQXException("Property 'resourceTitleName' is required.")
    if self.__resourceDate is None:
      raise WQXException("Property 'resourceDate' is required.")
    if self.__resourceIdentifier is None:
      raise WQXException("Property 'resourceIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    line('ResourceTitleName', self.__resourceTitleName)
    if self.__resourceCreatorName is not None:
      line('ResourceCreatorName', self.__resourceCreatorName)
    if self.__resourceSubjectText is not None:
      line('ResourceSubjectText', self.__resourceSubjectText)
    if self.__resourcePublisherName is not None:
      line('ResourcePublisherName', self.__resourcePublisherName)
    line('ResourceDate', self.__resourceDate)
    line('ResourceIdentifier', self.__resourceIdentifier)

    return indent(doc.getvalue(), indentation = ' '*2)
