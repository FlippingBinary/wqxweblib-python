from yattag import Doc, indent
from .SimpleContent import *

class Telephonic:
  """An identification of a telephone connection."""

  __telephoneNumberText: TelephoneNumberText
  __telephoneNumberTypeName: TelephoneNumberTypeName
  __telephoneExtensionNumberText: TelephoneExtensionNumberText

  def __init__(self):
    self.__telephoneNumberText = None
    self.__telephoneNumberTypeName = None
    self.__telephoneExtensionNumberText = None

  @property
  def telephoneNumberText(self) -> TelephoneNumberText:
    return self.__telephoneNumberText
  @telephoneNumberText.setter
  def telephoneNumberText(self, val:TelephoneNumberText) -> None:
    self.__telephoneNumberText = None if val is None else TelephoneNumberText(val)

  @property
  def telephoneNumberTypeName(self) -> TelephoneNumberTypeName:
    return self.__telephoneNumberTypeName
  @telephoneNumberTypeName.setter
  def telephoneNumberTypeName(self, val:TelephoneNumberTypeName) -> None:
    self.__telephoneNumberTypeName = None if val is None else TelephoneNumberTypeName(val)

  @property
  def telephoneExtensionNumberText(self) -> TelephoneExtensionNumberText:
    return self.__telephoneExtensionNumberText
  @telephoneExtensionNumberText.setter
  def telephoneExtensionNumberText(self, val:TelephoneExtensionNumberText) -> None:
    self.__telephoneExtensionNumberText = None if val is None else TelephoneExtensionNumberText(val)

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__telephoneNumberText is not None:
      line('TelephoneNumberText', self.__telephoneNumberText)
    if self.__telephoneNumberTypeName is not None:
      line('TelephoneNumberTypeName', self.__telephoneNumberTypeName)
    if self.__telephoneExtensionNumberText is not None:
      line('TelephoneExtensionNumberText', self.__telephoneExtensionNumberText)

    return doc.getvalue()
