from typing import List
from yattag import Doc, indent
from .AttachedBinaryObject import AttachedBinaryObject
from .ProjectMonitoringLocationWeighting import ProjectMonitoringLocationWeighting
from .SimpleContent import *
from ..common import WQXException

class Project:
  """An environmental data collection effort that has a stated purpose and puts a series of samples and results into a meaningful context."""

  __projectIdentifier: ProjectIdentifier
  __projectName: ProjectName
  __projectDescriptionText: ProjectDescriptionText
  __samplingDesignTypeCode: SamplingDesignTypeCode
  __qAPPApprovedIndicator: QAPPApprovedIndicator
  __qAPPApprovalAgencyName: QAPPApprovalAgencyName
  __attachedBinaryObject: List[AttachedBinaryObject]
  __projectMonitoringLocationWeighting: List[ProjectMonitoringLocationWeighting]

  def __init__(self):
    self.__projectIdentifier = None
    self.__projectName = None
    self.__projectDescriptionText = None
    self.__samplingDesignTypeCode = None
    self.__qAPPApprovedIndicator = None
    self.__qAPPApprovalAgencyName = None
    self.__attachedBinaryObject = None
    self.__projectMonitoringLocationWeighting = None

  @property
  def projectIdentifier(self) -> ProjectIdentifier:
    return self.__projectIdentifier
  @projectIdentifier.setter
  def projectIdentifier(self, val:ProjectIdentifier) -> None:
    self.__projectIdentifier = ProjectIdentifier(val)

  @property
  def projectName(self) -> ProjectName:
    return self.__projectName
  @projectName.setter
  def projectName(self, val:ProjectName) -> None:
    self.__projectName = ProjectName(val)

  @property
  def projectDescriptionText(self) -> ProjectDescriptionText:
    return self.__projectDescriptionText
  @projectDescriptionText.setter
  def projectDescriptionText(self, val:ProjectDescriptionText) -> None:
    self.__projectDescriptionText = None if val is None else ProjectDescriptionText(val)

  @property
  def samplingDesignTypeCode(self) -> SamplingDesignTypeCode:
    return self.__samplingDesignTypeCode
  @samplingDesignTypeCode.setter
  def samplingDesignTypeCode(self, val:SamplingDesignTypeCode) -> None:
    self.__samplingDesignTypeCode = None if val is None else SamplingDesignTypeCode(val)

  @property
  def qAPPApprovedIndicator(self) -> QAPPApprovedIndicator:
    return self.__qAPPApprovedIndicator
  @qAPPApprovedIndicator.setter
  def qAPPApprovedIndicator(self, val:QAPPApprovedIndicator) -> None:
    self.__qAPPApprovedIndicator = None if val is None else QAPPApprovedIndicator(val)

  @property
  def qAPPApprovalAgencyName(self) -> QAPPApprovalAgencyName:
    return self.__qAPPApprovalAgencyName
  @qAPPApprovalAgencyName.setter
  def qAPPApprovalAgencyName(self, val:QAPPApprovalAgencyName) -> None:
    self.__qAPPApprovalAgencyName = None if val is None else QAPPApprovalAgencyName(val)

  @property
  def attachedBinaryObject(self) -> List[AttachedBinaryObject]:
    return self.__attachedBinaryObject
  @attachedBinaryObject.setter
  def attachedBinaryObject(self, val:List[AttachedBinaryObject]) -> None:
    self.__attachedBinaryObject = val

  @property
  def projectMonitoringLocationWeighting(self) -> List[ProjectMonitoringLocationWeighting]:
    return self.__projectMonitoringLocationWeighting
  @projectMonitoringLocationWeighting.setter
  def projectMonitoringLocationWeighting(self, val:List[ProjectMonitoringLocationWeighting]) -> None:
    self.__projectMonitoringLocationWeighting = val

  def generateXML(self):
    if self.__projectIdentifier is None:
      WQXException("Attribute 'projectIdentifier' is required.")
    if self.__projectName is None:
      WQXException("Attribute 'projectName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('ProjectIdentifier', self.__projectIdentifier)
    line('ProjectName', self.__projectName)
    if self.__projectDescriptionText is not None:
      line('ProjectDescriptionText', self.__projectDescriptionText)
    if self.__samplingDesignTypeCode is not None:
      line('SamplingDesignTypeCode', self.__samplingDesignTypeCode)
    if self.__qAPPApprovedIndicator is not None:
      line('QAPPApprovedIndicator', self.__qAPPApprovedIndicator)
    if self.__qAPPApprovalAgencyName is not None:
      line('QAPPApprovalAgencyName', self.__qAPPApprovalAgencyName)
    for x in self.__attachedBinaryObject:
      with tag('AttachedBinaryObject'):
        doc.asis(x.generateXML())
    for x in self.__projectMonitoringLocationWeighting:
      with tag('ProjectMonitoringLocationWeighting'):
        doc.asis(x.generateXML())

    return doc.getvalue()
