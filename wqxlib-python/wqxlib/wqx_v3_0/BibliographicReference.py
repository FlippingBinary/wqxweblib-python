from yattag import Doc, indent
from .SimpleContent import (
  ResourceTitleName,
  ResourceCreatorName,
  ResourceSubjectText,
  ResourcePublisherName,
  ResourceDate,
  ResourceIdentifier
)
from ..common import WQXException

class BibliographicReference:
  """The descriptors used to identify and catalog an object."""

  __resourceTitleName: ResourceTitleName
  __resourceCreatorName: ResourceCreatorName
  __resourceSubjectText: ResourceSubjectText
  __resourcePublisherName: ResourcePublisherName
  __resourceDate: ResourceDate
  __resourceIdentifier: ResourceIdentifier

  def __init__(self):
    self.__resourceTitleName = None
    self.__resourceCreatorName = None
    self.__resourceSubjectText = None
    self.__resourcePublisherName = None
    self.__resourceDate = None
    self.__resourceIdentifier = None

  @property
  def ResourceTitleName(self) -> ResourceTitleName:
    return self.__ResourceTitleName
  @ResourceTitleName.setter
  def ResourceTitleName(self, val:ResourceTitleName) -> None:
    self.__ResourceTitleName = ResourceTitleName(val)

  @property
  def ResourceCreatorName(self) -> ResourceCreatorName:
    return self.__ResourceCreatorName
  @ResourceCreatorName.setter
  def ResourceCreatorName(self, val:ResourceCreatorName) -> None:
    self.__ResourceCreatorName = None if val is None else ResourceCreatorName(val)

  @property
  def ResourceSubjectText(self) -> ResourceSubjectText:
    return self.__ResourceSubjectText
  @ResourceSubjectText.setter
  def ResourceSubjectText(self, val:ResourceSubjectText) -> None:
    self.__ResourceSubjectText = None if val is None else ResourceSubjectText(val)

  @property
  def ResourcePublisherName(self) -> ResourcePublisherName:
    return self.__ResourcePublisherName
  @ResourcePublisherName.setter
  def ResourcePublisherName(self, val:ResourcePublisherName) -> None:
    self.__ResourcePublisherName = None if val is None else ResourcePublisherName(val)

  @property
  def ResourceDate(self) -> ResourceDate:
    return self.__ResourceDate
  @ResourceDate.setter
  def ResourceDate(self, val:ResourceDate) -> None:
    self.__ResourceDate = ResourceDate(val)

  @property
  def ResourceIdentifier(self) -> ResourceIdentifier:
    return self.__ResourceIdentifier
  @ResourceIdentifier.setter
  def ResourceIdentifier(self, val:ResourceIdentifier) -> None:
    self.__ResourceIdentifier = ResourceIdentifier(val)

  def generateXML(self):
    if self.__resourceTitleName is None:
      raise WQXException("Attribute 'ResourceTitleName' is required.")
    if self.__resourceDate is None:
      raise WQXException("Attribute 'ResourceDate' is required.")
    if self.__resourceIdentifier is None:
      raise WQXException("Attribute 'ResourceIdentifier' is required.")

    doc, tag, text, line = Doc().ttl()

    line('ResourceTitleName', self.__resourceTitleName)
    if self.__resourceCreatorName is not None:
      doc.asis(self.__resourceCreatorName.generateXML())
    if self.__resourceSubjectText is not None:
      doc.asis(self.__resourceSubjectText.generateXML())
    if self.__resourcePublisherName is not None:
      doc.asis(self.__resourcePublisherName.generateXML())
    line('ResourceDate', self.__resourceDate)
    line('ResourceIdentifier', self.__resourceIdentifier)

    return doc.getvalue()
