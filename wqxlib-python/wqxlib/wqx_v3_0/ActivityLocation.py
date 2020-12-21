from yattag import Doc, indent
from .MeasureCompact import MeasureCompact
from .SimpleContent import *
from ..WQXException import WQXException

class ActivityLocation:
  """Geospatial description of monitoring site, if it is different from that described in the station description."""

  __latitudeMeasure: LatitudeMeasure
  __longitudeMeasure: LongitudeMeasure
  __sourceMapScale: SourceMapScale
  __horizontalAccuracyMeasure: MeasureCompact
  __horizontalCollectionMethodName: HorizontalCollectionMethodName
  __horizontalCoordinateReferenceSystemDatumName: HorizontalCoordinateReferenceSystemDatumName
  __activityLocationDescriptionText: ActivityLocationDescriptionText

  def __init__(self):
    self.__latitudeMeasure = None
    self.__longitudeMeasure = None
    self.__sourceMapScale = None
    self.__horizontalAccuracyMeasure = None
    self.__horizontalCollectionMethodName = None
    self.__horizontalCoordinateReferenceSystemDatumName = None
    self.__activityLocationDescriptionText = None

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
    self.__sourceMapScale = None if val is None else SourceMapScale(val)

  @property
  def horizontalAccuracyMeasure(self) -> MeasureCompact:
    return self.__horizontalAccuracyMeasure
  @horizontalAccuracyMeasure.setter
  def horizontalAccuracyMeasure(self, val:MeasureCompact) -> None:
    self.__horizontalAccuracyMeasure = val

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
  def activityLocationDescriptionText(self) -> ActivityLocationDescriptionText:
    return self.__activityLocationDescriptionText
  @activityLocationDescriptionText.setter
  def activityLocationDescriptionText(self, val:ActivityLocationDescriptionText) -> None:
    self.__activityLocationDescriptionText = None if val is None else ActivityLocationDescriptionText(val)

  def generateXML(self):
    if self.__latitudeMeasure is None:
      WQXException("Attribute 'latitudeMeasure' is required.")
    if self.__longitudeMeasure is None:
      WQXException("Attribute 'longitudeMeasure' is required.")
    if self.__horizontalCollectionMethodName is None:
      WQXException("Attribute 'horizontalCollectionMethodName' is required.")
    if self.__horizontalCoordinateReferenceSystemDatumName is None:
      WQXException("Attribute 'horizontalCoordinateReferenceSystemDatumName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('LatitudeMeasure', self.__latitudeMeasure)
    line('LongitudeMeasure', self.__longitudeMeasure)
    if self.__sourceMapScale is not None:
      line('SourceMapScale',self.__sourceMapScale)
    if self.__horizontalAccuracyMeasure is not None:
      with tag('HorizontalAccuracyMeasure'):
        doc.asis(self.__horizontalAccuracyMeasure.generateXML())
    line('HorizontalCollectionMethodName', self.__horizontalCollectionMethodName)
    line('HorizontalCoordinateReferenceSystemDatumName', self.__horizontalCoordinateReferenceSystemDatumName)
    if self.__activityLocationDescriptionText is not None:
      line('ActivityLocationDescriptionText',self.__activityLocationDescriptionText)

    return indent(doc.getvalue(), indentation = ' '*2)
