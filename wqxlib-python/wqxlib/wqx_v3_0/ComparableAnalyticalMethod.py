from yattag import Doc, indent
from .SimpleContent import (
  MethodIdentifier,
  MethodIdentifierContext,
  MethodModificationText,
)
from ..common import WQXException

class ComparableAnalyticalMethod:
  """Identifies the procedures, processes, and references required to determine the analytical methods used to obtain a result."""

  __methodIdentifier: MethodIdentifier
  __methodIdentifierContext: MethodIdentifierContext
  __methodModificationText: MethodModificationText

  def __init__(self):
    self.__methodIdentifier = None
    self.__methodIdentifierContext = None
    self.__methodModificationText = None

  @property
  def methodIdentifier(self) -> MethodIdentifier:
    return self.__methodIdentifier
  @methodIdentifier.setter
  def methodIdentifier(self, val:MethodIdentifier) -> None:
    self.__methodIdentifier = MethodIdentifier(val)

  @property
  def methodIdentifierContext(self) -> MethodIdentifierContext:
    return self.__methodIdentifierContext
  @methodIdentifierContext.setter
  def methodIdentifierContext(self, val:MethodIdentifierContext) -> None:
    self.__methodIdentifierContext = MethodIdentifierContext(val)

  @property
  def methodModificationText(self) -> MethodModificationText:
    return self.__methodModificationText
  @methodModificationText.setter
  def methodModificationText(self, val:MethodModificationText) -> None:
    self.__methodModificationText = None if val is None else MethodModificationText(val)

  def generateXML(self):
    if self.__methodIdentifier is None:
      raise WQXException("Attribute 'methodIdentifier' is required.")
    if self.__methodIdentifierContext is None:
      raise WQXException("Attribute 'methodIdentifierContext' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MethodIdentifier', self.__methodIdentifier)
    line('MethodIdentifierContext', self.__methodIdentifierContext)
    if self.__methodModificationText is not None:
      line('MethodModificationText', self.__methodModificationText)

    return indent(doc.getvalue(), indentation = ' '*2)
