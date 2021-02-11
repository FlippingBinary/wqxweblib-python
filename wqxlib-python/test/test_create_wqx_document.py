import unittest
import xml.etree.cElementTree as ET
from wqxlib import ( # type: ignore
  Document,
  Header,
  Payload,
  Submission
)
from wqxlib.wqx_v3_0 import ( # type: ignore
  MonitoringLocation,
  MonitoringLocationGeospatial,
  MonitoringLocationIdentity,
  Organization,
  OrganizationDescription,
  WQX
)


#from .Document import Document
#from .Header import Header
#from .Payload import Payload
#from .Submission import Submission
#from .wqx_v3_0 import (
#  Activity,
#  ActivityDescription,
#  Measure,
#  MonitoringLocation,
#  MonitoringLocationIdentity,
#  MonitoringLocationGeospatial,
#  Organization,
#  OrganizationDescription,
#  Result,
#  ResultDescription,
#  ActivityStartDate,
#  WQX
#)

class TestCreateWQXDocument(unittest.TestCase):

  def test_create_wqx_document(self):

    submission = Submission(
      document=Document(
        id='20201209ML8',
        header=Header(
          author = "Test Author",
          organization = "Test Organization",
          contactInfo = "Test Organization Mailing or Physical Address",
          notification = "test@example.org"
        ),
        # Even though we are assigning a single object to the payload key here,
        # it becomes a list item which can be appended to later
        payload=Payload(
          operation='Update-Insert',
          wqx=WQX(
            organization=Organization(
              organizationDescription=OrganizationDescription(
                organizationIdentifier = "WQXTEST",
                organizationFormalName = "WQX Test Organization",
                organizationDescriptionText = "Test"
              ),
              monitoringLocation=MonitoringLocation(
                monitoringLocationGeospatial=MonitoringLocationGeospatial(
                  latitudeMeasure = "38.6470",
                  longitudeMeasure = "-82.8587",
                  sourceMapScale = "2400",
                  horizontalCollectionMethodName = "Interpolation-Map",
                  horizontalCoordinateReferenceSystemDatumName = "NAD83",
                  countryCode = "US",
                  stateCode = "WV",
                  countyCode = "039"
                ),
                monitoringLocationIdentity=MonitoringLocationIdentity(
                  monitoringLocationIdentifier = "GREENUP",
                  monitoringLocationName = "Greenup Dam",
                  monitoringLocationTypeName = "River/Stream",
                  hucEightDigitCode = "05090103",
                  hucTwelveDigitCode = "050901030107",
                  tribalLandIndicator = False
                )
              )
            )
          )
        )
      )
    )
    doc = submission.document.generateXML()

    tree = ET.ElementTree(ET.fromstring(doc))
    root = tree.getroot()
    self.assertEqual(root.tag,'{http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd}Document')
    header = root[0]
    self.assertEqual(header.tag,'{http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd}Header')
    self.assertEqual(header[0].text,'Test Author')
    self.assertEqual(header[1].text,'Test Organization')
    self.assertEqual(header[2].text,'WQX')
    self.assertEqual(header[4].text,'Test Organization Mailing or Physical Address')
    self.assertEqual(header[5].text,'test@example.org')
    payload = root[1]
    self.assertEqual(payload.tag,'{http://www.exchangenetwork.net/schema/v1.0/ExchangeNetworkDocument.xsd}Payload')
    self.assertEqual(payload.attrib.get('Operation'),'Update-Insert')


  # Add an additional payload to the existing submission document
  # This demonstrates how a document can be modified on the fly so
  # it can be built as the data is gathered rather than waiting until
  # all data is known.
#  submission.document.payload.append(Payload(
#    operation=Payload.UPDATE_INSERT,
#    wqx=WQX(
#      organization=Organization(
#        organizationDescription=OrganizationDescription(
#          organizationIdentifier = "WQXTEST",
#          organizationFormalName = "WQX Test Organization",
#          organizationDescriptionText = "Test organization"
#        ),
#        activity=Activity(
#          activityDescription=ActivityDescription(
#            activityIdentifier="Work",
#            activityTypeCode="Basic?",
#            activityMediaName="Water",
#            activityStartDate=ActivityStartDate(year=2021, month=1, day=1),
#            projectIdentifier="Something"
#          ),
#          result=Result(
#            resultDescription=ResultDescription(
#              characteristicName="Test",
#              resultStatusIdentifier="",
#              resultMeasure=Measure(
#                resultMeasureValue="15.4",
#                measureUnitCode="lbs"
#              )
#            )
#          )
#        )
#      )
#    )
#  ))
