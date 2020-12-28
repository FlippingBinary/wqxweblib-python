from yattag import Doc, indent
from .CollectionEffort import CollectionEffort
from .MeasureCompact import MeasureCompact
from .NetInformation import NetInformation
from .SimpleContent import *

class BiologicalHabitatCollectionInformation:
  """Allows for the reporting of biological habitat sample collection information."""

  __collectionDuration: MeasureCompact
  __collectionArea: MeasureCompact
  __collectionEffort: CollectionEffort
  __reachLengthMeasure: MeasureCompact
  __reachWidthMeasure: MeasureCompact
  __collectionDescriptionText: CollectionDescriptionText
  __passCount: PassCount
  __netInformation: NetInformation

  def __init__(self):
    self.__collectionDuration = None
    self.__collectionArea = None
    self.__collectionEffort = None
    self.__reachLengthMeasure = None
    self.__reachWidthMeasure = None
    self.__collectionDescriptionText = None
    self.__passCount = None
    self.__netInformation = None

  @property
  def collectionDuration(self) -> MeasureCompact:
    """The length of time a collection procedure or protocol was performed (e.g. total energized time for electrofishing, or total time kick net used)."""
    return self.__collectionDuration
  @collectionDuration.setter
  def collectionDuration(self, val:MeasureCompact) -> None:
    """The length of time a collection procedure or protocol was performed (e.g. total energized time for electrofishing, or total time kick net used)."""
    self.__collectionDuration = val

  @property
  def collectionArea(self) -> MeasureCompact:
    """The area of a collection procedure or protocol was performed (e.g. total area coverage for electrofishing, or total area  kick net used)."""
    return self.__collectionArea
  @collectionArea.setter
  def collectionArea(self, val:MeasureCompact) -> None:
    """The area of a collection procedure or protocol was performed (e.g. total area coverage for electrofishing, or total area  kick net used)."""
    self.__collectionArea = val

  @property
  def collectionEffort(self) -> CollectionEffort:
    return self.__collectionEffort
  @collectionEffort.setter
  def collectionEffort(self, val:CollectionEffort) -> None:
    self.__collectionEffort = val

  @property
  def reachLengthMeasure(self) -> MeasureCompact:
    """A measurement of the water body length distance in which the procedure or protocol was performed."""
    return self.__reachLengthMeasure
  @reachLengthMeasure.setter
  def reachLengthMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the water body length distance in which the procedure or protocol was performed."""
    self.__reachLengthMeasure = val

  @property
  def reachWidthMeasure(self) -> MeasureCompact:
    """A measurement of the reach width during collection procedures."""
    return self.__reachWidthMeasure
  @reachWidthMeasure.setter
  def reachWidthMeasure(self, val:MeasureCompact) -> None:
    """A measurement of the reach width during collection procedures."""
    self.__reachWidthMeasure = val

  @property
  def collectionDescriptionText(self) -> CollectionDescriptionText:
    return self.__collectionDescriptionText
  @collectionDescriptionText.setter
  def collectionDescriptionText(self, val:CollectionDescriptionText) -> None:
    self.__collectionDescriptionText = None if val is None else CollectionDescriptionText(val)

  @property
  def passCount(self) -> PassCount:
    return self.__passCount
  @passCount.setter
  def passCount(self, val:PassCount) -> None:
    self.__passCount = None if val is None else PassCount(val)

  @property
  def netInformation(self) -> NetInformation:
    return self.__netInformation
  @netInformation.setter
  def netInformation(self, val:NetInformation) -> None:
    self.__netInformation = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__collectionDuration is not None:
      with tag('CollectionDuration'):
        doc.asis(self.__collectionDuration.generateXML())
    if self.__collectionArea is not None:
      with tag('CollectionArea'):
        doc.asis(self.__collectionArea.generateXML())
    if self.__collectionEffort is not None:
      with tag('CollectionEffort'):
        doc.asis(self.__collectionEffort.generateXML())
    if self.__reachLengthMeasure is not None:
      with tag('ReachLengthMeasure'):
        doc.asis(self.__reachLengthMeasure.generateXML())
    if self.__reachWidthMeasure is not None:
      with tag('ReachWidthMeasure'):
        doc.asis(self.__reachWidthMeasure.generateXML())
    if self.__collectionDescriptionText is not None:
      line('CollectionDescriptionText', self.__collectionDescriptionText)
    if self.__passCount is not None:
      line('PassCount', self.__passCount)
    if self.__netInformation is not None:
      with tag('NetInformation'):
        doc.asis(self.__netInformation.generateXML())

    return doc.getvalue()
