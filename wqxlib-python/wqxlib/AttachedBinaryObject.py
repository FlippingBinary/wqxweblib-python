from yattag import Doc, indent
from .WQXException import WQXException

class AttachedBinaryObject:
  __binaryObjectFileName: str # required
  __binaryObjectFileTypeCode: str # required

  @property
  def binaryObjectFileName(self) -> str:
    return self.__binaryObjectFileName
  @binaryObjectFileName.setter
  def binaryObjectFileName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'binaryObjectFileName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'binaryObjectFileName' is required.")
    self.__binaryObjectFileName = val

  @property
  def binaryObjectFileTypeCode(self) -> str:
    return self.__binaryObjectFileTypeCode
  @binaryObjectFileTypeCode.setter
  def binaryObjectFileTypeCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'binaryObjectFileTypeCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'binaryObjectFileTypeCode' is required.")
    self.__binaryObjectFileTypeCode = val

  def generateXML(self):
    if self.__binaryObjectFileName is None:
      raise WQXException("Property 'binaryObjectFileName' is required.")
    if self.__binaryObjectFileTypeCode is None:
      raise WQXException("Property 'binaryObjectFileTypeCode' is required.")
    doc, tag, text, line = Doc().ttl()
    line('BinaryObjectFileName', self.__binaryObjectFileName)
    line('BinaryObjectFileTypeCode', self.__binaryObjectFileTypeCode)
    return indent(doc.getvalue(), indentation = ' '*2)
