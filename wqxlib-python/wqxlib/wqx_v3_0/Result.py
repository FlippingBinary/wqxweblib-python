from typing import List
from yattag import Doc, indent
from .AttachedBinaryObject import AttachedBinaryObject
from .BiologicalResultDescription import BiologicalResultDescription
from .ComparableAnalyticalMethod import ComparableAnalyticalMethod
from .LabSamplePreparation import LabSamplePreparation
from .ResultAnalyticalMethod import ResultAnalyticalMethod
from .ResultDescription import ResultDescription
from .ResultLabInformation import ResultLabInformation
from ..WQXException import WQXException

class Result:
  """Describes the results of a field measurement, observation, or laboratory analysis."""
  __resultDescription: ResultDescription
  __biologicalResultDescription: BiologicalResultDescription
  __attachedBinaryObject: List[AttachedBinaryObject]
  __resultAnalyticalMethod: ResultAnalyticalMethod
  __comparableAnalyticalMethod: ComparableAnalyticalMethod
  __resultLabInformation: ResultLabInformation
  __labSamplePreparation: List[LabSamplePreparation]

  def __init__(self):
    self.__resultDescription = None
    self.__biologicalResultDescription = None
    self.__attachedBinaryObject = None
    self.__resultAnalyticalMethod = None
    self.__comparableAnalyticalMethod = None
    self.__resultLabInformation = None
    self.__labSamplePreparation = None

  @property
  def resultDescription(self) -> ResultDescription:
    return self.__resultDescription
  @resultDescription.setter
  def resultDescription(self, val:ResultDescription) -> None:
    self.__resultDescription = None if val is None else ResultDescription(val)

  @property
  def biologicalResultDescription(self) -> BiologicalResultDescription:
    return self.__biologicalResultDescription
  @biologicalResultDescription.setter
  def biologicalResultDescription(self, val:BiologicalResultDescription) -> None:
    self.__biologicalResultDescription = BiologicalResultDescription(val)

  @property
  def attachedBinaryObject(self) -> List[AttachedBinaryObject]:
    return self.__attachedBinaryObject
  @attachedBinaryObject.setter
  def attachedBinaryObject(self, val:List[AttachedBinaryObject]) -> None:
    self.__attachedBinaryObject = val

  @property
  def resultAnalyticalMethod(self) -> ResultAnalyticalMethod:
    return self.__resultAnalyticalMethod
  @resultAnalyticalMethod.setter
  def resultAnalyticalMethod(self, val:ResultAnalyticalMethod) -> None:
    self.__resultAnalyticalMethod = None if val is None else ResultAnalyticalMethod(val)

  @property
  def comparableAnalyticalMethod(self) -> ComparableAnalyticalMethod:
    return self.__comparableAnalyticalMethod
  @comparableAnalyticalMethod.setter
  def comparableAnalyticalMethod(self, val:ComparableAnalyticalMethod) -> None:
    self.__comparableAnalyticalMethod = None if val is None else ComparableAnalyticalMethod(val)

  @property
  def resultLabInformation(self) -> ResultLabInformation:
    return self.__resultLabInformation
  @resultLabInformation.setter
  def resultLabInformation(self, val:ResultLabInformation) -> None:
    self.__resultLabInformation = None if val is None else ResultLabInformation(val)

  @property
  def labSamplePreparation(self) -> List[LabSamplePreparation]:
    return self.__labSamplePreparation
  @labSamplePreparation.setter
  def labSamplePreparation(self, val:List[LabSamplePreparation]) -> None:
    self.__labSamplePreparation = val

  def generateXML(self):
    if self.__resultDescription is None:
      raise WQXException("Attribute 'resultDescription' is required.")
    doc, tag, text, line = Doc().ttl()

    line('ResultDescription', self.__resultDescription)
    if self.__biologicalResultDescription is not None:
      line('BiologicalResultDescription', self.__biologicalResultDescription)
    for x in self.__attachedBinaryObject:
      line('AttachedBinaryObject', self.__attachedBinaryObject)
    if self.__resultAnalyticalMethod is not None:
      line('ResultAnalyticalMethod', self.__resultAnalyticalMethod)
    if self.__comparableAnalyticalMethod is not None:
      line('ComparableAnalyticalMethod', self.__comparableAnalyticalMethod)
    if self.__resultLabInformation is not None:
      line('ResultLabInformation', self.__resultLabInformation)
    for x in self.__labSamplePreparation:
      line('LabSamplePreparation', self.__labSamplePreparation)

    return indent(doc.getvalue(), indentation = ' '*2)
