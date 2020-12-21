from yattag import Doc, indent
from .SimpleContent import *
from ..WQXException import WQXException

class ElectronicAddress:
  """A location within a system of worldwide electronic communication where a computer user can access information or receive electronic mail."""

  __electronicAddressText: ElectronicAddressText
  __electronicAddressTypeName: ElectronicAddressTypeName

  def __init__(self):
    self.__electronicAddressText = None
    self.__electronicAddressTypeName = None

  @property
  def electronicAddressText(self) -> ElectronicAddressText:
    return self.__electronicAddressText
  @electronicAddressText.setter
  def electronicAddressText(self, val:ElectronicAddressText) -> None:
    self.__electronicAddressText = None if val is None else ElectronicAddressText(val)

  @property
  def electronicAddressTypeName(self) -> ElectronicAddressTypeName:
    return self.__electronicAddressTypeName
  @electronicAddressTypeName.setter
  def electronicAddressTypeName(self, val:ElectronicAddressTypeName) -> None:
    self.__electronicAddressTypeName = None if val is None else ElectronicAddressTypeName(val)

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    line('ElectronicAddressText', self.__electronicAddressText)
    line('ElectronicAddressTypeName', self.__electronicAddressTypeName)

    return indent(doc.getvalue(), indentation = ' '*2)
