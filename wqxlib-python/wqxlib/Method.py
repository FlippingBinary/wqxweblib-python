from yattag import Doc, indent
from .WQXException import WQXException

class Method:
  __methodDescriptionText: str # optional
  __methodIdentifier: str # required
  __methodIdentifierContext: str # required
  __methodName: str # required
  __methodQuantifierTypeName: str # optional

  def __init__(self):
    self.__methodDescriptionText = None
    self.__methodQuantifierTypeName = None

  @property
  def methodDescriptionText(self) -> str:
    return self.__methodDescriptionText
  @methodDescriptionText.setter
  def methodDescriptionText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'methodDescriptionText' must be a string, if provided.")
    self.__methodDescriptionText = val

  @property
  def methodIdentifier(self) -> str:
    return self.__methodIdentifier
  @methodIdentifier.setter
  def methodIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'methodIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'methodIdentifier' is required.")
    self.__methodIdentifier = val

  @property
  def methodIdentifierContext(self) -> str:
    return self.__methodIdentifierContext
  @methodIdentifierContext.setter
  def methodIdentifierContext(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'methodIdentifierContext' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'methodIdentifierContext' is required.")
    self.__methodIdentifierContext = val

  @property
  def methodName(self) -> str:
    return self.__methodName
  @methodName.setter
  def methodName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'methodName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'methodName' is required.")
    self.__methodName = val

  @property
  def methodQuantifierTypeName(self) -> str:
    return self.__methodQuantifierTypeName
  @methodQuantifierTypeName.setter
  def methodQuantifierTypeName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'methodQuantifierTypeName' must be a string, if provided.")
    self.__methodQuantifierTypeName = val

  def generateXML(self):
    if self.__methodIdentifier is None:
      raise WQXException("Property 'methodIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MethodIdentifier', self.__methodIdentifier)
    line('MethodIdentifierContext', self.__methodIdentifierContext)
    line('MethodName', self.__methodName)
    if self.__methodQuantifierTypeName is not None:
      line('MethodQuantifierTypeName', self.__methodQuantifierTypeName)
    if self.__methodDescriptionText is not None:
      line('MethodDescriptionText', self.__methodDescriptionText)

    return indent(doc.getvalue(), indentation = ' '*2)
