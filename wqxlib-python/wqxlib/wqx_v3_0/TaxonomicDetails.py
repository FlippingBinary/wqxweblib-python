from typing import List
from yattag import Doc, indent
from .BibliographicReference import BibliographicReference
from .SimpleContent import (
  CellFormName,
  CellShapeName,
  HabitName,
  VoltinismName,
  TaxonomicPollutionTolerance,
  TaxonomicPollutionToleranceScaleText,
  TrophicLevelName,
  FunctionalFeedingGroupName
)

class TaxonomicDetails:
  """This section allows for the further definition of user-defined details for taxa."""

  __cellFormName: CellFormName
  __cellShapeName: CellShapeName
  __habitName: HabitName
  __voltinismName: VoltinismName
  __taxonomicPollutionTolerance: TaxonomicPollutionTolerance
  __taxonomicPollutionToleranceScaleText: TaxonomicPollutionToleranceScaleText
  __trophicLevelName: TrophicLevelName
  __functionalFeedingGroupName: FunctionalFeedingGroupName
  __taxonomicDetailsCitation: BibliographicReference

  def __init__(self):
    self.__cellFormName = None
    self.__cellShapeName = None
    self.__habitName = None
    self.__voltinismName = None
    self.__taxonomicPollutionTolerance = None
    self.__taxonomicPollutionToleranceScaleText = None
    self.__trophicLevelName = None
    self.__functionalFeedingGroupName = None
    self.__taxonomicDetailsCitation = None

  @property
  def cellFormName(self) -> CellFormName:
    return self.__cellFormName
  @cellFormName.setter
  def cellFormName(self, val:CellFormName) -> None:
    self.__cellFormName = None if val is None else CellFormName(val)

  @property
  def cellShapeName(self) -> CellShapeName:
    return self.__cellShapeName
  @cellShapeName.setter
  def cellShapeName(self, val:CellShapeName) -> None:
    self.__cellShapeName = None if val is None else CellShapeName(val)

  @property
  def habitName(self) -> HabitName:
    return self.__habitName
  @habitName.setter
  def habitName(self, val:List[HabitName]) -> None:
    if not isinstance(val, list) or val.length > 3:
      raise ValueError("Attribute habitName must be a list with 0 to 3 values.")
    self.__habitName = val

  @property
  def voltinismName(self) -> VoltinismName:
    return self.__voltinismName
  @voltinismName.setter
  def voltinismName(self, val:VoltinismName) -> None:
    self.__voltinismName = None if val is None else VoltinismName(val)

  @property
  def taxonomicPollutionTolerance(self) -> TaxonomicPollutionTolerance:
    return self.__taxonomicPollutionTolerance
  @taxonomicPollutionTolerance.setter
  def taxonomicPollutionTolerance(self, val:TaxonomicPollutionTolerance) -> None:
    self.__taxonomicPollutionTolerance = None if val is None else TaxonomicPollutionTolerance(val)

  @property
  def taxonomicPollutionToleranceScaleText(self) -> TaxonomicPollutionToleranceScaleText:
    return self.__taxonomicPollutionToleranceScaleText
  @taxonomicPollutionToleranceScaleText.setter
  def taxonomicPollutionToleranceScaleText(self, val:TaxonomicPollutionToleranceScaleText) -> None:
    self.__taxonomicPollutionToleranceScaleText = None if val is None else TaxonomicPollutionToleranceScaleText(val)

  @property
  def trophicLevelName(self) -> TrophicLevelName:
    return self.__trophicLevelName
  @trophicLevelName.setter
  def trophicLevelName(self, val:TrophicLevelName) -> None:
    self.__trophicLevelName = None if val is None else TrophicLevelName(val)

  @property
  def functionalFeedingGroupName(self) -> FunctionalFeedingGroupName:
    return self.__functionalFeedingGroupName
  @functionalFeedingGroupName.setter
  def functionalFeedingGroupName(self, val:List[FunctionalFeedingGroupName]) -> None:
    if not isinstance(val, list) or val.length > 3:
      ValueError("Attribute functionalFeedingGroupName must be a list with 0 to 3 values.")
    self.__functionalFeedingGroupName = val

  @property
  def taxonomicDetailsCitation(self) -> BibliographicReference:
    return self.__taxonomicDetailsCitation
  @taxonomicDetailsCitation.setter
  def taxonomicDetailsCitation(self, val:BibliographicReference) -> None:
    self.__taxonomicDetailsCitation = None if val is None else BibliographicReference(val)

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__cellFormName is not None:
      line('CellFormName', self.__cellFormName)
    if self.__cellShapeName is not None:
      line('CellShapeName', self.__cellShapeName)
    for x in self.__HabitName:
      line('HabitName', x)
    if self.__voltinismName is not None:
      line('VoltinismName', self.__voltinismName)
    if self.__taxonomicPollutionTolerance is not None:
      line('TaxonomicPollutionTolerance', self.__taxonomicPollutionTolerance)
    if self.__taxonomicPollutionToleranceScaleText is not None:
      line('TaxonomicPollutionToleranceScaleText', self.__taxonomicPollutionToleranceScaleText)
    if self.__trophicLevelName is not None:
      line('TrophicLevelName', self.__trophicLevelName)
    for x in self.__FunctionalFeedingGroupName:
      line('FunctionalFeedingGroupName', x)
    if self.__taxonomicDetailsCitation is not None:
      line('TaxonomicDetailsCitation', self.__taxonomicDetailsCitation)

    return indent(doc.getvalue(), indentation = ' '*2)
