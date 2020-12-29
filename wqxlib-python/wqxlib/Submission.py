from io import BytesIO
from yattag import Doc, indent
from zipfile import ZipFile
from .Document import Document
from .common import WQXException

class Submission:
  __document: Document

  def __init__(self, o=None, *,
    document:Document = None
  ):
    if isinstance(o, Document):
      # Assign attributes from object without typechecking
      self.__document = o.document
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.document = o.get('document', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.document = document
  
  @property
  def document(self) -> Document:
    return self.__document
  @document.setter
  def document(self, val:Document) -> None:
    if not isinstance(val, Document):
      raise TypeError("Attribute 'document' must be a Document object.")
    self.__document = val

  def generateXML(self) -> str:
    if not self.__document:
      raise WQXException("Attribute 'document' is required.")

    doc, tag, text, line = Doc().ttl()

    doc.asis('<?xml version="1.0" encoding="UTF-8"?>')
    doc.asis(self.__document.generateXML('Document'))

    return doc.getvalue()

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
