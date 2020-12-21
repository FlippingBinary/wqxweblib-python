from yattag import Doc, indent
from .BibliographicReference import BibliographicReference
from .MeasureCompact import MeasureCompact
from .SimpleContent import *
from ..WQXException import WQXException

class ProjectMonitoringLocationWeighting:
  """Describes the probability weighting information for a given Project / Monitoring Location Assignment."""

  __monitoringLocationIdentifier: MonitoringLocationIdentifier
  __locationWeightingFactorMeasure: MeasureCompact
  __statisticalStratumText: StatisticalStratumText
  __locationCategoryName: LocationCategoryName
  __locationStatusName: LocationStatusName
  __referenceLocationTypeCode: ReferenceLocationTypeCode
  __referenceLocationStartDate: ReferenceLocationStartDate
  __referenceLocationEndDate: ReferenceLocationEndDate
  __referenceLocationCitation: BibliographicReference
  __commentText: CommentText

  def __init__(self):
    self.__monitoringLocationIdentifier = None
    self.__locationWeightingFactorMeasure = None
    self.__statisticalStratumText = None
    self.__locationCategoryName = None
    self.__locationStatusName = None
    self.__referenceLocationTypeCode = None
    self.__referenceLocationStartDate = None
    self.__referenceLocationEndDate = None
    self.__referenceLocationCitation = None
    self.__commentText = None

  @property
  def monitoringLocationIdentifier(self) -> MonitoringLocationIdentifier:
    return self.__monitoringLocationIdentifier
  @monitoringLocationIdentifier.setter
  def monitoringLocationIdentifier(self, val:MonitoringLocationIdentifier) -> None:
    self.__monitoringLocationIdentifier = MonitoringLocationIdentifier(val)

  @property
  def locationWeightingFactorMeasure(self) -> MeasureCompact:
    """A measurement of the monitoring location selection weighting factor."""
    return self.__locationWeightingFactorMeasure
  @locationWeightingFactorMeasure.setter
  def locationWeightingFactorMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the monitoring location selection weighting factor."""
    self.__locationWeightingFactorMeasure = MeasureCompact(val)

  @property
  def statisticalStratumText(self) -> StatisticalStratumText:
    return self.__statisticalStratumText
  @statisticalStratumText.setter
  def statisticalStratumText(self, val:StatisticalStratumText) -> None:
    self.__statisticalStratumText = None if val is None else StatisticalStratumText(val)

  @property
  def locationCategoryName(self) -> LocationCategoryName:
    return self.__locationCategoryName
  @locationCategoryName.setter
  def locationCategoryName(self, val:LocationCategoryName) -> None:
    self.__locationCategoryName = None if val is None else LocationCategoryName(val)

  @property
  def locationStatusName(self) -> LocationStatusName:
    return self.__locationStatusName
  @locationStatusName.setter
  def locationStatusName(self, val:LocationStatusName) -> None:
    self.__locationStatusName = None if val is None else LocationStatusName(val)

  @property
  def referenceLocationTypeCode(self) -> ReferenceLocationTypeCode:
    return self.__referenceLocationTypeCode
  @referenceLocationTypeCode.setter
  def referenceLocationTypeCode(self, val:ReferenceLocationTypeCode) -> None:
    self.__referenceLocationTypeCode = None if val is None else ReferenceLocationTypeCode(val)

  @property
  def referenceLocationStartDate(self) -> ReferenceLocationStartDate:
    return self.__referenceLocationStartDate
  @referenceLocationStartDate.setter
  def referenceLocationStartDate(self, val:ReferenceLocationStartDate) -> None:
    self.__referenceLocationStartDate = None if val is None else ReferenceLocationStartDate(val)

  @property
  def referenceLocationEndDate(self) -> ReferenceLocationEndDate:
    return self.__referenceLocationEndDate
  @referenceLocationEndDate.setter
  def referenceLocationEndDate(self, val:ReferenceLocationEndDate) -> None:
    self.__referenceLocationEndDate = None if val is None else ReferenceLocationEndDate(val)

  @property
  def referenceLocationCitation(self) -> BibliographicReference:
    """Identifes the source that created or defined the Reference Location."""
    return self.__referenceLocationCitation
  @referenceLocationCitation.setter
  def referenceLocationCitation(self, val:BibliographicReference) -> None:
    """Identifes the source that created or defined the Reference Location."""
    self.__referenceLocationCitation = None if val is None else BibliographicReference(val)

  @property
  def commentText(self) -> CommentText:
    return self.__commentText
  @commentText.setter
  def commentText(self, val:CommentText) -> None:
    self.__commentText = None if val is None else CommentText(val)

  def generateXML(self):
    if self.__monitoringLocationIdentifier is None:
      WQXException("Attribute 'monitoringLocationIdentifier' is required.")
    if self.__locationWeightingFactorMeasure is None:
      WQXException("Attribute 'measureCompact' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MonitoringLocationIdentifier', self.__monitoringLocationIdentifier)
    with tag('LocationWeightingFactorMeasure'):
      doc.asis(self.__locationWeightingFactorMeasure.generateXML())
    if self.__statisticalStratumText is not None:
      line('StatisticalStratumText', self.__statisticalStratumText)
    if self.__locationCategoryName is not None:
      line('LocationCategoryName', self.__locationCategoryName)
    if self.__locationStatusName is not None:
      line('LocationStatusName', self.__locationStatusName)
    if self.__referenceLocationTypeCode is not None:
      line('ReferenceLocationTypeCode', self.__referenceLocationTypeCode)
    if self.__referenceLocationStartDate is not None:
      line('ReferenceLocationStartDate', self.__referenceLocationStartDate)
    if self.__referenceLocationEndDate is not None:
      line('ReferenceLocationEndDate', self.__referenceLocationEndDate)
    if self.__referenceLocationCitation is not None:
      with tag('ReferenceLocationCitation'):
        doc.asis(self.__referenceLocationCitation.generateXML())
    if self.__commentText is not None:
      line('CommentText', self.__commentText)
