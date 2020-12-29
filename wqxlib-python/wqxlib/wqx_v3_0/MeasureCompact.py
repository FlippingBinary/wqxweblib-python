from yattag import Doc, indent
from .SimpleContent import MeasureValue, MeasureUnitCode
from ..common import WQXException

class MeasureCompact:
  """Identifies only the value and the associated units of measure for measuring the observation or analytical result value."""

  __measureUnitCode: MeasureUnitCode
  __measureValue: MeasureValue

  def __init__(self, o=None, *,
    measureUnitCode:MeasureUnitCode = None,
    measureValue:MeasureValue = None
  ):
    if isinstance(o, MeasureCompact):
      # Assign attributes from object without typechecking
      self.__measureUnitCode = o.measureUnitCode
      self.__measureValue = o.measureValue
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.measureUnitCode = o.get('measureUnitCode', default = None)
      self.measureValue = o.get('measureValue', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.measureUnitCode = measureUnitCode
      self.measureValue = measureValue

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
    self.__measureValue = None if val is None else MeasureValue(val)

  def generateXML(self):
    if self.__measureUnitCode is None:
      raise WQXException("Attribute 'measureUnitCode' is required.")
    if self.__measureValue is None:
      raise WQXException("Attribute 'measureValue' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MeasureValue', self.__measureValue)
    line('MeasureUnitCode', self.__measureUnitCode)

    return doc.getvalue()
