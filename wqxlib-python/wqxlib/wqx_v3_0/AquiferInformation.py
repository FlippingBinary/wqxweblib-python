from yattag import Doc, indent
from .SimpleContent import *
from ..common import WQXException

class AquiferInformation:
  """Identifies the procedures, processes, and references required to determine the methods used to obtain a result."""

  __localAquiferCode: LocalAquiferCode
  __localAquiferCodeContext: LocalAquiferCodeContext
  __localAquiferName: LocalAquiferName
  __localAquiferDescriptionText: LocalAquiferDescriptionText

  def __init__(self):
    self.__localAquiferCode = None
    self.__localAquiferCodeContext = None
    self.__localAquiferName = None
    self.__localAquiferDescriptionText = None

  @property
  def localAquiferCode(self) -> LocalAquiferCode:
    return self.__localAquiferCode
  @localAquiferCode.setter
  def localAquiferCode(self, val:LocalAquiferCode) -> None:
    self.__localAquiferCode = LocalAquiferCode(val)

  @property
  def localAquiferCodeContext(self) -> LocalAquiferCodeContext:
    return self.__localAquiferCodeContext
  @localAquiferCodeContext.setter
  def localAquiferCodeContext(self, val:LocalAquiferCodeContext) -> None:
    self.__localAquiferCodeContext = LocalAquiferCodeContext(val)

  @property
  def localAquiferName(self) -> LocalAquiferName:
    return self.__localAquiferName
  @localAquiferName.setter
  def localAquiferName(self, val:LocalAquiferName) -> None:
    self.__localAquiferName = LocalAquiferName(val)

  @property
  def localAquiferDescriptionText(self) -> LocalAquiferDescriptionText:
    return self.__localAquiferDescriptionText
  @localAquiferDescriptionText.setter
  def localAquiferDescriptionText(self, val:LocalAquiferDescriptionText) -> None:
    self.__localAquiferDescriptionText = None if val is None else LocalAquiferDescriptionText(val)

  def generateXML(self):
    if self.__localAquiferCode is None:
      WQXException("Attribute 'localAquiferCode' is required.")
    if self.__localAquiferCodeContext is None:
      WQXException("Attribute 'localAquiferCodeContext' is required.")
    if self.__localAquiferName is None:
      WQXException("Attribute 'localAquiferName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('LocalAquiferCode', self.__localAquiferCode)
    line('LocalAquiferCodeContext', self.__localAquiferCodeContext)
    line('LocalAquiferName', self.__localAquiferName)
    if self.__localAquiferDescriptionText is not None:
      line('LocalAquiferDescriptionText', self.__localAquiferDescriptionText)

    return indent(doc.getvalue(), indentation = ' '*2)
