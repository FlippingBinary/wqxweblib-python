from typing import List, Union
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

  def __init__(self, o=None, *,
    activityDescription:ActivityDescription = None,
    activityLocation:ActivityLocation = None,
    biologicalActivityDescription:BiologicalActivityDescription = None,
    sampleDescription:SampleDescription = None,
    activityMetric:List[ActivityMetric] = None,
    attachedBinaryObject:List[AttachedBinaryObject] = None,
    result:List[Result] = None
  ):
    if isinstance(o, Activity):
      # Assign attributes from object without typechecking
      self.__activityDescription = o.activityDescription
      self.__activityLocation = o.activityLocation
      self.__biologicalActivityDescription = o.biologicalActivityDescription
      self.__sampleDescription = o.sampleDescription
      self.__activityMetric = o.activityMetric
      self.__attachedBinaryObject = o.attachedBinaryObject
      self.__result = o.result
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.activityDescription = o.get('activityDescription', default = None)
      self.activityLocation = o.get('activityLocation', default = None)
      self.biologicalActivityDescription = o.get('biologicalActivityDescription', default = None)
      self.sampleDescription = o.get('sampleDescription', default = None)
      self.activityMetric = o.get(activityMetric, default = [])
      self.attachedBinaryObject = o.get('attachedBinaryObject', default = [])
      self.result = o.get('result', default = [])
    else:
      # Assign attributes from named keywords with typechecking
      self.activityDescription = activityDescription
      self.activityLocation = activityLocation
      self.biologicalActivityDescription = biologicalActivityDescription
      self.sampleDescription = sampleDescription
      self.activityMetric = activityMetric
      self.attachedBinaryObject = attachedBinaryObject
      self.result = result

  @property
  def activityDescription(self) -> ActivityDescription:
    return self.__activityDescription
  @activityDescription.setter
  def activityDescription(self, val:ActivityDescription) -> None:
    self.__activityDescription = None if val is None else ActivityDescription(val)

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
  def activityMetric(self, val:Union[ActivityMetric,List[ActivityMetric]]) -> None:
    if val is None:
      self.__activityMetric = []
    elif isinstance(val, list):
      r:List[ActivityMetric] = []
      for x in val:
        r.append(ActivityMetric(x))
      self.__activityMetric = r
    else:
      self.__activityMetric = [ActivityMetric(val)]

  @property
  def attachedBinaryObject(self) -> List[AttachedBinaryObject]:
    return self.__attachedBinaryObject
  @attachedBinaryObject.setter
  def attachedBinaryObject(self, val:Union[AttachedBinaryObject,List[AttachedBinaryObject]]) -> None:
    if val is None:
      self.__attachedBinaryObject = []
    elif isinstance(val, list):
      r:List[AttachedBinaryObject] = []
      for x in val:
        r.append(AttachedBinaryObject(x))
      self.__attachedBinaryObject = r
    else:
      self.__attachedBinaryObject = [AttachedBinaryObject(val)]

  @property
  def result(self) -> List[Result]:
    return self.__result
  @result.setter
  def result(self, val:Union[Result,List[Result]]) -> None:
    if val is None:
      self.__result = []
    elif isinstance(val, list):
      r:List[Result] = []
      for x in val:
        r.append(Result(x))
      self.__result = r
    else:
      self.__result = [Result(val)]

  def generateXML(self):

    doc, tag, text, line = Doc().ttl()

    with tag('ActivityDescription'):
      if self.__activityDescription is None:
        raise WQXException("Attribute 'activityDescription' is required.")
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

    return doc.getvalue()
