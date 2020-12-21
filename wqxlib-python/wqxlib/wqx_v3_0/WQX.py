from yattag import Doc, indent
from .Organization import Organization
from ..WQXException import WQXException

class WQX:
  """Main Schema used to transfer water monitoring results to EPA Office of Water."""

  __organization: Organization

  def __init__(self):
    self.__organization = None


  @property
  def organization(self) -> Organization:
    return self.__organization
  @organization.setter
  def organization(self, val:Organization) -> None:
    self.__organization = Organization(val)


  def generateXML(self):
    if self.__organization is None:
      raise WQXException("Attribute 'organization' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag('Organization'):
      doc.asis(self.__organization.generateXML())

    return indent(doc.getvalue(), indentation = ' '*2)
