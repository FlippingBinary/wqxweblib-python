from typing import List
from yattag import Doc, indent
from .SimpleContent import MeasureQualifierCode, MeasureUnitCode, ResultMeasureValue

class Measure:
  """Identifies the value, associated units of measure, and qualifier for measuring the observation or analytical result value."""

  __measureQualifierCode: List[MeasureQualifierCode]
  __measureUnitCode: MeasureUnitCode # required, constrained
  __resultMeasureValue: ResultMeasureValue # required

  @property
  def measureQualifierCode(self) -> List[MeasureQualifierCode]:
    return self.__measureQualifierCode
  @measureQualifierCode.setter
  def measureQualifierCode(self, val:List[MeasureQualifierCode]) -> None:
    self.__measureQualifierCode = None if val is None else List[MeasureQualifierCode](val)

  @property
  def measureUnitCode(self) -> MeasureUnitCode:
    return self.__measureUnitCode
  @measureUnitCode.setter
  def measureUnitCode(self, val:MeasureUnitCode) -> None:
    self.__measureUnitCode = None if val is None else MeasureUnitCode(val)

  @property
  def resultMeasureValue(self) -> ResultMeasureValue:
    return self.__resultMeasureValue
  @resultMeasureValue.setter
  def resultMeasureValue(self, val:ResultMeasureValue) -> None:
    self.__resultMeasureValue = None if val is None else ResultMeasureValue(val)

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__resultMeasureValue is not None:
      line('ResultMeasureValue', self.__resultMeasureValue)
    if self.__measureUnitCode is not None:
      line('MeasureUnitCode', self.__measureUnitCode)
    if self.__measureQualifierCode is not None:
      for x in self.__measureQualifierCode:
        line('MeasureQualifierCode', x)

    return doc.getvalue()
