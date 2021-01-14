from .Document import Document
from .Header import Header
from .Payload import Payload
from .Submission import Submission
from .wqx_v3_0.Activity import Activity
from .wqx_v3_0.ActivityDescription import ActivityDescription
from .wqx_v3_0.Measure import Measure
from .wqx_v3_0.MonitoringLocation import MonitoringLocation
from .wqx_v3_0.MonitoringLocationGeospatial import *
from .wqx_v3_0.MonitoringLocationIdentity import MonitoringLocationIdentity
from .wqx_v3_0.Organization import Organization
from .wqx_v3_0.OrganizationDescription import OrganizationDescription
from .wqx_v3_0.Result import Result
from .wqx_v3_0.ResultDescription import ResultDescription
from .wqx_v3_0.SimpleContent import ActivityStartDate
from .wqx_v3_0.WQX import WQX
import sys

def main(argv:list):
  if len(argv) < 1 or argv[0] != 'test':
    print('This module does not yet support direct execution. It should be used as a library.')
    print('More information is available at https://github.com/Flippingbinary/wqxlib/wqxlib-python')
    return 0

  # Hidden behavior for testing purposes
  submission = Submission(
    document=Document(
      id='20201209ML8',
      header=Header(
        author = "Name of Author",
        organization = "WVSU / Agricultural and Environmental Research Station",
        contactInfo = "P.O. Box 1000, Institute, WV 25112",
        notification = "nobody@nowhere.com"
      ),
      payload=Payload(
        operation='Update-Insert',
        wqx=WQX(
          organization=Organization(
            organizationDescription=OrganizationDescription(
              organizationIdentifier = "WQXTEST",
              organizationFormalName = "WQX Test Organization",
              organizationDescriptionText = "Test organization"
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

  submission.document.payload.append(Payload(
    operation=Payload.UPDATE_INSERT,
    wqx=WQX(
      organization=Organization(
        organizationDescription=OrganizationDescription(
          organizationIdentifier = "WQXTEST",
          organizationFormalName = "WQX Test Organization",
          organizationDescriptionText = "Test organization"
        ),
        activity=Activity(
          activityDescription=ActivityDescription(
            activityIdentifier="Work",
            activityTypeCode="Basic?",
            activityMediaName="Water",
            activityStartDate=ActivityStartDate(year=2021, month=1, day=1),
            projectIdentifier="Something"
          ),
          result=Result(
            resultDescription=ResultDescription(
              characteristicName="Test",
              resultStatusIdentifier="",
              resultMeasure=Measure(
                resultMeasureValue="15.4",
                measureUnitCode="lbs"
              )
            )
          )
        )
      )
    )
  ))

  print(submission.document.generateXML())

if __name__ == "__main__":
  main(sys.argv[1:])
