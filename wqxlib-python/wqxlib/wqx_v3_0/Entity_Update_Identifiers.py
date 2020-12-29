from ..common import WQXException
from .SimpleContent import (
  NewIdentifier,
  OldIdentifier,
  OrganizationIdentifier
)
from typing import List
from yattag import Doc

class IdentifierUpdate:
  """Allows a Project Identifier to be changed."""

  __oldIdentifier: OldIdentifier
  __newIdentifier: NewIdentifier

  def __init__(self, o=None, *,
    oldIdentifier:OldIdentifier = None,
    newIdentifier:NewIdentifier = None
  ):
    if isinstance(o, IdentifierUpdate):
      # Assign attributes from object without typechecking
      self.__oldIdentifier = o.oldIdentifier
      self.__newIdentifier = o.newIdentifier
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.oldIdentifier = o.get('oldIdentifier', default = None)
      self.newIdentifier = o.get('newIdentifier', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.oldIdentifier = oldIdentifier
      self.newIdentifier = newIdentifier

  @property
  def oldIdentifier(self) -> OldIdentifier:
    return self.__oldIdentifier
  @oldIdentifier.setter
  def oldIdentifier(self, val:OldIdentifier) -> None:
    self.__oldIdentifier = None if val is None else OldIdentifier(val)

  @property
  def newIdentifier(self) -> NewIdentifier:
    return self.__newIdentifier
  @newIdentifier.setter
  def newIdentifier(self, val:NewIdentifier) -> None:
    self.__newIdentifier = None if val is None else NewIdentifier(val)

  def generateXML(self, name = 'IdentifierUpdate'):
    doc, tag, text, line = Doc().ttl()

    with tag(name):
      if self.__oldIdentifier is None:
        raise WQXException("Attribute 'oldIdentifier' is required.")
      line('OldIdentifier', self.__oldIdentifier)
      if self.__newIdentifier is None:
        raise WQXException("Attribute 'newIdentifier' is required.")
      line('NewIdentifier', self.__newIdentifier)

    return doc.getvalue()

class UpdateIdentifiers:
  """Allows a set of identifiers to be changed."""

  __organizationIdentifier: OrganizationIdentifier
  __projectIdentifierUpdate: List[IdentifierUpdate]
  __monitoringLocationIdentifierUpdate: List[IdentifierUpdate]
  __indexIdentifierUpdate: List[IdentifierUpdate]
  __activityIdentifierUpdate: List[IdentifierUpdate]
  __activityGroupIdentifierUpdate: List[IdentifierUpdate]

  def __init__(self):
    self.__organizationIdentifier = None
    self.__projectIdentifierUpdate = []
    self.__monitoringLocationIdentifierUpdate = []
    self.__indexIdentifierUpdate = []
    self.__activityIdentifierUpdate = []
    self.__activityGroupIdentifierUpdate = []

  @property
  def organizationIdentifier(self) -> OrganizationIdentifier:
    return self.__organizationIdentifier
  @organizationIdentifier.setter
  def organizationIdentifier(self, val:OrganizationIdentifier) -> None:
    self.__organizationIdentifier = OrganizationIdentifier(val)

  @property
  def projectIdentifierUpdate(self) -> List[IdentifierUpdate]:
    return self.__projectIdentifierUpdate
  @projectIdentifierUpdate.setter
  def projectIdentifierUpdate(self, val: List[IdentifierUpdate]) -> None:
    if val is None:
      self.__projectIdentifierUpdate = []
    elif isinstance(val, list):
      r:List[IdentifierUpdate] = []
      for x in val:
        r.append(IdentifierUpdate(x))
      self.__projectIdentifierUpdate = r
    else:
      self.__projectIdentifierUpdate = [IdentifierUpdate(val)]

  @property
  def monitoringLocationIdentifierUpdate(self) -> List[IdentifierUpdate]:
    return self.__monitoringLocationIdentifierUpdate
  @monitoringLocationIdentifierUpdate.setter
  def monitoringLocationIdentifierUpdate(self, val: List[IdentifierUpdate]) -> None:
    if val is None:
      self.__monitoringLocationIdentifierUpdate = []
    elif isinstance(val, list):
      r:List[IdentifierUpdate] = []
      for x in val:
        r.append(IdentifierUpdate(x))
      self.__monitoringLocationIdentifierUpdate = r
    else:
      self.__monitoringLocationIdentifierUpdate = [IdentifierUpdate(val)]

  @property
  def indexIdentifierUpdate(self) -> List[IdentifierUpdate]:
    return self.__indexIdentifierUpdate
  @indexIdentifierUpdate.setter
  def indexIdentifierUpdate(self, val: List[IdentifierUpdate]) -> None:
    if val is None:
      self.__indexIdentifierUpdate = []
    elif isinstance(val, list):
      r:List[IdentifierUpdate] = []
      for x in val:
        r.append(IdentifierUpdate(x))
      self.__indexIdentifierUpdate = r
    else:
      self.__indexIdentifierUpdate = [IdentifierUpdate(val)]

  @property
  def activityIdentifierUpdate(self) -> List[IdentifierUpdate]:
    return self.__activityIdentifierUpdate
  @activityIdentifierUpdate.setter
  def activityIdentifierUpdate(self, val: List[IdentifierUpdate]) -> None:
    if val is None:
      self.__activityIdentifierUpdate = []
    elif isinstance(val, list):
      r:List[IdentifierUpdate] = []
      for x in val:
        r.append(IdentifierUpdate(x))
      self.__activityIdentifierUpdate = r
    else:
      self.__activityIdentifierUpdate = [IdentifierUpdate(val)]

  @property
  def activityGroupIdentifierUpdate(self) -> List[IdentifierUpdate]:
    return self.__activityGroupIdentifierUpdate
  @activityGroupIdentifierUpdate.setter
  def activityGroupIdentifierUpdate(self, val: List[IdentifierUpdate]) -> None:
    if val is None:
      self.__activityGroupIdentifierUpdate = []
    elif isinstance(val, list):
      r:List[IdentifierUpdate] = []
      for x in val:
        r.append(IdentifierUpdate(x))
      self.__activityGroupIdentifierUpdate = r
    else:
      self.__activityGroupIdentifierUpdate = [IdentifierUpdate(val)]

  def generateXML(self, name = 'UpdateIdentifiers'):
    doc, tag, text, line = Doc().ttl()

    with tag(name):
      if self.__organizationIdentifier is None:
        raise WQXException("Attribute 'organizationIdentifier' is required.")
      line('OrganizationIdentifier', self.__organizationIdentifier)
      for x in self.__projectIdentifierUpdate:
        doc.asis(x.generateXML('ProjectIdentifierUpdate'))
      for x in self.__monitoringLocationIdentifierUpdate:
        doc.asis(x.generateXML('MonitoringLocationIdentifierUpdate'))
      for x in self.__indexIdentifierUpdate:
        doc.asis(x.generateXML('IndexIdentifierUpdate'))
      for x in self.__activityIdentifierUpdate:
        doc.asis(x.generateXML('ActivityIdentifierUpdate'))
      for x in self.__activityGroupIdentifierUpdate:
        doc.asis(x.generateXML('ActivityGroupIdentifierUpdate'))

    return doc.getvalue()
