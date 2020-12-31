from .Document import Document
from .Header import Header
from .Payload import Payload
from .Submission import Submission
from .wqx_v3_0.MonitoringLocation import MonitoringLocation
from .wqx_v3_0.MonitoringLocationGeospatial import *
from .wqx_v3_0.MonitoringLocationIdentity import MonitoringLocationIdentity
from .wqx_v3_0.Organization import Organization
from .wqx_v3_0.OrganizationDescription import OrganizationDescription
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

  print(submission.document.generateXML())

if __name__ == "__main__":
  main(sys.argv[1:])
