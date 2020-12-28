from yattag import Doc, indent
from .SimpleContent import (
  FrequencyClassDescriptorCode,
  FrequencyClassDescriptorUnitCode,
  LowerClassBoundValue,
  UpperClassBoundValue
)
from ..common import WQXException

class FrequencyClassInformation:
  """This section allows for the definition of a subgroup of biological communities by life stage, physical attribute, or abnormality to support frequency class studies."""

  __frequencyClassDescriptorCode: FrequencyClassDescriptorCode
  __frequencyClassDescriptorUnitCode: FrequencyClassDescriptorUnitCode
  __lowerClassBoundValue: LowerClassBoundValue
  __upperClassBoundValue: UpperClassBoundValue

  def __init__(self, o=None, *,
    frequencyClassDescriptorCode:FrequencyClassDescriptorCode = None,
    frequencyClassDescriptorUnitCode:FrequencyClassDescriptorUnitCode = None,
    lowerClassBoundValue:LowerClassBoundValue = None,
    upperClassBoundValue:UpperClassBoundValue = None
  ):
    if isinstance(o, FrequencyClassInformation):
      # Assign attributes from object without typechecking
      self.__frequencyClassDescriptorCode = o.frequencyClassDescriptorCode
      self.__frequencyClassDescriptorUnitCode = o.frequencyClassDescriptorUnitCode
      self.__lowerClassBoundValue = o.lowerClassBoundValue
      self.__upperClassBoundValue = o.upperClassBoundValue
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.frequencyClassDescriptorCode = o.get('frequencyClassDescriptorCode', default = None)
      self.frequencyClassDescriptorUnitCode = o.get('frequencyClassDescriptorUnitCode', default = None)
      self.lowerClassBoundValue = o.get('lowerClassBoundValue', default = None)
      self.upperClassBoundValue = o.get('upperClassBoundValue', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.frequencyClassDescriptorCode = frequencyClassDescriptorCode
      self.frequencyClassDescriptorUnitCode = frequencyClassDescriptorUnitCode
      self.lowerClassBoundValue = lowerClassBoundValue
      self.upperClassBoundValue = upperClassBoundValue


  @property
  def frequencyClassDescriptorCode(self) -> FrequencyClassDescriptorCode:
    return self.__frequencyClassDescriptorCode
  @frequencyClassDescriptorCode.setter
  def frequencyClassDescriptorCode(self, val:FrequencyClassDescriptorCode) -> None:
    self.__frequencyClassDescriptorCode = FrequencyClassDescriptorCode(val)

  @property
  def frequencyClassDescriptorUnitCode(self) -> FrequencyClassDescriptorUnitCode:
    return self.__frequencyClassDescriptorUnitCode
  @frequencyClassDescriptorUnitCode.setter
  def frequencyClassDescriptorUnitCode(self, val:FrequencyClassDescriptorUnitCode) -> None:
    self.__frequencyClassDescriptorUnitCode = None if val is None else FrequencyClassDescriptorUnitCode(val)

  @property
  def lowerClassBoundValue(self) -> LowerClassBoundValue:
    return self.__lowerClassBoundValue
  @lowerClassBoundValue.setter
  def lowerClassBoundValue(self, val:LowerClassBoundValue) -> None:
    self.__lowerClassBoundValue = None if val is None else LowerClassBoundValue(val)

  @property
  def upperClassBoundValue(self) -> UpperClassBoundValue:
    return self.__upperClassBoundValue
  @upperClassBoundValue.setter
  def upperClassBoundValue(self, val:UpperClassBoundValue) -> None:
    self.__upperClassBoundValue = None if val is None else UpperClassBoundValue(val)

  def generateXML(self):
    if self.__frequencyClassDescriptorCode is None:
      raise WQXException("Attribute 'frequencyClassDescriptorCode' is required.")

    doc, tag, text, line = Doc().ttl()

    line( 'FrequencyClassDescriptorCode', self.__frequencyClassDescriptorCode)
    if self.__frequencyClassDescriptorUnitCode is not None:
      line('FrequencyClassDescriptorUnitCode', self.__frequencyClassDescriptorUnitCode)
    if self.__lowerClassBoundValue is not None:
      line('LowerClassBoundValue', self.__lowerClassBoundValue)
    if self.__upperClassBoundValue is not None:
      line('UpperClassBoundValue', self.__upperClassBoundValue)

    return doc.getvalue()
