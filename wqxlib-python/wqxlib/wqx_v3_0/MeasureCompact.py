from yattag import Doc, indent
from .SimpleContent import MeasureValue, MeasureUnitCode
from ..common import WQXException

class MeasureCompact:
  """Identifies only the value and the associated units of measure for measuring the observation or analytical result value."""
  __measureUnitCode: MeasureUnitCode
  __measureValue: MeasureValue

  def __init__(self):
    self.__measureUnitCode = None
    self.__measureValue = None

  @property
  def measureUnitCode(self) -> MeasureUnitCode:
    return self.__measureUnitCode
  @measureUnitCode.setter
  def measureUnitCode(self, val:MeasureUnitCode) -> None:
    self.__measureUnitCode = None if val is None else MeasureUnitCode(val)

  @property
  def measureValue(self) -> MeasureValue:
    return self.__measureValue
  @measureValue.setter
  def measureValue(self, val:MeasureValue) -> None:
    self.__measureValue = MeasureValue(val)

  def generateXML(self):
    if self.__measureUnitCode is None:
      raise WQXException("Attribute 'measureUnitCode' is required.")
    if self.__measureValue is None:
      raise WQXException("Attribute 'measureValue' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MeasureValue', self.__measureValue)
    line('MeasureUnitCode', self.__measureUnitCode)

    return doc.getvalue()
