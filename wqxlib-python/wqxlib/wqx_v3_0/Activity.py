from typing import List
from yattag import Doc, indent
from .ActivityDescription import ActivityDescription
from .ActivityLocation import ActivityLocation
from .BiologicalActivityDescription import BiologicalActivityDescription
from .SampleDescription import SampleDescription
from .ActivityMetric import ActivityMetric
from .AttachedBinaryObject import AttachedBinaryObject
from .Result import Result
from ..common import WQXException

class Activity:
  """Allows for the reporting of monitoring activities conducted at a Monitoring Location."""

  __activityDescription: ActivityDescription
  __activityLocation: ActivityLocation
  __biologicalActivityDescription: BiologicalActivityDescription
  __sampleDescription: SampleDescription
  __activityMetric: List[ActivityMetric]
  __attachedBinaryObject: List[AttachedBinaryObject]
  __result: List[Result]

  def __init__(self):
    self.__activityDescription = None
    self.__activityLocation = None
    self.__biologicalActivityDescription = None
    self.__sampleDescription = None
    self.__activityMetric = None
    self.__attachedBinaryObject = None
    self.__result = None

  @property
  def activityDescription(self) -> ActivityDescription:
    return self.__activityDescription
  @activityDescription.setter
  def activityDescription(self, val:ActivityDescription) -> None:
    self.__activityDescription = val

  @property
  def activityLocation(self) -> ActivityLocation:
    return self.__activityLocation
  @activityLocation.setter
  def activityLocation(self, val:ActivityLocation) -> None:
    self.__activityLocation = None if val is None else ActivityLocation(val)

  @property
  def biologicalActivityDescription(self) -> BiologicalActivityDescription:
    return self.__biologicalActivityDescription
  @biologicalActivityDescription.setter
  def biologicalActivityDescription(self, val:BiologicalActivityDescription) -> None:
    self.__biologicalActivityDescription = None if val is None else BiologicalActivityDescription(val)

  @property
  def sampleDescription(self) -> SampleDescription:
    return self.__sampleDescription
  @sampleDescription.setter
  def sampleDescription(self, val:SampleDescription) -> None:
    self.__sampleDescription = None if val is None else SampleDescription(val)

  @property
  def activityMetric(self) -> List[ActivityMetric]:
    return self.__activityMetric
  @activityMetric.setter
  def activityMetric(self, val:List[ActivityMetric]) -> None:
    self.__activityMetric = val

  @property
  def attachedBinaryObject(self) -> List[AttachedBinaryObject]:
    return self.__attachedBinaryObject
  @attachedBinaryObject.setter
  def attachedBinaryObject(self, val:List[AttachedBinaryObject]) -> None:
    self.__attachedBinaryObject = val

  @property
  def result(self) -> List[Result]:
    return self.__result
  @result.setter
  def result(self, val:List[Result]) -> None:
    self.__result = val

  def generateXML(self):
    if self.__activityDescription is None:
      WQXException("Attribute 'activityDescription' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag('ActivityDescription'):
      doc.asis(self.__activityDescription.generateXML())
    with tag('ActivityLocation'):
      doc.asis(self.__activityLocation.generateXML())
    with tag('BiologicalActivityDescription'):
      doc.asis(self.__biologicalActivityDescription.generateXML())
    with tag('SampleDescription'):
      doc.asis(self.__sampleDescription.generateXML())
    for x in self.__activityMetric:
      with tag('ActivityMetric'):
        doc.asis(x.generateXML())
    for x in self.__attachedBinaryObject:
      with tag('AttachedBinaryObject'):
        doc.asis(x.generateXML())
    for x in self.__result:
      with tag('Result'):
        doc.asis(x.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)
