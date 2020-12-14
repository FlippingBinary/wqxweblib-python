from datetime import date
from typing import List
from yattag import Doc, indent
from .BinaryObject import BinaryObject
from .Measure import Measure
from .Resource import Resource
from .WQXException import WQXException

class ProjectMonitoringLocationWeighting:
  __commentText: str # optional
  __locationCategoryName: str # optional
  __locationStatusName: str # optional
  __locationWeightingFactorMeasure: Measure # required
  __monitoringLocationIdentifier: str # required
  __referenceLocationCitation: Resource # optional
  __referenceLocationEndDate: date # optional
  __referenceLocationStartDate: date # optional
  __referenceLocationTypeCode: str # optional, constrained
  __statisticalStratumText: str # optional

  def __init__(self):
    self.__commentText = None
    self.__locationCategoryName = None
    self.__locationStatusName = None
    self.__referenceLocationCitation = None
    self.__referenceLocationEndDate = None
    self.__referenceLocationStartDate = None
    self.__referenceLocationTypeCode = None
    self.__statisticalStratumText = None

  @property
  def commentText(self) -> str:
    return self.__commentText
  @commentText.setter
  def commentText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'commentText' must be a string, if provided.")
    self.__commentText = val

  @property
  def locationCategoryName(self) -> str:
    return self.__locationCategoryName
  @locationCategoryName.setter
  def locationCategoryName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'locationCategoryName' must be a string, if provided.")
    self.__locationCategoryName = val

  @property
  def locationStatusName(self) -> str:
    return self.__locationStatusName
  @locationStatusName.setter
  def locationStatusName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'locationStatusName' must be a string, if provided.")
    self.__locationStatusName = val

  @property
  def locationWeightingFactorMeasure(self) -> Measure:
    return self.__locationWeightingFactorMeasure
  @locationWeightingFactorMeasure.setter
  def locationWeightingFactorMeasure(self, val:Measure) -> None:
    if not isinstance(val, Measure):
      raise TypeError("Property 'locationWeightingFactorMeasure' must be a Measure object.")
    if len(val) < 1:
      raise TypeError("Property 'locationWeightingFactorMeasure' is required.")
    self.__locationWeightingFactorMeasure = val

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

  @property
  def referenceLocationCitation(self) -> Resource:
    return self.__referenceLocationCitation
  @referenceLocationCitation.setter
  def referenceLocationCitation(self, val:Resource) -> None:
    if val is not None and not isinstance(val, Resource):
      raise TypeError("Property 'referenceLocationCitation' must be a Resource object, if provided.")
    self.__referenceLocationCitation = val

  @property
  def referenceLocationEndDate(self) -> date:
    return self.__referenceLocationEndDate
  @referenceLocationEndDate.setter
  def referenceLocationEndDate(self, val:date) -> None:
    if val is not None and not isinstance(val, date):
      raise TypeError("Property 'referenceLocationEndDate' must be a date object, if provided.")
    self.__referenceLocationEndDate = val

  @property
  def referenceLocationStartDate(self) -> date:
    return self.__referenceLocationStartDate
  @referenceLocationStartDate.setter
  def referenceLocationStartDate(self, val:date) -> None:
    if val is not None and not isinstance(val, date):
      raise TypeError("Property 'referenceLocationStartDate' must be a date object, if provided.")
    self.__referenceLocationStartDate = val

  @property
  def referenceLocationTypeCode(self) -> str:
    return self.__referenceLocationTypeCode
  @referenceLocationTypeCode.setter
  def referenceLocationTypeCode(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'referenceLocationTypeCode' must be a string, if provided.")
    self.__referenceLocationTypeCode = val

  @property
  def statisticalStratumText(self) -> str:
    return self.__statisticalStratumText
  @statisticalStratumText.setter
  def statisticalStratumText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'statisticalStratumText' must be a string, if provided.")
    self.__statisticalStratumText = val

  def generateXML(self):
    if self.__monitoringLocationIdentifier is None:
      raise WQXException("Property 'monitoringLocationIdentifier' is required.")
    if self.__locationWeightingFactorMeasure is None:
      raise WQXException("Property 'locationWeightingFactorMeasure' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MonitoringLocationIdentifier', self.__monitoringLocationIdentifier)
    doc.asis(self.__locationWeightingFactorMeasure.generateXML())
    if self.__statisticalStratumText is not None:
      line('StatisticalStratumText', self.__statisticalStratumText)
    if self.__locationCategoryName is not None:
      line('LocationCategoryName', self.__locationCategoryName)
    if self.__locationStatusName is not None:
      line('LocationStatusName', self.__locationStatusName)
    if self.__referenceLocationTypeCode is not None:
      line('ReferenceLocationTypeCode', self.__referenceLocationTypeCode)
    if self.__referenceLocationStartDate is not None:
      line('ReferenceLocationStartDate', self.__referenceLocationStartDate)
    if self.__referenceLocationEndDate is not None:
      line('ReferenceLocationEndDate', self.__referenceLocationEndDate)
    if self.__referenceLocationCitation is not None:
      doc.asis(self.__referenceLocationCitation.generateXML())
    if self.__commentText is not None:
      line('CommentText', self.__commentText)

    return indent(doc.getvalue(), indentation = ' '*2)

class Project:
  __attachedBinaryObject: List[BinaryObject] # 0 or more
  __projectDescriptionText: str # optional
  __projectIdentifier: str # required
  __projectMonitoringLocationWeighting: List[ProjectMonitoringLocationWeighting] # 0 or more
  __projectName: str # required
  __qappApprovalAgencyName: str # optional
  __qappApprovedIndicator: str # optional
  __samplingDesignTypeCode: str # optional, constrained

  def __init__(self):
    self.__attachedBinaryObject = []
    self.__projectDescriptionText = None
    self.__projectMonitoringLocationWeighting = []
    self.__qappApprovalAgencyName = None
    self.__qappApprovedIndicator = None
    self.__samplingDesignTypeCode = None

  @property
  def projectIdentifier(self) -> str:
    return self.__projectIdentifier
  @projectIdentifier.setter
  def projectIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'projectIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'projectIdentifier' is required.")
    self.__projectIdentifier = val

  @property
  def projectName(self) -> str:
    return self.__projectName
  @projectName.setter
  def projectName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'projectName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'projectName' is required.")
    self.__projectName = val

  @property
  def projectDescriptionText(self) -> str:
    return self.__projectDescriptionText
  @projectDescriptionText.setter
  def projectDescriptionText(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'projectDescriptionText' must be a string, if provided.")
    self.__projectDescriptionText = val

  @property
  def samplingDesignTypeCode(self) -> str:
    return self.__samplingDesignTypeCode
  @samplingDesignTypeCode.setter
  def samplingDesignTypeCode(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'samplingDesignTypeCode' must be a string, if provided.")
    self.__samplingDesignTypeCode = val

  @property
  def qappApprovedIndicator(self) -> str:
    return self.__qappApprovedIndicator
  @qappApprovedIndicator.setter
  def qappApprovedIndicator(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'qappApprovedIndicator' must be a string, if provided.")
    self.__qappApprovedIndicator = val

  @property
  def qappApprovalAgencyName(self) -> str:
    return self.__qappApprovalAgencyName
  @qappApprovalAgencyName.setter
  def qappApprovalAgencyName(self, val:str) -> None:
    if val is not None and not isinstance(val, str):
      raise TypeError("Property 'qappApprovalAgencyName' must be a string, if provided.")
    self.__qappApprovalAgencyName = val

  @property
  def attachedBinaryObject(self) -> List[BinaryObject]:
    return self.__attachedBinaryObject
  @attachedBinaryObject.setter
  def attachedBinaryObject(self, val:List[BinaryObject]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'attachedBinaryObject' must be a list of 0 or more BinaryObject objects.")
    for i in val:
      if not isinstance(i, BinaryObject):
        raise TypeError("Property 'attachedBinaryObject must contain only BinaryObject objects.")
    self.__attachedBinaryObject = val

  @property
  def projectMonitoringLocationWeighting(self) -> List[ProjectMonitoringLocationWeighting]:
    return self.__projectMonitoringLocationWeighting
  @projectMonitoringLocationWeighting.setter
  def projectMonitoringLocationWeighting(self, val:List[ProjectMonitoringLocationWeighting]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'projectMonitoringLocationWeighting' must be a list of 0 or more ProjectMonitoringLocationWeighting objects.")
    for i in val:
      if not isinstance(i, ProjectMonitoringLocationWeighting):
        raise TypeError("Property 'projectMonitoringLocationWeighting must contain only ProjectMonitoringLocationWeighting objects.")
    self.__projectMonitoringLocationWeighting = val

  def generateXML(self):
    if self.__projectIdentifier is None:
      raise WQXException("Property 'projectIdentifier' is required.")
    if self.__projectName is None:
      raise WQXException("Property 'projectName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('ProjectIdentifier', self.__projectIdentifier)
    line('ProjectName', self.__projectName)
    if self.__projectDescriptionText is not None:
      line('ProjectDescriptionText', self.__projectDescriptionText)
    if self.__samplingDesignTypeCode is not None:
      line('SamplingDesignTypeCode', self.__samplingDesignTypeCode)
    if self.__qappApprovedIndicator is not None:
      line('QAPPApprovedIndicator', self.__qappApprovedIndicator)
    if self.__qappApprovalAgencyName is not None:
      line('QAPPApprovalAgencyName', self.__qappApprovalAgencyName)
    if self.__attachedBinaryObject is not None:
      for x in self.__attachedBinaryObject:
        doc.asis(x.generateXML())
    if self.__projectMonitoringLocationWeighting is not None:
      for x in self.__projectMonitoringLocationWeighting:
        doc.asis(x.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)
