from datetime import datetime
from io import BytesIO
from yattag import Doc, indent
from zipfile import ZipFile
from .MonitoringLocation import MonitoringLocation
from .WQXException import WQXException

class Submission:
  __author: str
  __comment: str
  __contactInfo: str
  __creationTime: datetime
  __id: str
  __monitoringLocation: MonitoringLocation
  __notification: str
  __organization: str
  __organizationDescriptionText: str
  __organizationFormalName: str
  __organizationIdentifier: str
  __payloadOperation: str
  __title: str

  def __init__(self,Id:str) -> None:
    if not isinstance(Id, str):
      raise ValueError( "Id must be a string.")
    self.__author = None
    self.__comment = None
    self.__contactInfo = None
    self.__creationTime = datetime.now()
    self.__id = Id
    self.__monitoringLocation = None
    self.__notification = None
    self.__organization = None
    self.__organizationDescriptionText = None
    self.__organizationFormalName = None
    self.__organizationIdentifier = None
    self.__payloadOperation = None
    self.__title = 'WQX'
  
  @property
  def author(self) -> str:
    return self.__author
  @author.setter
  def author(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'author' must be a string.")
    if len(val) < 1:
      raise TypeError("Property 'author' is required.")
    self.__author = val

  @property
  def comment(self) -> str:
    return self.__comment
  @comment.setter
  def comment(self, val) -> None:
    if val is None or len(val) < 1:
      self.__comment = None
    if not isinstance(val, str):
      raise TypeError("Property 'comment' must be a string.")
    self.__comment = val

  @property
  def creationTime(self) -> datetime:
    return self.__creationTime
  @creationTime.setter
  def creationTime(self, val:datetime) -> None:
    if not isinstance(val, datetime):
      raise TypeError("Property 'creationTime' must be a datetime.")
    self.__creationTime = val
  
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
  def monitoringLocation(self) -> MonitoringLocation:
    return self.__monitoringLocation
  @monitoringLocation.setter
  def monitoringLocation(self, val:MonitoringLocation) -> None:
    if not isinstance(val, MonitoringLocation):
      raise TypeError("Property 'monitoringLocation' must be a MonitoringLocation")
    self.__monitoringLocation = val

  @property
  def notification(self) -> str:
    return self.__notification
  @notification.setter
  def notification(self, val) -> None:
    if val is None or len(val) < 1:
      self.__notification = None
    if not isinstance(val, str):
      raise TypeError("Property 'notification' must be a string.")
    self.__notification = val

  @property
  def organization(self) -> str:
    return self.__organization
  @organization.setter
  def organization(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'organization' must be a string.")
    if len(val) < 1:
      raise ValueError("Property 'organization is required.")
    self.__organization = val

  @property
  def organizationDescriptionText(self) -> str:
    return self.__organizationDescriptionText
  @organizationDescriptionText.setter
  def organizationDescriptionText(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'organizationDescriptionText' must be a string")
    if len(val) < 1:
      raise ValueError("Property 'organizationDescriptionText' is required.")
    self.__organizationDescriptionText = val

  @property
  def organizationFormalName(self) -> str:
    return self.__organizationFormalName
  @organizationFormalName.setter
  def organizationFormalName(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'organizationFormalName' must be a string")
    if len(val) < 1:
      raise ValueError("Property 'organizationFormalName' is required.")
    self.__organizationFormalName = val

  @property
  def organizationIdentifier(self) -> str:
    return self.__organizationIdentifier
  @organizationIdentifier.setter
  def organizationIdentifier(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'organizationIdentifier' must be a string")
    if len(val) < 1:
      raise ValueError("Property 'organizationIdentifier' is required.")
    self.__organizationIdentifier = val

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

  @property
  def title(self) -> str:
    return self.__title
  @title.setter
  def title(self, val:str) -> None:
    if not isinstance(val, str):
      raise TypeError("Property 'title' must be a string")
    if len(val) < 1:
      raise ValueError("Property 'title' is required.")
    self.__title = val


  def generateXML(self):
    if not self.__author:
      raise WQXException("Property 'author' must be set before XML can be generated.")
    if not self.__contactInfo:
      raise WQXException("Property 'contactInfo' must be set before XML can be generated.")
    if not self.__organization:
      raise WQXException("Property 'organization' must be set before XML can be generated.")
    if not self.__organizationDescriptionText:
      raise WQXException("Property 'organizationDescriptionText' must be set before XML can be generated.")
    if not self.__organizationFormalName:
      raise WQXException("Property 'organizationFormalName' must be set before XML can be generated.")
    if not self.__organizationIdentifier:
      raise WQXException("Property 'organizationIdentifier' must be set before XML can be generated.")
    if not self.__payloadOperation:
      raise WQXException("Property 'payloadOperation' must be set before XML can be generated.")

    doc, tag, text, line = Doc().ttl()
    doc.asis('<?xml version="1.0" encoding="UTF-8"?>')
    with tag('Document',  ('xmlns','http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd'), ('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')):
      with tag('Header'):
        line('Author', self.__author)
        line('Organization', self.__organization)
        line('Title', self.__title)
        line('CreationTime', self.__creationTime.astimezone().replace(microsecond=0).isoformat())
        line('ContactInfo', self.__contactInfo)
        line('Notification', self.__notification)
      with tag('Payload', ('Operation', self.__payloadOperation)):
        with tag('WQX', ('xmlns', 'http://www.exchangenetwork.net/schema/wqx/3'), ('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance'), ('xsi:schemaLocation','http://www.exchangenetwork.net/schema/wqx/3 http://www.exchangenetwork.net/schema/wqx/3/index.xsd')):
          with tag('Organization'):
            with tag('OrganizationDescription'):
              line('OrganizationIdentifier', self.__organizationIdentifier)
              line('OrganizationFormalName', self.__organizationFormalName)
              line('OrganizationDescriptionText', self.__organizationDescriptionText)
            if isinstance(self.__monitoringLocation, MonitoringLocation):
              doc.asis( self.__monitoringLocation.generateXML() )
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
