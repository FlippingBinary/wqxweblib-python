from typing import List, Union
from yattag import Doc, indent
from .SimpleContent import MeasureQualifierCode, MeasureUnitCode, ResultMeasureValue
from ..common import WQXException

class Measure:
  """Identifies the value, associated units of measure, and qualifier for measuring the observation or analytical result value."""

  __measureQualifierCode: List[MeasureQualifierCode]
  __measureUnitCode: MeasureUnitCode
  __resultMeasureValue: ResultMeasureValue

  def __init__(self, o=None, *,
    measureQualifierCode:List[MeasureQualifierCode] = None,
    measureUnitCode:MeasureUnitCode = None,
    resultMeasureValue:ResultMeasureValue = None,
  ):
    if isinstance(o, Measure):
      # Assign attributes from object without typechecking
      self.__measureQualifierCode = o.measureQualifierCode
      self.__measureUnitCode = o.measureUnitCode
      self.__resultMeasureValue = o.resultMeasureValue
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.__measureQualifierCode = o.get('measureQualifierCode', default = None)
      self.__measureUnitCode = o.get('measureUnitCode', default = None)
      self.__resultMeasureValue = o.get('resultMeasureValue', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.__measureQualifierCode = measureQualifierCode
      self.__measureUnitCode = measureUnitCode
      self.__resultMeasureValue = resultMeasureValue


  @property
  def measureQualifierCode(self) -> List[MeasureQualifierCode]:
    return self.__measureQualifierCode
  @measureQualifierCode.setter
  def measureQualifierCode(self, val:Union[MeasureQualifierCode,List[MeasureQualifierCode]]) -> None:
    if val is None:
      self.__measureQualifierCode = []
    elif isinstance(val, list):
      r:List[MeasureQualifierCode] = []
      for x in val:
        r.append(MeasureQualifierCode(x))
      self.__measureQualifierCode = r
    else:
      self.__measureQualifierCode = [MeasureQualifierCode(val)]

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
