from yattag import Doc, indent
from .SimpleContent import *
from ..WQXException import WQXException

class ActivityGroup:
  """Allows for the grouping of activities."""

  __activityGroupIdentifier: ActivityGroupIdentifier
  __activityGroupName: ActivityGroupName
  __activityGroupTypeCode: ActivityGroupTypeCode
  __activityIdentifier: ActivityIdentifier

  def __init__(self):
    self.__activityGroupIdentifier = None
    self.__activityGroupName = None
    self.__activityGroupTypeCode = None
    self.__activityIdentifier = None

  @property
  def activityGroupIdentifier(self) -> ActivityGroupIdentifier:
    return self.__activityGroupIdentifier
  @activityGroupIdentifier.setter
  def activityGroupIdentifier(self, val:ActivityGroupIdentifier) -> None:
    self.__activityGroupIdentifier = ActivityGroupIdentifier(val)

  @property
  def activityGroupName(self) -> ActivityGroupName:
    return self.__activityGroupName
  @activityGroupName.setter
  def activityGroupName(self, val:ActivityGroupName) -> None:
    self.__activityGroupName = None if val is None else ActivityGroupName(val)

  @property
  def activityGroupTypeCode(self) -> ActivityGroupTypeCode:
    return self.__activityGroupTypeCode
  @activityGroupTypeCode.setter
  def activityGroupTypeCode(self, val:ActivityGroupTypeCode) -> None:
    self.__activityGroupTypeCode = ActivityGroupTypeCode(val)

  @property
  def activityIdentifier(self) -> ActivityIdentifier:
    return self.__activityIdentifier
  @activityIdentifier.setter
  def activityIdentifier(self, val:ActivityIdentifier) -> None:
    self.__activityIdentifier = None if val is None else ActivityIdentifier(val)

  def generateXML(self):
    if self.__activityGroupIdentifier is None:
      WQXException("Attribute 'activityGroupIdentifier' is required.")
    if self.__activityGroupTypeCode is None:
      WQXException("Attribute 'activityGroupTypeCode' is required.")

    doc, tag, text, line = Doc().ttl()

    line('ActivityGroupIdentifier', self.__activityGroupIdentifier)
    if self.__activityGroupName is not None:
      line('ActivityGroupName', self.__activityGroupName)
    line('ActivityGroupTypeCode', self.__activityGroupTypeCode)
    for x in self.__activityIdentifier:
      line('ActivityIdentifier', x)

    return indent(doc.getvalue(), indentation = ' '*2)
