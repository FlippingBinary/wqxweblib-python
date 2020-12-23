from typing import List
from yattag import Doc, indent
from .SimpleContent import *
from ..common import WQXException

class OrganizationDelete:
  """Schema used to delete organization information"""

  __organizationIdentifier: OrganizationIdentifier
  __projectIdentifier: List[ProjectIdentifier]
  __monitoringLocationIdentifier: List[MonitoringLocationIdentifier]
  __activityIdentifier: List[ActivityIdentifier]
  __activityGroupIdentifier: List[ActivityGroupIdentifier]
  __indexIdentifier: List[IndexIdentifier]

  def __init__(self):
    self.__organizationIdentifier = None
    self.__projectIdentifier = None
    self.__monitoringLocationIdentifier = None
    self.__activityIdentifier = None
    self.__activityGroupIdentifier = None
    self.__indexIdentifier = None

  @property
  def organizationIdentifier(self) -> OrganizationIdentifier:
    return self.__organizationIdentifier
  @organizationIdentifier.setter
  def organizationIdentifier(self, val: OrganizationIdentifier) -> None:
    self.__organizationIdentifier = val

  @property
  def projectIdentifier(self) -> List[ProjectIdentifier]:
    return self.__projectIdentifier
  @projectIdentifier.setter
  def projectIdentifier(self, val:List[ProjectIdentifier]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'projectIdentifier' must be a list of 0 or more ProjectIdentifier objects.")
    for x in val:
      if not isinstance(x, ProjectIdentifier):
        raise TypeError("Attribute 'projectIdentifier' must be a list of 0 or more ProjectIdentifier objects.")
    self.__projectIdentifier = val

  @property
  def monitoringLocationIdentifier(self) -> List[MonitoringLocationIdentifier]:
    return self.__monitoringLocationIdentifier
  @monitoringLocationIdentifier.setter
  def monitoringLocationIdentifier(self, val:List[MonitoringLocationIdentifier]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'monitoringLocationIdentifier' must be a list of 0 or more MonitoringLocationIdentifier objects.")
    for x in val:
      if not isinstance(x, MonitoringLocationIdentifier):
        raise TypeError("Attribute 'monitoringLocationIdentifier' must be a list of 0 or more MonitoringLocationIdentifier objects.")
    self.__monitoringLocationIdentifier = val

  @property
  def activityIdentifier(self) -> List[ActivityIdentifier]:
    return self.__activityIdentifier
  @activityIdentifier.setter
  def activityIdentifier(self, val:List[ActivityIdentifier]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'activityIdentifier' must be a list of 0 or more ActivityIdentifier objects.")
    for x in val:
      if not isinstance(x, ActivityIdentifier):
        raise TypeError("Attribute 'activityIdentifier' must be a list of 0 or more ActivityIdentifier objects.")
    self.__activityIdentifier = val

  @property
  def activityGroupIdentifier(self) -> List[ActivityGroupIdentifier]:
    return self.__activityGroupIdentifier
  @activityGroupIdentifier.setter
  def activityGroupIdentifier(self, val:List[ActivityGroupIdentifier]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'activityGroupIdentifier' must be a list of 0 or more ActivityGroupIdentifier objects.")
    for x in val:
      if not isinstance(x, ActivityGroupIdentifier):
        raise TypeError("Attribute 'activityGroupIdentifier' must be a list of 0 or more ActivityGroupIdentifier objects.")
    self.__activityGroupIdentifier = val

  @property
  def indexIdentifier(self) -> List[IndexIdentifier]:
    return self.__indexIdentifier
  @indexIdentifier.setter
  def indexIdentifier(self, val:List[IndexIdentifier]) -> None:
    if not isinstance(val, list):
      raise TypeError("Attribute 'indexIdentifier' must be a list of 0 or more IndexIdentifier objects.")
    for x in val:
      if not isinstance(x, IndexIdentifier):
        raise TypeError("Attribute 'indexIdentifier' must be a list of 0 or more IndexIdentifier objects.")
    self.__indexIdentifier = val

  def generateXML(self, name = 'OrganizationDelete'):
    if self.__organizationIdentifier is None:
      raise WQXException("Attribute 'organizationIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(name):
      line('OrganizationIdentifier', self.__organizationIdentifier)
      for x in self.__projectIdentifier:
        line('ProjectIdentifier', x)
      for x in self.__monitoringLocationIdentifier:
        line('MonitoringLocationIdentifier', x)
      for x in self.__activityIdentifier:
        line('ActivityIdentifier', x)
      for x in self.__activityGroupIdentifier:
        line('ActivityGroupIdentifier', x)
      for x in self.__indexIdentifier:
        line('IndexIdentifier', x)

    return doc.getvalue()
