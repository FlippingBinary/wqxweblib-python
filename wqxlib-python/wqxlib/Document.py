import re
from typing import List, Union
from yattag import Doc, indent
from .Header import Header
from .Payload import Payload
from .common import WQXException

class ID(str):
  """The type ID is used for an attribute that uniquely identifies an element in an XML document. An ID value must be an NCName. This means that it must start with a letter or underscore, and can only contain letters, digits, underscores, hyphens, and periods."""

  __pattern = re.compile(r"^[:A-Z_a-z\xC0-\xD6\xD8-\xF6\xF8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD][-:0-9.A-Z_a-z\xC0-\xD6\xD8-\xF6\xF8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\xB7\u0300-\u036F\u203F-\u2040]*$")
  def __init__(self, o=None):
    if not isinstance(o, str) or re.match(self.__pattern, o):
      raise ValueError("Attribute of type 'ID' must be a valid XML Identifier.")

class Document:
  """The base document type used for submission to WQXWeb."""

  __id: ID
  __header: Header
  __payload: List[Payload]

  def __init__(self, o=None, *,
    id:ID = None,
    header:Header = None,
    payload:List[Payload] = None
  ):
    if isinstance(o, Document):
      # Assign attributes from object without typechecking
      self.__id = o.id
      self.__header = o.header
      self.__payload = o.payload
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.id = o.get('id', default = None)
      self.header = o.get('header', default = None)
      self.payload = o.get('payload', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.header = header
      self.id = id
      self.payload = payload

  @property
  def header(self) -> Header:
    return self.__header
  @header.setter
  def header(self, val:Header) -> None:
    self.__header = None if val is None else Header(val)

  @property
  def id(self) -> ID:
    return self.__id
  @id.setter
  def id(self, val:ID) -> None:
    self.__id = ID(val)

  @property
  def payload(self) -> List[Payload]:
    return self.__payload
  @payload.setter
  def payload(self, val:Union[Payload,List[Payload]]) -> None:
    if val is None:
      self.__payload = []
    elif isinstance(val, list):
      r:List[Payload] = []
      for x in val:
        r.append(Payload(x))
      self.__payload = r
    else:
      self.__payload = [Payload(val)]

  def generateXML(self, name:str = 'Document') -> str:
    doc, tag, text, line = Doc().ttl()

    if self.__id is None:
      raise WQXException("Attribute 'id' is required.")
    with tag(name,
      ('Id', self.__id),
      ('xmlns','http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd'),
      ('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
    ):
      if self.__header is None:
        raise WQXException("Attribute 'header' is required.")
      doc.asis(self.__header.generateXML('Header'))
      if len(self.__payload) < 1:
        raise WQXException("Attribute 'payload' must be a list of 1 or more Payload objects.")
      for x in self.__payload:
        doc.asis(x.generateXML('Payload'))

    return indent(doc.getvalue(), indentation = ' '*2)
