from datetime import date
from yattag import Doc, indent
from .WQXException import WQXException

class Resource:
  __resourceCreatorName: str # optional
  __resourceDate: date # optional
  __resourcePublisherName: str # optional
  __resourceSubjectText: str # optional
  __resourceTitleName: str # required

  def __init__(self):
    self.__resourceCreatorName = None
    self.__resourceDate = None
    self.__resourcePublisherName = None
    self.__resourceSubjectText = None

  @property
  def resourceTitleName(self) -> str:
    return self.__resourceTitleName
  @resourceTitleName.setter
  def resourceTitleName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'resourceTitleName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'resourceTitleName' is required.")
    self.__resourceTitleName = val

  @property
  def resourceCreatorName(self) -> str:
    return self.__resourceCreatorName
  @resourceCreatorName.setter
  def resourceCreatorName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'resourceCreatorName' must be a string, if provided.")
    self.__resourceCreatorName = val

  @property
  def resourceSubjectText(self) -> str:
    return self.__resourceSubjectText
  @resourceSubjectText.setter
  def resourceSubjectText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'resourceSubjectText' must be a string, if provided.")
    self.__resourceSubjectText = val

  @property
  def resourcePublisherName(self) -> str:
    return self.__resourcePublisherName
  @resourcePublisherName.setter
  def resourcePublisherName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'resourcePublisherName' must be a string, if provided.")
    self.__resourcePublisherName = val

  @property
  def resourceDate(self) -> date:
    return self.__resourceDate
  @resourceDate.setter
  def resourceDate(self, val:date) -> None:
    if val is not None and not isinstance(val, date):
      raise TypeError("Property 'resourceDate' must be a date object, if provided.")
    self.__resourceDate = val

  def generateXML(self):
    if self.__resourceTitleName is None:
      raise WQXException("Property 'resourceTitleName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('ResourceTitleName', self.__resourceTitleName)
    if self.__resourceCreatorName is not None:
      line('ResourceCreatorName', self.__resourceCreatorName)
    if self.__resourceSubjectText is not None:
      line('ResourceSubjectText', self.__resourceSubjectText)
    if self.__resourcePublisherName is not None:
      line('ResourcePublisherName', self.__resourcePublisherName)
    if self.__resourceDate is not None:
      line('ResourceDate', self.__resourceDate)

    return indent(doc.getvalue(), indentation = ' '*2)

class IndexType:
  __indexTypeCitation: Resource # optional
  __indexTypeIdentifier: str # required
  __indexTypeIdentifierContext: str # required
  __indexTypeName: str # required
  __indexTypeScaleText: str # optional

  def __init__(self):
    self.__indexTypeCitation = None
    self.__indexTypeScaleText = None

  @property
  def indexTypeCitation(self) -> Resource:
    return self.__indexTypeCitation
  @indexTypeCitation.setter
  def indexTypeCitation(self, val:Resource) -> None:
    if val is not None and not isinstance(val, Resource):
      raise TypeError("Property 'indexTypeCitation' must be a Resource object, if provided.")
    self.__indexTypeCitation = val

  @property
  def indexTypeIdentifier(self) -> str:
    return self.__indexTypeIdentifier
  @indexTypeIdentifier.setter
  def indexTypeIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'indexTypeIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'indexTypeIdentifier' is required.")
    self.__indexTypeIdentifier = val

  @property
  def indexTypeIdentifierContext(self) -> str:
    return self.__indexTypeIdentifierContext
  @indexTypeIdentifierContext.setter
  def indexTypeIdentifierContext(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'indexTypeIdentifierContext' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'indexTypeIdentifierContext' is required.")
    self.__indexTypeIdentifierContext = val

  @property
  def indexTypeName(self) -> str:
    return self.__indexTypeName
  @indexTypeName.setter
  def indexTypeName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'indexTypeName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'indexTypeName' is required.")
    self.__indexTypeName = val

  @property
  def indexTypeScaleText(self) -> str:
    return self.__indexTypeScaleText
  @indexTypeScaleText.setter
  def indexTypeScaleText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'indexTypeScaleText' must be a string, if provided.")
    self.__indexTypeScaleText = val

  def generateXML(self):
    if self.__indexTypeIdentifier is None:
      raise WQXException("Property 'indexIdentifier' is required.")
    if self.__indexTypeIdentifierContext is None:
      raise WQXException("Property 'indexTypeIdentifierContext' is required.")
    if self.__indexTypeName is None:
      raise WQXException("Property 'indexTypeName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('IndexTypeIdentifier', self.__indexTypeIdentifier)
    line('IndexTypeIdentifierContext', self.__indexTypeIdentifierContext)
    line('IndexTypeName', self.__indexTypeName)
    if self.__indexTypeCitation is not None:
      doc.asis(self.__indexTypeCitation.generateXML())
    if self.__indexTypeScaleText is not None:
      line('IndexTypeScaleText', self.__indexTypeScaleText)

    return indent(doc.getvalue(), indentation = ' '*2)

class BiologicalHabitatIndex:
  __indexIdentifier: str # required
  __indexType: IndexType # required
  __indexScore: str # required
  __indexQualifierCode: str # optional
  __indexCommentText: str # optional
  __indexCalculatedDate: date # optional
  __monitoringLocationIdentifier: str # required

  def __init__(self):
    self.__indexQualifierCode = None
    self.__indexCommentText = None
    self.__indexCalculatedDate = None

  @property
  def indexIdentifier(self) -> str:
    return self.__indexIdentifier
  @indexIdentifier.setter
  def indexIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'indexIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'indexIdentifier' is required.")
    self.__indexIdentifier = val

  @property
  def indexType(self) -> IndexType:
    return self.__indexType
  @indexType.setter
  def indexType(self, val:IndexType) -> None:
    if not isinstance(val, IndexType):
      raise TypeError("Property 'indexType' must be an IndexType object.")
    if len(val) < 1:
      raise TypeError("Property 'indexType' is required.")
    self.__indexType = val

  @property
  def indexScore(self) -> str:
    return self.__indexScore
  @indexScore.setter
  def indexScore(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'indexScore' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'indexScore' is required.")
    self.__indexScore = val

  @property
  def indexQualifierCode(self) -> str:
    return self.__indexQualifierCode
  @indexQualifierCode.setter
  def indexQualifierCode(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'indexQualifierCode' must be a string, if provided.")
    self.__indexQualifierCode = val

  @property
  def indexCommentText(self) -> str:
    return self.__indexCommentText
  @indexCommentText.setter
  def indexCommentText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'indexCommentText' must be a string, if provided.")
    self.__indexCommentText = val

  @property
  def indexCalculatedDate(self) -> date:
    return self.__indexCalculatedDate
  @indexCalculatedDate.setter
  def indexCalculatedDate(self, val:date) -> None:
    if val is not None and not isinstance(val, date):
      raise TypeError("Property 'indexCalculatedDate' must be a date object, if provided.")
    self.__indexCalculatedDate = val

  @property
  def monitoringLocationIdentifier(self) -> str:
    return self.__monitoringLocationIdentifier
  @monitoringLocationIdentifier.setter
  def monitoringLocationIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'monitoringLocationIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'monitoringLocationIdentifier' is required.")
    self.__monitoringLocationIdentifier = val

  def generateXML(self):
    if self.__indexIdentifier is None:
      raise WQXException("Property 'indexIdentifier' is required.")
    if self.__indexType is None:
      raise WQXException("Property 'indexType' is required.")
    if self.__indexScore is None:
      raise WQXException("Property 'indexScore' is required.")
    if self.__monitoringLocationIdentifier is None:
      raise WQXException("Property 'monitoringLocationIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    line('IndexIdentifier', self.__indexIdentifier)
    line('IndexType', self.__indexType)
    line('IndexScore', self.__indexScore)
    if self.__indexQualifierCode is not None:
      line('IndexQualifierCode', self.__indexQualifierCode)
    if self.__indexCommentText is not None:
      line('IndexCommentText', self.__indexCommentText)
    if self.__indexCalculatedDate is not None:
      line('IndexCalculatedDate', self.__indexCalculatedDate)
    line('MonitoringLocationIdentifier', self.__monitoringLocationIdentifier)

    return indent(doc.getvalue(), indentation = ' '*2)
