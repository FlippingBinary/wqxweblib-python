from typing import List, Union
from yattag import Doc, indent
from .OrganizationDescription import OrganizationDescription
from .ElectronicAddress import ElectronicAddress
from .Telephonic import Telephonic
from .OrganizationAddress import OrganizationAddress
from .Project import Project
from .MonitoringLocation import MonitoringLocation
from .Activity import Activity
from .ActivityGroup import ActivityGroup
from .BiologicalHabitatIndex import BiologicalHabitatIndex
from ..common import WQXException

class Organization:
  """Schema used to transfer organization information."""

  __organizationDescription: OrganizationDescription
  __electronicAddress: List[ElectronicAddress]
  __telephonic: List[Telephonic]
  __organizationAddress: List[OrganizationAddress]
  __project: List[Project]
  __monitoringLocation: List[MonitoringLocation]
  __biologicalHabitatIndex: List[BiologicalHabitatIndex]
  __activity: List[Activity]
  __activityGroup: List[ActivityGroup]

  def __init__(self,
    organizationDescription:OrganizationDescription = None,
    electronicAddress:ElectronicAddress = [],
    telephonic:Telephonic = [],
    organizationAddress:OrganizationAddress = [],
    project:Project = [],
    monitoringLocation:MonitoringLocation = [],
    biologicalHabitatIndex:BiologicalHabitatIndex = [],
    activity:Activity = [],
    activityGroup:ActivityGroup = []
  ):
    self.organizationDescription = organizationDescription
    self.electronicAddress = electronicAddress
    self.telephonic = telephonic
    self.organizationAddress = organizationAddress
    self.project = project
    self.monitoringLocation = monitoringLocation
    self.biologicalHabitatIndex = biologicalHabitatIndex
    self.activity = activity
    self.activityGroup = activityGroup

  @property
  def organizationDescription(self) -> OrganizationDescription:
    return self.__organizationDescription
  @organizationDescription.setter
  def organizationDescription(self, val:OrganizationDescription) -> None:
    if val is not None and not isinstance(val, OrganizationDescription):
      raise WQXException("Property 'organizationDescription' must be an OrganizationDescription object.")
    self.__organizationDescription = val

  @property
  def electronicAddress(self) -> List[ElectronicAddress]:
    return self.__electronicAddress
  @electronicAddress.setter
  def electronicAddress(self, val:List[ElectronicAddress]) -> None:
    self.__electronicAddress = val

  @property
  def telephonic(self) -> List[Telephonic]:
    return self.__telephonic
  @telephonic.setter
  def telephonic(self, val:List[Telephonic]) -> None:
    self.__telephonic = val

  @property
  def organizationAddress(self) -> List[OrganizationAddress]:
    return self.__organizationAddress
  @organizationAddress.setter
  def organizationAddress(self, val:List[OrganizationAddress]) -> None:
    if val is not None and (not isinstance(val, list) or len(val) > 3):
      raise ValueError("Attribute 'organizationAddress' must be a list with 0 to 3 values.")
    self.__organizationAddress = [] if val is None else val

  @property
  def project(self) -> List[Project]:
    return self.__project
  @project.setter
  def project(self, val:Union[Project,List[Project]]) -> None:
    if val is not None and not isinstance(val, list) and not isinstance(val, Project):
      raise WQXException("Attribute 'project' must be a list of Project objects.")
    self.__project = [] if val is None else val if isinstance(val, list) else [val]

  @property
  def monitoringLocation(self) -> List[MonitoringLocation]:
    return self.__monitoringLocation
  @monitoringLocation.setter
  def monitoringLocation(self, val:Union[MonitoringLocation,List[MonitoringLocation]]) -> None:
    if val is not None and not isinstance(val, list) and not isinstance(val, MonitoringLocation):
      raise WQXException("Attribute 'monitoringLocation' must be a list of MonitoringLocation objects.")
    self.__monitoringLocation = [] if val is None else val if isinstance(val, list) else [val]

  @property
  def biologicalHabitatIndex(self) -> List[BiologicalHabitatIndex]:
    return self.__biologicalHabitatIndex
  @biologicalHabitatIndex.setter
  def biologicalHabitatIndex(self, val:Union[BiologicalHabitatIndex,List[BiologicalHabitatIndex]]) -> None:
    if val is not None and not isinstance(val, list) and not isinstance(val, BiologicalHabitatIndex):
      raise WQXException("Attribute 'biologicalHabitatIndex' must be a list of BiologicalHabitatIndex objects.")
    self.__biologicalHabitatIndex = [] if val is None else val if isinstance(val, list) else [val]

  @property
  def activity(self) -> List[Activity]:
    return self.__activity
  @activity.setter
  def activity(self, val:Union[Activity,List[Activity]]) -> None:
    if val is not None and not isinstance(val, list) and not isinstance(val, Activity):
      raise WQXException("Attribute 'activity' must be a list of Activity objects.")
    self.__activity = [] if val is None else val if isinstance(val, list) else [val]

  @property
  def activityGroup(self) -> List[ActivityGroup]:
    return self.__activityGroup
  @activityGroup.setter
  def activityGroup(self, val:Union[ActivityGroup,List[ActivityGroup]]) -> None:
    if val is not None and not isinstance(val, list) and not isinstance(val, ActivityGroup):
      raise WQXException("Attribute 'activityGroup' must be a list of ActivityGroup objects.")
    self.__activityGroup = [] if val is None else val if isinstance(val, list) else [val]

  def generateXML(self):
    if self.__organizationDescription is None:
      raise WQXException("Attribute 'organizationDescription' is required.")
    
    doc, tag, text, line = Doc().ttl()

    with tag('OrganizationDescription'):
      doc.asis(self.__organizationDescription.generateXML())
    if self.__electronicAddress is not None:
      for x in self.__electronicAddress:
        with tag('ElectronicAddress'):
          doc.asis(x.generateXML())
    if self.__telephonic is not None:
      for x in self.__telephonic:
        with tag('Telephonic'):
          doc.asis(x.generateXML())
    if self.__organizationAddress is not None:
      for x in self.__organizationAddress:
        with tag('OrganizationAddress'):
          doc.asis(x.generateXML())
    if self.__project is not None:
      for x in self.__project:
        with tag('Project'):
          doc.asis(x.generateXML())
    if self.__monitoringLocation is not None:
      for x in self.__monitoringLocation:
        with tag('MonitoringLocation'):
          doc.asis(x.generateXML())
    if self.__biologicalHabitatIndex is not None:
      for x in self.__biologicalHabitatIndex:
        with tag('BiologicalHabitatIndex'):
          doc.asis(x.generateXML())
    if self.__activity is not None:
      for x in self.__activity:
        with tag('Activity'):
          doc.asis(x.generateXML())
    if self.__activityGroup is not None:
      for x in self.__activityGroup:
        with tag('ActivityGroup'):
          doc.asis(x.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)
