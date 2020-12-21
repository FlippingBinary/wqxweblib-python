from yattag import Doc, indent
from .MeasureCompact import MeasureCompact
from .SimpleContent import *
from .WQXTime import WQXTime
from ..WQXException import WQXException

class ActivityDescription:
  """Basic identification information for an activity conducted within a project."""

  __activityIdentifier: ActivityIdentifier
  __activityIdentifierUserSupplied: ActivityIdentifierUserSupplied
  __activityTypeCode: ActivityTypeCode
  __activityMediaName: ActivityMediaName
  __activityMediaSubdivisionName: ActivityMediaSubdivisionName
  __activityStartDate: ActivityStartDate
  __activityStartTime: WQXTime
  __activityEndDate: ActivityEndDate
  __activityEndTime: WQXTime
  __activityRelativeDepthName: ActivityRelativeDepthName
  __activityDepthHeightMeasure: MeasureCompact
  __activityTopDepthHeightMeasure: MeasureCompact
  __activityBottomDepthHeightMeasure: MeasureCompact
  __activityDepthAltitudeReferencePointText: DepthAltitudeReferencePointText
  __projectIdentifier: ProjectIdentifier
  __activityConductingOrganizationText: ActivityConductingOrganizationText
  __monitoringLocationIdentifier: MonitoringLocationIdentifier
  __samplingComponentName: SamplingComponentName
  __activityCommentText: CommentText

  def __init__(self):
    self.__activityIdentifier = None
    self.__activityIdentifierUserSupplied = None
    self.__activityTypeCode = None
    self.__activityMediaName = None
    self.__activityMediaSubdivisionName = None
    self.__activityStartDate = None
    self.__activityStartTime = None
    self.__activityEndDate = None
    self.__activityEndTime = None
    self.__activityRelativeDepthName = None
    self.__activityDepthHeightMeasure = None
    self.__activityTopDepthHeightMeasure = None
    self.__activityBottomDepthHeightMeasure = None
    self.__activityDepthAltitudeReferencePointText = None
    self.__projectIdentifier = None
    self.__activityConductingOrganizationText = None
    self.__monitoringLocationIdentifier = None
    self.__samplingComponentName = None
    self.__activityCommentText = None

  @property
  def activityIdentifier(self) -> ActivityIdentifier:
    return self.__activityIdentifier
  @activityIdentifier.setter
  def activityIdentifier(self, val:ActivityIdentifier) -> None:
    self.__activityIdentifier = ActivityIdentifier(val)

  @property
  def activityIdentifierUserSupplied(self) -> ActivityIdentifierUserSupplied:
    return self.__activityIdentifierUserSupplied
  @activityIdentifierUserSupplied.setter
  def activityIdentifierUserSupplied(self, val:ActivityIdentifierUserSupplied) -> None:
    self.__activityIdentifierUserSupplied = None if val is None else ActivityIdentifierUserSupplied(val)

  @property
  def activityTypeCode(self) -> ActivityTypeCode:
    return self.__activityTypeCode
  @activityTypeCode.setter
  def activityTypeCode(self, val:ActivityTypeCode) -> None:
    self.__activityTypeCode = ActivityTypeCode(val)

  @property
  def activityMediaName(self) -> ActivityMediaName:
    return self.__activityMediaName
  @activityMediaName.setter
  def activityMediaName(self, val:ActivityMediaName) -> None:
    self.__activityMediaName = ActivityMediaName(val)

  @property
  def activityMediaSubdivisionName(self) -> ActivityMediaSubdivisionName:
    return self.__activityMediaSubdivisionName
  @activityMediaSubdivisionName.setter
  def activityMediaSubdivisionName(self, val:ActivityMediaSubdivisionName) -> None:
    self.__activityMediaSubdivisionName = None if val is None else ActivityMediaSubdivisionName(val)

  @property
  def activityStartDate(self) -> ActivityStartDate:
    return self.__activityStartDate
  @activityStartDate.setter
  def activityStartDate(self, val:ActivityStartDate) -> None:
    self.__activityStartDate = ActivityStartDate(val)

  @property
  def activityStartTime(self) -> WQXTime:
    """The measure of clock time when the field activity began."""
    return self.__activityStartTime
  @activityStartTime.setter
  def activityStartTime(self, val:WQXTime) -> None:
    """The measure of clock time when the field activity began."""
    self.__activityStartTime = val

  @property
  def activityEndDate(self) -> ActivityEndDate:
    return self.__activityEndDate
  @activityEndDate.setter
  def activityEndDate(self, val:ActivityEndDate) -> None:
    self.__activityEndDate = None if val is None else ActivityEndDate(val)

  @property
  def activityEndTime(self) -> WQXTime:
    """The measure of clock time when the field activity ended."""
    return self.__activityEndTime
  @activityEndTime.setter
  def activityEndTime(self, val:WQXTime) -> None:
    """The measure of clock time when the field activity ended."""
    self.__activityEndTime = val

  @property
  def activityRelativeDepthName(self) -> ActivityRelativeDepthName:
    return self.__activityRelativeDepthName
  @activityRelativeDepthName.setter
  def activityRelativeDepthName(self, val:ActivityRelativeDepthName) -> None:
    self.__activityRelativeDepthName = None if val is None else ActivityRelativeDepthName(val)

  @property
  def activityDepthHeightMeasure(self) -> MeasureCompact:
    """A measurement of the vertical location (measured from a reference point) at which an activity occurred."""
    return self.__activityDepthHeightMeasure
  @activityDepthHeightMeasure.setter
  def activityDepthHeightMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the vertical location (measured from a reference point) at which an activity occurred."""
    self.__activityDepthHeightMeasure = val

  @property
  def activityTopDepthHeightMeasure(self) -> MeasureCompact:
    """A measurement of the upper vertical location of a vertical location range (measured from a reference point) at which an activity occurred."""
    return self.__activityTopDepthHeightMeasure
  @activityTopDepthHeightMeasure.setter
  def activityTopDepthHeightMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the upper vertical location of a vertical location range (measured from a reference point) at which an activity occurred."""
    self.__activityTopDepthHeightMeasure = val

  @property
  def activityBottomDepthHeightMeasure(self) -> MeasureCompact:
    """A measurement of the lower vertical location of a vertical location range (measured from a reference point) at which an activity occurred."""
    return self.__activityBottomDepthHeightMeasure
  @activityBottomDepthHeightMeasure.setter
  def activityBottomDepthHeightMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the lower vertical location of a vertical location range (measured from a reference point) at which an activity occurred."""
    self.__activityBottomDepthHeightMeasure = val

  @property
  def activityDepthAltitudeReferencePointText(self) -> DepthAltitudeReferencePointText:
    """The reference used to indicate the datum or reference used to establish the depth/altitude of an activity."""
    return self.__activityDepthAltitudeReferencePointText
  @activityDepthAltitudeReferencePointText.setter
  def activityDepthAltitudeReferencePointText(self, val:DepthAltitudeReferencePointText) -> None:
    """The reference used to indicate the datum or reference used to establish the depth/altitude of an activity."""
    self.__activityDepthAltitudeReferencePointText = None if val is None else DepthAltitudeReferencePointText(val)

  @property
  def projectIdentifier(self) -> ProjectIdentifier:
    return self.__projectIdentifier
  @projectIdentifier.setter
  def projectIdentifier(self, val:ProjectIdentifier) -> None:
    self.__projectIdentifier = None if val is None else ProjectIdentifier(val)

  @property
  def activityConductingOrganizationText(self) -> ActivityConductingOrganizationText:
    return self.__activityConductingOrganizationText
  @activityConductingOrganizationText.setter
  def activityConductingOrganizationText(self, val:ActivityConductingOrganizationText) -> None:
    self.__activityConductingOrganizationText = val

  @property
  def monitoringLocationIdentifier(self) -> MonitoringLocationIdentifier:
    return self.__monitoringLocationIdentifier
  @monitoringLocationIdentifier.setter
  def monitoringLocationIdentifier(self, val:MonitoringLocationIdentifier) -> None:
    self.__monitoringLocationIdentifier = None if val is None else MonitoringLocationIdentifier(val)

  @property
  def samplingComponentName(self) -> SamplingComponentName:
    return self.__samplingComponentName
  @samplingComponentName.setter
  def samplingComponentName(self, val:SamplingComponentName) -> None:
    self.__samplingComponentName = None if val is None else SamplingComponentName(val)

  @property
  def activityCommentText(self) -> CommentText:
    """General comments concerning the activity."""
    return self.__activityCommentText
  @activityCommentText.setter
  def activityCommentText(self, val:CommentText) -> None:
    """General comments concerning the activity."""
    self.__activityCommentText = None if val is None else CommentText(val)

  def generateXML(self):
    if self.__activityIdentifier is None:
      WQXException("Attribute 'activityIdentifier' is required.")
    if self.__activityTypeCode is None:
      WQXException("Attribute 'activityTypeCode' is required.")
    if self.__activityMediaName is None:
      WQXException("Attribute 'activityMediaName' is required.")
    if self.__activityStartDate is None:
      WQXException("Attribute 'activityStartDate' is required.")
    if self.__projectIdentifier is None:
      WQXException("Attribute 'projectIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    line('ActivityIdentifier', self.__activityIdentifier)
    if self.__activityIdentifierUserSupplied is not None:
      line('ActivityIdentifierUserSupplied', self.__activityIdentifierUserSupplied)
    line('ActivityTypeCode', self.__activityTypeCode)
    line('ActivityMediaName', self.__activityMediaName)
    if self.__activityMediaSubdivisionName is not None:
      line('ActivityMediaSubdivisionName', self.__activityMediaSubdivisionName)
    line('ActivityStartDate', self.__activityStartDate)
    if self.__activityStartTime is not None:
      with tag('ActivityStartTime'):
        doc.asis(self.__activityStartTime.generateXML())
    if self.__activityEndDate is not None:
      line('ActivityEndDate', self.__activityEndDate)
    if self.__activityEndTime is not None:
      with tag('ActivityEndTime'):
        doc.asis(self.__activityEndTime.generateXML())
    if self.__activityRelativeDepthName is not None:
      line('ActivityRelativeDepthName', self.__activityRelativeDepthName)
    if self.__activityDepthHeightMeasure is not None:
      with tag('ActivityDepthHeightMeasure'):
        doc.asis(self.__activityDepthHeightMeasure.generateXML())
    if self.__activityTopDepthHeightMeasure is not None:
      with tag('ActivityTopDepthHeightMeasure'):
        doc.asis(self.__activityTopDepthHeightMeasure.generateXML())
    if self.__activityBottomDepthHeightMeasure is not None:
      with tag('ActivityBottomDepthHeightMeasure'):
        doc.asis(self.__activityBottomDepthHeightMeasure.generateXML())
    if self.__activityDepthAltitudeReferencePointText is not None:
      line('ActivityDepthAltitudeReferencePointText', self.__activityDepthAltitudeReferencePointText)
    for x in self.__projectIdentifier:
      line('ProjectIdentifier', x)
    for x in self.__activityConductingOrganizationText:
      line('ActivityConductingOrganizationText', x)
    if self.__monitoringLocationIdentifier is not None:
      line('MonitoringLocationIdentifier', self.__monitoringLocationIdentifier)
    if self.__samplingComponentName is not None:
      line('SamplingComponentName', self.__samplingComponentName)
    if self.__activityCommentText is not None:
      line('ActivityCommentText', self.__activityCommentText)

    return indent(doc.getvalue(), indentation = ' '*2)
