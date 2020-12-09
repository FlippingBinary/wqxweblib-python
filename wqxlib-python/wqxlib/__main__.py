import sys
from .Submission import Submission

def main(argv:list):
  if len(argv) < 1 or argv[0] != 'test':
    print('This module does not yet support direct execution. It should be used as a library.')
    print('More information is available at https://github.com/Flippingbinary/wqxlib/wqxlib-python')
    return 0

  # Hidden behavior for testing purposes
  sub = Submission('20201209ML8')
  sub.author = "Name of Author"
  sub.organization = "WVSU / Agricultural and Environmental Research Station"
  sub.contactInfo = "P.O. Box 1000, Institute, WV 25112"
  sub.notification = "nobody@nowhere.com"
  sub.payloadOperation = "Update-Insert"
  sub.organizationIdentifier = "WQXTEST"
  sub.organizationFormalName = "WQX Test Organization"
  sub.organizationDescriptionText = "Test organization"
  sub.payload.monitoringLocation.monitoringLocationIdentity.monitoringLocationIdentifier = "GREENUP"
  sub.payload.monitoringLocation.monitoringLocationIdentity.monitoringLocationName = "Greenup Dam"
  sub.payload.monitoringLocation.monitoringLocationIdentity.monitoringLocationTypeName = "River/Stream"
  sub.payload.monitoringLocation.monitoringLocationIdentity.hucEightDigitCode = "05090103"
  sub.payload.monitoringLocation.monitoringLocationIdentity.hucTwelveDigitCode = "050901030107"
  sub.payload.monitoringLocation.monitoringLocationIdentity.tribalLandIndicator = False
  sub.payload.monitoringLocation.monitoringLocationGeospatial.latitudeMeasure = "38.6470"
  sub.payload.monitoringLocation.monitoringLocationGeospatial.longitudeMeasure = "-82.8587"
  sub.payload.monitoringLocation.monitoringLocationGeospatial.sourceMapScale = "2400"
  sub.payload.monitoringLocation.monitoringLocationGeospatial.horizontalCollectionMethodName = "Interpolation-Map"
  sub.payload.monitoringLocation.monitoringLocationGeospatial.horizontalCoordinateReferenceSystemDatumName = "NAD83"
  sub.payload.monitoringLocation.monitoringLocationGeospatial.countryCode = "US"
  sub.payload.monitoringLocation.monitoringLocationGeospatial.stateCode = "WV"
  sub.payload.monitoringLocation.monitoringLocationGeospatial.countyCode = "039"
  print(sub.generateXML())

if __name__ == "__main__":
  main(sys.argv[1:])
