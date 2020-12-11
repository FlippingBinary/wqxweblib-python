from yattag import Doc, indent
from .Activity import Activity
from .ActivityGroup import ActivityGroup
from .BiologicalHabitatIndex import BiologicalHabitatIndex
from .MonitoringLocation import MonitoringLocation
from .Project import Project
from .WQXException import WQXException

class Payload:
  __activity: Activity # optional
  __activityGroup: ActivityGroup # optional
  __biologicalHabitatIndex: BiologicalHabitatIndex # optional
  __monitoringLocation: MonitoringLocation # optional
  __project: Project # optional

  def __init__(self):
    self.__activity = None
    self.__activityGroup = None
    self.__biologicalHabitatIndex = None
    self.__monitoringLocation = None
    self.__project = None

  @property
  def activity(self) -> Activity:
    if self.__activity is None:
      self.__activity = Activity()
    return self.__activity
  @activity.setter
  def activity(self, val:Activity) -> None:
    if val is not None and not isinstance(val, Activity):
      raise TypeError("Property 'activity' must be an Activity object, if provided.")
    self.__activity = val

  @property
  def activityGroup(self) -> ActivityGroup:
    if self.__activityGroup is None:
      self.__activityGroup = ActivityGroup()
    return self.__activityGroup
  @activityGroup.setter
  def activityGroup(self, val:ActivityGroup) -> None:
    if val is not None and not isinstance(val, ActivityGroup):
      raise TypeError("Property 'activityGroup' must be an ActivityGroup object, if provided.")
    self.__activityGroup = val

  @property
  def biologicalHabitatIndex(self) -> BiologicalHabitatIndex:
    if self.__biologicalHabitatIndex is None:
      self.__biologicalHabitatIndex = BiologicalHabitatIndex()
    return self.__biologicalHabitatIndex
  @biologicalHabitatIndex.setter
  def biologicalHabitatIndex(self, val:BiologicalHabitatIndex) -> None:
    if val is not None and not isinstance(val, BiologicalHabitatIndex):
      raise TypeError("Property 'biologicalHabitatIndex' must be a BiologicalHabitatIndex object, if provided.")
    self.__biologicalHabitatIndex = val

  @property
  def monitoringLocation(self) -> MonitoringLocation:
    if self.__monitoringLocation is None:
      self.__monitoringLocation = MonitoringLocation()
    return self.__monitoringLocation
  @monitoringLocation.setter
  def monitoringLocation(self, val:MonitoringLocation) -> None:
    if val is not None and not isinstance(val, MonitoringLocation):
      raise TypeError("Property 'monitoringLocation' must be a MonitoringLocation object, if provided.")
    self.__monitoringLocation = val

  @property
  def project(self) -> Project:
    if self.__project is None:
      self.__project = Project()
    return self.__project
  @project.setter
  def project(self, val:Project) -> None:
    if val is not None and not isinstance(val, Project):
      raise TypeError("Property 'project' must be a Project object, if provided.")
    self.__project = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    if self.__project is not None:
      doc.asis(self.__project.generateXML())
    if self.__monitoringLocation is not None:
      doc.asis(self.__monitoringLocation.generateXML())
    if self.__biologicalHabitatIndex is not None:
      doc.asis(self.__biologicalHabitatIndex.generateXML())
    if self.__activityGroup is not None:
      doc.asis(self.__activityGroup.generateXML())
    if self.__activity is not None:
      doc.asis(self.__activity.generateXML())
    return indent(doc.getvalue(), indentation = ' '*2)
