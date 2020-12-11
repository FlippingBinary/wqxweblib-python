from datetime import datetime
from io import BytesIO
from yattag import Doc, indent
from zipfile import ZipFile
from .Header import Header
from .Organization import Organization
from .Payload import Payload
from .WQXException import WQXException

class Submission:
  __header: Header
  __id: str
  __organization: Organization
  __payload: Payload
  __payloadOperation: str

  def __init__(self,Id:str) -> None:
    if not isinstance(Id, str):
      raise ValueError( "Id must be a string.")
    self.__header = Header()
    self.__id = Id
    self.__organization = Organization()
    self.__payload = Payload()
    self.__payloadOperation = None
  
  @property
  def header(self) -> Header:
    return self.__header
  @header.setter
  def header(self, val:Header) -> None:
    if not isinstance(val, Header):
      raise TypeError("Property 'header' must be a Header")
    self.__header = val

  @property
  def id(self) -> str:
    return self.__id
  @id.setter
  def id(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'id' must be a string.")
    if len(val) < 1:
      raise ValueError("Property 'id' is required.")
    self.__id = val

  @property
  def organization(self) -> Organization:
    return self.__organization
  @organization.setter
  def organization(self, val:Organization) -> None:
    if not isinstance(val, Organization):
      raise TypeError("Property 'organization' must be a Organization")
    self.__organization = val

  @property
  def payload(self) -> Payload:
    return self.__payload
  @payload.setter
  def payload(self, val:Payload) -> None:
    if not isinstance(val, Payload):
      raise TypeError("Property 'payload' must be a Payload")
    self.__payload = val

  @property
  def payloadOperation(self) -> str:
    return self.__payloadOperation
  @payloadOperation.setter
  def payloadOperation(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'payloadOperation' must be a string")
    if len(val) < 1:
      raise ValueError("Property 'payloadOperation' is required.")
    self.__payloadOperation = val

  def generateXML(self):
    if not self.__payloadOperation:
      raise WQXException("Property 'payloadOperation' must be set before XML can be generated.")

    doc, tag, text, line = Doc().ttl()
    doc.asis('<?xml version="1.0" encoding="UTF-8"?>')
    with tag('Document', ('Id', self.__id), ('xmlns','http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd'), ('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')):
      with tag('Header'):
        doc.asis(self.__header.generateXML())
      with tag('Payload', ('Operation', self.__payloadOperation)):
        with tag('WQX', ('xmlns', 'http://www.exchangenetwork.net/schema/wqx/3'), ('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance'), ('xsi:schemaLocation','http://www.exchangenetwork.net/schema/wqx/3 http://www.exchangenetwork.net/schema/wqx/3/index.xsd')):
          with tag('Organization'):
            doc.asis(self.__organization.generateXML())
            doc.asis(self.__payload.generateXML())
    return indent(doc.getvalue(), indentation = ' '*2)

  def generateZIP(self, fileName:str=None):
    if not isinstance(fileName, str):
      raise TypeError("Parameter 'fileName' must be a string.")

    mem = BytesIO()
    zip = ZipFile(mem, mode='w')

    results = self.generateXML()
    zip.writestr('results.xml', results)

    # TODO: Add attachment files, if necessary. Example:
    #   zip.writestr('rawdata.csv', self.data)

    zip.close()
    mem.seek(0)

    with open(fileName, 'wb') as out:
      out.write(mem.read())
