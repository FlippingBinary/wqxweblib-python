from yattag import Doc, indent
from .SimpleContent import BiasValue, ConfidenceIntervalValue, LowerConfidenceLimitValue, PrecisionValue, UpperConfidenceLimitValue

class DataQuality:
  """The quantitative statistics and qualitative descriptors that are used to interpret the degree of acceptability or utility of data to the user."""

  __precisionValue: PrecisionValue # optional
  __biasValue: BiasValue # optional
  __confidenceIntervalValue: ConfidenceIntervalValue # optional
  __upperConfidenceLimitValue: UpperConfidenceLimitValue # optional
  __lowerConfidenceLimitValue: LowerConfidenceLimitValue # optional
  
  def __init__(self):
    self.__precisionValue = None
    self.__biasValue = None
    self.__confidenceIntervalValue = None
    self.__upperConfidenceLimitValue = None
    self.__lowerConfidenceLimitValue = None

  @property
  def precisionValue(self) -> PrecisionValue:
    return self.__precisionValue
  @precisionValue.setter
  def precisionValue(self, val:PrecisionValue) -> None:
    self.__precisionValue = None if val is None else PrecisionValue(val)

  @property
  def biasValue(self) -> BiasValue:
    return self.__biasValue
  @biasValue.setter
  def biasValue(self, val:BiasValue) -> None:
    self.__biasValue = None if val is None else BiasValue(val)

  @property
  def confidenceIntervalValue(self) -> ConfidenceIntervalValue:
    return self.__confidenceIntervalValue
  @confidenceIntervalValue.setter
  def confidenceIntervalValue(self, val:ConfidenceIntervalValue) -> None:
    self.__confidenceIntervalValue = None if val is None else ConfidenceIntervalValue(val)

  @property
  def upperConfidenceLimitValue(self) -> UpperConfidenceLimitValue:
    return self.__upperConfidenceLimitValue
  @upperConfidenceLimitValue.setter
  def upperConfidenceLimitValue(self, val:UpperConfidenceLimitValue) -> None:
    self.__upperConfidenceLimitValue = None if val is None else UpperConfidenceLimitValue(val)

  @property
  def lowerConfidenceLimitValue(self) -> LowerConfidenceLimitValue:
    return self.__lowerConfidenceLimitValue
  @lowerConfidenceLimitValue.setter
  def lowerConfidenceLimitValue(self, val:LowerConfidenceLimitValue) -> None:
    self.__lowerConfidenceLimitValue = None if val is None else LowerConfidenceLimitValue(val)

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__precisionValue is not None:
      line('PrecisionValue', self.__precisionValue)
    if self.__biasValue is not None:
      line('BiasValue', self.__biasValue)
    if self.__confidenceIntervalValue is not None:
      line('ConfidenceIntervalValue', self.__confidenceIntervalValue)
    if self.__upperConfidenceLimitValue is not None:
      line('UpperConfidenceLimitValue', self.__upperConfidenceLimitValue)
    if self.__lowerConfidenceLimitValue is not None:
      line('LowerConfidenceLimitValue', self.__lowerConfidenceLimitValue)

    return indent(doc.getvalue(), indentation = ' '*2)
