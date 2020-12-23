from yattag import Doc, indent
from .AquiferInformation import AquiferInformation
from .MeasureCompact import MeasureCompact
from .SimpleContent import *
from ..common import WQXException

class WellInformation:
  """Description of the attributes of a well."""

  __wellTypeText: WellTypeText
  __aquiferTypeName: AquiferTypeName
  __nationalAquiferCode: NationalAquiferCode
  __aquiferInformation: AquiferInformation
  __formationTypeText: FormationTypeText
  __wellHoleDepthMeasure: MeasureCompact
  __constructionDate: ConstructionDate
  __wellDepthMeasure: MeasureCompact

  def __init__(self):
    self.__wellTypeText = None
    self.__aquiferTypeName = None
    self.__nationalAquiferCode = None
    self.__aquiferInformation = None
    self.__formationTypeText = None
    self.__wellHoleDepthMeasure = None
    self.__constructionDate = None
    self.__wellDepthMeasure = None

  @property
  def wellTypeText(self) -> WellTypeText:
    return self.__wellTypeText
  @wellTypeText.setter
  def wellTypeText(self, val:WellTypeText) -> None:
    self.__wellTypeText = WellTypeText(val)

  @property
  def aquiferTypeName(self) -> AquiferTypeName:
    return self.__aquiferTypeName
  @aquiferTypeName.setter
  def aquiferTypeName(self, val:AquiferTypeName) -> None:
    self.__aquiferTypeName = None if val is None else AquiferTypeName(val)

  @property
  def nationalAquiferCode(self) -> NationalAquiferCode:
    return self.__nationalAquiferCode
  @nationalAquiferCode.setter
  def nationalAquiferCode(self, val:NationalAquiferCode) -> None:
    self.__nationalAquiferCode = None if val is None else NationalAquiferCode(val)

  @property
  def aquiferInformation(self) -> AquiferInformation:
    return self.__aquiferInformation
  @aquiferInformation.setter
  def aquiferInformation(self, val:AquiferInformation) -> None:
    self.__aquiferInformation = None if val is None else AquiferInformation(val)

  @property
  def formationTypeText(self) -> FormationTypeText:
    return self.__formationTypeText
  @formationTypeText.setter
  def formationTypeText(self, val:FormationTypeText) -> None:
    self.__formationTypeText = None if val is None else FormationTypeText(val)

  @property
  def wellHoleDepthMeasure(self) -> MeasureCompact:
    """Depth below land surface datum (LSD) to the bottom of the hole on completion of drilling."""
    return self.__wellHoleDepthMeasure
  @wellHoleDepthMeasure.setter
  def wellHoleDepthMeasure(self, val:MeasureCompact) -> None:
    """Depth below land surface datum (LSD) to the bottom of the hole on completion of drilling."""
    self.__wellHoleDepthMeasure = None if val is None else MeasureCompact(val)

  @property
  def constructionDate(self) -> ConstructionDate:
    return self.__constructionDate
  @constructionDate.setter
  def constructionDate(self, val:ConstructionDate) -> None:
    self.__constructionDate = None if val is None else ConstructionDate(val)

  @property
  def wellDepthMeasure(self) -> MeasureCompact:
    """Depth below land surface datum (LSD) to the bottom of the hole on completion of drilling. ie. completion depth"""
    return self.__wellDepthMeasure
  @wellDepthMeasure.setter
  def wellDepthMeasure(self, val:MeasureCompact) -> None:
    """Depth below land surface datum (LSD) to the bottom of the hole on completion of drilling. ie. completion depth"""
    self.__wellDepthMeasure = None if val is None else MeasureCompact(val)

  def generateXML(self):
    if self.__wellTypeText is None:
      WQXException("Attribute 'WellTypeText' is required.")

    doc, tag, text, line = Doc().ttl()

    line('WellTypeText', self.__wellTypeText)
    if self.__aquiferTypeName is not None:
      line('AquiferTypeName', self.__aquiferTypeName)
    if self.__nationalAquiferCode is not None:
      line('NationalAquiferCode', self.__nationalAquiferCode)
    if self.__aquiferInformation is not None:
      with tag('AquiferInformation'):
        doc.asis(self.__aquiferInformation.generateXML())
    if self.__formationTypeText is not None:
      line('FormationTypeText', self.__formationTypeText)
    if self.__wellHoleDepthMeasure is not None:
      with tag('WellHoleDepthMeasure'):
        doc.asis(self.__wellHoleDepthMeasure.generateXML())
    if self.__constructionDate is not None:
      line('ConstructionDate', self.__constructionDate)
    if self.__wellDepthMeasure is not None:
      with tag('WellDepthMeasure'):
        doc.asis(self.__wellDepthMeasure.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)
