from datetime import datetime
from yattag import Doc, indent
from .MonitoringLocation import MonitoringLocation

class Submission:

  def __init__(self,Id):
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
