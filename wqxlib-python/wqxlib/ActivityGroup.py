from typing import List
from yattag import Doc, indent
from .WQXException import WQXException

class ActivityGroup:
  __activityGroupIdentifier: str # required
  __activityGroupName: str # optional
  __activityGroupTypeCode: str # optional, constrained
  __activityIdentifier: List[str] # 2 or more

  def __init__(self):
    self.__activityGroupName = None
    self.__activityGroupTypeCode = None
    self.__activityIdentifier = []

  @property
  def activityGroupIdentifier(self) -> str:
    return self.__activityGroupIdentifier
  @activityGroupIdentifier.setter
  def activityGroupIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'activityGroupIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'activityGroupIdentifier' is required.")
    self.__activityGroupIdentifier = val

  @property
  def activityGroupName(self) -> str:
    return self.__activityGroupName
  @activityGroupName.setter
  def activityGroupName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'activityGroupName' must be a string, if provided.")
    self.__activityGroupName = val

  @property
  def activityGroupTypeCode(self) -> str:
    return self.__activityGroupTypeCode
  @activityGroupTypeCode.setter
  def activityGroupTypeCode(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'activityGroupTypeCode' must be a string, if provided.")
    self.__activityGroupTypeCode = val

  @property
  def activityIdentifier(self) -> List[str]:
    return self.__activityIdentifier
  @activityIdentifier.setter
  def activityIdentifier(self, val:List[str]) -> None:
    if not isinstance(val, list) or len(list) < 2:
      raise TypeError("Property 'activityIdentifier' must be a list of 2 or more strings.")
    for i in val:
      if not isinstance(i, str):
        raise TypeError("Property 'activityIdentifier must contain only str objects.")
    self.__activityIdentifier = val

  def generateXML(self):
    if self.__activityGroupIdentifier is None:
      raise WQXException("Property 'activityGroupIdentifier' is required.")
    if self.__activityIdentifier is None or len(self.__activityIdentifier) < 2:
      raise WQXException("Property 'activityIdentifier' must be a list of 2 or more strings.")

    doc, tag, text, line = Doc().ttl()

    line('ActivityGroupIdentifier', self.__activityGroupIdentifier)
    if self.__activityGroupName is not None:
      line('ActivityGroupName', self.__activityGroupName)
    if self.__activityGroupTypeCode is not None:
      line('ActivityGroupTypeCode', self.__activityGroupTypeCode)
    for x in self.__activityIdentifier:
      doc.asis(x.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)
