from typing import List
from yattag import Doc, indent
from .Organization_Delete import OrganizationDelete
from ..common import WQXException

class WQXDelete:
  """Main Schema used to delete a portion of water monitoring results from EPA Office of Water system."""

  __organizationDelete: List[OrganizationDelete]

  def __init__(self):
    self.__organizationDelete = []

  @property
  def organizationDelete(self) -> List[OrganizationDelete]:
    return self.__organizationDelete
  @organizationDelete.setter
  def organizationDelete(self, val: List[OrganizationDelete]) -> None:
    if not isinstance(val, list) or len(val) < 1:
      raise TypeError("Attribute 'organizationDelete' must be a list of 1 or more OrganizationDelete objects.")
    for x in val:
      if not isinstance(x, OrganizationDelete):
        raise TypeError("Attribute 'organizationDelete' must be a list of 1 or more OrganizationDelete objects.")
    self.__organizationDelete = val

  def generateXML(self, name = 'WQXDelete'):
    if self.__organizationDelete is None:
      raise WQXException("Attribute 'organizationDelete' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(
      name,
      ('xmlns','http://www.exchangenetwork.net/schema/wqx/3'),
      ('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance'),
      ('xsi:schemaLocation','http://www.exchangenetwork.net/schema/wqx/3 http://www.exchangenetwork.net/schema/wqx/3/index.xsd')
    ):
      for x in self.__organizationDelete:
        doc.asis(x.generateXML('OrganizationDelete'))

    return doc.getvalue()
