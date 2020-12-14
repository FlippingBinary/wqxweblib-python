from datetime import date, time
from typing import List
from yattag import Doc, indent
from .BinaryObject import BinaryObject
from .Measure import Measure
from .Method import Method
from .WQXException import WQXException

class ActivityDescription:
  __activityBottomDepthHeightMeasure: Measure # optional
  __activityCommentText: str # optional
  __activityConductingOrganizationText: List[str] # 0 or more
  __activityDepthAltitudeReferencePointText: str # optional
  __activityDepthHeightMeasure: Measure # optional
  __activityEndDate: date # required
  __activityEndTime: time # optional
  __activityIdentifier: str # required
  __activityIdentifierUserSupplied: str # optional
  __activityMediaName: str # required, constrained
  __activityMediaSubdivisionName: str # optional, constrained
  __activityRelativeDepthName: str # optional
  __activityStartDate: date # required
  __activityStartTime: time # optional
  __activityTopDepthHeightMeasure: Measure # optional
  __activityTypeCode: str # required, constrained
  __monitoringLocationIdentifier: str # optional
  __projectIdentifier: List[str] # 1 or more

  def __init__(self):
    self.__activityBottomDepthHeightMeasure = None
    self.__activityCommentText = None
    self.__activityConductingOrganizationText = []
    self.__activityDepthAltitudeReferencePointText = None
    self.__activityDepthHeightMeasure = None
    self.__activityEndTime = None
    self.__activityIdentifierUserSupplied = None
    self.__activityMediaSubdivisionName = None
    self.__activityRelativeDepthName = None
    self.__activityStartTime = None
    self.__activityTopDepthHeightMeasure = None
    self.__monitoringLocationIdentifier = None
    self.__projectIdentifier = []

  @property
  def activityBottomDepthHeightMeasure(self) -> Measure:
    return self.__activityBottomDepthHeightMeasure
  @activityBottomDepthHeightMeasure.setter
  def activityBottomDepthHeightMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'activityBottomDepthHeightMeasure' must be a Measure object, if provided.")
    self.__activityBottomDepthHeightMeasure = val

  @property
  def activityCommentText(self) -> str:
    return self.__activityCommentText
  @activityCommentText.setter
  def activityCommentText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'activityCommentText' must be a string, if provided.")
    self.__activityCommentText = val

  @property
  def activityConductingOrganizationText(self) -> List[str]:
    return self.__activityConductingOrganizationText
  @activityConductingOrganizationText.setter
  def activityConductingOrganizationText(self, val:List[str]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'activityConductingOrganizationText' must be a list of 0 or more objects.")
    for i in val:
      if not isinstance(i, str):
        raise TypeError("Property 'activityConductingOrganizationText must contain only strings.")
    self.__activityConductingOrganizationText = val

  @property
  def activityConductingOrganizationText(self) -> str:
    return self.__activityConductingOrganizationText
  @activityConductingOrganizationText.setter
  def activityConductingOrganizationText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'activityConductingOrganizationText' must be a string, if provided.")
    self.__activityConductingOrganizationText = val

  @property
  def activityDepthAltitudeReferencePointText(self) -> str:
    return self.__activityDepthAltitudeReferencePointText
  @activityDepthAltitudeReferencePointText.setter
  def activityDepthAltitudeReferencePointText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'activityDepthAltitudeReferencePointText' must be a string, if provided.")
    self.__activityDepthAltitudeReferencePointText = val

  @property
  def activityDepthHeightMeasure(self) -> Measure:
    return self.__activityDepthHeightMeasure
  @activityDepthHeightMeasure.setter
  def activityDepthHeightMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'activityDepthHeightMeasure' must be a Measure object, if provided.")
    self.__activityDepthHeightMeasure = val

  @property
  def activityEndDate(self) -> date:
    return self.__activityEndDate
  @activityEndDate.setter
  def activityEndDate(self, val:date) -> None:
    if not isinstance(val, date):
      raise TypeError("Property 'activityEndDate' must be a date object.")
    self.__activityEndDate = val

  @property
  def activityEndTime(self) -> time:
    return self.__activityEndTime
  @activityEndTime.setter
  def activityEndTime(self, val:time) -> None:
    if val is not None and not isinstance(val, time):
      raise TypeError("Property 'activityEndTime' must be a time object, if provided.")
    self.__activityEndTime = val

  @property
  def activityIdentifier(self) -> str:
    return self.__activityIdentifier
  @activityIdentifier.setter
  def activityIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'activityIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'activityIdentifier' is required.")
    self.__activityIdentifier = val

  @property
  def activityIdentifierUserSupplied(self) -> str:
    return self.__activityIdentifierUserSupplied
  @activityIdentifierUserSupplied.setter
  def activityIdentifierUserSupplied(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'activityIdentifierUserSupplied' must be a string, if provided.")
    self.__activityIdentifierUserSupplied = val

  @property
  def activityMediaName(self) -> str:
    return self.__activityMediaName
  @activityMediaName.setter
  def activityMediaName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'activityMediaName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'activityMediaName' is required.")
    self.__activityMediaName = val

  @property
  def activityMediaSubdivisionName(self) -> str:
    return self.__activityMediaSubdivisionName
  @activityMediaSubdivisionName.setter
  def activityMediaSubdivisionName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'activityMediaSubdivisionName' must be a string, if provided.")
    self.__activityMediaSubdivisionName = val

  @property
  def activityRelativeDepthName(self) -> str:
    return self.__activityRelativeDepthName
  @activityRelativeDepthName.setter
  def activityRelativeDepthName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'activityRelativeDepthName' must be a string, if provided.")
    self.__activityRelativeDepthName = val

  @property
  def activityStartDate(self) -> date:
    return self.__activityStartDate
  @activityStartDate.setter
  def activityStartDate(self, val:date) -> None:
    if not isinstance(val, date):
      raise TypeError("Property 'activityStartDate' must be a date object.")
    self.__activityStartDate = val

  @property
  def activityStartTime(self) -> time:
    return self.__activityStartTime
  @activityStartTime.setter
  def activityStartTime(self, val:time) -> None:
    if val is not None and not isinstance(val, time):
      raise TypeError("Property 'activityStartTime' must be a time object, if provided.")
    self.__activityStartTime = val

  @property
  def activityTopDepthHeightMeasure(self) -> Measure:
    return self.__activityTopDepthHeightMeasure
  @activityTopDepthHeightMeasure.setter
  def activityTopDepthHeightMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'activityTopDepthHeightMeasure' must be a Measure object, if provided.")
    self.__activityTopDepthHeightMeasure = val

  @property
  def activityTypeCode(self) -> str:
    return self.__activityTypeCode
  @activityTypeCode.setter
  def activityTypeCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'activityTypeCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'activityTypeCode' is required.")
    self.__activityTypeCode = val

  @property
  def monitoringLocationIdentifier(self) -> str:
    return self.__monitoringLocationIdentifier
  @monitoringLocationIdentifier.setter
  def monitoringLocationIdentifier(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'monitoringLocationIdentifier' must be a string, if provided.")
    self.__monitoringLocationIdentifier = val

  @property
  def projectIdentifier(self) -> List[str]:
    return self.__projectIdentifier
  @projectIdentifier.setter
  def projectIdentifier(self, val:List[str]) -> None:
    if not isinstance(val, list) or len(list) < 1:
      raise TypeError("Property 'projectIdentifier' must be a list of 1 or more objects.")
    for i in val:
      if not isinstance(i, str):
        raise TypeError("Property 'projectIdentifier must contain only strings.")
    self.__projectIdentifier = val

  def generateXML(self):
    if self.__activityEndDate is None:
      raise WQXException("Property 'activityEndDate' is required.")
    if self.__activityMediaName is None:
      raise WQXException("Property 'activityMediaName' is required.")
    if self.__activityStartDate is None:
      raise WQXException("Property 'activityStartDate' is required.")
    if self.__activityTypeCode is None:
      raise WQXException("Property 'activityTypeCode' is required.")
    if self.__projectIdentifier is None:
      raise WQXException("Property 'projectIdentifier' is required.")

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
      doc.asis(self.__activityStartTime)
    line('ActivityEndDate', self.__activityEndDate)
    if self.__activityEndTime is not None:
      doc.asis(self.__activityEndTime)
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
    if self.__activityCommentText is not None:
      line('ActivityCommentText', self.__activityCommentText)

    return indent(doc.getvalue(), indentation = ' '*2)

class ActivityLocation:
  __activityLocationDescriptionText: str # optional
  __horizontalAccuracyMeasure: Measure # required
  __horizontalCollectionMethodName: str # required, constrained
  __horizontalCoordinateReferenceSystemDatumName: str # required, constrained
  __latitudeMeasure: str # required
  __longitudeMeasure: str # required
  __sourceMapScale: str # optional

  def __init__(self):
    self.__sourceMapScale = None
    self.__activityLocationDescriptionText = None

  @property
  def activityLocationDescriptionText(self) -> str:
    return self.__activityLocationDescriptionText
  @activityLocationDescriptionText.setter
  def activityLocationDescriptionText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'activityLocationDescriptionText' must be a string, if provided.")
    self.__activityLocationDescriptionText = val

  @property
  def horizontalAccuracyMeasure(self) -> Measure:
    return self.__horizontalAccuracyMeasure
  @horizontalAccuracyMeasure.setter
  def horizontalAccuracyMeasure(self, val:Measure) -> None:
    if not isinstance(val, Measure):
      raise TypeError("Property 'horizontalAccuracyMeasure' must be a Measure object.")
    if len(val) < 1:
      raise TypeError("Property 'horizontalAccuracyMeasure' is required.")
    self.__horizontalAccuracyMeasure = val

  @property
  def horizontalCollectionMethodName(self) -> str:
    return self.__horizontalCollectionMethodName
  @horizontalCollectionMethodName.setter
  def horizontalCollectionMethodName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'horizontalCollectionMethodName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'horizontalCollectionMethodName' is required.")
    self.__horizontalCollectionMethodName = val

  @property
  def horizontalCoordinateReferenceSystemDatumName(self) -> str:
    return self.__horizontalCoordinateReferenceSystemDatumName
  @horizontalCoordinateReferenceSystemDatumName.setter
  def horizontalCoordinateReferenceSystemDatumName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'horizontalCoordinateReferenceSystemDatumName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'horizontalCoordinateReferenceSystemDatumName' is required.")
    self.__horizontalCoordinateReferenceSystemDatumName = val

  @property
  def latitudeMeasure(self) -> str:
    return self.__latitudeMeasure
  @latitudeMeasure.setter
  def latitudeMeasure(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'latitudeMeasure' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'latitudeMeasure' is required.")
    self.__latitudeMeasure = val

  @property
  def longitudeMeasure(self) -> str:
    return self.__longitudeMeasure
  @longitudeMeasure.setter
  def longitudeMeasure(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'longitudeMeasure' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'longitudeMeasure' is required.")
    self.__longitudeMeasure = val

  @property
  def sourceMapScale(self) -> str:
    return self.__sourceMapScale
  @sourceMapScale.setter
  def sourceMapScale(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'sourceMapScale' must be a string, if provided.")
    self.__sourceMapScale = val

  def generateXML(self):
    if self.__horizontalAccuracyMeasure is None:
      raise WQXException("Property 'horizontalAccuracyMeasure' is required.")
    if self.__horizontalCollectionMethodName is None:
      raise WQXException("Property 'horizontalCollectionMethodName' is required.")
    if self.__horizontalCoordinateReferenceSystemDatumName is None:
      raise WQXException("Property 'horizontalCoordinateReferenceSystemDatumName' is required.")
    if self.__latitudeMeasure is None:
      raise WQXException("Property 'latitudeMeasure' is required.")
    if self.__longitudeMeasure is None:
      raise WQXException("Property 'longitudeMeasure' is required.")

    doc, tag, text, line = Doc().ttl()

    line('LatitudeMeasure', self.__latitudeMeasure)
    line('LongitudeMeasure', self.__longitudeMeasure)
    if self.__sourceMapScale is not None:
      line('SourceMapScale', self.__sourceMapScale)
    with tag('HorizontalAccuracyMeasure'):
      doc.asis(self.__horizontalAccuracyMeasure.generateXML())
    line('HorizontalCollectionMethodName', self.__horizontalCollectionMethodName)
    line('HorizontalCoordinateReferenceSystemDatumName', self.__horizontalCoordinateReferenceSystemDatumName)
    if self.__activityLocationDescriptionText is not None:
      line('ActivityLocationDescriptionText', self.__activityLocationDescriptionText)

    return indent(doc.getvalue(), indentation = ' '*2)

class Effort:
  __gearProcedureUnitCode: str # required, constrained
  __measureValue: str # required

  @property
  def gearProcedureUnitCode(self) -> str:
    return self.__gearProcedureUnitCode
  @gearProcedureUnitCode.setter
  def gearProcedureUnitCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'gearProcedureUnitCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'gearProcedureUnitCode' is required.")
    self.__gearProcedureUnitCode = val

  @property
  def measureValue(self) -> str:
    return self.__measureValue
  @measureValue.setter
  def measureValue(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'measureValue' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'measureValue' is required.")
    self.__measureValue = val

  def generateXML(self):
    if self.__measureValue is None:
      raise WQXException("Property 'measureValue' is required.")
    if self.__gearProcedureUnitCode is None:
      raise WQXException("Property 'gearProcedureUnitCode' is required.")
      
    doc, tag, text, line = Doc().ttl()

    line('MeasureValue', self.__measureValue)
    line('GearProcedureUnitCode', self.__gearProcedureUnitCode)

    return indent(doc.getvalue(), indentation = ' '*2)

class NetInformation:
  __boatSpeedMeasure: Measure # optional
  __currentSpeedMeasure: Measure # optional
  __netMeshSizeMeasure: Measure # optional
  __netSurfaceAreaMeasure: Measure # optional
  __netTypeName: str # required, constrained

  def __init__(self):
    self.__boatSpeedMeasure = None
    self.__currentSpeedMeasure = None
    self.__netMeshSizeMeasure = None
    self.__netSurfaceAreaMeasure = None

  @property
  def boatSpeedMeasure(self) -> Measure:
    return self.__boatSpeedMeasure
  @boatSpeedMeasure.setter
  def boatSpeedMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'boatSpeedMeasure' must be a Measure object, if provided.")
    self.__boatSpeedMeasure = val

  @property
  def currentSpeedMeasure(self) -> Measure:
    return self.__currentSpeedMeasure
  @currentSpeedMeasure.setter
  def currentSpeedMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'currentSpeedMeasure' must be a Measure object, if provided.")
    self.__currentSpeedMeasure = val

  @property
  def netMeshSizeMeasure(self) -> Measure:
    return self.__netMeshSizeMeasure
  @netMeshSizeMeasure.setter
  def netMeshSizeMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'netMeshSizeMeasure' must be a Measure object, if provided.")
    self.__netMeshSizeMeasure = val

  @property
  def netSurfaceAreaMeasure(self) -> Measure:
    return self.__netSurfaceAreaMeasure
  @netSurfaceAreaMeasure.setter
  def netSurfaceAreaMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'netSurfaceAreaMeasure' must be a Measure object, if provided.")
    self.__netSurfaceAreaMeasure = val

  @property
  def netTypeName(self) -> str:
    return self.__netTypeName
  @netTypeName.setter
  def netTypeName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'netTypeName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'netTypeName' is required.")
    self.__netTypeName = val

  def generateXML(self):
    if self.__netTypeName is None:
      raise WQXException("Property 'netTypeName' is required.")
      
    doc, tag, text, line = Doc().ttl()

    line('NetTypeName', self.__netTypeName)
    if self.__netSurfaceAreaMeasure is not None:
      doc.asis(self.__netSurfaceAreaMeasure.generateXML())
    if self.__netMeshSizeMeasure is not None:
      doc.asis(self.__netMeshSizeMeasure.generateXML())
    if self.__boatSpeedMeasure is not None:
      doc.asis(self.__boatSpeedMeasure.generateXML())
    if self.__currentSpeedMeasure is not None:
      doc.asis(self.__currentSpeedMeasure.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)

class BiologicalHabitatCollectionInformation:
  __collectionArea: Measure # optional
  __collectionDescriptionText: str # optional
  __collectionDuration: Measure # optional
  __collectionEffort: Effort # optional
  __netInformation: NetInformation # optional
  __passCount: str # optional
  __reachLengthMeasure: Measure # optional
  __reachWidthMeasure: Measure # optional

  def __init__(self):
    self.__collectionArea = None
    self.__collectionDescriptionText = None
    self.__collectionDuration = None
    self.__collectionEffort = None
    self.__netInformation = None
    self.__passCount = None
    self.__reachLengthMeasure = None
    self.__reachWidthMeasure = None

  @property
  def collectionArea(self) -> Measure:
    return self.__collectionArea
  @collectionArea.setter
  def collectionArea(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'collectionArea' must be a Measure object, if provided.")
    self.__collectionArea = val

  @property
  def collectionDescriptionText(self) -> str:
    return self.__collectionDescriptionText
  @collectionDescriptionText.setter
  def collectionDescriptionText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'collectionDescriptionText' must be a string, if provided.")
    self.__collectionDescriptionText = val

  @property
  def collectionDuration(self) -> Measure:
    return self.__collectionDuration
  @collectionDuration.setter
  def collectionDuration(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'collectionDuration' must be a Measure object, if provided.")
    self.__collectionDuration = val

  @property
  def collectionEffort(self) -> Effort:
    return self.__collectionEffort
  @collectionEffort.setter
  def collectionEffort(self, val:Effort) -> None:
    if val is not None and not isinstance(val, Effort):
      raise TypeError("Property 'collectionEffort' must be an Effort object, if provided.")
    self.__collectionEffort = val

  @property
  def netInformation(self) -> NetInformation:
    return self.__netInformation
  @netInformation.setter
  def netInformation(self, val:NetInformation) -> None:
    if val is not None and not isinstance(val, NetInformation):
      raise TypeError("Property 'netInformation' must be a NetInformation object, if provided.")
    self.__netInformation = val

  @property
  def passCount(self) -> str:
    return self.__passCount
  @passCount.setter
  def passCount(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'passCount' must be a string, if provided.")
    self.__passCount = val

  @property
  def reachLengthMeasure(self) -> Measure:
    return self.__reachLengthMeasure
  @reachLengthMeasure.setter
  def reachLengthMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'reachLengthMeasure' must be a Measure object, if provided.")
    self.__reachLengthMeasure = val

  @property
  def reachWidthMeasure(self) -> Measure:
    return self.__reachWidthMeasure
  @reachWidthMeasure.setter
  def reachWidthMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'reachWidthMeasure' must be a Measure object, if provided.")
    self.__reachWidthMeasure = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__collectionDuration is not None:
      with tag('CollectionDuration'):
        doc.asis(self.__collectionDuration.generateXML())
    if self.__collectionArea is not None:
      with tag('CollectionArea'):
        doc.asis(self.__collectionArea.generateXML())
    if self.__collectionEffort is not None:
      with tag('CollectionEffort'):
        doc.asis(self.__collectionEffort.generateXML())
    if self.__reachLengthMeasure is not None:
      with tag('ReachLengthMeasure'):
        doc.asis(self.__reachLengthMeasure.generateXML())
    if self.__reachWidthMeasure is not None:
      with tag('ReachWidthMeasure'):
        doc.asis(self.__reachWidthMeasure.generateXML())
    if self.__collectionDescriptionText is not None:
      line('CollectionDescriptionText', self.__collectionDescriptionText)
    if self.__passCount is not None:
      line('PassCount', self.__passCount)
    if self.__netInformation is not None:
      with tag('NetInformation'):
        doc.asis(self.__netInformation.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)

class BiologicalActivityDescription:
  __assemblageSampledName: str # optional, constrained
  __biologicalHabitatCollectionInformation: BiologicalHabitatCollectionInformation # optional
  __habitatSelectionMethod: str # optional, constrained
  __toxicityTestType: str # optional, constrained
  
  def __init__(self):
    self.__assemblageSampledName = None
    self.__biologicalHabitatCollectionInformation = None
    self.__habitatSelectionMethod = None
    self.__toxicityTestType = None

  @property
  def assemblageSampledName(self) -> str:
    return self.__assemblageSampledName
  @assemblageSampledName.setter
  def assemblageSampledName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'assemblageSampledName' must be a string, if provided.")
    self.__assemblageSampledName = val

  @property
  def biologicalHabitatCollectionInformation(self) -> BiologicalHabitatCollectionInformation:
    return self.__biologicalHabitatCollectionInformation
  @biologicalHabitatCollectionInformation.setter
  def biologicalHabitatCollectionInformation(self, val:BiologicalHabitatCollectionInformation) -> None:
    if val is not None and not isinstance(val, BiologicalHabitatCollectionInformation):
      raise TypeError("Property 'biologicalHabitatCollectionInformation' must be a BiologicalHabitatCollectionInformation object, if provided.")
    self.__biologicalHabitatCollectionInformation = val

  @property
  def habitatSelectionMethod(self) -> str:
    return self.__habitatSelectionMethod
  @habitatSelectionMethod.setter
  def habitatSelectionMethod(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'habitatSelectionMethod' must be a string, if provided.")
    self.__habitatSelectionMethod = val

  @property
  def toxicityTestType(self) -> str:
    return self.__toxicityTestType
  @toxicityTestType.setter
  def toxicityTestType(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'toxicityTestType' must be a string, if provided.")
    self.__toxicityTestType = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__assemblageSampledName is not None:
      line('AssemblageSampledName', self.__assemblageSampledName)
    if self.__biologicalHabitatCollectionInformation is not None:
      doc.asis(self.__biologicalHabitatCollectionInformation.generateXML())
    if self.__toxicityTestType is not None:
      line('ToxicityTestType', self.__toxicityTestType)
    if self.__habitatSelectionMethod is not None:
      line('HabitatSelectionMethod', self.__habitatSelectionMethod)

    return indent(doc.getvalue(), indentation = ' '*2)

class SamplePreparation:
  __chemicalPreservativeUsedName: str # optional
  __sampleContainerColorName: str # optional, constrained
  __sampleContainerLabelName: str # optional
  __sampleContainerTypeName: str # optional, constrained
  __samplePreparationMethod: Method # optional
  __sampleTransportStorageDescription: str # optional
  __thermalPreservativeUsedName: str # optional

  def __init__(self):
    self.__chemicalPreservativeUsedName = None
    self.__sampleContainerColorName = None
    self.__sampleContainerLabelName = None
    self.__sampleContainerTypeName = None
    self.__samplePreparationMethod = None
    self.__sampleTransportStorageDescription = None
    self.__thermalPreservativeUsedName = None

  @property
  def chemicalPreservativeUsedName(self) -> str:
    return self.__chemicalPreservativeUsedName
  @chemicalPreservativeUsedName.setter
  def chemicalPreservativeUsedName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'chemicalPreservativeUsedName' must be a string, if provided.")
    self.__chemicalPreservativeUsedName = val

  @property
  def sampleContainerColorName(self) -> str:
    return self.__sampleContainerColorName
  @sampleContainerColorName.setter
  def sampleContainerColorName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'sampleContainerColorName' must be a string, if provided.")
    self.__sampleContainerColorName = val

  @property
  def sampleContainerLabelName(self) -> str:
    return self.__sampleContainerLabelName
  @sampleContainerLabelName.setter
  def sampleContainerLabelName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'sampleContainerLabelName' must be a string, if provided.")
    self.__sampleContainerLabelName = val

  @property
  def sampleContainerTypeName(self) -> str:
    return self.__sampleContainerTypeName
  @sampleContainerTypeName.setter
  def sampleContainerTypeName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'sampleContainerTypeName' must be a string, if provided.")
    self.__sampleContainerTypeName = val

  @property
  def samplePreparationMethod(self) -> Method:
    return self.__samplePreparationMethod
  @samplePreparationMethod.setter
  def samplePreparationMethod(self, val:Method) -> None:
    if val is not None and not isinstance(val, Method):
      raise TypeError("Property 'samplePreparationMethod' must be a Method object, if provided.")
    self.__samplePreparationMethod = val

  @property
  def sampleTransportStorageDescription(self) -> str:
    return self.__sampleTransportStorageDescription
  @sampleTransportStorageDescription.setter
  def sampleTransportStorageDescription(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'sampleTransportStorageDescription' must be a string, if provided.")
    self.__sampleTransportStorageDescription = val

  @property
  def thermalPreservativeUsedName(self) -> str:
    return self.__thermalPreservativeUsedName
  @thermalPreservativeUsedName.setter
  def thermalPreservativeUsedName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'thermalPreservativeUsedName' must be a string, if provided.")
    self.__thermalPreservativeUsedName = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__samplePreparationMethod is not None:
      doc.asis(self.__samplePreparationMethod.generateXML())
    if self.__sampleContainerLabelName is not None:
      line('SampleContainerLabelName', self.__sampleContainerLabelName)
    if self.__sampleContainerTypeName is not None:
      line('SampleContainerTypeName', self.__sampleContainerTypeName)
    if self.__sampleContainerColorName is not None:
      line('SampleContainerColorName', self.__sampleContainerColorName)
    if self.__chemicalPreservativeUsedName is not None:
      line('ChemicalPreservativeUsedName', self.__chemicalPreservativeUsedName)
    if self.__thermalPreservativeUsedName is not None:
      line('ThermalPreservativeUsedName', self.__thermalPreservativeUsedName)
    if self.__sampleTransportStorageDescription is not None:
      line('SampleTransportStorageDescription', self.__sampleTransportStorageDescription)

    return indent(doc.getvalue(), indentation = ' '*2)

class SampleDescription:
  __hydrologicCondition: str # optional, constrained
  __hydrologicEvent: str # optional, constrained
  __sampleCollectionEquipmentCommentText: str # optional
  __sampleCollectionEquipmentName: str # required, constrained
  __sampleCollectionMethod: Method # optional
  __samplePreparation: SamplePreparation # optional

  def __init__(self):
    self.__hydrologicCondition = None
    self.__hydrologicEvent = None
    self.__sampleCollectionEquipmentCommentText = None
    self.__sampleCollectionEquipmentName = None
    self.__sampleCollectionMethod = None
    self.__samplePreparation = None

  @property
  def hydrologicCondition(self) -> str:
    return self.__hydrologicCondition
  @hydrologicCondition.setter
  def hydrologicCondition(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'hydrologicCondition' must be a string, if provided.")
    self.__hydrologicCondition = val

  @property
  def hydrologicEvent(self) -> str:
    return self.__hydrologicEvent
  @hydrologicEvent.setter
  def hydrologicEvent(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'hydrologicEvent' must be a string, if provided.")
    self.__hydrologicEvent = val

  @property
  def sampleCollectionEquipmentCommentText(self) -> str:
    return self.__sampleCollectionEquipmentCommentText
  @sampleCollectionEquipmentCommentText.setter
  def sampleCollectionEquipmentCommentText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'sampleCollectionEquipmentCommentText' must be a string, if provided.")
    self.__sampleCollectionEquipmentCommentText = val

  @property
  def sampleCollectionEquipmentName(self) -> str:
    return self.__sampleCollectionEquipmentName
  @sampleCollectionEquipmentName.setter
  def sampleCollectionEquipmentName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'sampleCollectionEquipmentName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'sampleCollectionEquipmentName' is required.")
    self.__sampleCollectionEquipmentName = val

  @property
  def sampleCollectionMethod(self) -> Method:
    return self.__sampleCollectionMethod
  @sampleCollectionMethod.setter
  def sampleCollectionMethod(self, val:Method) -> None:
    if val is not None and not isinstance(val, Method):
      raise TypeError("Property 'sampleCollectionMethod' must be a Method object, if provided.")
    self.__sampleCollectionMethod = val

  @property
  def samplePreparation(self) -> SamplePreparation:
    return self.__samplePreparation
  @samplePreparation.setter
  def samplePreparation(self, val:SamplePreparation) -> None:
    if val is not None and not isinstance(val, SamplePreparation):
      raise TypeError("Property 'samplePreparation' must be a SamplePreparation object, if provided.")
    self.__samplePreparation = val

  def generateXML(self):
    if self.__sampleCollectionEquipmentName is None:
      raise WQXException("Property 'sampleCollectionEquipmentName' is required.")

    doc, tag, text, line = Doc().ttl()

    if self.__sampleCollectionMethod is not None:
      doc.asis(self.__sampleCollectionMethod.generateXML())
    doc.line('SampleCollectionEquipmentName', self.__sampleCollectionEquipmentName)
    if self.__sampleCollectionEquipmentCommentText is not None:
      line('SampleCollectionEquipmentCommentText', self.__sampleCollectionEquipmentCommentText)
    if self.__samplePreparation is not None:
      doc.asis(self.__samplePreparation.generateXML())
    if self.__hydrologicCondition is not None:
      line('HydrologicCondition', self.__hydrologicCondition)
    if self.__hydrologicEvent is not None:
      line('HydrologicEvent', self.__hydrologicEvent)

    return indent(doc.getvalue(), indentation = ' '*2)

class Activity:
  __activityDescription: ActivityDescription # required
  __activityLocation: ActivityLocation # optional
  __biologicalActivityDescription: BiologicalActivityDescription # optional
  __sampleDescription: SampleDescription # optional
  __attachedBinaryObject: BinaryObject # optional

  def __init__(self):
    self.__activityLocation = None

  @property
  def activityDescription(self) -> ActivityDescription:
    return self.__activityDescription
  @activityDescription.setter
  def activityDescription(self, val:ActivityDescription) -> None:
    if not isinstance(val, ActivityDescription):
      raise TypeError("Property 'activityDescription' must be a ActivityDescription object.")
    if len(val) < 1:
      raise TypeError("Property 'activityDescription' is required.")
    self.__activityDescription = val

  @property
  def activityLocation(self) -> ActivityLocation:
    if self.__activityLocation is None:
      self.__activityLocation = ActivityLocation()
    return self.__activityLocation
  @activityLocation.setter
  def activityLocation(self, val:ActivityLocation) -> None:
    if val is not None and not isinstance(val, ActivityLocation):
      raise TypeError("Property 'activityLocation' must be an ActivityLocation object, if provided.")
    self.__activityLocation = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    with tag('ActivityDescription'):
      doc.asis(self.__activityDescription.generateXML())
    with tag('ActivityLocation'):
      doc.asis(self.__activityLocation.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)
