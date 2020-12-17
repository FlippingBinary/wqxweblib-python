from yattag import Doc, indent
from .SimpleContent import (
  MethodIdentifier,
  MethodIdentifierContext,
  MethodName,
  MethodQualifierTypeName,
  MethodDescriptionText
)
from ..WQXException import WQXException

class ReferenceMethod:
  """Identifies the procedures, processes, and references required to determine the methods used to obtain a result."""

  __methodIdentifier: MethodIdentifier
  __methodIdentifierContext: MethodIdentifierContext
  __methodName: MethodName
  __methodQualifierTypeName: MethodQualifierTypeName
  __methodDescriptionText: MethodDescriptionText

  def __init__(self):
    self.__methodIdentifier = None
    self.__methodIdentifierContext = None
    self.__methodName = None
    self.__methodQualifierTypeName = None
    self.__methodDescriptionText = None

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
  def methodName(self) -> MethodName:
    return self.__methodName
  @methodName.setter
  def methodName(self, val:MethodName) -> None:
    self.__methodName = MethodName(val)

  @property
  def methodQualifierTypeName(self) -> MethodQualifierTypeName:
    return self.__methodQualifierTypeName
  @methodQualifierTypeName.setter
  def methodQualifierTypeName(self, val:MethodQualifierTypeName) -> None:
    self.__methodQualifierTypeName = None if val is None else MethodQualifierTypeName(val)

  @property
  def methodDescriptionText(self) -> MethodDescriptionText:
    return self.__methodDescriptionText
  @methodDescriptionText.setter
  def methodDescriptionText(self, val:MethodDescriptionText) -> None:
    self.__methodDescriptionText = None if val is None else MethodDescriptionText(val)

  def generateXML(self):
    if self.__methodIdentifier is None:
      raise WQXException("Attribute 'MethodIdentifier' is required.")
    if self.__methodIdentifierContext is None:
      raise WQXException("Attribute 'MethodIdentifierContext' is required.")
    if self.__methodName is None:
      raise WQXException("Attribute 'MethodName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MethodIdentifier', self.__methodIdentifier)
    line('MethodIdentifierContext', self.__methodIdentifierContext)
    line('MethodName', self.__methodName)
    if self.__methodQualifierTypeName is not None:
      line('MethodQualifierTypeName', self.__methodQualifierTypeName)
    if self.__methodDescriptionText is not None:
      line('MethodDescriptionText', self.__methodDescriptionText)

    return indent(doc.getvalue(), indentation = ' '*2)
