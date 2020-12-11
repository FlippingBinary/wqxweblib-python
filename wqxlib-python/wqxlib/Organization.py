from typing import List
from yattag import Doc, indent
from .WQXException import WQXException

class OrganizationDescription:
  __organizationIdentifier: str # required, constrained
  __organizationFormalName: str # required
  __organizationDescriptionText: str # optional
  __tribalCode: str # optional, constrained

  @property
  def organizationIdentifier(self) -> str:
    return self.__organizationIdentifier
  @organizationIdentifier.setter
  def organizationIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'organizationIdentifier' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'organizationIdentifier' is required.")
    self.__organizationIdentifier = val

  @property
  def organizationFormalName(self) -> str:
    return self.__organizationFormalName
  @organizationFormalName.setter
  def organizationFormalName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'organizationFormalName' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'organizationFormalName' is required.")
    self.__organizationFormalName = val

  @property
  def organizationDescriptionText(self) -> str:
    return self.__organizationDescriptionText
  @organizationDescriptionText.setter
  def organizationDescriptionText(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'organizationDescriptionText' must be a string, if provided.")
    self.__organizationDescriptionText = val

  @property
  def tribalCode(self) -> str:
    return self.__tribalCode
  @tribalCode.setter
  def tribalCode(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'tribalCode' must be a string, if provided.")
    self.__tribalCode = val

  def generateXML(self):
    if self.__organizationIdentifier is None:
      raise WQXException("Property 'organizationIdentifier' is required.")
    if self.__organizationFormalName is None:
      raise WQXException("Property 'organizationFormalName' is required.")
    doc, tag, text, line = Doc().ttl()
    line('OrganizationIdentifier', self.__organizationIdentifier)
    line('OrganizationFormalName', self.__organizationFormalName)
    if self.__organizationDescriptionText is not None:
      line('OrganizationDescriptionText', self.__organizationDescriptionText)
    if self.__tribalCode is not None:
      line('TribalCode', self.__tribalCode)
    return indent(doc.getvalue(), indentation = ' '*2)

class ElectronicAddress:
  __electronicAddressText: str # optional
  __electronicAddressTypeName: str # optional, constrained

  def __init__(self):
    self.__electronicAddressText = None
    self.__electronicAddressTypeName = None

  @property
  def electronicAddressText(self) -> str:
    return self.__electronicAddressText
  @electronicAddressText.setter
  def electronicAddressText(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'electronicAddressText' must be a string, if provided.")
    self.__electronicAddressText = val

  @property
  def electronicAddressTypeName(self) -> str:
    return self.__electronicAddressTypeName
  @electronicAddressTypeName.setter
  def electronicAddressTypeName(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'electronicAddressTypeName' must be a string, if provided.")
    self.__electronicAddressTypeName = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    if self.__electronicAddressText is not None:
      line('ElectronicAddressText', self.__electronicAddressText)
    if self.__electronicAddressTypeName is not None:
      line('ElectronicAddressTypeName', self.__electronicAddressTypeName)
    return indent(doc.getvalue(), indentation = ' '*2)

class Telephonic:
  __telephoneNumberText: str # optional
  __telephoneNumberTypeName: str # optional, constrained
  __telephoneExtensionNumberText: str # optional

  def __init__(self):
    self.__telephoneNumberText = None
    self.__telephoneNumberTypeName = None
    self.__telephoneExtensionNumberText = None

  @property
  def telephoneNumberText(self) -> str:
    return self.__telephoneNumberText
  @telephoneNumberText.setter
  def telephoneNumberText(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'telephoneNumberText' must be a string, if provided.")
    self.__telephoneNumberText = val

  @property
  def telephoneNumberTypeName(self) -> str:
    return self.__telephoneNumberTypeName
  @telephoneNumberTypeName.setter
  def telephoneNumberTypeName(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'telephoneNumberTypeName' must be a string, if provided.")
    self.__telephoneNumberTypeName = val

  @property
  def telephoneExtensionNumberText(self) -> str:
    return self.__telephoneExtensionNumberText
  @telephoneExtensionNumberText.setter
  def telephoneExtensionNumberText(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'telephoneExtensionNumberText' must be a string, if provided.")
    self.__telephoneExtensionNumberText = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    if self.__telephoneNumberText is not None:
      line('TelephoneNumberText', self.__telephoneNumberText)
    if self.__telephoneNumberTypeName is not None:
      line('TelephoneNumberTypeName', self.__telephoneNumberTypeName)
    if self.__telephoneExtensionNumberText is not None:
      line('TelephoneExtensionNumberText', self.__telephoneExtensionNumberText)
    return indent(doc.getvalue(), indentation = ' '*2)

class OrganizationAddress:
  __addressTypeName: str # optional, constrained
  __addressText: str # optional
  __supplementalAddressText: str # optional
  __localityName: str # optional
  __stateCode: str # optional, constrained
  __postalCode: str # optional, constrained
  __countryCode: str # optional, constrained
  __countyCode: str # optional, constrained

  def __init__(self):
    self.__addressTypeName = None
    self.__addressText = None
    self.__supplementalAddressText = None
    self.__localityName = None
    self.__stateCode = None
    self.__postalCode = None
    self.__countryCode = None
    self.__countyCode = None

  @property
  def addressTypeName(self) -> str:
    return self.__addressTypeName
  @addressTypeName.setter
  def addressTypeName(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'addressTypeName' must be a string, if provided.")
    self.__addressTypeName = val

  @property
  def addressText(self) -> str:
    return self.__addressText
  @addressText.setter
  def addressText(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'addressText' must be a string, if provided.")
    self.__addressText = val

  @property
  def supplementalAddressText(self) -> str:
    return self.__supplementalAddressText
  @supplementalAddressText.setter
  def supplementalAddressText(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'supplementalAddressText' must be a string, if provided.")
    self.__supplementalAddressText = val

  @property
  def localityName(self) -> str:
    return self.__localityName
  @localityName.setter
  def localityName(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'localityName' must be a string, if provided.")
    self.__localityName = val

  @property
  def stateCode(self) -> str:
    return self.__stateCode
  @stateCode.setter
  def stateCode(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'stateCode' must be a string, if provided.")
    self.__stateCode = val

  @property
  def postalCode(self) -> str:
    return self.__postalCode
  @postalCode.setter
  def postalCode(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'postalCode' must be a string, if provided.")
    self.__postalCode = val

  @property
  def countryCode(self) -> str:
    return self.__countryCode
  @countryCode.setter
  def countryCode(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'countryCode' must be a string, if provided.")
    self.__countryCode = val

  @property
  def countyCode(self) -> str:
    return self.__countyCode
  @countyCode.setter
  def countyCode(self, val:str) -> None:
    if not None and not isinstance(val, str):
      raise TypeError("Property 'countyCode' must be a string, if provided.")
    self.__countyCode = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    if self.__addressTypeName is not None:
      line('AddressTypeName', self.__addressTypeName)
    if self.__addressText is not None:
      line('AddressText', self.__addressText)
    if self.__supplementalAddressText is not None:
      line('SupplementalAddressText', self.__supplementalAddressText)
    if self.__localityName is not None:
      line('LocalityName', self.__localityName)
    if self.__stateCode is not None:
      line('StateCode', self.__stateCode)
    if self.__postalCode is not None:
      line('PostalCode', self.__postalCode)
    if self.__countryCode is not None:
      line('CountryCode', self.__countryCode)
    if self.__countyCode is not None:
      line('CountyCode', self.__countyCode)
    return indent(doc.getvalue(), indentation = ' '*2)

class Organization:
  __organizationDescription: OrganizationDescription
  __electronicAddress: List[ElectronicAddress]
  __telephonic: List[Telephonic]
  __organizationAddress: List[OrganizationAddress]

  def __init__(self):
    self.__organizationDescription = OrganizationDescription()
    self.__electronicAddress = []
    self.__telephonic = []
    self.__organizationAddress = []

  @property
  def electronicAddress(self) -> List[ElectronicAddress]:
    return self.__electronicAddress
  @electronicAddress.setter
  def electronicAddress(self, val:List[ElectronicAddress]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'electronicAddress' must be a list of 0 or more ElectronicAddress objects.")
    self.__electronicAddress = val

  @property
  def organizationDescription(self) -> OrganizationDescription:
    return self.__organizationDescription
  @organizationDescription.setter
  def organizationDescription(self, val:OrganizationDescription) -> None:
    if not isinstance(val, OrganizationDescription):
      raise TypeError("Property 'organizationDescription' must be a OrganizationDescription object.")
    if len(val) < 1:
      raise TypeError("Property 'organizationDescription' is required.")
    self.__organizationDescription = val

  @property
  def telephonic(self) -> List[Telephonic]:
    return self.__telephonic
  @telephonic.setter
  def telephonic(self, val:List[Telephonic]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'telephonic' must be a list of 0 or more Telephonic objects.")
    self.__telephonic = val

  @property
  def organizationAddress(self) -> List[ElectronicAddress]:
    return self.__organizationAddress
  @organizationAddress.setter
  def organizationAddress(self, val:List[ElectronicAddress]) -> None:
    if not isinstance(val, list):
      raise TypeError("Property 'organizationAddress' must be a list of 0 or more ElectronicAddress objects.")
    self.__organizationAddress = val

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()

    with tag('OrganizationDescription'):
      doc.asis(self.__organizationDescription.generateXML())
    for x in self.__electronicAddress:
      with tag('ElectronicAddress'):
        doc.asis(x.generateXML())
    for x in self.__telephonic:
      with tag('Telephonic'):
        doc.asis(x.generateXML())
    for x in self.__organizationAddress:
      with tag('OrganizationAddress'):
        doc.asis(x.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)
