from enum import Enum
from yattag import Doc, indent
from .wqx_v3_0.WQX import WQX
from .wqx_v3_0.WQX_Update_Identifiers import WQXUpdateIdentifiers
from .wqx_v3_0.WQX_Delete import WQXDelete
from .common import WQXException

class OperationType( Enum ):
  UPDATE_INSERT = 'Update-Insert'
  DELETE = 'Delete'

class Payload:
  __operation: OperationType
  __wqx: WQX
  __wqxUpdateIdentifiers: WQXUpdateIdentifiers
  __wqxDelete: WQXDelete

  def __init__(self,
    operation = None,
    wqx = None,
    wqxUpdateIdentifiers = None,
    wqxDelete = None
  ):
    self.__operation = operation
    self.__wqx = wqx
    self.__wqxUpdateIdentifiers = wqxUpdateIdentifiers
    self.__wqxDelete = wqxDelete

  @property
  def operation(self) -> OperationType:
    return self.__operation
  @operation.setter
  def operation(self, val:OperationType) -> None:
    self.__operation = OperationType(val)

  @property
  def wqx(self) -> WQX:
    return self.__wqx
  @wqx.setter
  def wqx(self, val:WQX) -> None:
    if val is not None and not isinstance(val, WQX):
      raise WQXException("Attribute 'wqx' must be a WQX object, if provided.")
    self.__wqx = val

  @property
  def wqxUpdateIdentifiers(self) -> WQXUpdateIdentifiers:
    return self.__wqxUpdateIdentifiers
  @wqxUpdateIdentifiers.setter
  def wqxUpdateIdentifiers(self, val:WQXUpdateIdentifiers) -> None:
    if val is not None and not isinstance(val, WQXUpdateIdentifiers):
      raise WQXException("Attribute 'wqxUpdateIdentifiers' must be a WQXUpdateIdentifiers object, if provided.")
    self.__wqxUpdateIdentifiers = val

  @property
  def wqxDelete(self) -> WQXDelete:
    return self.__wqxDelete
  @wqxDelete.setter
  def wqxDelete(self, val:WQXDelete) -> None:
    if val is not None and not isinstance(val, WQXDelete):
      raise WQXException("Attribute 'wqxDelete' must be a WQXDelete object, if provided.")
    self.__wqxDelete

  def generateXML(self, name:str = 'Payload') -> str:
    if self.__operation is None:
      raise WQXException("Attribute 'operation' is required.")
    if self.__operation == OperationType.UPDATE_INSERT:
      if self.__wqxDelete is not None:
        raise WQXException("Attribute 'wqxDelete' must be set to None for 'Update-Insert' operation.")
      if self.__wqx is None and self.__wqxUpdateIdentifiers is None:
        raise WQXException("One of attributes 'wqx' or 'wqxUpdateIdentifiers' are required for 'Update-Insert' operation.")
      if self.__wqx is not None and self.__wqxUpdateIdentifiers is not None:
        raise WQXException("One of attributes 'wqx' or 'wqxUpdateIdentifiers' must be set to None for 'Update-Insert' operation.")
    if self.__operation == OperationType.DELETE:
      if self.__wqx is not None:
        raise WQXException("Attribute 'wqx' must be set to None for 'Delete' operation.")
      if self.__wqxUpdateIdentifiers is not None:
        raise WQXException("Attribute 'wqxUpdateIdentifiers' must be set to None for 'Delete' operation.")
      if self.__wqxDelete is None:
        raise WQXException("Attribute 'wqxDelete' is required for 'Delete' operation.")

    doc, tag, text, line = Doc().ttl()

    with tag(name, ('Operation', self.__operation)):
      if self.__operation == OperationType.UPDATE_INSERT:
        if self.__wqx is not None:
          doc.asis(self.__wqx.generateXML('WQX'))
        elif self.__wqxUpdateIdentifiers is not None:
          doc.asis(self.__wqxUpdateIdentifiers.generateXML('WQXUpdateIdentifiers'))
      elif self.__operation == OperationType.DELETE:
        doc.asis(self.__wqxDelete.generateXML('WQXDelete'))

    return doc.getvalue()