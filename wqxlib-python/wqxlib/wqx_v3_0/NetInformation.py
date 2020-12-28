from yattag import Doc, indent, indentation
from .MeasureCompact import MeasureCompact
from .SimpleContent import *
from ..common import WQXException

class NetInformation:
  """Allows for the reporting of net sample collection information."""

  __netTypeName: NetTypeName
  __netSurfaceAreaMeasure: MeasureCompact
  __netMeshSizeMeasure: MeasureCompact
  __boatSpeedMeasure: MeasureCompact
  __currentSpeedMeasure: MeasureCompact

  def __init__(self):
    self.__netTypeName = None
    self.__netSurfaceAreaMeasure = None
    self.__netMeshSizeMeasure = None
    self.__boatSpeedMeasure = None
    self.__currentSpeedMeasure = None

  @property
  def netTypeName(self) -> NetTypeName:
    return self.__netTypeName
  @netTypeName.setter
  def netTypeName(self, val:NetTypeName) -> None:
    self.__netTypeName = NetTypeName(val)

  @property
  def netSurfaceAreaMeasure(self) -> MeasureCompact:
    """A measurement of the effective surface area of the net used during biological monitoring sample collection."""
    return self.netSurfaceAreaMeasure
  @netSurfaceAreaMeasure.setter
  def netSurfaceAreaMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the effective surface area of the net used during biological monitoring sample collection."""
    self.__netSurfaceAreaMeasure = val

  @property
  def netMeshSizeMeasure(self) -> MeasureCompact:
    """A measurement of the mesh size of the net used during biological monitoring sample collection."""
    return self.netMeshSizeMeasure
  @netMeshSizeMeasure.setter
  def netMeshSizeMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the mesh size of the net used during biological monitoring sample collection."""
    self.__netMeshSizeMeasure = val

  @property
  def boatSpeedMeasure(self) -> MeasureCompact:
    """A measurement of the boat speed during biological monitoring sample collection."""
    return self.boatSpeedMeasure
  @boatSpeedMeasure.setter
  def boatSpeedMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the boat speed during biological monitoring sample collection."""
    self.__boatSpeedMeasure = val

  @property
  def currentSpeedMeasure(self) -> MeasureCompact:
    """A measurement of the current during biological monitoring sample collection."""
    return self.currentSpeedMeasure
  @currentSpeedMeasure.setter
  def currentSpeedMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the current during biological monitoring sample collection."""
    self.__currentSpeedMeasure = val

  def generateXML(self):
    if self.__netTypeName is None:
      WQXException("Attribute 'netTypeName' is required.")

    doc, tag, text, line = Doc().ttl()

    line('NetTypeName', self.__netTypeName)
    if self.__netSurfaceAreaMeasure is not None:
      with tag('NetSurfaceAreaMeasure'):
        doc.asis(self.__netSurfaceAreaMeasure.generateXML())
    if self.__netMeshSizeMeasure is not None:
      with tag('NetMeshSizeMeasure'):
        doc.asis(self.__netMeshSizeMeasure.generateXML())
    if self.__boatSpeedMeasure is not None:
      with tag('BoatSpeedMeasure'):
        doc.asis(self.__boatSpeedMeasure.generateXML())
    if self.__currentSpeedMeasure is not None:
      with tag('CurrentSpeedMeasure'):
        doc.asis(self.__currentSpeedMeasure.generateXML())

    return doc.getvalue()
