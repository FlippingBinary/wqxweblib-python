from typing import List
from yattag import Doc, indent
from .SimpleContent import *
from ..common import WQXException

class ProjectIdentifierUpdate:
  """Allows a Project Identifier to be changed."""

  __oldIdentifier: OldIdentifier
  __newIdentifier: NewIdentifier

  def __init__(self, o=None, *,
    oldIdentifier:OldIdentifier = None,
    newIdentifier:NewIdentifier = None
  ):
    if isinstance(o, ProjectIdentifierUpdate):
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
    """This is the old identifier to be replaced."""
    return self.__oldIdentifier
  @oldIdentifier.setter
  def oldIdentifier(self, val:OldIdentifier) -> None:
    if not isinstance(val, OldIdentifier):
      raise WQXException("Attribute 'oldIdentifier' must be an OldIdentifier object.")
    self.__oldIdentifier = val

  @property
  def newIdentifier(self) -> NewIdentifier:
    """This is the new identifier replacing the old identifier."""
    return self.__newIdentifier
  @newIdentifier.setter
  def newIdentifier(self, val:NewIdentifier) -> None:
    if not isinstance(val, NewIdentifier):
      raise WQXException("Attribute 'newIdentifier' must be an NewIdentifier object.")
    self.__newIdentifier = val

  def generateXML(self, name = 'ProjectIdentifierUpdate'):
    if self.__oldIdentifier is None:
      raise WQXException("Attribute 'oldIdentifier' is required.")
    if self.__newIdentifier is None:
      raise WQXException("Attribute 'newIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(name):
      line('OldIdentifier', self.__oldIdentifier)
      line('NewIdentifier', self.__newIdentifier)

    return doc.getvalue()

class MonitoringLocationIdentifierUpdate:
  """Allows a MonitoringLocation Identifier to be changed."""

  __oldIdentifier: OldIdentifier
  __newIdentifier: NewIdentifier

  def __init__(self, old = None, new = None):
    self.__oldIdentifier = old
    self.__newIdentifier = new

  @property
  def oldIdentifier(self) -> OldIdentifier:
    """This is the old identifier to be replaced."""
    return self.__oldIdentifier
  @oldIdentifier.setter
  def oldIdentifier(self, val:OldIdentifier) -> None:
    if not isinstance(val, OldIdentifier):
      raise WQXException("Attribute 'oldIdentifier' must be an OldIdentifier object.")
    self.__oldIdentifier = val

  @property
  def newIdentifier(self) -> NewIdentifier:
    """This is the new identifier replacing the old identifier."""
    return self.__newIdentifier
  @newIdentifier.setter
  def newIdentifier(self, val:NewIdentifier) -> None:
    if not isinstance(val, NewIdentifier):
      raise WQXException("Attribute 'newIdentifier' must be an NewIdentifier object.")
    self.__newIdentifier = val

  def generateXML(self, name = 'MonitoringLocationIdentifierUpdate'):
    if self.__oldIdentifier is None:
      raise WQXException("Attribute 'oldIdentifier' is required.")
    if self.__newIdentifier is None:
      raise WQXException("Attribute 'newIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(name):
      line('OldIdentifier', self.__oldIdentifier)
      line('NewIdentifier', self.__newIdentifier)

    return doc.getvalue()

class IndexIdentifierUpdate:
  """Allows a Index Identifier to be changed."""

  __oldIdentifier: OldIdentifier
  __newIdentifier: NewIdentifier

  def __init__(self, old = None, new = None):
    self.__oldIdentifier = old
    self.__newIdentifier = new

  @property
  def oldIdentifier(self) -> OldIdentifier:
    """This is the old identifier to be replaced."""
    return self.__oldIdentifier
  @oldIdentifier.setter
  def oldIdentifier(self, val:OldIdentifier) -> None:
    if not isinstance(val, OldIdentifier):
      raise WQXException("Attribute 'oldIdentifier' must be an OldIdentifier object.")
    self.__oldIdentifier = val

  @property
  def newIdentifier(self) -> NewIdentifier:
    """This is the new identifier replacing the old identifier."""
    return self.__newIdentifier
  @newIdentifier.setter
  def newIdentifier(self, val:NewIdentifier) -> None:
    if not isinstance(val, NewIdentifier):
      raise WQXException("Attribute 'newIdentifier' must be an NewIdentifier object.")
    self.__newIdentifier = val

  def generateXML(self, name = 'IndexIdentifierUpdate'):
    if self.__oldIdentifier is None:
      raise WQXException("Attribute 'oldIdentifier' is required.")
    if self.__newIdentifier is None:
      raise WQXException("Attribute 'newIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(name):
      line('OldIdentifier', self.__oldIdentifier)
      line('NewIdentifier', self.__newIdentifier)

    return doc.getvalue()

class ActivityIdentifierUpdate:
  """Allows a Activity Identifier to be changed."""

  __oldIdentifier: OldIdentifier
  __newIdentifier: NewIdentifier

  def __init__(self, old = None, new = None):
    self.__oldIdentifier = old
    self.__newIdentifier = new

  @property
  def oldIdentifier(self) -> OldIdentifier:
    """This is the old identifier to be replaced."""
    return self.__oldIdentifier
  @oldIdentifier.setter
  def oldIdentifier(self, val:OldIdentifier) -> None:
    if not isinstance(val, OldIdentifier):
      raise WQXException("Attribute 'oldIdentifier' must be an OldIdentifier object.")
    self.__oldIdentifier = val

  @property
  def newIdentifier(self) -> NewIdentifier:
    """This is the new identifier replacing the old identifier."""
    return self.__newIdentifier
  @newIdentifier.setter
  def newIdentifier(self, val:NewIdentifier) -> None:
    if not isinstance(val, NewIdentifier):
      raise WQXException("Attribute 'newIdentifier' must be an NewIdentifier object.")
    self.__newIdentifier = val

  def generateXML(self, name = 'ActivityIdentifierUpdate'):
    if self.__oldIdentifier is None:
      raise WQXException("Attribute 'oldIdentifier' is required.")
    if self.__newIdentifier is None:
      raise WQXException("Attribute 'newIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(name):
      line('OldIdentifier', self.__oldIdentifier)
      line('NewIdentifier', self.__newIdentifier)

    return doc.getvalue()

class ActivityGroupIdentifierUpdate:
  """Allows a ActivityGroup Identifier to be changed."""

  __oldIdentifier: OldIdentifier
  __newIdentifier: NewIdentifier

  def __init__(self, old = None, new = None):
    self.__oldIdentifier = old
    self.__newIdentifier = new

  @property
  def oldIdentifier(self) -> OldIdentifier:
    """This is the old identifier to be replaced."""
    return self.__oldIdentifier
  @oldIdentifier.setter
  def oldIdentifier(self, val:OldIdentifier) -> None:
    if not isinstance(val, OldIdentifier):
      raise WQXException("Attribute 'oldIdentifier' must be an OldIdentifier object.")
    self.__oldIdentifier = val

  @property
  def newIdentifier(self) -> NewIdentifier:
    """This is the new identifier replacing the old identifier."""
    return self.__newIdentifier
  @newIdentifier.setter
  def newIdentifier(self, val:NewIdentifier) -> None:
    if not isinstance(val, NewIdentifier):
      raise WQXException("Attribute 'newIdentifier' must be an NewIdentifier object.")
    self.__newIdentifier = val

  def generateXML(self, name = 'ActivityGroupIdentifierUpdate'):
    if self.__oldIdentifier is None:
      raise WQXException("Attribute 'oldIdentifier' is required.")
    if self.__newIdentifier is None:
      raise WQXException("Attribute 'newIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(name):
      line('OldIdentifier', self.__oldIdentifier)
      line('NewIdentifier', self.__newIdentifier)

    return doc.getvalue()

class UpdateIdentifiers:
  """Allows a set of identifiers to be changed."""

  __organizationIdentifier: OrganizationIdentifier
  __projectIdentifierUpdate: List[ProjectIdentifierUpdate]
  __monitoringLocationIdentifierUpdate: List[MonitoringLocationIdentifierUpdate]
  __indexIdentifierUpdate: List[IndexIdentifierUpdate]
  __activityIdentifierUpdate: List[ActivityIdentifierUpdate]
  __activityGroupIdentifierUpdate: List[ActivityGroupIdentifierUpdate]

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
  def projectIdentifierUpdate(self) -> List[ProjectIdentifierUpdate]:
    return self.__projectIdentifierUpdate
  @projectIdentifierUpdate.setter
  def projectIdentifierUpdate(self, val: List[ProjectIdentifierUpdate]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'projectIdentifierUpdate' must be a list of 0 or more ProjectIdentifierUpdate objects.")
    for x in val:
      if not isinstance(x, ProjectIdentifierUpdate):
        raise TypeError("Attribute 'projectIdentifierUpdate' must be a list of 0 or more ProjectIdentifierUpdate objects.")
    self.__projectIdentifierUpdate = val

  @property
  def monitoringLocationIdentifierUpdate(self) -> List[MonitoringLocationIdentifierUpdate]:
    return self.__monitoringLocationIdentifierUpdate
  @monitoringLocationIdentifierUpdate.setter
  def monitoringLocationIdentifierUpdate(self, val: List[MonitoringLocationIdentifierUpdate]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'monitoringLocationIdentifierUpdate' must be a list of 0 or more MonitoringLocationIdentifierUpdate objects.")
    for x in val:
      if not isinstance(x, MonitoringLocationIdentifierUpdate):
        raise TypeError("Attribute 'monitoringLocationIdentifierUpdate' must be a list of 0 or more MonitoringLocationIdentifierUpdate objects.")
    self.__monitoringLocationIdentifierUpdate = val

  @property
  def indexIdentifierUpdate(self) -> List[IndexIdentifierUpdate]:
    return self.__indexIdentifierUpdate
  @indexIdentifierUpdate.setter
  def indexIdentifierUpdate(self, val: List[IndexIdentifierUpdate]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'indexIdentifierUpdate' must be a list of 0 or more IndexIdentifierUpdate objects.")
    for x in val:
      if not isinstance(x, IndexIdentifierUpdate):
        raise TypeError("Attribute 'indexIdentifierUpdate' must be a list of 0 or more IndexIdentifierUpdate objects.")
    self.__indexIdentifierUpdate = val

  @property
  def activityIdentifierUpdate(self) -> List[ActivityIdentifierUpdate]:
    return self.__activityIdentifierUpdate
  @activityIdentifierUpdate.setter
  def activityIdentifierUpdate(self, val: List[ActivityIdentifierUpdate]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'activityIdentifierUpdate' must be a list of 0 or more ActivityIdentifierUpdate objects.")
    for x in val:
      if not isinstance(x, ActivityIdentifierUpdate):
        raise TypeError("Attribute 'activityIdentifierUpdate' must be a list of 0 or more ActivityIdentifierUpdate objects.")
    self.__activityIdentifierUpdate = val

  @property
  def activityGroupIdentifierUpdate(self) -> List[ActivityGroupIdentifierUpdate]:
    return self.__activityGroupIdentifierUpdate
  @activityGroupIdentifierUpdate.setter
  def activityGroupIdentifierUpdate(self, val: List[ActivityGroupIdentifierUpdate]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'activityGroupIdentifierUpdate' must be a list of 0 or more ActivityGroupIdentifierUpdate objects.")
    for x in val:
      if not isinstance(x, ActivityGroupIdentifierUpdate):
        raise TypeError("Attribute 'activityGroupIdentifierUpdate' must be a list of 0 or more ActivityGroupIdentifierUpdate objects.")
    self.__activityGroupIdentifierUpdate = val

  def generateXML(self, name = 'UpdateIdentifiers'):
    if self.__organizationIdentifier is None:
      raise WQXException("Attribute 'organizationIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(name):
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
