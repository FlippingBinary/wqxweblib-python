from typing import List
from yattag import Doc, indent
from .AlternateMonitoringLocationIdentity import AlternateMonitoringLocationIdentity
from .MeasureCompact import MeasureCompact
from .SimpleContent import *
from ..common import WQXException

class MonitoringLocationIdentity:
  """Basic identification information for the location/site that is monitored or used for sampling."""

  __monitoringLocationIdentifier: MonitoringLocationIdentifier
  __monitoringLocationName: MonitoringLocationName
  __monitoringLocationTypeName: MonitoringLocationTypeName
  __monitoringLocationDescriptionText: MonitoringLocationDescriptionText
  __hucEightDigitCode: HUCEightDigitCode
  __hucTwelveDigitCode: HUCTwelveDigitCode
  __tribalLandIndicator: TribalLandIndicator
  __tribalLandName: TribalLandName
  __alternateMonitoringLocationIdentity: List[AlternateMonitoringLocationIdentity]
  __drainageAreaMeasure: MeasureCompact
  __contributingDrainageAreaMeasure: MeasureCompact

  def __init__(self,
    monitoringLocationIdentifier = None,
    monitoringLocationName = None,
    monitoringLocationTypeName = None,
    monitoringLocationDescriptionText = None,
    hucEightDigitCode = None,
    hucTwelveDigitCode = None,
    tribalLandIndicator = None,
    tribalLandName = None,
    alternateMonitoringLocationIdentity = [],
    drainageAreaMeasure = None,
    contributingDrainageAreaMeasure = None
  ):
    self.__monitoringLocationIdentifier = monitoringLocationIdentifier
    self.__monitoringLocationName = monitoringLocationName
    self.__monitoringLocationTypeName = monitoringLocationTypeName
    self.__monitoringLocationDescriptionText = monitoringLocationDescriptionText
    self.__hucEightDigitCode = hucEightDigitCode
    self.__hucTwelveDigitCode = hucTwelveDigitCode
    self.__tribalLandIndicator = tribalLandIndicator
    self.__tribalLandName = tribalLandName
    self.__alternateMonitoringLocationIdentity = alternateMonitoringLocationIdentity
    self.__drainageAreaMeasure = drainageAreaMeasure
    self.__contributingDrainageAreaMeasure = contributingDrainageAreaMeasure

  @property
  def monitoringLocationIdentifier(self) -> MonitoringLocationIdentifier:
    return self.__monitoringLocationIdentifier
  @monitoringLocationIdentifier.setter
  def monitoringLocationIdentifier(self, val:MonitoringLocationIdentifier) -> None:
    self.__monitoringLocationIdentifier = val

  @property
  def monitoringLocationName(self) -> MonitoringLocationName:
    return self.__monitoringLocationName
  @monitoringLocationName.setter
  def monitoringLocationName(self, val:MonitoringLocationName) -> None:
    self.__monitoringLocationName = val

  @property
  def monitoringLocationTypeName(self) -> MonitoringLocationTypeName:
    return self.__monitoringLocationTypeName
  @monitoringLocationTypeName.setter
  def monitoringLocationTypeName(self, val:MonitoringLocationTypeName) -> None:
    self.__monitoringLocationTypeName = val

  @property
  def monitoringLocationDescriptionText(self) -> MonitoringLocationDescriptionText:
    return self.__monitoringLocationDescriptionText
  @monitoringLocationDescriptionText.setter
  def monitoringLocationDescriptionText(self, val:MonitoringLocationDescriptionText) -> None:
    self.__monitoringLocationDescriptionText = None if val is None else MonitoringLocationDescriptionText(val)

  @property
  def hucEightDigitCode(self) -> HUCEightDigitCode:
    return self.__hucEightDigitCode
  @hucEightDigitCode.setter
  def hucEightDigitCode(self, val:HUCEightDigitCode) -> None:
    self.__hucEightDigitCode = None if val is None else HUCEightDigitCode(val)

  @property
  def hucTwelveDigitCode(self) -> HUCTwelveDigitCode:
    return self.__hucTwelveDigitCode
  @hucTwelveDigitCode.setter
  def hucTwelveDigitCode(self, val:HUCTwelveDigitCode) -> None:
    self.__hucTwelveDigitCode = None if val is None else HUCTwelveDigitCode(val)

  @property
  def tribalLandIndicator(self) -> TribalLandIndicator:
    return self.__tribalLandIndicator
  @tribalLandIndicator.setter
  def tribalLandIndicator(self, val:TribalLandIndicator) -> None:
    self.__tribalLandIndicator = None if val is None else TribalLandIndicator(val)

  @property
  def tribalLandName(self) -> TribalLandName:
    return self.__tribalLandName
  @tribalLandName.setter
  def tribalLandName(self, val:TribalLandName) -> None:
    self.__tribalLandName = None if val is None else TribalLandName(val)

  @property
  def alternateMonitoringLocationIdentity(self) -> List[AlternateMonitoringLocationIdentity]:
    return self.__alternateMonitoringLocationIdentity
  @alternateMonitoringLocationIdentity.setter
  def alternateMonitoringLocationIdentity(self, val:List[AlternateMonitoringLocationIdentity]) -> None:
    self.__alternateMonitoringLocationIdentity = val

  @property
  def drainageAreaMeasure(self) -> MeasureCompact:
    """The drainage basin of a lake, stream, wetland, or estuary site."""
    return self.__drainageAreaMeasure
  @drainageAreaMeasure.setter
  def drainageAreaMeasure(self, val:MeasureCompact) -> None:
    """The drainage basin of a lake, stream, wetland, or estuary site."""
    self.__drainageAreaMeasure = val

  @property
  def contributingDrainageAreaMeasure(self) -> MeasureCompact:
    """The contributing drainage area of a lake, stream, wetland, or estuary site."""
    return self.__contributingDrainageAreaMeasure
  @contributingDrainageAreaMeasure.setter
  def contributingDrainageAreaMeasure(self, val:MeasureCompact) -> None:
    """The contributing drainage area of a lake, stream, wetland, or estuary site."""
    self.__contributingDrainageAreaMeasure = val

  def generateXML(self):
    if self.__monitoringLocationIdentifier is None:
      WQXException("Attribute 'MonitoringLocationIdentifier' is required.")
    if self.__monitoringLocationName is None:
      WQXException("Attribute 'MonitoringLocationName' is required.")
    if self.__monitoringLocationTypeName is None:
      WQXException("Attribute 'MonitoringLocationTypeName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MonitoringLocationIdentifier', self.__monitoringLocationIdentifier)
    line('MonitoringLocationName', self.__monitoringLocationName)
    line('MonitoringLocationTypeName', self.__monitoringLocationTypeName)
    if self.__monitoringLocationDescriptionText is not None:
      line('MonitoringLocationDescriptionText',self.__monitoringLocationDescriptionText)
    if self.__hucEightDigitCode is not None:
      line('HUCEightDigitCode',self.__hucEightDigitCode)
    if self.__hucTwelveDigitCode is not None:
      line('HUCTwelveDigitCode',self.__hucTwelveDigitCode)
    if self.__tribalLandIndicator is not None:
      line('TribalLandIndicator',self.__tribalLandIndicator)
    if self.__tribalLandName is not None:
      line('TribalLandName',self.__tribalLandName)
    for x in self.__alternateMonitoringLocationIdentity:
      with tag('AlternateMonitoringLocationIdentity'):
        doc.asis(x.generateXML())
    if self.__drainageAreaMeasure is not None:
      with tag('DrainageAreaMeasure'):
        doc.asis(self.__drainageAreaMeasure.generateXML())
    if self.__contributingDrainageAreaMeasure is not None:
      with tag('ContributingDrainageAreaMeasure'):
        doc.asis(self.__contributingDrainageAreaMeasure.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)
