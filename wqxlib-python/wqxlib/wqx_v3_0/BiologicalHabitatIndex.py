from yattag import Doc, indent
from .IndexType import IndexType
from .SimpleContent import *
from ..common import WQXException

class BiologicalHabitatIndex:
  """This section allows for the reporting of habitat and biotic integrity indices as a representation of water quality conditions."""

  __indexIdentifier: IndexIdentifier
  __indexType: IndexType
  __indexScore: IndexScore
  __indexQualifierCode: IndexQualifierCode
  __indexCommentText: CommentText
  __indexCalculatedDate: IndexCalculatedDate
  __monitoringLocationIdentifier: MonitoringLocationIdentifier

  def __init__(self):
    self.__indexIdentifier = None
    self.__indexType = None
    self.__indexScore = None
    self.__indexQualifierCode = None
    self.__indexCommentText = None
    self.__indexCalculatedDate = None
    self.__monitoringLocationIdentifier = None

  @property
  def indexIdentifier(self) -> IndexIdentifier:
    return self.__indexIdentifier
  @indexIdentifier.setter
  def indexIdentifier(self, val:IndexIdentifier) -> None:
    self.__indexIdentifier = IndexIdentifier(val)

  @property
  def indexType(self) -> IndexType:
    return self.__indexType
  @indexType.setter
  def indexType(self, val:IndexType) -> None:
    self.__indexType = val

  @property
  def indexScore(self) -> IndexScore:
    return self.__indexScore
  @indexScore.setter
  def indexScore(self, val:IndexScore) -> None:
    self.__indexScore = IndexScore(val)

  @property
  def indexQualifierCode(self) -> IndexQualifierCode:
    return self.__indexQualifierCode
  @indexQualifierCode.setter
  def indexQualifierCode(self, val:IndexQualifierCode) -> None:
    self.__indexQualifierCode = None if val is None else IndexQualifierCode(val)

  @property
  def indexCommentText(self) -> CommentText:
    """Free text with general comments concerning the index."""
    return self.__indexCommentText
  @indexCommentText.setter
  def indexCommentText(self, val:CommentText) -> None:
    """Free text with general comments concerning the index."""
    self.__indexCommentText = val

  @property
  def indexCalculatedDate(self) -> IndexCalculatedDate:
    return self.__indexCalculatedDate
  @indexCalculatedDate.setter
  def indexCalculatedDate(self, val:IndexCalculatedDate) -> None:
    self.__indexCalculatedDate = None if val is None else IndexCalculatedDate(val)

  @property
  def monitoringLocationIdentifier(self) -> MonitoringLocationIdentifier:
    return self.__monitoringLocationIdentifier
  @monitoringLocationIdentifier.setter
  def monitoringLocationIdentifier(self, val:MonitoringLocationIdentifier) -> None:
    self.__monitoringLocationIdentifier = MonitoringLocationIdentifier(val)

  def generateXML(self):
    if self.__indexIdentifier is None:
      WQXException("Attribute 'indexIdentifier' is required.")
    if self.__indexType is None:
      WQXException("Attribute 'indexType' is required.")
    if self.__indexScore is None:
      WQXException("Attribute 'indexScore' is required.")
    if self.__monitoringLocationIdentifier is None:
      WQXException("Attribute 'monitoringLocationIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    line('IndexIdentifier', self.__indexIdentifier)
    with tag('IndexType'):
      doc.asis(self.__indexType.generateXML())
    line('IndexScore', self.__indexScore)
    if self.__indexQualifierCode is not None:
      line('IndexQualifierCode', self.__indexQualifierCode)
    if self.__indexCommentText is not None:
      line('IndexCommentText', self.__indexCommentText)
    if self.__indexCalculatedDate is not None:
      line('IndexCalculatedDate', self.__indexCalculatedDate)
    line('MonitoringLocationIdentifier', self.__monitoringLocationIdentifier)

    return doc.getvalue()
