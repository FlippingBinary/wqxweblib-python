from yattag import Doc, indent
from .MeasureCompact import MeasureCompact
from .SimpleContent import *
from ..common import WQXException

class MonitoringLocationGeospatial:
  """Monitoring location geographic location."""

  __latitudeMeasure: LatitudeMeasure
  __longitudeMeasure: LongitudeMeasure
  __sourceMapScale: SourceMapScale
  __horizontalAccuracyMeasure: MeasureCompact
  __verticalAccuracyMeasure: MeasureCompact
  __horizontalCollectionMethodName: HorizontalCollectionMethodName
  __horizontalCoordinateReferenceSystemDatumName: HorizontalCoordinateReferenceSystemDatumName
  __verticalMeasure: MeasureCompact
  __verticalCollectionMethodName: VerticalCollectionMethodName
  __verticalCoordinateReferenceSystemDatumName: VerticalCoordinateReferenceSystemDatumName
  __countryCode: CountryCode
  __stateCode: StateCode
  __countyCode: CountyCode

  def __init__(self, o=None, *,
    latitudeMeasure:LatitudeMeasure = None,
    longitudeMeasure:LongitudeMeasure = None,
    sourceMapScale:SourceMapScale = None,
    horizontalAccuracyMeasure:MeasureCompact = None,
    verticalAccuracyMeasure:MeasureCompact = None,
    horizontalCollectionMethodName:HorizontalCollectionMethodName = None,
    horizontalCoordinateReferenceSystemDatumName:HorizontalCoordinateReferenceSystemDatumName = None,
    verticalMeasure:MeasureCompact = None,
    verticalCollectionMethodName:VerticalCollectionMethodName = None,
    verticalCoordinateReferenceSystemDatumName:VerticalCoordinateReferenceSystemDatumName = None,
    countryCode:CountryCode = None,
    stateCode:StateCode = None,
    countyCode:CountyCode = None
  ):
    if isinstance(o, MonitoringLocationGeospatial):
      # Assign attributes from object without typechecking
      self.__latitudeMeasure = o.latitudeMeasure
      self.__longitudeMeasure = o.longitudeMeasure
      self.__sourceMapScale = o.sourceMapScale
      self.__horizontalAccuracyMeasure = o.horizontalAccuracyMeasure
      self.__verticalAccuracyMeasure = o.verticalAccuracyMeasure
      self.__horizontalCollectionMethodName = o.horizontalCollectionMethodName
      self.__horizontalCoordinateReferenceSystemDatumName = o.horizontalCoordinateReferenceSystemDatumName
      self.__verticalMeasure = o.verticalMeasure
      self.__verticalCollectionMethodName = o.verticalCollectionMethodName
      self.__verticalCoordinateReferenceSystemDatumName = o.verticalCoordinateReferenceSystemDatumName
      self.__countryCode = o.countryCode
      self.__stateCode = o.stateCode
      self.__countyCode = o.countyCode
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.latitudeMeasure = o.get('latitudeMeasure', default = None)
      self.longitudeMeasure = o.get('longitudeMeasure', default = None)
      self.sourceMapScale = o.get('sourceMapScale', default = None)
      self.horizontalAccuracyMeasure = o.get('horizontalAccuracyMeasure', default = None)
      self.verticalAccuracyMeasure = o.get('verticalAccuracyMeasure', default = None)
      self.horizontalCollectionMethodName = o.get('horizontalCollectionMethodName', default = None)
      self.horizontalCoordinateReferenceSystemDatumName = o.get('horizontalCoordinateReferenceSystemDatumName', default = None)
      self.verticalMeasure = o.get('verticalMeasure', default = None)
      self.verticalCollectionMethodName = o.get('verticalCollectionMethodName', default = None)
      self.verticalCoordinateReferenceSystemDatumName = o.get('verticalCoordinateReferenceSystemDatumName', default = None)
      self.countryCode = o.get('countryCode', default = None)
      self.stateCode = o.get('stateCode', default = None)
      self.countyCode = o.get('countyCode', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.latitudeMeasure = latitudeMeasure
      self.longitudeMeasure = longitudeMeasure
      self.sourceMapScale = sourceMapScale
      self.horizontalAccuracyMeasure = horizontalAccuracyMeasure
      self.verticalAccuracyMeasure = verticalAccuracyMeasure
      self.horizontalCollectionMethodName = horizontalCollectionMethodName
      self.horizontalCoordinateReferenceSystemDatumName = horizontalCoordinateReferenceSystemDatumName
      self.verticalMeasure = verticalMeasure
      self.verticalCollectionMethodName = verticalCollectionMethodName
      self.verticalCoordinateReferenceSystemDatumName = verticalCoordinateReferenceSystemDatumName
      self.countryCode = countryCode
      self.stateCode = stateCode
      self.countyCode = countyCode

  @property
  def latitudeMeasure(self) -> LatitudeMeasure:
    return self.__latitudeMeasure
  @latitudeMeasure.setter
  def latitudeMeasure(self, val:LatitudeMeasure) -> None:
    self.__latitudeMeasure = LatitudeMeasure(val)

  @property
  def longitudeMeasure(self) -> LongitudeMeasure:
    return self.__longitudeMeasure
  @longitudeMeasure.setter
  def longitudeMeasure(self, val:LongitudeMeasure) -> None:
    self.__longitudeMeasure = LongitudeMeasure(val)

  @property
  def sourceMapScale(self) -> SourceMapScale:
    return self.__sourceMapScale
  @sourceMapScale.setter
  def sourceMapScale(self, val:SourceMapScale) -> None:
    self.__sourceMapScale = SourceMapScale(val)

  @property
  def horizontalAccuracyMeasure(self) -> MeasureCompact:
    """The horizontal measure of the relative accuracy of the latitude and longitude coordinates."""
    return self.__horizontalAccuracyMeasure
  @horizontalAccuracyMeasure.setter
  def horizontalAccuracyMeasure(self, val:MeasureCompact) -> None:
    """The horizontal measure of the relative accuracy of the latitude and longitude coordinates."""
    self.__horizontalAccuracyMeasure = MeasureCompact(val)

  @property
  def verticalAccuracyMeasure(self) -> MeasureCompact:
    """Depth below land surface datum (LSD) to the bottom of the hole on completion of drilling."""
    return self.__verticalAccuracyMeasure
  @verticalAccuracyMeasure.setter
  def verticalAccuracyMeasure(self, val:MeasureCompact) -> None:
    """Depth below land surface datum (LSD) to the bottom of the hole on completion of drilling."""
    self.__verticalAccuracyMeasure = MeasureCompact(val)

  @property
  def horizontalCollectionMethodName(self) -> HorizontalCollectionMethodName:
    return self.__horizontalCollectionMethodName
  @horizontalCollectionMethodName.setter
  def horizontalCollectionMethodName(self, val:HorizontalCollectionMethodName) -> None:
    self.__horizontalCollectionMethodName = HorizontalCollectionMethodName(val)

  @property
  def horizontalCoordinateReferenceSystemDatumName(self) -> HorizontalCoordinateReferenceSystemDatumName:
    return self.__horizontalCoordinateReferenceSystemDatumName
  @horizontalCoordinateReferenceSystemDatumName.setter
  def horizontalCoordinateReferenceSystemDatumName(self, val:HorizontalCoordinateReferenceSystemDatumName) -> None:
    self.__horizontalCoordinateReferenceSystemDatumName = HorizontalCoordinateReferenceSystemDatumName(val)

  @property
  def verticalMeasure(self) -> MeasureCompact:
    """The measure of elevation (i.e., the altitude), above or below a reference datum."""
    return self.__verticalMeasure
  @verticalMeasure.setter
  def verticalMeasure(self, val:MeasureCompact) -> None:
    """The measure of elevation (i.e., the altitude), above or below a reference datum."""
    self.__verticalMeasure = MeasureCompact(val)

  @property
  def verticalCollectionMethodName(self) -> VerticalCollectionMethodName:
    return self.__verticalCollectionMethodName
  @verticalCollectionMethodName.setter
  def verticalCollectionMethodName(self, val:VerticalCollectionMethodName) -> None:
    self.__verticalCollectionMethodName = VerticalCollectionMethodName(val)

  @property
  def verticalCoordinateReferenceSystemDatumName(self) -> VerticalCoordinateReferenceSystemDatumName:
    return self.__verticalCoordinateReferenceSystemDatumName
  @verticalCoordinateReferenceSystemDatumName.setter
  def verticalCoordinateReferenceSystemDatumName(self, val:VerticalCoordinateReferenceSystemDatumName) -> None:
    self.__verticalCoordinateReferenceSystemDatumName = VerticalCoordinateReferenceSystemDatumName(val)

  @property
  def countryCode(self) -> CountryCode:
    return self.__countryCode
  @countryCode.setter
  def countryCode(self, val:CountryCode) -> None:
    self.__countryCode = CountryCode(val)

  @property
  def stateCode(self) -> StateCode:
    return self.__stateCode
  @stateCode.setter
  def stateCode(self, val:StateCode) -> None:
    self.__stateCode = StateCode(val)

  @property
  def countyCode(self) -> CountyCode:
    return self.__countyCode
  @countyCode.setter
  def countyCode(self, val:CountyCode) -> None:
    self.__countyCode = CountyCode(val)

  def generateXML(self):
    if self.__latitudeMeasure is None:
      WQXException("Attribute 'LatitudeMeasure' is required.")
    if self.__longitudeMeasure is None:
      WQXException("Attribute 'LongitudeMeasure' is required.")
    if self.__horizontalCollectionMethodName is None:
      WQXException("Attribute 'HorizontalCollectionMethodName' is required.")
    if self.__horizontalCoordinateReferenceSystemDatumName is None:
      WQXException("Attribute 'HorizontalCoordinateReferenceSystemDatumName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('LatitudeMeasure', self.__latitudeMeasure)
    line('LongitudeMeasure', self.__longitudeMeasure)
    if self.__sourceMapScale is not None:
      line('SourceMapScale', self.__sourceMapScale)
    if self.__horizontalAccuracyMeasure is not None:
      line('HorizontalAccuracyMeasure', self.__horizontalAccuracyMeasure)
    if self.__verticalAccuracyMeasure is not None:
      line('VerticalAccuracyMeasure', self.__verticalAccuracyMeasure)
    line('HorizontalCollectionMethodName', self.__horizontalCollectionMethodName)
    line('HorizontalCoordinateReferenceSystemDatumName', self.__horizontalCoordinateReferenceSystemDatumName)
    if self.__verticalMeasure is not None:
      line('VerticalMeasure', self.__verticalMeasure)
    if self.__verticalCollectionMethodName is not None:
      line('VerticalCollectionMethodName', self.__verticalCollectionMethodName)
    if self.__verticalCoordinateReferenceSystemDatumName is not None:
      line('VerticalCoordinateReferenceSystemDatumName', self.__verticalCoordinateReferenceSystemDatumName)
    if self.__countryCode is not None:
      line('CountryCode', self.__countryCode)
    if self.__stateCode is not None:
      line('StateCode', self.__stateCode)
    if self.__countyCode is not None:
      line('CountyCode', self.__countyCode)

    return doc.getvalue()
