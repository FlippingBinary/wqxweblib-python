from yattag import Doc, indent
from .BiologicalHabitatCollectionInformation import BiologicalHabitatCollectionInformation
from .SimpleContent import *

class BiologicalActivityDescription:
  """Allows for the reporting of biological monitoring activities conducted at a Monitoring Location."""

  __assemblageSampledName: AssemblageSampledName
  __biologicalHabitatCollectionInformation: BiologicalHabitatCollectionInformation
  __toxicityTestType: ToxicityTestType
  __habitatSelectionMethod: HabitatSelectionMethod

  def __init__(self):
    self.__assemblageSampledName = None
    self.__biologicalHabitatCollectionInformation = None
    self.__toxicityTestType = None
    self.__habitatSelectionMethod = None

  @property
  def assemblageSampledName(self) -> AssemblageSampledName:
    return self.__assemblageSampledName
  @assemblageSampledName.setter
  def assemblageSampledName(self, val:AssemblageSampledName) -> None:
    self.__assemblageSampledName = None if val is None else AssemblageSampledName(val)

  @property
  def biologicalHabitatCollectionInformation(self) -> BiologicalHabitatCollectionInformation:
    return self.__biologicalHabitatCollectionInformation
  @biologicalHabitatCollectionInformation.setter
  def biologicalHabitatCollectionInformation(self, val:BiologicalHabitatCollectionInformation) -> None:
    self.__biologicalHabitatCollectionInformation = val

  @property
  def toxicityTestType(self) -> ToxicityTestType:
    return self.__toxicityTestType
  @toxicityTestType.setter
  def toxicityTestType(self, val:ToxicityTestType) -> None:
    self.__toxicityTestType = None if val is None else ToxicityTestType(val)

  @property
  def habitatSelectionMethod(self) -> HabitatSelectionMethod:
    return self.__habitatSelectionMethod
  @habitatSelectionMethod.setter
  def habitatSelectionMethod(self, val:HabitatSelectionMethod) -> None:
    self.__habitatSelectionMethod = None if val is None else HabitatSelectionMethod(val)

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__assemblageSampledName is not None:
      line('AssemblageSampledName', self.__assemblageSampledName)
    if self.__biologicalHabitatCollectionInformation is not None:
      with tag('BiologicalHabitatCollectionInformation'):
        doc.asis(self.__biologicalHabitatCollectionInformation.generateXML())
    if self.__toxicityTestType is not None:
      line('ToxicityTestType', self.__toxicityTestType)
    if self.__habitatSelectionMethod is not None:
      line('HabitatSelectionMethod', self.__habitatSelectionMethod)

    return indent(doc.getvalue(), indentation = ' '*2)
