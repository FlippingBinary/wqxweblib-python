from yattag import Doc, indent
from .ReferenceMethod import ReferenceMethod
from .SimpleContent import (
  PreparationStartDate,
  PreparationEndDate,
  SubstanceDilutionFactor
)
from .WQXTime import WQXTime

class LabSamplePreparation:
  """Describes Lab Sample Preparation procedures which may alter the original state of the Sample and produce Lab subsamples.  These Lab Subsamples are analyized and reported by the Lab as Sample results."""

  __labSamplePreparationMethod: ReferenceMethod
  __preparationStartDate: PreparationStartDate
  __preparationStartTime: WQXTime
  __preparationEndDate: PreparationEndDate
  __preparationEndTime: WQXTime
  __substanceDilutionFactor: SubstanceDilutionFactor

  def __init__(self):
    self.__labSamplePreparationMethod = None
    self.__preparationStartDate = None
    self.__preparationStartTime = None
    self.__preparationEndDate = None
    self.__preparationEndTime = None
    self.__substanceDilutionFactor = None

  @property
  def labSamplePreparationMethod(self) -> ReferenceMethod:
    """Identifying information about the method followed to prepare a sample for analysis."""
    return self.__labSamplePreparationMethod
  @labSamplePreparationMethod.setter
  def labSamplePreparationMethod(self, val:ReferenceMethod) -> None:
    """Identifying information about the method followed to prepare a sample for analysis."""
    self.__labSamplePreparationMethod = None if val is None else ReferenceMethod(val)

  @property
  def preparationStartDate(self) -> PreparationStartDate:
    return self.__preparationStartDate
  @preparationStartDate.setter
  def preparationStartDate(self, val:PreparationStartDate) -> None:
    self.__preparationStartDate = None if val is None else PreparationStartDate(val)

  @property
  def preparationStartTime(self) -> WQXTime:
    """The local time when the preparation/extraction of the sample for analysis began."""
    return self.__preparationStartTime
  @preparationStartTime.setter
  def preparationStartTime(self, val:WQXTime) -> None:
    """The local time when the preparation/extraction of the sample for analysis began."""
    self.__preparationStartTime = None if val is None else WQXTime(val)

  @property
  def preparationEndDate(self) -> PreparationEndDate:
    return self.__preparationEndDate
  @preparationEndDate.setter
  def preparationEndDate(self, val:PreparationEndDate) -> None:
    self.__preparationEndDate = None if val is None else PreparationEndDate(val)

  @property
  def preparationEndTime(self) -> WQXTime:
    """The local time when the preparation/extraction of the sample for analysis was finished."""
    return self.__preparationEndTime
  @preparationEndTime.setter
  def preparationEndTime(self, val:WQXTime) -> None:
    """The local time when the preparation/extraction of the sample for analysis was finished."""
    self.__preparationEndTime = None if val is None else WQXTime(val)

  @property
  def substanceDilutionFactor(self) -> SubstanceDilutionFactor:
    return self.__substanceDilutionFactor
  @substanceDilutionFactor.setter
  def substanceDilutionFactor(self, val:SubstanceDilutionFactor) -> None:
    self.__substanceDilutionFactor = None if val is None else SubstanceDilutionFactor(val)

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__labSamplePreparationMethod is not None:
      line('ReferenceMethod', self.__labSamplePreparationMethod)
    if self.__preparationStartDate is not None:
      line('PreparationStartDate', self.__preparationStartDate)
    if self.__preparationStartTime is not None:
      line('WQXTime', self.__preparationStartTime)
    if self.__preparationEndDate is not None:
      line('PreparationEndDate', self.__preparationEndDate)
    if self.__preparationEndTime is not None:
      line('WQXTime', self.__preparationEndTime)
    if self.__substanceDilutionFactor is not None:
      line('SubstanceDilutionFactor', self.__substanceDilutionFactor)

    return doc.getvalue()
