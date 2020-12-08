from yattag import Doc, indent

class MonitoringLocation:
  monitoringLocationIdentifier: str
  monitoringLocationName: str
  monitoringLocationTypeName: str
  hucEightDigitCode: str
  hucTwelveDigitCode: str
  tribalLandIndicator: str
  latitudeMeasure: str
  longitudeMeasure: str
  sourceMapScale: str
  horizontalCollectionMethodName: str
  horizontalCoordinateReferenceSystemDatumName: str
  countryCode: str
  stateCode: str
  countyCode: str

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
