from yattag import Doc, indent
from .FrequencyClassInformation import FrequencyClassInformation
from .MeasureCompact import MeasureCompact
from .SimpleContent import (
  BiologicalIntentName,
  BiologicalIndividualIdentifier,
  SubjectTaxonomicName,
  SubjectTaxonomicNameUserSupplied,
  SubjectTaxonomicNameUserSuppliedReferenceText,
  UnidentifiedSpeciesIdentifier,
  SampleTissueAnatomyName,
  GroupSummaryCount
)
from .TaxonomicDetails import TaxonomicDetails
from ..WQXException import WQXException

class BiologicalResultDescription:
  """Allows for the reporting of biological result information."""

  __biologicalIntentName: BiologicalIntentName
  __biologicalIndividualIdentifier: BiologicalIndividualIdentifier
  __subjectTaxonomicName: SubjectTaxonomicName
  __subjectTaxonomicNameUserSupplied: SubjectTaxonomicNameUserSupplied
  __subjectTaxonomicNameUserSuppliedReferenceText: SubjectTaxonomicNameUserSuppliedReferenceText
  __unidentifiedSpeciesIdentifier: UnidentifiedSpeciesIdentifier
  __sampleTissueAnatomyName: SampleTissueAnatomyName
  __groupSummaryCount: GroupSummaryCount
  __groupSummaryWeightMeasure: MeasureCompact
  __taxonomicDetails: TaxonomicDetails
  __frequencyClassInformation: FrequencyClassInformation

  def __init__(self):
    self.__biologicalIntentName = None
    self.__biologicalIndividualIdentifier = None
    self.__subjectTaxonomicName = None
    self.__subjectTaxonomicNameUserSupplied = None
    self.__subjectTaxonomicNameUserSuppliedReferenceText = None
    self.__unidentifiedSpeciesIdentifier = None
    self.__sampleTissueAnatomyName = None
    self.__groupSummaryCount = None
    self.__groupSummaryWeightMeasure = None
    self.__taxonomicDetails = None
    self.__frequencyClassInformation = None

  @property
  def biologicalIntentName(self) -> BiologicalIntentName:
    return self.__biologicalIntentName
  @biologicalIntentName.setter
  def biologicalIntentName(self, val:BiologicalIntentName) -> None:
    self.__biologicalIntentName = BiologicalIntentName(val)

  @property
  def biologicalIndividualIdentifier(self) -> BiologicalIndividualIdentifier:
    return self.__biologicalIndividualIdentifier
  @biologicalIndividualIdentifier.setter
  def biologicalIndividualIdentifier(self, val:BiologicalIndividualIdentifier) -> None:
    self.__biologicalIndividualIdentifier = None if val is None else BiologicalIndividualIdentifier(val)

  @property
  def subjectTaxonomicName(self) -> SubjectTaxonomicName:
    return self.__subjectTaxonomicName
  @subjectTaxonomicName.setter
  def subjectTaxonomicName(self, val:SubjectTaxonomicName) -> None:
    self.__subjectTaxonomicName = SubjectTaxonomicName(val)

  @property
  def subjectTaxonomicNameUserSupplied(self) -> SubjectTaxonomicNameUserSupplied:
    return self.__subjectTaxonomicNameUserSupplied
  @subjectTaxonomicNameUserSupplied.setter
  def subjectTaxonomicNameUserSupplied(self, val:SubjectTaxonomicNameUserSupplied) -> None:
    self.__subjectTaxonomicNameUserSupplied = None if val is None else SubjectTaxonomicNameUserSupplied(val)

  @property
  def subjectTaxonomicNameUserSuppliedReferenceText(self) -> SubjectTaxonomicNameUserSuppliedReferenceText:
    return self.__subjectTaxonomicNameUserSuppliedReferenceText
  @subjectTaxonomicNameUserSuppliedReferenceText.setter
  def subjectTaxonomicNameUserSuppliedReferenceText(self, val:SubjectTaxonomicNameUserSuppliedReferenceText) -> None:
    self.__subjectTaxonomicNameUserSuppliedReferenceText = None if val is None else SubjectTaxonomicNameUserSuppliedReferenceText(val)

  @property
  def unidentifiedSpeciesIdentifier(self) -> UnidentifiedSpeciesIdentifier:
    return self.__unidentifiedSpeciesIdentifier
  @unidentifiedSpeciesIdentifier.setter
  def unidentifiedSpeciesIdentifier(self, val:UnidentifiedSpeciesIdentifier) -> None:
    self.__unidentifiedSpeciesIdentifier = None if val is None else UnidentifiedSpeciesIdentifier(val)

  @property
  def sampleTissueAnatomyName(self) -> SampleTissueAnatomyName:
    return self.__sampleTissueAnatomyName
  @sampleTissueAnatomyName.setter
  def sampleTissueAnatomyName(self, val:SampleTissueAnatomyName) -> None:
    self.__sampleTissueAnatomyName = None if val is None else SampleTissueAnatomyName(val)

  @property
  def groupSummaryCount(self) -> GroupSummaryCount:
    """Captures the total count or total sample weight for a Group Summary."""
    return self.__groupSummaryCount
  @groupSummaryCount.setter
  def groupSummaryCount(self, val:GroupSummaryCount) -> None:
    """Captures the total count or total sample weight for a Group Summary."""
    self.__groupSummaryCount = None if val is None else GroupSummaryCount(val)

  @property
  def groupSummaryWeightMeasure(self) -> MeasureCompact:
    return self.__groupSummaryWeightMeasure
  @groupSummaryWeightMeasure.setter
  def groupSummaryWeightMeasure(self, val:MeasureCompact) -> None:
    self.__groupSummaryWeightMeasure = None if val is None else MeasureCompact(val)

  @property
  def taxonomicDetails(self) -> TaxonomicDetails:
    return self.__taxonomicDetails
  @taxonomicDetails.setter
  def taxonomicDetails(self, val:TaxonomicDetails) -> None:
    self.__taxonomicDetails = None if val is None else TaxonomicDetails(val)

  @property
  def frequencyClassInformation(self) -> FrequencyClassInformation:
    return self.__frequencyClassInformation
  @frequencyClassInformation.setter
  def frequencyClassInformation(self, val:FrequencyClassInformation) -> None:
    self.__frequencyClassInformation = None if val is None else FrequencyClassInformation(val)


  def generateXML(self):
    if self.__biologicalIntentName is None:
      raise WQXException("Attribute 'biologicalIntentName' is required.")
    if self.__subjectTaxonomicName is None:
      raise WQXException("Attribute 'subjectTaxonomicName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('BiologicalIntentName',self.__biologicalIntentName)
    if self.__biologicalIndividualIdentifier is not None:
      line('BiologicalIndividualIdentifier', self.__biologicalIndividualIdentifier)
    line('SubjectTaxonomicName',self.__subjectTaxonomicName)
    if self.__subjectTaxonomicNameUserSupplied is not None:
      line('SubjectTaxonomicNameUserSupplied', self.__subjectTaxonomicNameUserSupplied)
    if self.__subjectTaxonomicNameUserSuppliedReferenceText is not None:
      line('SubjectTaxonomicNameUserSuppliedReferenceText', self.__subjectTaxonomicNameUserSuppliedReferenceText)
    if self.__unidentifiedSpeciesIdentifier is not None:
      line('UnidentifiedSpeciesIdentifier', self.__unidentifiedSpeciesIdentifier)
    if self.__sampleTissueAnatomyName is not None:
      line('SampleTissueAnatomyName', self.__sampleTissueAnatomyName)
    if self.__groupSummaryCount is not None:
      line('GroupSummaryCount', self.__groupSummaryCount)
    if self.__groupSummaryWeightMeasure is not None:
      line('MeasureCompact', self.__groupSummaryWeightMeasure)
    if self.__taxonomicDetails is not None:
      line('TaxonomicDetails', self.__taxonomicDetails)
    for x in self.__frequencyClassInformation:
      line('FrequencyClassInformation', x)

    return indent(doc.getvalue(), indentation = ' '*2)
