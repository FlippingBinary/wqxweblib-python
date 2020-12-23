from yattag import Doc, indent
from .Organization import Organization
from ..common import WQXException

class WQX:
  """Main Schema used to transfer water monitoring results to EPA Office of Water."""

  __organization: Organization

  def __init__(self,
    organization = None
  ):
    self.organization = organization


  @property
  def organization(self) -> Organization:
    return self.__organization
  @organization.setter
  def organization(self, val:Organization) -> None:
    self.__organization = Organization(val)


  def generateXML(self, name = 'WQX'):
    if self.__organization is None:
      raise WQXException("Attribute 'organization' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(
      name,
      ('xmlns','http://www.exchangenetwork.net/schema/wqx/3'),
      ('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance'),
      ('xsi:schemaLocation','http://www.exchangenetwork.net/schema/wqx/3 http://www.exchangenetwork.net/schema/wqx/3/index.xsd')
    ):
      with tag('Organization'):
        doc.asis(self.__organization.generateXML())

    return doc.getvalue()
