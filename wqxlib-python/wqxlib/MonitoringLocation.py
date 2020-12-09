from yattag import Doc, indent

class MonitoringLocation:
  __countryCode: str # optional, constrained
  __countyCode: str # optional, constrained
  __horizontalCollectionMethodName: str # required, constrained
  __horizontalCoordinateReferenceSystemDatumName: str # required, constrained
  __hucEightDigitCode: str  # optional
  __hucTwelveDigitCode: str # optional
  __latitudeMeasure: str  # required
  __longitudeMeasure: str # required
  __monitoringLocationIdentifier: str # required
  __monitoringLocationName: str # required
  __monitoringLocationTypeName: str # required, constrained
  __sourceMapScale: str # optional
  __stateCode: str  # optional, constrained
  __tribalLandIndicator: str  # optional

  def __init__(self):
    # Document / Payload / WQX / Organization / MonitoringLocation / MonitoringLocationIdentity
    self.monitoringLocationIdentifier = 'GREENUP'
    self.monitoringLocationName = 'Greenup Dam'
    self.monitoringLocationTypeName = 'River/Stream'
    self.hucEightDigitCode = '05090103'
    self.hucTwelveDigitCode = '050901030107'
    self.tribalLandIndicator = True
    # Document / Payload / WQX / Organization / MonitoringLocation / MonitoringLocationGeospatial
    self.latitudeMeasure = '38.6470'
    self.longitudeMeasure = '-82.8587'
    self.sourceMapScale = '2400'
    self.horizontalCollectionMethodName = 'Interpolation-Map'
    self.horizontalCoordinateReferenceSystemDatumName = 'NAD83'
    self.countryCode = 'US'
    self.stateCode = 'WV'
    self.countyCode = '039'

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
  def hucEightDigitCode(self) -> str:
    return self.__hucEightDigitCode
  @hucEightDigitCode.setter
  def hucEightDigitCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'hucEightDigitCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'hucEightDigitCode' is required.")
    self.__hucEightDigitCode = val

  @property
  def hucTwelveDigitCode(self) -> str:
    return self.__hucTwelveDigitCode
  @hucTwelveDigitCode.setter
  def hucTwelveDigitCode(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'hucTwelveDigitCode' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'hucTwelveDigitCode' is required.")
    self.__hucTwelveDigitCode = val

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
  def tribalLandIndicator(self) -> str:
    return self.__tribalLandIndicator
  @tribalLandIndicator.setter
  def tribalLandIndicator(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'tribalLandIndicator' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'tribalLandIndicator' is required.")
    self.__tribalLandIndicator = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    with tag('MonitoringLocation'):
      with tag('MonitoringLocationIdentity'):
        line('MonitoringLocationIdentifier', self.monitoringLocationIdentifier)
        line('MonitoringLocationName', self.monitoringLocationName)
        line('MonitoringLocationTypeName', self.monitoringLocationTypeName)
        line('HUCEightDigitCode', self.hucEightDigitCode)
        line('HUCTwelveDigitCode', self.hucTwelveDigitCode)
        line('TribalLandIndicator', 'true' if self.tribalLandIndicator else 'false')
      with tag('MonitoringLocationGeospatial'):
        line('LatitudeMeasure', self.latitudeMeasure)
        line('LongitudeMeasure', self.longitudeMeasure)
        line('SourceMapScale', self.sourceMapScale)
        line('HorizontalCollectionMethodName', self.horizontalCollectionMethodName)
        line('HorizontalCoordinateReferenceSystemDatumName', self.horizontalCoordinateReferenceSystemDatumName)
        line('CountryCode', self.countryCode)
        line('StateCode', self.stateCode)
        line('CountyCode', self.countyCode)
    return indent(doc.getvalue(), indentation = ' '*2)
