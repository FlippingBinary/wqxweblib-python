from yattag import Doc, indent
from .ReferenceMethod import ReferenceMethod
from .SimpleContent import *

class SamplePreparation:
  """Describes a sample preparation procedure which may be conducted on an initial Sample or on subsequent subsamples."""

  __samplePreparationMethod: ReferenceMethod
  __sampleContainerLabelName: SampleContainerLabelName
  __sampleContainerTypeName: SampleContainerTypeName
  __sampleContainerColorName: SampleContainerColorName
  __chemicalPreservativeUsedName: ChemicalPreservativeUsedName
  __thermalPreservativeUsedName: ThermalPreservativeUsedName
  __sampleTransportStorageDescription: SampleTransportStorageDescription

  def __init__(self):
    self.__samplePreparationMethod = None
    self.__sampleContainerLabelName = None
    self.__sampleContainerTypeName = None
    self.__sampleContainerColorName = None
    self.__chemicalPreservativeUsedName = None
    self.__thermalPreservativeUsedName = None
    self.__sampleTransportStorageDescription = None

  @property
  def samplePreparationMethod(self) -> ReferenceMethod:
    """Identifying information about the method(s) followed to prepare a sample for analysis."""
    return self.__samplePreparationMethod
  @samplePreparationMethod.setter
  def samplePreparationMethod(self, val:ReferenceMethod) -> None:
    """Identifying information about the method(s) followed to prepare a sample for analysis."""
    self.__samplePreparationMethod = val

  @property
  def sampleContainerLabelName(self) -> SampleContainerLabelName:
    return self.__sampleContainerLabelName
  @sampleContainerLabelName.setter
  def sampleContainerLabelName(self, val:SampleContainerLabelName) -> None:
    self.__sampleContainerLabelName = None if val is None else SampleContainerLabelName(val)

  @property
  def sampleContainerTypeName(self) -> SampleContainerTypeName:
    return self.__sampleContainerTypeName
  @sampleContainerTypeName.setter
  def sampleContainerTypeName(self, val:SampleContainerTypeName) -> None:
    self.__sampleContainerTypeName = None if val is None else SampleContainerTypeName(val)

  @property
  def sampleContainerColorName(self) -> SampleContainerColorName:
    return self.__sampleContainerColorName
  @sampleContainerColorName.setter
  def sampleContainerColorName(self, val:SampleContainerColorName) -> None:
    self.__sampleContainerColorName = None if val is None else SampleContainerColorName(val)

  @property
  def chemicalPreservativeUsedName(self) -> ChemicalPreservativeUsedName:
    return self.__chemicalPreservativeUsedName
  @chemicalPreservativeUsedName.setter
  def chemicalPreservativeUsedName(self, val:ChemicalPreservativeUsedName) -> None:
    self.__chemicalPreservativeUsedName = None if val is None else ChemicalPreservativeUsedName(val)

  @property
  def thermalPreservativeUsedName(self) -> ThermalPreservativeUsedName:
    return self.__thermalPreservativeUsedName
  @thermalPreservativeUsedName.setter
  def thermalPreservativeUsedName(self, val:ThermalPreservativeUsedName) -> None:
    self.__thermalPreservativeUsedName = None if val is None else ThermalPreservativeUsedName(val)

  @property
  def sampleTransportStorageDescription(self) -> SampleTransportStorageDescription:
    return self.__sampleTransportStorageDescription
  @sampleTransportStorageDescription.setter
  def sampleTransportStorageDescription(self, val:SampleTransportStorageDescription) -> None:
    self.__sampleTransportStorageDescription = None if val is None else SampleTransportStorageDescription(val)

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    if self.__samplePreparationMethod is not None:
      with tag('SamplePreparationMethod'):
        doc.asis(self.__samplePreparationMethod.generateXML())
    if self.__sampleContainerLabelName is not None:
      line('SampleContainerLabelName', self.__sampleContainerLabelName)
    if self.__sampleContainerTypeName is not None:
      line('SampleContainerTypeName', self.__sampleContainerTypeName)
    if self.__sampleContainerColorName is not None:
      line('SampleContainerColorName', self.__sampleContainerColorName)
    if self.__chemicalPreservativeUsedName is not None:
      line('ChemicalPreservativeUsedName', self.__chemicalPreservativeUsedName)
    if self.__thermalPreservativeUsedName is not None:
      line('ThermalPreservativeUsedName', self.__thermalPreservativeUsedName)
    if self.__sampleTransportStorageDescription is not None:
      line('SampleTransportStorageDescription', self.__sampleTransportStorageDescription)

    return indent(doc.getvalue(), indentation = ' '*2)
