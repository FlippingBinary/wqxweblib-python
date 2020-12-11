from yattag import Doc, indent

class Measure:
  __measureUnitCode: str # required, constrained
  __measureValue: str # required

  @property
  def measureUnitCode(self) -> str:
    return self.__measureUnitCode
  @measureUnitCode.setter
  def measureUnitCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'measureUnitCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'measureUnitCode' is required.")
    self.__measureUnitCode = val

  @property
  def measureValue(self) -> str:
    return self.__measureValue
  @measureValue.setter
  def measureValue(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'measureValue' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'measureValue' is required.")
    self.__measureValue = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    line('MeasureValue', self.__measureValue)
    line('MeasureUnitCode', self.__measureUnitCode)
    return indent(doc.getvalue(), indentation = ' '*2)
