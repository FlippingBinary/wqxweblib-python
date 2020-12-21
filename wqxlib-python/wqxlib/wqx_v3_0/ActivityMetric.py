from yattag import Doc, indent
from .ActivityMetricType import ActivityMetricType
from .MeasureCompact import MeasureCompact
from .SimpleContent import *
from ..WQXException import WQXException

class ActivityMetric:
  """This section allows for the reporting of metrics to support habitat or biotic integrity indices."""

  __activityMetricType: ActivityMetricType
  __metricValueMeasure: MeasureCompact
  __metricScore: MetricScore
  __metricSamplingPointPlaceInSeries: MetricSamplingPointPlaceInSeries
  __metricCommentText: CommentText
  __indexIdentifier: IndexIdentifier

  def __init__(self):
    self.__activityMetricType = None
    self.__metricValueMeasure = None
    self.__metricScore = None
    self.__metricSamplingPointPlaceInSeries = None
    self.__metricCommentText = None
    self.__indexIdentifier = None

  @property
  def activityMetricType(self) -> ActivityMetricType:
    return self.__activityMetricType
  @activityMetricType.setter
  def activityMetricType(self, val:ActivityMetricType) -> None:
    self.__activityMetricType = val

  @property
  def metricValueMeasure(self) -> MeasureCompact:
    """A non-scaled value calculated from raw results that may be scaled into a metric score."""
    return self.__metricValueMeasure
  @metricValueMeasure.setter
  def metricValueMeasure(self, val:MeasureCompact) -> None:
    """A non-scaled value calculated from raw results that may be scaled into a metric score."""
    self.__metricValueMeasure = val

  @property
  def metricScore(self) -> MetricScore:
    return self.__metricScore
  @metricScore.setter
  def metricScore(self, val:MetricScore) -> None:
    self.__metricScore = val

  @property
  def metricSamplingPointPlaceInSeries(self) -> MetricSamplingPointPlaceInSeries:
    return self.__metricSamplingPointPlaceInSeries
  @metricSamplingPointPlaceInSeries.setter
  def metricSamplingPointPlaceInSeries(self, val:MetricSamplingPointPlaceInSeries):
    self.__metricSamplingPointPlaceInSeries = None if val is None else MetricSamplingPointPlaceInSeries(val)

  @property
  def metricCommentText(self) -> CommentText:
    """Free text with general comments concerning the metric."""
    return self.__metricCommentText
  @metricCommentText.setter
  def metricCommentText(self, val:CommentText) -> None:
    """Free text with general comments concerning the metric."""
    self.__metricCommentText = val

  @property
  def indexIdentifier(self) -> IndexIdentifier:
    return self.__indexIdentifier
  @indexIdentifier.setter
  def indexIdentifier(self, val:IndexIdentifier) -> None:
    self.__indexIdentifier = val

  def generateXML(self):
    if self.__activityMetricType is None:
      WQXException("Attribute 'activityMetricType' is required.")
    if self.__metricScore is None:
      WQXException("Attribute 'metricScore' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag('ActivityMetricType'):
      doc.asis(self.__activityMetricType.generateXML())
    if self.__metricValueMeasure is not None:
      with tag('MetricValueMeasure'):
        doc.asis(self.__metricValueMeasure.generateXML())
    line('MetricScore', self.__metricScore)
    if self.__metricSamplingPointPlaceInSeries is not None:
      with tag('MetricSamplingPointPlaceInSeries'):
        doc.asis(self.__metricSamplingPointPlaceInSeries.generateXML())
    if self.__metricCommentText is not None:
      line('MetricCommentText', self.__metricCommentText)
    if self.__indexIdentifier is not None:
      line('IndexIdentifier', self.__indexIdentifier)

    return indent(doc.getvalue(), indentation = ' '*2)
