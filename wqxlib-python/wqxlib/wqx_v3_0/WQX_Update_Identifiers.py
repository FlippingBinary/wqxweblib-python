from typing import List
from yattag import Doc, indent
from .Entity_Update_Identifiers import UpdateIdentifiers
from ..common import WQXException

class WQXUpdateIdentifiers:
  """Main Schema used to update identifiers for major entities (projects, monitoring locations, activity, activity groups, and indexes)."""

  __updateIdentifiers: List[UpdateIdentifiers]

  def __init__(self):
    self.__updateIdentifiers = None

  @property
  def updateIdentifiers(self) -> List[UpdateIdentifiers]:
    return self.__updateIdentifiers
  @updateIdentifiers.setter
  def updateIdentifiers(self, val:List[UpdateIdentifiers]) -> None:
    if not isinstance(val, list) or len(val) < 1:
      raise TypeError("Property 'updateIdentifiers' must be a list of 1 or more UpdateIdentifiers objects.")
    for x in val:
      if not isinstance(x, UpdateIdentifiers):
        raise TypeError("Property 'updateIdentifiers' must be a list of 1 or more UpdateIdentifiers objects.")
    self.__updateIdentifiers = val

  def generateXML(self, name = 'UpdateIdentifiers') -> str:
    if self.__updateIdentifiers is None:
      raise WQXException("Attribute 'updateIdentifiers' is required.")

    doc, tag, text, line = Doc().ttl()

    with tag(
      name,
      ('xmlns','http://www.exchangenetwork.net/schema/wqx/3'),
      ('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance'),
      ('xsi:schemaLocation','http://www.exchangenetwork.net/schema/wqx/3 http://www.exchangenetwork.net/schema/wqx/3/index.xsd')
    ):
      for x in self.__updateIdentifiers:
        doc.asis(x.generateXML('UpdateIdentifiers'))

    return doc.getvalue()
