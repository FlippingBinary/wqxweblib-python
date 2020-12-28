from typing import List
from yattag import Doc, indent
from .MonitoringLocationIdentity import MonitoringLocationIdentity
from .MonitoringLocationGeospatial import MonitoringLocationGeospatial
from .WellInformation import WellInformation
from .AttachedBinaryObject import AttachedBinaryObject
from ..common import WQXException

class MonitoringLocation:
  """An identifiable location where an environmental sample, onsite measurement, and/or observation is determined."""

  __monitoringLocationIdentity: MonitoringLocationIdentity
  __monitoringLocationGeospatial: MonitoringLocationGeospatial
  __wellInformation: WellInformation
  __attachedBinaryObject: List[AttachedBinaryObject]

  def __init__(self,
    monitoringLocationIdentity = None,
    monitoringLocationGeospatial = None,
    wellInformation = None,
    attachedBinaryObject = []
  ):
    self.monitoringLocationIdentity = monitoringLocationIdentity
    self.monitoringLocationGeospatial = monitoringLocationGeospatial
    self.wellInformation = wellInformation
    self.attachedBinaryObject = attachedBinaryObject

  @property
  def monitoringLocationIdentity(self) -> MonitoringLocationIdentity:
    return self.__monitoringLocationIdentity
  @monitoringLocationIdentity.setter
  def monitoringLocationIdentity(self, val:MonitoringLocationIdentity) -> None:
    self.__monitoringLocationIdentity = val

  @property
  def monitoringLocationGeospatial(self) -> MonitoringLocationGeospatial:
    return self.__monitoringLocationGeospatial
  @monitoringLocationGeospatial.setter
  def monitoringLocationGeospatial(self, val:MonitoringLocationGeospatial) -> None:
    self.__monitoringLocationGeospatial = val

  @property
  def wellInformation(self) -> WellInformation:
    return self.__wellInformation
  @wellInformation.setter
  def wellInformation(self, val:WellInformation) -> None:
    self.__wellInformation = val

  @property
  def attachedBinaryObject(self) -> List[AttachedBinaryObject]:
    return self.__attachedBinaryObject
  @attachedBinaryObject.setter
  def attachedBinaryObject(self, val:List[AttachedBinaryObject]) -> None:
    self.__attachedBinaryObject = val

  def generateXML(self):
    if self.__monitoringLocationIdentity is None:
      WQXException("Attribute 'MonitoringLocationIdentity' is required.")
    if self.__monitoringLocationGeospatial is None:
      WQXException("Attribute 'MonitoringLocationGeospatial' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag('MonitoringLocationIdentity'):
      doc.asis(self.__monitoringLocationIdentity.generateXML())
    with tag('MonitoringLocationGeospatial'):
      doc.asis(self.__monitoringLocationGeospatial.generateXML())
    if self.__wellInformation is not None:
      with tag('WellInformation'):
        doc.asis(self.__wellInformation.generateXML())
    for x in self.__attachedBinaryObject:
      with tag('AttachedBinaryObject'):
        doc.asis(x.generateXML())

    return doc.getvalue()
