from yattag import Doc, indent
from .SimpleContent import *

class OrganizationAddress:
  """The physical address of an organization."""

  __addressTypeName: AddressTypeName
  __addressText: AddressText
  __supplementalAddressText: SupplementalAddressText
  __localityName: LocalityName
  __stateCode: StateCode
  __postalCode: PostalCode
  __countryCode: CountryCode
  __countyCode: CountyCode

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
  def addressTypeName(self) -> AddressTypeName:
    return self.__addressTypeName
  @addressTypeName.setter
  def addressTypeName(self, val:AddressTypeName) -> None:
    self.__addressTypeName = None if val is None else AddressTypeName(val)

  @property
  def addressText(self) -> AddressText:
    return self.__addressText
  @addressText.setter
  def addressText(self, val:AddressText) -> None:
    self.__addressText = None if val is None else AddressText(val)

  @property
  def supplementalAddressText(self) -> SupplementalAddressText:
    return self.__supplementalAddressText
  @supplementalAddressText.setter
  def supplementalAddressText(self, val:SupplementalAddressText) -> None:
    self.__supplementalAddressText = None if val is None else SupplementalAddressText(val)

  @property
  def localityName(self) -> LocalityName:
    return self.__localityName
  @localityName.setter
  def localityName(self, val:LocalityName) -> None:
    self.__localityName = None if val is None else LocalityName(val)

  @property
  def stateCode(self) -> StateCode:
    return self.__stateCode
  @stateCode.setter
  def stateCode(self, val:StateCode) -> None:
    self.__stateCode = None if val is None else StateCode(val)

  @property
  def postalCode(self) -> PostalCode:
    return self.__postalCode
  @postalCode.setter
  def postalCode(self, val:PostalCode) -> None:
    self.__postalCode = None if val is None else PostalCode(val)

  @property
  def countryCode(self) -> CountryCode:
    return self.__countryCode
  @countryCode.setter
  def countryCode(self, val:CountryCode) -> None:
    self.__countryCode = None if val is None else CountryCode(val)

  @property
  def countyCode(self) -> CountyCode:
    return self.__countyCode
  @countyCode.setter
  def countyCode(self, val:CountyCode) -> None:
    self.__countyCode = None if val is None else CountyCode(val)

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
