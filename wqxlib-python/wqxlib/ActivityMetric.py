from typing import List
from yattag import Doc, indent
from .Measure import Measure
from .Resource import Resource
from .WQXException import WQXException

class MetricType:
  __metricTypeIdentifier: str # required, conditionally constrained
  __metricTypeIdentifierContext: str # required, constrained
  __metricTypeName: str # optional
  __metricTypeCitation: Resource # optional
  __metricTypeScaleText: str # optional
  __formulaDescriptionText: str # optional

  def __init__(self):
    self.__metricTypeName = None
    self.__metricTypeCitation = None
    self.__metricTypeScaleText = None
    self.__formulaDescriptionText = None

  @property
  def metricTypeIdentifier(self) -> str:
    return self.__metricTypeIdentifier
  @metricTypeIdentifier.setter
  def metricTypeIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'metricTypeIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'metricTypeIdentifier' is required.")
    self.__metricTypeIdentifier = val

  @property
  def metricTypeIdentifierContext(self) -> str:
    return self.__metricTypeIdentifierContext
  @metricTypeIdentifierContext.setter
  def metricTypeIdentifierContext(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'metricTypeIdentifierContext' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'metricTypeIdentifierContext' is required.")
    self.__metricTypeIdentifierContext = val

  @property
  def metricTypeName(self) -> str:
    return self.__metricTypeName
  @metricTypeName.setter
  def metricTypeName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'metricTypeName' must be a string, if provided.")
    self.__metricTypeName = val

  @property
  def metricTypeCitation(self) -> Resource:
    return self.__metricTypeCitation
  @metricTypeCitation.setter
  def metricTypeCitation(self, val:Resource) -> None:
    if val is not None and not isinstance(val, Resource):
      raise TypeError("Property 'metricTypeCitation' must be a Resource object, if provided.")
    self.__metricTypeCitation = val

  @property
  def metricTypeScaleText(self) -> str:
    return self.__metricTypeScaleText
  @metricTypeScaleText.setter
  def metricTypeScaleText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'metricTypeScaleText' must be a string, if provided.")
    self.__metricTypeScaleText = val

  @property
  def formulaDescriptionText(self) -> str:
    return self.__formulaDescriptionText
  @formulaDescriptionText.setter
  def formulaDescriptionText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'formulaDescriptionText' must be a string, if provided.")
    self.__formulaDescriptionText = val

  def generateXML(self):
    if self.__metricTypeIdentifier is None:
      raise WQXException("Property 'metricTypeIdentifier' is required.")
    if self.__metricTypeIdentifierContext is None:
      raise WQXException("Property 'metricTypeIdentifierContext' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MetricTypeIdentifier', self.__metricTypeIdentifier)
    line('MetricTypeIdentifierContext', self.__metricTypeIdentifierContext)
    if self.__metricTypeName is not None:
      line('MetricTypeName', self.__metricTypeName)
    if self.__metricTypeCitation is not None:
      line('MetricTypeCitation', self.__metricTypeCitation)
    if self.__metricTypeCitation is not None:
      with tag('MetricTypeCitation'):
        doc.asis(self.__metricTypeCitation.generateXML())
    if self.__metricTypeScaleText is not None:
      line('MetricTypeScaleText', self.__metricTypeScaleText)
    if self.__formulaDescriptionText is not None:
      line('FormulaDescriptionText', self.__formulaDescriptionText)

    return indent(doc.getvalue(), indentation = ' '*2)

class ActivityMetric:
  __activityMetricType: MetricType # required
  __indexIdentifier: List[str] # 0 or more
  __metricCommentText: str # optional
  __metricSamplingPointPlaceInSeries: str # optional
  __metricScore: str # required
  __metricValueMeasure: Measure # optional

  def __init__(self):
    self.__indexIdentifier = []
    self.__metricCommentText = None
    self.__metricSamplingPointPlaceInSeries = None
    self.__metricValueMeasure = None

  @property
  def activityMetricType(self) -> MetricType:
    return self.__activityMetricType
  @activityMetricType.setter
  def activityMetricType(self, val:MetricType) -> None:
    if not isinstance(val, MetricType):
      raise TypeError("Property 'activityMetricType' must be a MetricType object.")
    if len(val) < 1:
      raise TypeError("Property 'activityMetricType' is required.")
    self.__activityMetricType = val

  @property
  def indexIdentifier(self) -> List[str]:
    return self.__indexIdentifier
  @indexIdentifier.setter
  def indexIdentifier(self, val:List[str]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'indexIdentifier' must be a list of strings.")
    for i in val:
      if not isinstance(i, str):
        raise TypeError("Property 'indexIdentifier must contain only strings.")
    self.__indexIdentifier = val

  @property
  def metricCommentText(self) -> str:
    return self.__metricCommentText
  @metricCommentText.setter
  def metricCommentText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'metricCommentText' must be a string, if provided.")
    self.__metricCommentText = val

  @property
  def metricSamplingPointPlaceInSeries(self) -> str:
    return self.__metricSamplingPointPlaceInSeries
  @metricSamplingPointPlaceInSeries.setter
  def metricSamplingPointPlaceInSeries(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'metricSamplingPointPlaceInSeries' must be a string, if provided.")
    self.__metricSamplingPointPlaceInSeries = val

  @property
  def metricScore(self) -> str:
    return self.__metricScore
  @metricScore.setter
  def metricScore(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'metricScore' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'metricScore' is required.")
    self.__metricScore = val

  @property
  def metricValueMeasure(self) -> Measure:
    return self.__metricValueMeasure
  @metricValueMeasure.setter
  def metricValueMeasure(self, val:Measure) -> None:
    if val is not None and not isinstance(val, Measure):
      raise TypeError("Property 'metricValueMeasure' must be a Measure object, if provided.")
    self.__metricValueMeasure = val

  def generateXML(self):
    if self.__activityGroupIdentifier is None:
      raise WQXException("Property 'activityGroupIdentifier' is required.")
    if self.__activityIdentifier is None or len(self.__activityIdentifier) < 2:
      raise WQXException("Property 'activityIdentifier' must be a list of 2 or more strings.")

    doc, tag, text, line = Doc().ttl()

    doc.asis(self.__activityMetricType.generateXML())
    if self.__metricValueMeasure is not None:
      doc.asis(self.__metricValueMeasure.generateXML())
    line('MetricScore', self.__metricScore)
    if self.__metricSamplingPointPlaceInSeries is not None:
      line('MetricSamplingPointPlaceInSeries', self.__metricSamplingPointPlaceInSeries)
    if self.__metricCommentText is not None:
      line('MetricCommentText', self.__metricCommentText)
    for x in self.__indexIdentifier:
      line('IndexIdentifier', x)

    return indent(doc.getvalue(), indentation = ' '*2)
