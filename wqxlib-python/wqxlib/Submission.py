from datetime import datetime
from io import BytesIO
from yattag import Doc, indent
from zipfile import ZipFile
from .MonitoringLocation import MonitoringLocation

class Submission:
  author: str
  contactInfo: str
  creationTime: datetime
  id: str
  monitoringLocation: MonitoringLocation
  notification: str
  organization: str
  organizationDescriptionText: str
  organizationFormalName: str
  organizationIdentifier: str
  payloadOperation: str
  title: str

  def __init__(self,Id:str) -> None:
    if not isinstance(Id, str):
      raise ValueError( "Id must be a string.")
    self.id = Id
    # Document / Header
    self.author = ''
    self.organization = ''
    self.title = 'WQX'
    self.creationTime = datetime.now()
    self.contactInfo = ''
    self.notification = ''
    # Document / Payload
    self.payloadOperation = ''
    # Document / Payload / WQX / Organization / OrganizationDescription
    self.organizationIdentifier = 'WQXTEST'
    self.organizationFormalName = 'WQX Test'
    self.organizationDescriptionText = 'WQX Test'
    self.monitoringLocation = None

  def generateXML(self):
    doc, tag, text, line = Doc().ttl()
    doc.asis('<?xml version="1.0" encoding="UTF-8"?>')
    with tag('Document',  ('xmlns','http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd'), ('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')):
      with tag('Header'):
        line('Author', self.author)
        line('Organization', self.organization)
        line('Title', self.title)
        line('CreationTime', self.creationTime.astimezone().replace(microsecond=0).isoformat())
        line('ContactInfo', self.contactInfo)
        line('Notification', self.notification)
      with tag('Payload', ('Operation', self.payloadOperation)):
        with tag('WQX', ('xmlns', 'http://www.exchangenetwork.net/schema/wqx/3'), ('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance'), ('xsi:schemaLocation','http://www.exchangenetwork.net/schema/wqx/3 http://www.exchangenetwork.net/schema/wqx/3/index.xsd')):
          with tag('Organization'):
            with tag('OrganizationDescription'):
              line('OrganizationIdentifier', self.organizationIdentifier)
              line('OrganizationFormalName', self.organizationFormalName)
              line('OrganizationDescriptionText', self.organizationDescriptionText)
            if isinstance(self.monitoringLocation, MonitoringLocation):
              doc.asis( self.monitoringLocation.generateXML() )
    return indent(doc.getvalue(), indentation = ' '*2)

  def generateZIP(self, fileName:str=None):
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
