from typing import List
from yattag import Doc, indent
from .Measure import Measure
from .WQXException import WQXException

class AlternateMonitoringLocationIdentity:
  __monitoringLocationIdentifier: str # required
  __monitoringLocationIdentifierContext: str # required

  @property
  def monitoringLocationIdentifier(self) -> str:
    return self.__monitoringLocationIdentifier
  @monitoringLocationIdentifier.setter
  def monitoringLocationIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'monitoringLocationIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'monitoringLocationIdentifier' is required.")
    self.__monitoringLocationIdentifier = val

  @property
  def monitoringLocationIdentifierContext(self) -> str:
    return self.__monitoringLocationIdentifierContext
  @monitoringLocationIdentifierContext.setter
  def monitoringLocationIdentifierContext(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'monitoringLocationIdentifierContext' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'monitoringLocationIdentifierContext' is required.")
    self.__monitoringLocationIdentifierContext = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    line('MonitoringLocationIdentifier', self.__monitoringLocationIdentifier)
    line('MonitoringLocationIdentifierContext', self.__monitoringLocationIdentifierContext)
    return indent(doc.getvalue(), indentation = ' '*2)

class MonitoringLocationIdentity:
  __alternateMonitoringLocationIdentity: List[AlternateMonitoringLocationIdentity] # 0 or more
  __contributingDrainageAreaMeasure: Measure # optional
  __drainageAreaMeasure: Measure # optional
  __hucEightDigitCode: str  # optional
  __hucTwelveDigitCode: str # optional
  __monitoringLocationDescriptionText: str # optional
  __monitoringLocationIdentifier: str # required
  __monitoringLocationName: str # required
  __monitoringLocationTypeName: str # required, constrained
  __tribalLandIndicator: str  # optional
  __tribalLandName: str # optional

  def __init__(self):
    self.__alternateMonitoringLocationIdentity = []
    self.__contributingDrainageAreaMeasure = None
    self.__drainageAreaMeasure = None
    self.__hucEightDigitCode = None
    self.__hucTwelveDigitCode = None
    self.__monitoringLocationDescriptionText = None
    self.__tribalLandIndicator = None
    self.__tribalLandName = None

  @property
  def alternateMonitoringLocationIdentity(self) -> List[AlternateMonitoringLocationIdentity]:
    return self.__alternateMonitoringLocationIdentity
  @alternateMonitoringLocationIdentity.setter
  def alternateMonitoringLocationIdentity(self, val:List[AlternateMonitoringLocationIdentity]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'alternateMonitoringLocationIdentity' must be a list of 0 or more objects.")
    for i in val:
      if not isinstance(i, AlternateMonitoringLocationIdentity):
        raise TypeError("Property 'alternateMonitoringLocationIdentity must contain only AlternateMonitoringLocationIdentity objects.")
    self.__alternateMonitoringLocationIdentity = val

  @property
  def contributingDrainageAreaMeasure(self) -> Measure:
    return self.__contributingDrainageAreaMeasure
  @contributingDrainageAreaMeasure.setter
  def contributingDrainageAreaMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'contributingDrainageAreaMeasure' must be a Measure object, if provided.")
    self.__contributingDrainageAreaMeasure = val

  @property
  def drainageAreaMeasure(self) -> Measure:
    return self.__drainageAreaMeasure
  @drainageAreaMeasure.setter
  def drainageAreaMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'drainageAreaMeasure' must be a Measure object, if provided.")
    self.__drainageAreaMeasure = val

  @property
  def hucEightDigitCode(self) -> str:
    return self.__hucEightDigitCode
  @hucEightDigitCode.setter
  def hucEightDigitCode(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'hucEightDigitCode' must be a string, if provided.")
    self.__hucEightDigitCode = val

  @property
  def hucTwelveDigitCode(self) -> str:
    return self.__hucTwelveDigitCode
  @hucTwelveDigitCode.setter
  def hucTwelveDigitCode(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'hucTwelveDigitCode' must be a string, if provided.")
    self.__hucTwelveDigitCode = val

  @property
  def monitoringLocationDescriptionText(self) -> str:
    return self.__monitoringLocationDescriptionText
  @monitoringLocationDescriptionText.setter
  def monitoringLocationDescriptionText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'monitoringLocationDescriptionText' must be a string, if provided.")
    self.__monitoringLocationDescriptionText = val

  @property
  def monitoringLocationIdentifier(self) -> str:
    return self.__monitoringLocationIdentifier
  @monitoringLocationIdentifier.setter
  def monitoringLocationIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'monitoringLocationIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'monitoringLocationIdentifier' is required.")
    self.__monitoringLocationIdentifier = val

  @property
  def monitoringLocationName(self) -> str:
    return self.__monitoringLocationName
  @monitoringLocationName.setter
  def monitoringLocationName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'monitoringLocationName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'monitoringLocationName' is required.")
    self.__monitoringLocationName = val

  @property
  def monitoringLocationTypeName(self) -> str:
    return self.__monitoringLocationTypeName
  @monitoringLocationTypeName.setter
  def monitoringLocationTypeName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'monitoringLocationTypeName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'monitoringLocationTypeName' is required.")
    self.__monitoringLocationTypeName = val

  @property
  def tribalLandIndicator(self) -> bool:
    return self.__tribalLandIndicator
  @tribalLandIndicator.setter
  def tribalLandIndicator(self, val:bool) -> None:
    if val is not None and not isinstance(val, bool):
      raise TypeError("Property 'tribalLandIndicator' must be a boolean, if provided.")
    self.__tribalLandIndicator = val

  @property
  def tribalLandName(self) -> str:
    return self.__tribalLandName
  @tribalLandName.setter
  def tribalLandName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'tribalLandName' must be a string, if provided.")
    self.__tribalLandName = val

  def generateXML(self):
    if self.__monitoringLocationIdentifier is None:
      raise WQXException("Property 'monitoringLocationIdentifier' is required.")
    if self.__monitoringLocationName is None:
      raise WQXException("Property 'monitoringLocationName' is required.")
    if self.__monitoringLocationTypeName is None:
      raise WQXException("Property 'monitoringLocationTypeName' is required.")
    doc, tag, text, line = Doc().ttl()
    line('MonitoringLocationIdentifier', self.__monitoringLocationIdentifier)
    line('MonitoringLocationName', self.__monitoringLocationName)
    line('MonitoringLocationTypeName', self.__monitoringLocationTypeName)
    if self.__hucEightDigitCode is not None:
      line('HUCEightDigitCode', self.__hucEightDigitCode)
    if self.__hucTwelveDigitCode is not None:
      line('HUCTwelveDigitCode', self.__hucTwelveDigitCode)
    if self.__tribalLandIndicator is not None:
      line('TribalLandIndicator', 'true' if self.__tribalLandIndicator else 'false')
    if self.__alternateMonitoringLocationIdentity is not None:
      for x in self.__alternateMonitoringLocationIdentity:
        with tag('AlternateMonitoringLocationIdentity'):
          doc.asis(x.generateXML())
    if self.__drainageAreaMeasure is not None:
      doc.asis(self.__drainageAreaMeasure.generateXML())
    if self.__contributingDrainageAreaMeasure is not None:
      doc.asis(self.__contributingDrainageAreaMeasure.generateXML())
    return indent(doc.getvalue(), indentation = ' '*2)

class MonitoringLocationGeospatial:
  __countryCode: str # optional, constrained
  __countyCode: str # optional, constrained
  __horizontalAccuracyMeasure: Measure # optional
  __horizontalCollectionMethodName: str # required, constrained
  __horizontalCoordinateReferenceSystemDatumName: str # required, constrained
  __latitudeMeasure: str  # required
  __longitudeMeasure: str # required
  __sourceMapScale: str # optional
  __stateCode: str  # optional, constrained
  __verticalAccuracyMeasure: Measure # optional
  __verticalCollectionMethodName: str # optional, constrained
  __verticalCoordinateReferenceSystemDatumName: str # optional, constrained
  __verticalMeasure: Measure # optional

  def __init__(self):
    self.__countryCode = None
    self.__countyCode = None
    self.__horizontalAccuracyMeasure = None
    self.__sourceMapScale = None
    self.__stateCode = None
    self.__verticalAccuracyMeasure = None
    self.__verticalCollectionMethodName = None
    self.__verticalCoordinateReferenceSystemDatumName = None
    self.__verticalMeasure = None

  @property
  def countryCode(self) -> str:
    return self.__countryCode
  @countryCode.setter
  def countryCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'countryCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'countryCode' is required.")
    self.__countryCode = val

  @property
  def countyCode(self) -> str:
    return self.__countyCode
  @countyCode.setter
  def countyCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'countyCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'countyCode' is required.")
    self.__countyCode = val

  @property
  def horizontalAccuracyMeasure(self) -> Measure:
    return self.__horizontalAccuracyMeasure
  @horizontalAccuracyMeasure.setter
  def horizontalAccuracyMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'horizontalAccuracyMeasure' must be a Measure object, if provided.")
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
    if not isinstance(val, str):
      raise TypeError("Property 'sourceMapScale' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'sourceMapScale' is required.")
    self.__sourceMapScale = val

  @property
  def stateCode(self) -> str:
    return self.__stateCode
  @stateCode.setter
  def stateCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'stateCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'stateCode' is required.")
    self.__stateCode = val

  @property
  def verticalAccuracyMeasure(self) -> Measure:
    return self.__verticalAccuracyMeasure
  @verticalAccuracyMeasure.setter
  def verticalAccuracyMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'verticalAccuracyMeasure' must be a Measure object, if provided.")
    self.__verticalAccuracyMeasure = val

  @property
  def verticalCollectionMethodName(self) -> str:
    return self.__verticalCollectionMethodName
  @verticalCollectionMethodName.setter
  def verticalCollectionMethodName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'verticalCollectionMethodName' must be a string, if provided.")
    self.__verticalCollectionMethodName = val

  @property
  def verticalCoordinateReferenceSystemDatumName(self) -> str:
    return self.__verticalCoordinateReferenceSystemDatumName
  @verticalCoordinateReferenceSystemDatumName.setter
  def verticalCoordinateReferenceSystemDatumName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'verticalCoordinateReferenceSystemDatumName' must be a string, if provided.")
    self.__verticalCoordinateReferenceSystemDatumName = val

  @property
  def verticalMeasure(self) -> Measure:
    return self.__verticalMeasure
  @verticalMeasure.setter
  def verticalMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'verticalMeasure' must be a Measure object, if provided.")
    self.__verticalMeasure = val

  def generateXML(self):
    if self.__latitudeMeasure is None:
      raise WQXException("Property 'latitudeMeasure' is required.")
    if self.__longitudeMeasure is None:
      raise WQXException("Property 'longitudeMeasure' is required.")
    if self.__horizontalCollectionMethodName is None:
      raise WQXException("Property 'horizontalCollectionMethodName' is required.")
    if self.__horizontalCoordinateReferenceSystemDatumName is None:
      raise WQXException("Property 'horizontalCoordinateReferenceSystemDatumName' is required.")
    doc, tag, text, line = Doc().ttl()
    line('LatitudeMeasure', self.__latitudeMeasure)
    line('LongitudeMeasure', self.__longitudeMeasure)
    if self.__sourceMapScale is not None:
      line('SourceMapScale', self.__sourceMapScale)
    if self.__horizontalAccuracyMeasure is not None:
      doc.asis(self.__horizontalAccuracyMeasure.generateXML())
    if self.__verticalAccuracyMeasure is not None:
      doc.asis(self.__verticalAccuracyMeasure.generateXML())
    line('HorizontalCollectionMethodName', self.horizontalCollectionMethodName)
    line('HorizontalCoordinateReferenceSystemDatumName', self.horizontalCoordinateReferenceSystemDatumName)
    if self.__verticalMeasure is not None:
      doc.asis(self.__verticalMeasure.generateXML())
    if self.__verticalCollectionMethodName is not None:
      line('VerticalCollectionMethodName', self.__verticalCollectionMethodName)
    if self.__verticalCoordinateReferenceSystemDatumName is not None:
      line('VerticalCoordinateReferenceSystemDatumName', self.__verticalCoordinateReferenceSystemDatumName)
    if self.__countryCode is not None:
      line('CountryCode', self.countryCode)
    if self.__stateCode is not None:
      line('StateCode', self.stateCode)
    if self.__countyCode is not None:
      line('CountyCode', self.countyCode)
    return indent(doc.getvalue(), indentation = ' '*2)

class AquiferInformation:
  __localAquiferCode: str # required
  __localAquiferCodeContext: str # required
  __localAquiferName: str # required
  __localAquiferDescriptionText: str # optional

  def __init__(self):
    self.__localAquiferDescriptionText = None

  @property
  def localAquiferCode(self) -> str:
    return self.__localAquiferCode
  @localAquiferCode.setter
  def localAquiferCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'localAquiferCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'localAquiferCode' is required.")
    self.__localAquiferCode = val

  @property
  def localAquiferCodeContext(self) -> str:
    return self.__localAquiferCodeContext
  @localAquiferCodeContext.setter
  def localAquiferCodeContext(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'localAquiferCodeContext' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'localAquiferCodeContext' is required.")
    self.__localAquiferCodeContext = val

  @property
  def localAquiferName(self) -> str:
    return self.__localAquiferName
  @localAquiferName.setter
  def localAquiferName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'localAquiferName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'localAquiferName' is required.")
    self.__localAquiferName = val

  @property
  def localAquiferDescriptionText(self) -> str:
    return self.__localAquiferDescriptionText
  @localAquiferDescriptionText.setter
  def localAquiferDescriptionText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'localAquiferDescriptionText' must be a string, if provided.")
    self.__localAquiferDescriptionText = val

  def generateXML(self):
    if self.__localAquiferCode is None:
      raise WQXException("Property 'localAquiferCode' is required.")
    if self.__localAquiferCodeContext is None:
      raise WQXException("Property 'localAquiferCodeContext' is required.")
    if self.__localAquiferName is None:
      raise WQXException("Property 'localAquiferName' is required.")
    doc, tag, text, line = Doc().ttl()
    line('LocalAquiferCode', self.__localAquiferCode)
    line('LocalAquiferCodeContext', self.__localAquiferCodeContext)
    line('LocalAquiferName', self.__localAquiferName)
    if self.__localAquiferDescriptionText is not None:
      line('LocalAquiferDescriptionText', self.__localAquiferDescriptionText)
    return indent(doc.getvalue(), indentation = ' '*2)

class WellInformation:
  __aquiferInformation: AquiferInformation # optional
  __aquiferTypeName: str # optional
  __constructionDate: str # optional
  __formationTypeText: str # optional
  __nationalAquiferCode: str # optional
  __wellDepthMeasure: Measure # optional
  __wellHoleDepthMeasure: Measure # optional
  __wellTypeText: str # required

  def __init__(self):
    self.__aquiferInformation = None
    self.__aquiferTypeName = None
    self.__constructionDate = None
    self.__formationTypeText = None
    self.__nationalAquiferCode = None
    self.__wellDepthMeasure = None
    self.__wellHoleDepthMeasure = None

  @property
  def aquiferInformation(self) -> AquiferInformation:
    return self.__aquiferInformation
  @aquiferInformation.setter
  def aquiferInformation(self, val:AquiferInformation) -> None:
    if val is not None and not isinstance(val, AquiferInformation):
      raise TypeError("Property 'aquiferInformation' must be an AquiferInformation object, if provided.")
    self.__aquiferInformation = val

  @property
  def aquiferTypeName(self) -> str:
    return self.__aquiferTypeName
  @aquiferTypeName.setter
  def aquiferTypeName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'aquiferTypeName' must be a string, if provided.")
    self.__aquiferTypeName = val

  @property
  def constructionDate(self) -> str:
    return self.__constructionDate
  @constructionDate.setter
  def constructionDate(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'constructionDate' must be a string, if provided.")
    self.__constructionDate = val

  @property
  def formationTypeText(self) -> str:
    return self.__formationTypeText
  @formationTypeText.setter
  def formationTypeText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'formationTypeText' must be a string, if provided.")
    self.__formationTypeText = val

  @property
  def nationalAquiferCode(self) -> str:
    return self.__nationalAquiferCode
  @nationalAquiferCode.setter
  def nationalAquiferCode(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'nationalAquiferCode' must be a string, if provided.")
    self.__nationalAquiferCode = val

  @property
  def wellDepthMeasure(self) -> Measure:
    return self.__wellDepthMeasure
  @wellDepthMeasure.setter
  def wellDepthMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'wellDepthMeasure' must be a Measure object, if provided.")
    self.__wellDepthMeasure = val

  @property
  def wellHoleDepthMeasure(self) -> Measure:
    return self.__wellHoleDepthMeasure
  @wellHoleDepthMeasure.setter
  def wellHoleDepthMeasure(self, val:Measure) -> None:
    if not isinstance(val, Measure):
      raise TypeError("Property 'wellHoleDepthMeasure' must be a Measure object.")
    if len(val) < 1:
      raise TypeError("Property 'wellHoleDepthMeasure' is required.")
    self.__wellHoleDepthMeasure = val

  @property
  def wellTypeText(self) -> str:
    return self.__wellTypeText
  @wellTypeText.setter
  def wellTypeText(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'wellTypeText' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'wellTypeText' is required.")
    self.__wellTypeText = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    line('WellTypeText', self.__wellTypeText)
    if self.__aquiferTypeName is not None:
      line('AquiferTypeName', self.__aquiferTypeName)
    if self.__nationalAquiferCode is not None:
      line('NationalAquiferCode', self.__nationalAquiferCode)
    if self.__aquiferInformation is not None:
      with tag('AquiferInformation'):
        doc.asis(self.__aquiferInformation.generateXML())
    if self.__formationTypeText is not None:
      line('FormationTypeText', self.__formationTypeText)
    if self.__wellHoleDepthMeasure is not None:
      with tag('WellHoleDepthMeasure'):
        line('MeasureValue', self.__wellHoleDepthMeasure.measureValue)
        line('MeasureUnitCode', self.__wellHoleDepthMeasure.measureUnitCode)
    if self.__constructionDate is not None:
      line('ConstructionDate', self.__constructionDate)
    if self.__wellDepthMeasure is not None:
      with tag('WellDepthMeasure'):
        line('MeasureValue', self.__wellDepthMeasure.measureValue)
        line('MeasureUnitCode', self.__wellDepthMeasure.measureUnitCode)
    return indent(doc.getvalue(), indentation = ' '*2)

class AttachedBinaryObject:
  __binaryObjectFileName: str # required
  __binaryObjectFileTypeCode: str # required

  @property
  def binaryObjectFileName(self) -> str:
    return self.__binaryObjectFileName
  @binaryObjectFileName.setter
  def binaryObjectFileName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'binaryObjectFileName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'binaryObjectFileName' is required.")
    self.__binaryObjectFileName = val

  @property
  def binaryObjectFileTypeCode(self) -> str:
    return self.__binaryObjectFileTypeCode
  @binaryObjectFileTypeCode.setter
  def binaryObjectFileTypeCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'binaryObjectFileTypeCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'binaryObjectFileTypeCode' is required.")
    self.__binaryObjectFileTypeCode = val

  def generateXML(self):
    if self.__binaryObjectFileName is None:
      raise WQXException("Property 'binaryObjectFileName' is required.")
    if self.__binaryObjectFileTypeCode is None:
      raise WQXException("Property 'binaryObjectFileTypeCode' is required.")
    doc, tag, text, line = Doc().ttl()
    line('BinaryObjectFileName', self.__binaryObjectFileName)
    line('BinaryObjectFileTypeCode', self.__binaryObjectFileTypeCode)
    return indent(doc.getvalue(), indentation = ' '*2)

class MonitoringLocation:
  __attachedBinaryObject: List[AttachedBinaryObject] # 0 or more
  __monitoringLocationGeospatial: MonitoringLocationGeospatial # required
  __monitoringLocationIdentity: MonitoringLocationIdentity # required
  __wellInformation: WellInformation # optional

  def __init__(self):
    self.__attachedBinaryObject = []
    self.__monitoringLocationGeospatial = MonitoringLocationGeospatial()
    self.__monitoringLocationIdentity = MonitoringLocationIdentity()
    self.__wellInformation = None

  @property
  def attachedBinaryObject(self) -> List[AttachedBinaryObject]:
    return self.__attachedBinaryObject
  @attachedBinaryObject.setter
  def attachedBinaryObject(self, val:List[AttachedBinaryObject]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'attachedBinaryObject' must be a list of 0 or more AttachedBinaryObject objects.")
    self.__attachedBinaryObject = val

  @property
  def monitoringLocationGeospatial(self) -> MonitoringLocationGeospatial:
    return self.__monitoringLocationGeospatial
  @monitoringLocationGeospatial.setter
  def monitoringLocationGeospatial(self, val:MonitoringLocationGeospatial) -> None:
    if not isinstance(val, MonitoringLocationGeospatial):
      raise TypeError("Property 'monitoringLocationGeospatial' must be a MonitoringLocationGeospatial object.")
    if len(val) < 1:
      raise TypeError("Property 'monitoringLocationGeospatial' is required.")
    self.__monitoringLocationGeospatial = val

  @property
  def monitoringLocationIdentity(self) -> MonitoringLocationIdentity:
    return self.__monitoringLocationIdentity
  @monitoringLocationIdentity.setter
  def monitoringLocationIdentity(self, val:MonitoringLocationIdentity) -> None:
    if not isinstance(val, MonitoringLocationIdentity):
      raise TypeError("Property 'monitoringLocationIdentity' must be a MonitoringLocationIdentity object.")
    if len(val) < 1:
      raise TypeError("Property 'monitoringLocationIdentity' is required.")
    self.__monitoringLocationIdentity = val

  @property
  def wellInformation(self) -> WellInformation:
    return self.__wellInformation
  @wellInformation.setter
  def wellInformation(self, val:WellInformation) -> None:
    if not isinstance(val, WellInformation):
      raise TypeError("Property 'wellInformation' must be a WellInformation object.")
    if len(val) < 1:
      raise TypeError("Property 'wellInformation' is required.")
    self.__wellInformation = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    with tag('MonitoringLocationIdentity'):
      doc.asis(self.__monitoringLocationIdentity.generateXML())
    with tag('MonitoringLocationGeospatial'):
      doc.asis(self.__monitoringLocationGeospatial.generateXML())
    if self.__wellInformation is not None:
      with tag('WellInformation'):
        doc.asis(self.__wellInformation.generateXML())
    return indent(doc.getvalue(), indentation = ' '*2)
