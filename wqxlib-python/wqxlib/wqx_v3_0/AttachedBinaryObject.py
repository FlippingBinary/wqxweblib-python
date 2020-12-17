from yattag import Doc, indent
from .SimpleContent import (
  BinaryObjectFileName,
  BinaryObjectFileTypeCode
)
from ..WQXException import WQXException

class AttachedBinaryObject:
  """Reference document, image, photo, GIS data layer, laboratory material or other electronic object attached within a data exchange, as well as information used to describe the object."""
  __binaryObjectFileName: BinaryObjectFileName
  __binaryObjectFileTypeCode: BinaryObjectFileTypeCode

  @property
  def binaryObjectFileName(self) -> BinaryObjectFileName:
    return self.__binaryObjectFileName
  @binaryObjectFileName.setter
  def binaryObjectFileName(self, val:BinaryObjectFileName) -> None:
    self.__binaryObjectFileName = BinaryObjectFileName(val)

  @property
  def binaryObjectFileTypeCode(self) -> BinaryObjectFileTypeCode:
    return self.__binaryObjectFileTypeCode
  @binaryObjectFileTypeCode.setter
  def binaryObjectFileTypeCode(self, val:BinaryObjectFileTypeCode) -> None:
    self.__binaryObjectFileTypeCode = BinaryObjectFileTypeCode(val)

  def generateXML(self):
    if self.__binaryObjectFileName is None:
      raise WQXException("Attribute 'binaryObjectFileName' is required.")
    if self.__binaryObjectFileTypeCode is None:
      raise WQXException("Attribute 'binaryObjectFileTypeCode' is required.")

    doc, tag, text, line = Doc().ttl()

    line('BinaryObjectFileName', self.__binaryObjectFileName)
    line('BinaryObjectFileTypeCode', self.__binaryObjectFileTypeCode)

    return indent(doc.getvalue(), indentation = ' '*2)
