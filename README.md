# Python library for WQX (wqxlib)

This is a simple Python library for interacting with the EPA's WQX data submission service. It serves two purposes. First, it aims to be mimick the [WQX Web API endpoints](https://www.epa.gov/sites/production/files/2018-09/documents/wqx_web_application_programming_interface_api.pdf) as much as possible with the `WQXWeb` class. Second, it simplifies the creation of XML documents for direct submission without using an import configuration file. If your use-case is complex, that second feature may save you the hassle of uploading incremental changes to an import configuration file as you detect more edge cases. Just modify your code to produce the proper XML file and use the `WQXWeb` class to upload that. It's also useful for submitting new monitoring locations or other types of data which are one-off situations. Sometimes it's easier to just build the XML file directly than it is to first create an import configuration file (or copy one) and specify the parameters in a CSV or XSL file. If you find a bug, please submit a pull request on [Github](https://github.com/FlippingBinary/wqxlib) or open an issue there. I'm also open to suggestions for how to improve the creation of XML files. Currently, it's quite complex due to its flexibility.

_NOTE: This module is useless without EPA credentials for WQX submission._

## Contents

- [Python library for WQX (wqxlib)](#python-library-for-wqx-wqxlib)
  - [Contents](#contents)
  - [Getting Started](#getting-started)
  - [WQXWeb Data Submission Patterns](#wqxweb-data-submission-patterns)
  - [Import WQXWeb Module](#import-wqxweb-module)
- [WQXLib's WQXWeb API Reference](#wqxlibs-wqxweb-api-reference)
  - [Upload](#upload)
  - [UploadAttachment](#uploadattachment)
  - [StartImport](#startimport)
  - [StartXmlExport](#startxmlexport)
  - [SubmitDatasetToCdx](#submitdatasettocdx)
  - [SubmitFileToCdx](#submitfiletocdx)
  - [GetStatus](#getstatus)
  - [GetDocumentList](#getdocumentlist)
  - [Projects](#projects)
  - [MonitoringLocations](#monitoringlocations)
- [WQXLib XML API Reference](#wqxlib-xml-api-reference)
  - [Document](#document)
  - [Header](#header)
  - [Payload](#payload)
  - [Submission](#submission)
- [WQXLib's WQX v3.0 XML API Reference](#wqxlibs-wqx-v30-xml-api-reference)
  - [Activity](#activity)
  - [ActivityDescription](#activitydescription)
  - [ActivityGroup](#activitygroup)
  - [ActivityLocation](#activitylocation)
  - [ActivityMetric](#activitymetric)
  - [ActivityMetricType](#activitymetrictype)
  - [AlternateMonitoringLocationIdentity](#alternatemonitoringlocationidentity)
  - [AquiferInformation](#aquiferinformation)
  - [AttachedBinaryObject](#attachedbinaryobject)
  - [BibliographicReference](#bibliographicreference)
  - [BiologicalActivityDescription](#biologicalactivitydescription)
  - [BiologicalHabitatCollectionInformation](#biologicalhabitatcollectioninformation)
  - [BiologicalHabitatIndex](#biologicalhabitatindex)
  - [BiologicalResultDescription](#biologicalresultdescription)
  - [CollectionEffort](#collectioneffort)
  - [ComparableAnalyticalMethod](#comparableanalyticalmethod)
  - [DataQualityIndicator](#dataqualityindicator)
  - [DetectionQuantitationLimit](#detectionquantitationlimit)
  - [ElectronicAddress](#electronicaddress)
  - [Entity_Update_Identifiers](#entity_update_identifiers)
  - [FrequencyClassInformation](#frequencyclassinformation)
  - [HorizontalAccuracyMeasure](#horizontalaccuracymeasure)
  - [IndexType](#indextype)
  - [LabSamplePreparation](#labsamplepreparation)
  - [Measure](#measure)
  - [MeasureCompact](#measurecompact)
  - [MonitoringLocation](#monitoringlocation)
  - [MonitoringLocationGeospatial](#monitoringlocationgeospatial)
  - [MonitoringLocationIdentity](#monitoringlocationidentity)
  - [NetInformation](#netinformation)
  - [Organization](#organization)
  - [OrganizationAddress](#organizationaddress)
  - [OrganizationDescription](#organizationdescription)
  - [Organization_Delete](#organization_delete)
  - [Project](#project)
  - [ProjectMonitoringLocationWeighting](#projectmonitoringlocationweighting)
  - [ReferenceMethod](#referencemethod)
  - [Result](#result)
  - [ResultAnalyticalMethod](#resultanalyticalmethod)
  - [ResultDescription](#resultdescription)
  - [ResultLabInformation](#resultlabinformation)
  - [SampleDescription](#sampledescription)
  - [SamplePreparation](#samplepreparation)
  - [SimpleContent](#simplecontent)
  - [TaxonomicDetails](#taxonomicdetails)
  - [Telephonic](#telephonic)
  - [WellInformation](#wellinformation)
  - [WQX](#wqx)
  - [WQXTime](#wqxtime)
  - [WQXDelete](#wqxdelete)
  - [WQXUpdateIdentifiers](#wqxupdateidentifiers)

## Getting Started

Install this package using `pip`

    pip install wqxlib

**Semantic Versioning** - This package uses semantic versioning to protect you against changes which break backward compatibility. The version number will be in the form: `x.y.z` where `x` represents the major release number, `y` represents the minor release number, and `z` represents the patch release number. Backward compatible bug fixes result in an increased patch release number. Backward compatible new features are introduced with an increased minor release number. Changes which break backward compatibility are indicated with an increased major release number. I recommend locking the major release number in your `requirements.txt` file if you are using one.

## WQXWeb Data Submission Patterns

**Aggressive Method** - Use this if you trust the data you produce.

1. Upload a file using `Upload`.
2. (optional) Upload an attachment file using `UploadAttachment`.
3. Start the import with auto export and auto submit using `StartImport`.
4. Periodically check the status using `GetStatus`.

**Cautious Method** - Use this if you want to check how WQX responds to your data before submitting.

1. Upload a file using `Upload`.
2. (optional) Upload an attachment file using `UploadAttachment`.
3. Start the import with auto export and without auto submit using `StartImport`.
4. Periodically check the status using `GetStatus`.
5. Submit dataset to CDX using `SubmitDatasetToCdx`.
6. Periodically check the status using `GetStatus`.

**Micromanaging Method** - Use this method if you want to manage each step of the process that you can.
1. Upload a file using `Upload`.
2. (optional) Upload an attachment file using `UploadAttachment`.
3. Start the import without auto export and without auto submit using `StartImport`.
4. Periodically check the status using `GetStatus`.
5. Start the XML Export using `StartXmlExport`.
6. Periodically check the status using `GetStatus`.
7. Submit dataset to CDX using `SubmitDatasetToCdx`.
8. Periodically check the status using `GetStatus`.

![Flowchart representing the methods described above](https://raw.githubusercontent.com/FlippingBinary/wqxlib/main/wqxlib-python/flowchart.jpg)

## Import WQXWeb Module

This module must be imported and instantiated with your `userID` and `privateKey` before any of the other functions can be used.

    from wqxlib import WQXWeb

    wqx = WQXWeb("my username", "my private key")

# WQXLib's WQXWeb API Reference

This following methods mirror what is shown in the EPA's documentation for the WQX Web API endpoints. Some differences exist for the sake of Python integration while still allowing the inputs indicated in the documentation.

## Upload

Upload a file to the web server (to be imported).

**Parameters:**

- `filename` (required string) - A name to give the file. This does not need to match any local filename. The allowed file extensions are:
  - txt
  - csv
  - xlsx
  - xls
  - xml
  - zip
- `contents` (required bytes) - The contents of the file to be uploaded provided either by converting some provided `data` string with the `bytes(data, 'utf-8')` function or by passing some `file` object's `file.read()` function.

**Returns:** `fileId` - A unique identifier for the uploaded file.

**Example with generated data:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    data="""column1,column2
    value1,value2"""

    fileId = wqx.Upload( filename="datafile.csv", content=bytes(data,'utf-8') )

    print( f"The uploaded file has been assigned fileId {fileId}." )

**Example using a file from the local filesystem:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    with open( 'data.csv', 'rb' ) as f:
        fileId = wqx.Upload( filename="datafile.csv", contents=f.read() )

        print( f"The uploaded file has been assigned fileId {fileId}." )

## UploadAttachment

Upload an attachment to the web server (to be imported).

**Parameters:**

- `filename` (required string) - A name to give the file. This does not need to match any local filename. The only allowed file extension is:
  - zip
- `contents` (required bytes) - The contents of the file to be uploaded provided either by converting some provided `data` string with the `bytes(data, 'utf-8')` function or by passing some `file` object's `file.read()` function.

**Returns:** `fileId` - A unique identifier for the uploaded file.

**Example using a file from the local filesystem:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    with open( 'attachment.zip', 'rb' ) as f:
        attachmentFileId = wqx.UploadAttachment( filename="attach.zip", contents=f.read() )

        print( f"The uploaded file has been assigned attachmentFileID {attachmentFileID}." )

## StartImport

Start importing a file and attachment that was previously uploaded.

**Parameters:**

- `importConfigurationId` (required string) - The Import Configuration ID of an existing Import Configuration which should be applied to the import.
- `fileId` (required string) - The return value of `Upload`.
- `attachmentFileId` (optional string) - The return value of `UploadAttachment`.
- `fileType` (required enum or string) - The type of file you uploaded with `Upload`. This must be one of the following enum members provided by the `WQX` module or their corresponding strings:
  - `CSV`
  - `TAB`
  - `TILDE`
  - `PIPE`
  - `XLS`
  - `XLSX`
- `newOrExistingData` (required enum or integer) - Declare whether the contents of your upload represents new data or replaces existing data. This must be one of the following enum members provided by the `WQX` module or their corresponding integers:
  - `CONTAINS_NEW_OR_EXISTING` (0) - file may contain new and/or existing data.
  - `CONTAINS_NEW_ONLY` (1) - file contains new data only.
  - `CONTAINS_EXISTING_ONLY` (2) - file contains existing data only (to be replaced).
- `uponCompletion` (required enum or integer) - Declare what to do after the upload finishes. This must be one of the following enum members provided by the `WQX` module or their corresponding integers:
  - `DO_NOT_EXPORT` (0) - do nothing.
  - `EXPORT_IMPORT` (1) - start export.
  - `SUBMIT_IMPORT` (2) - start export and submit to CDX.
- `uponCompletionCondition` (optionally required enum or integer) - Declare what conditions permit auto export or auto submit. This must be one of the following enum members provided by the `WQX` module or their corresponding integers:
  - `NOT_APPLICABLE` (0) - not applicable (`uponCompletion` is `DO_NOTHING` or not provided).
  - `EXPORT_IF_NO_ERROR` (1) - start export only if no import errors.
  - `EXPORT_IF_NO_WARNING` (2) - start export only if no import errors and no warnings.
  - `EXPORT_ALWAYS` (3) - start export even when there are import errors.
- `worksheetsToImport` (optional string) - If provided, this must be a comma delimited list of values (1-based), e.g. "`1,3`". This parameter value will be ignored when the fileType is not `XLS` or `XLSX`. If no value is passed in (and it's applicable) then we'll use the value from the Import Configuration.
- `ignoreFirstRowOfFile` (optional boolean) - Ignore the first row of the data file if this parameter is true. This parameter value will be ignored for Expert Mode Import Configurations.
- `generatedElements` (optional dictionary) - Each key must match an existing generated element name from the import configuration. No more than five keys can be in the dictionary and this parameter cannot be used along with the `generatedElementName1`, `generatedElementName2`, `generatedElementName3`, `generatedElementName4`, or `generatedElementName5` parameters.
- `generatedElementName1` (optional string) - Must match an existing generated element name from the import configuration.
- `generatedElementValue1` (optionally required string) - Must provide a value if `generatedElementName1` is provided.
- `generatedElementName2` (optional string) - Must match an existing generated element name from the import configuration.
- `generatedElementValue2` (optionally required string) - Must provide a value if `generatedElementName2` is provided.
- `generatedElementName3` (optional string) - Must match an existing generated element name from the import configuration.
- `generatedElementValue3` (optionally required string) - Must provide a value if `generatedElementName3` is provided.
- `generatedElementName4` (optional string) - Must match an existing generated element name from the import configuration.
- `generatedElementValue4` (optionally required string) - Must provide a value if `generatedElementName4` is provided.
- `generatedElementName5` (optional string) - Must match an existing generated element name from the import configuration.
- `generatedElementValue5` (optionally required string) - Must provide a value if `generatedElementName5` is provided.

**Returns:** `datasetId` - A unique identifier for the dataset.

**Example without auto export:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    datasetId = wqx.StartImport( importConfigurationID, fileId, fileType=wqx.CSV, newOrExistingData=wqx.CONTAINS_NEW_OR_EXISTING, uponCompletion=wqx.DO_NOT_EXPORT, ignoreFirstRowOfFile=True )

    print( f"The import of dataset {datasetId} has begun. Check it's status with a call to wqx.GetStatus(datasetId)" )

**Example with auto export and without auto submit:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    datasetId = wqx.StartImport( importConfigurationID, fileId, fileType=wqx.CSV, newOrExistingData=wqx.CONTAINS_NEW_OR_EXISTING, uponCompletion=wqx.EXPORT_IMPORT, ignoreFirstRowOfFile=True )

    print( f"The import of dataset {datasetId} has begun. Check it's status with a call to wqx.GetStatus(datasetId)" )

**Example with auto submit:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    datasetId = wqx.StartImport( importConfigurationID, fileId, fileType=wqx.CSV, newOrExistingData=wqx.CONTAINS_NEW_OR_EXISTING, uponCompletion=wqx.SUBMIT_IMPORT, ignoreFirstRowOfFile=True )

    print( f"The import of dataset {datasetId} has begun. Check it's status with a call to wqx.GetStatus(datasetId)" )

## StartXmlExport

Start creating the XML submission file (for CDX).

**Parameters:**

- `datasetId` (required string) - The return value of `StartImport` or `SubmitFileToCdx`.
- `uponCompletion` (required enum or integer) - Declare what to do after the export finishes. This must be one of the following enum members provided by the `WQX` module or their corresponding integers:
  - `DO_NOT_SUBMIT` (0) - do nothing.
  - `SUBMIT_EXPORT` (1) - submit to CDX.

**Returns:** `status` - The initial status for the dataset.

**Example using enum:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    status = wqx.StartXmlExport( datasetId, wqx.SUBMIT_EXPORT )

    print( "The initial status of dataset {datasetId} is as follows:" )
    print( status )

**Example using integer:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    status = wqx.StartXmlExport( datasetId, 1 )

    print( "The initial status of dataset {datasetId} is as follows:" )
    print( status )

## SubmitDatasetToCdx

Submit a dataset to CDX.

**Parameters:**

- `datasetId` (required string) - The return value of `StartImport` or `SubmitFileToCdx`.

**Returns:** `status` - The initial status for the dataset.

**Example:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    status = wqx.SubmitDatasetToCdx( datasetId )

    print( "The initial status of dataset {datasetId} is as follows:" )
    print( status )

## SubmitFileToCdx

Submit a previously uploaded WQX XML file to CDX.

**Parameters:**

- `fileId` (required string) - The return value of `Upload`.

**Returns:** `datasetId` - The new dataset ID.

**Example:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    datasetId = wqx.SubmitFileToCdx( fileId )

    print( f"The uploaded file has been assigned datasetId {datasetId}" )

## GetStatus

Get the status for a dataset. To avoid undue burden on the server, it is recommended that you not call this service more often than every 10 seconds. For large imports (longer than 20 minutes), calling this service periodically will guarantee that the server will not shutdown before the import completes.

**Parameters:**

- `datasetId` (required string) - The return value of `StartImport` or `SubmitFileToCdx`.

**Returns:** `statusMsg` - The status, percent complete, and position in queue for the dataset. Possible statuses:

- 'Waiting to Import'
- 'Importing'
- 'Imported'
- 'Import Failed'
- 'Waiting to Export'
- 'Waiting to Export and Submit'
- 'Exporting'
- 'Exported'
- 'Export Failed'
- 'Processing at CDX'
- 'Completed at CDX'
- 'Failed at CDX'
- 'Waiting to Delete'
- 'Deleting'
- 'Delete Failed'
- 'Waiting to Update WQX'
- 'Updating WQX'
- 'Updated WQX'
- 'Update Failed'

**Example:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    statusMsg = wqx.GetStatus( datasetId )

    print( f"Current status of datasetId {datasetId} is {statusMsg}" )

## GetDocumentList

Get the list of available documents for a dataset. Documents that are typically available for a dataset include:

- the original import file
- event logs (for the import and/or export in WQX Web)
- validation report (for the XML submission file - from CDX)
- processing report (for the XML submission file - from WQX)

**Parameters:**

- `datasetId` (required string) - The return value of `StartImport` or `SubmitFileToCdx`.

**Returns:** `urls` - A list of document URLs which can be used to download the documents.

**Example:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    urls = wqx.GetDocumentList( datasetId )

    print( "The documents associated with {datasetId} are:" )
    for url in urls:
        print( f" - {url}" )

## Projects

Get the projects for an organization.

**Parameters:**

- `organizationIdentifiersCsv` (required string) - Comma delimited list of organization identifiers (e.g. "id1,id2,id3") NOTE: No spaces.
- `projectIdentifiersCsv` (optional string) - Comma delimited list of project identifiers (e.g. "id1,id2,id3") NOTE: No spaces.
- `transactionIdentifier` (optional string) - Transaction identifier e.g. "_23090c89-c6a6-4dd1-b16f-73f8ac36fac1".
- `lastChangeDateMin` (optional date) - Minimum last change date.
- `lastChangeDateMax` (optional date) - Maximum last change date.
- `startRow` (conditionally optional integer) - Zero based start row. Conditionally required if `rowsToRetrieve` is supplied.
- `rowsToRetrieve` (conditionally optional integer) - Number of rows to retrieve. Conditionally required if `startRow` is supplied.

**Returns:** `projects` - WQX Schema 2.2 element values including the transaction id for the project.

**Example:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    projects = wqx.Projects( organizationIdentifiersCsv )

    print( f"The projects associated with {organizationIdentifiersCsv} are:" )
    for project in projects:
        print( f" - {project}" )

**Example to list projects from the previous week:**

    from wqxlib import WQXWeb
    from datetime import date, timedelta

    wqx = WQXWeb( 'username', 'private key in base64' )

    today = date.today()
    lastWeek = today - timedelta(weeks=1)
    projects = wqx.Projects( organizationIdentifiersCsv, lastChangeDateMin=lastWeek )

    print( "The projects associated with {organizationIdentifiersCsv} and modified since {lastWeek.strftime( "%m/%d/%Y")} are:" )
    for project in projects:
        print( f" - {project}" )

## MonitoringLocations

Get the locations for an organization.

**Parameters:**

- `organizationIdentifiersCsv` (required string) - Comma delimited list of organization identifiers (e.g. "id1,id2,id3") NOTE: No spaces.
- `monitoringLocationIdentifiersCsv` (optional string) - Comma delimited list of monitoring location identifiers (e.g. "id1,id2,id3") NOTE: No spaces.
- `monitoringLocationName` (optional string) - Monitoring Location Name. Wildcards are supported (e.g. "Location%" means anything starting with "Location").
- `monitoringLocationType` (optional string) - Monitoring Location Type. Wildcards are supported (e.g. "Location%" means anything starting with "Location"). Allowed values (enforced by the endpoint, not this library):
  - Atmosphere
  - BEACH Program Site-Channelized stream
  - BEACH Program Site-Estuary
  - BEACH Program Site-Great Lake
  - BEACH Program Site-Lake
  - BEACH Program Site-Land
  - BEACH Program Site-Land runoff
  - BEACH Program Site-Ocean
  - BEACH Program Site-River/Stream
  - BEACH Program Site-Storm sewer
  - BEACH Program Site-Waste sewer
  - Borehole
  - Canal Drainage
  - Canal Irrigation
  - Canal Transport
  - Cave
  - CERCLA Superfund Site
  - Channelized Stream
  - Combined Sewer
  - Constructed Diversion Dam
  - Constructed Tunnel
  - Constructed Water Transport Structure
  - Constructed Wetland
  - Estuary
  - Facility Industrial
  - Facility Municipal Sewage (POTW)
  - Facility Other
  - Facility Privately Owned Non-industrial
  - Facility Public Water Supply (PWS)
  - Floodwater non-Urban
  - Floodwater Urban
  - Gallery
  - Gas-Condensate
  - Gas-Engine
  - Gas-Extraction
  - Gas-Flare
  - Gas-Monitoring Probe
  - Gas-Passive Vent
  - Gas-Subslab
  - Gas-Temporary
  - Great Lake
  - Lake
  - Land
  - Land Flood Plain
  - Land Runoff
  - Landfill
  - Leachate-Extraction
  - Leachate-Head Well
  - Leachate-Lysimeter
  - Leachate-SamplePoint
  - Local Air Monitoring Station
  - Mine Pit
  - Mine/Mine Discharge
  - Mine/Mine Discharge Adit (Mine Entrance)
  - Mine/Mine Discharge Tailings Pile
  - Mine/Mine Discharge Waste Rock Pile
  - National Air Monitoring Station
  - Ocean
  - Oil and Gas Well
  - Other-Ground Water
  - Other-Surface Water
  - Pipe, Unspecified Source
  - Playa
  - Pond-Anchialine
  - Pond-Sediment
  - Pond-Stock
  - Pond-Stormwater
  - Pond-Wastewater
  - Reservoir
  - River/Stream
  - River/stream Effluent-Dominated
  - River/Stream Ephemeral
  - River/Stream Intermittent
  - River/Stream Perennial
  - Riverine Impoundment
  - Seep
  - Spigot / Faucet
  - Spring
  - State/Local Air Monitoring Station
  - Storm Sewer
  - Survey Monument
  - Test Pit
  - Waste Pit
  - Waste Sewer
  - Well
  - Wetland Estuarine-Emergent
  - Wetland Estuarine-Forested
  - Wetland Estuarine-Scrub-Shrub
  - Wetland Lacustrine-Emergent
  - Wetland Palustrine Pond
  - Wetland Palustrine-Emergent
  - Wetland Palustrine-Forested
  - Wetland Palustrine-Moss-Lichen
  - Wetland Palustrine-Shrub-Scrub
  - Wetland Riverine-Emergent
  - Wetland Undifferentiated
- `transactionIdentifier` (optional string) - Transaction identifier e.g. "_23090c89-c6a6-4dd1-b16f-73f8ac36fac1".
- `lastChangeDateMin` (optional date) - Minimum last change date.
- `lastChangeDateMax` (optional date) - Maximum last change date.
- `startRow` (conditionally optional integer) - Zero based start row. Conditionally required if `rowsToRetrieve` is supplied.
- `rowsToRetrieve` (conditionally optional integer) - Number of rows to retrieve. Conditionally required if `startRow` is supplied.

**Returns:** `locations` - WQX Schema 2.2 element values including the transaction id for the monitoring location.

**Example:**

    from wqxlib import WQXWeb

    wqx = WQXWeb( 'username', 'private key in base64' )

    locations = wqx.MonitoringLocations( organizationIdentifiersCsv )

    print( "The locations associated with {organizationIdentifiersCsv} are: " )
    for location in locations:
        print( f" - {location['MonitoringLocationName']}" )

# WQXLib XML API Reference

The following classes describe the larger structure of a valid XML document for WQXWeb submission. These classes will contain the building blocks provided by WQX v3.0.

## Document

The base document type used for submission to WQXWeb.

**Parameters:**

- `id` (ID)
- `header` (Header)
- `payload` (List[Payload])

## Header

**Parameters:**

- `author` (str)
- `organization` (str)
- `title` (str)
- `creationTime` (datetime)
- `comment` (str)
- `dataService` (str)
- `contactInfo` (str)
- `notification` (List[uri_reference])
- `sensitivity` (str)
- `property` (dict)

## Payload

The Payload section of the document contains the WQX data.

- `operation` (OperationType) - either "UPDATE_INSERT" or "DELETE".
- `wqx` (WQX) - this must be a v3.0 `WQX` object as described in the next section, if provided.
- `wqxUpdateIdentifiers` (WQXUpdateIdentifiers) - this must be a v3.0 `WQXUpdateIdentifiers` object as described in the next section, if provided.
- `wqxDelete` (WQXDelete) - this must be a v3.0 `WQXDelete` object as described in the next section, if provided.

## Submission

This is the container of the entire submission.

**Parameters:**

- `document` (Document)

# WQXLib's WQX v3.0 XML API Reference

The following classes describe the building blocks of a v3.0 XML document for WQXWeb submission. This is the current version of the standard and there are no plans to create an API for the older versions. If you want to, please use the pattern of the v3.0 code and submit a pull request so others can benefit from your code too.

All of the described classes come directly from the XSD files which are used by WQX to validate input.

To import any of the following types, pull them from `wqxlib.wqx_v3_0` like this:

    from wqxlib.wqx_v3_0 import (
      MonitoringLocation,
      MonitoringLocationGeospatial,
      MonitoringLocationIdentity,
      Organization,
      OrganizationDescription,
      WQX
    )

## Activity

Allows for the reporting of monitoring activities conducted at a Monitoring Location.

**Parameters:**

- `activityDescription` (ActivityDescription)
- `activityLocation` (ActivityLocation)
- `biologicalActivityDescription` (BiologicalActivityDescription)
- `sampleDescription` (SampleDescription)
- `activityMetric` (List of ActivityMetric)
- `attachedBinaryObject` (List of AttachedBinaryObject)
- `result` (List of Result)

## ActivityDescription

Basic identification information for an activity conducted within a project.

**Parameters:**

- `activityIdentifier` (ActivityIdentifier)
- `activityIdentifierUserSupplied` (ActivityIdentifierUserSupplied)
- `activityTypeCode` (ActivityTypeCode)
- `activityMediaName` (ActivityMediaName)
- `activityMediaSubdivisionName` (ActivityMediaSubdivisionName)
- `activityStartDate` (ActivityStartDate)
- `activityStartTime` (WQXTime)
- `activityEndDate` (ActivityEndDate)
- `activityEndTime` (WQXTime)
- `activityRelativeDepthName` (ActivityRelativeDepthName)
- `activityDepthHeightMeasure` (MeasureCompact)
- `activityTopDepthHeightMeasure` (MeasureCompact)
- `activityBottomDepthHeightMeasure` (MeasureCompact)
- `activityDepthAltitudeReferencePointText` (DepthAltitudeReferencePointText)
- `projectIdentifier` (ProjectIdentifier)
- `activityConductingOrganizationText` (List of ActivityConductingOrganizationText)
- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)
- `samplingComponentName` (SamplingComponentName)
- `activityCommentText` (CommentText)

## ActivityGroup

Allows for the grouping of activities.

**Parameters:**

- `activityGroupIdentifier` (ActivityGroupIdentifier)
- `activityGroupName` (ActivityGroupName)
- `activityGroupTypeCode` (ActivityGroupTypeCode)
- `activityIdentifier` (ActivityIdentifier)
- `replaceActivities` (bool)

## ActivityLocation

Geospatial description of monitoring site, if it is different from that described in the station description.

**Parameters:**

- `latitudeMeasure` (LatitudeMeasure)
- `longitudeMeasure` (LongitudeMeasure)
- `sourceMapScale` (SourceMapScale)
- `horizontalAccuracyMeasure` (MeasureCompact)
- `horizontalCollectionMethodName` (HorizontalCollectionMethodName)
- `horizontalCoordinateReferenceSystemDatumName` (HorizontalCoordinateReferenceSystemDatumName)
- `activityLocationDescriptionText` (ActivityLocationDescriptionText)

## ActivityMetric

This section allows for the reporting of metrics to support habitat or biotic integrity indices.

**Parameters:**

- `activityMetricType` (ActivityMetricType)
- `metricValueMeasure` (MeasureCompact)
- `metricScore` (MetricScore)
- `metricSamplingPointPlaceInSeries` (MetricSamplingPointPlaceInSeries)
- `metricCommentText` (CommentText)
- `indexIdentifier` (IndexIdentifier)

## ActivityMetricType

This section identifies the metric type reported as part of an activity metric.

**Parameters:**

- `metricTypeIdentifier` (MetricTypeIdentifier),
- `metricTypeIdentifierContext` (MetricTypeIdentifierContext),
- `metricTypeName` (MetricTypeName),
- `metricTypeCitation` (BibliographicReference),
- `metricTypeScaleText` (MetricTypeScaleText),
- `formulaDescriptionText` (FormulaDescriptionText)

## AlternateMonitoringLocationIdentity

Alternate identifications of a monitoring location.

**Parameters:**

- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)
- `monitoringLocationIdentifierContext` (MonitoringLocationIdentifierContext)

## AquiferInformation

Identifies the procedures, processes, and references required to determine the methods used to obtain a result.

**Parameters:**

- `localAquiferCode` (LocalAquiferCode)
- `localAquiferCodeContext` (LocalAquiferCodeContext)
- `localAquiferName` (LocalAquiferName)
- `localAquiferDescriptionText` (LocalAquiferDescriptionText)

## AttachedBinaryObject

Reference document, image, photo, GIS data layer, laboratory material or other electronic object attached within a data exchange, as well as information used to describe the object.

**Parameters:**

- `binaryObjectFileName` (BinaryObjectFileName)
- `binaryObjectFileTypeCode` (BinaryObjectFileTypeCode)

## BibliographicReference

The descriptors used to identify and catalog an object.

**Parameters:**

- `resourceTitleName` (ResourceTitleName)
- `resourceCreatorName` (ResourceCreatorName)
- `resourceSubjectText` (ResourceSubjectText)
- `resourcePublisherName` (ResourcePublisherName)
- `resourceDate` (ResourceDate)
- `resourceIdentifier` (ResourceIdentifier)

## BiologicalActivityDescription

Allows for the reporting of biological monitoring activities conducted at a Monitoring Location.

**Parameters:**

- `assemblageSampledName` (AssemblageSampledName)
- `biologicalHabitatCollectionInformation` (BiologicalHabitatCollectionInformation)
- `toxicityTestType` (ToxicityTestType)
- `habitatSelectionMethod` (HabitatSelectionMethod)

## BiologicalHabitatCollectionInformation

Allows for the reporting of biological habitat sample collection information.

**Parameters:**

- `collectionDuration` (MeasureCompact)
- `collectionArea` (MeasureCompact)
- `collectionEffort` (CollectionEffort)
- `reachLengthMeasure` (MeasureCompact)
- `reachWidthMeasure` (MeasureCompact)
- `collectionDescriptionText` (CollectionDescriptionText)
- `passCount` (PassCount)
- `netInformation` (NetInformation)

## BiologicalHabitatIndex

This section allows for the reporting of habitat and biotic integrity indices as a representation of water quality conditions.

**Parameters:**

- `indexIdentifier` (IndexIdentifier)
- `indexType` (IndexType)
- `indexScore` (IndexScore)
- `indexQualifierCode` (IndexQualifierCode)
- `indexCommentText` (CommentText)
- `indexCalculatedDate` (IndexCalculatedDate)
- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)

## BiologicalResultDescription

Allows for the reporting of biological result information.

**Parameters:**

- `biologicalIntentName` (BiologicalIntentName)
- `biologicalIndividualIdentifier` (BiologicalIndividualIdentifier)
- `subjectTaxonomicName` (SubjectTaxonomicName)
- `subjectTaxonomicNameUserSupplied` (SubjectTaxonomicNameUserSupplied)
- `subjectTaxonomicNameUserSuppliedReferenceText` (SubjectTaxonomicNameUserSuppliedReferenceText)
- `unidentifiedSpeciesIdentifier` (UnidentifiedSpeciesIdentifier)
- `sampleTissueAnatomyName` (SampleTissueAnatomyName)
- `groupSummaryCount` (GroupSummaryCount)
- `groupSummaryWeightMeasure` (MeasureCompact)
- `taxonomicDetails` (TaxonomicDetails)
- `frequencyClassInformation` (FrequencyClassInformation)

## CollectionEffort

The fields to describe the effort used a collection.

**Parameters:**

- `measureValue` (MeasureValue)
- `gearProcedureUnitCode` (GearProcedureUnitCode)

## ComparableAnalyticalMethod

Identifies the procedures, processes, and references required to determine the analytical methods used to obtain a result.

**Parameters:**

- `methodIdentifier` (MethodIdentifier)
- `methodIdentifierContext` (MethodIdentifierContext)
- `methodModificationText` (MethodModificationText)

## DataQualityIndicator

The quantitative statistics and qualitative descriptors that are used to interpret the degree of acceptability or utility of data to the user.

**Parameters:**

- `precisionValue` (PrecisionValue)
- `biasValue` (BiasValue)
- `confidenceIntervalValue` (ConfidenceIntervalValue)
- `upperConfidenceLimitValue` (UpperConfidenceLimitValue)
- `lowerConfidenceLimitValue` (LowerConfidenceLimitValue)

## DetectionQuantitationLimit

Information that describes one of a variety of detection or quantitation limits determined in a laboratory.

**Parameters:**

- `detectionQuantitationLimitTypeName` (DetectionQuantitationLimitTypeName)
- `detectionQuantitationLimitMeasure` (MeasureCompact)
- `detectionQuantitationLimitCommentText` (DetectionQuantitationLimitCommentText)

## ElectronicAddress

A location within a system of worldwide electronic communication where a computer user can access information or receive electronic mail.

**Parameters:**

- `electronicAddressText` (ElectronicAddressText)
- `electronicAddressTypeName` (ElectronicAddressTypeName)

## Entity_Update_Identifiers

Allows a Project Identifier to be changed.

**Parameters:**

- `oldIdentifier` (OldIdentifier)
- `newIdentifier` (NewIdentifier)

## FrequencyClassInformation

This section allows for the definition of a subgroup of biological communities by life stage, physical attribute, or abnormality to support frequency class studies.

**Parameters:**

- `frequencyClassDescriptorCode` (FrequencyClassDescriptorCode)
- `frequencyClassDescriptorUnitCode` (FrequencyClassDescriptorUnitCode)
- `lowerClassBoundValue` (LowerClassBoundValue)
- `upperClassBoundValue` (UpperClassBoundValue)

## HorizontalAccuracyMeasure

This file was not converted from XSD because it is does not define a complex type. It only creates an element called "HorizontalAccuracyMeasure" of type "MeasureCompact".

## IndexType

This section identifies the index type reported as part of a biological or habitat index.

**Parameters:**

- `indexTypeIdentifier` (IndexTypeIdentifier)
- `indexTypeIdentifierContext` (IndexTypeIdentifierContext)
- `indexTypeName` (IndexTypeName)
- `indexTypeCitation` (BibliographicReference)
- `indexTypeScaleText` (IndexTypeScaleText)

## LabSamplePreparation

Describes Lab Sample Preparation procedures which may alter the original state of the Sample and produce Lab subsamples.  These Lab Subsamples are analyized and reported by the Lab as Sample results.

**Parameters:**

- `labSamplePreparationMethod` (ReferenceMethod)
- `preparationStartDate` (PreparationStartDate)
- `preparationStartTime` (WQXTime)
- `preparationEndDate` (PreparationEndDate)
- `preparationEndTime` (WQXTime)
- `substanceDilutionFactor` (SubstanceDilutionFactor)

## Measure

Identifies the value, associated units of measure, and qualifier for measuring the observation or analytical result value.

**Parameters:**

- `resultMeasureValue` (ResultMeasureValue)
- `measureUnitCode` (MeasureUnitCode)
- `measureQualifierCode` (List[MeasureQualifierCode])

## MeasureCompact

Identifies only the value and the associated units of measure for measuring the observation or analytical result value.

**Parameters:**

- `measureValue` (MeasureValue)
- `measureUnitCode` (MeasureUnitCode)

## MonitoringLocation

An identifiable location where an environmental sample, onsite measurement, and/or observation is determined.

**Parameters:**

- `monitoringLocationIdentity` (MonitoringLocationIdentity)
- `monitoringLocationGeospatial` (MonitoringLocationGeospatial)
- `wellInformation` (WellInformation)
- `attachedBinaryObject` (List[AttachedBinaryObject])

## MonitoringLocationGeospatial

Monitoring location geographic location.

**Parameters:**

- `latitudeMeasure` (LatitudeMeasure)
- `longitudeMeasure` (LongitudeMeasure)
- `sourceMapScale` (SourceMapScale)
- `horizontalAccuracyMeasure` (MeasureCompact)
- `verticalAccuracyMeasure` (MeasureCompact)
- `horizontalCollectionMethodName` (HorizontalCollectionMethodName)
- `horizontalCoordinateReferenceSystemDatumName` (HorizontalCoordinateReferenceSystemDatumName)
- `verticalMeasure` (MeasureCompact)
- `verticalCollectionMethodName` (VerticalCollectionMethodName)
- `verticalCoordinateReferenceSystemDatumName` (VerticalCoordinateReferenceSystemDatumName)
- `countryCode` (CountryCode)
- `stateCode` (StateCode)
- `countyCode` (CountyCode)

## MonitoringLocationIdentity

Basic identification information for the location/site that is monitored or used for sampling.

**Parameters:**

- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)
- `monitoringLocationName` (MonitoringLocationName)
- `monitoringLocationTypeName` (MonitoringLocationTypeName)
- `monitoringLocationDescriptionText` (MonitoringLocationDescriptionText)
- `hucEightDigitCode` (HUCEightDigitCode)
- `hucTwelveDigitCode` (HUCTwelveDigitCode)
- `tribalLandIndicator` (TribalLandIndicator)
- `tribalLandName` (TribalLandName)
- `alternateMonitoringLocationIdentity` (List[AlternateMonitoringLocationIdentity])
- `drainageAreaMeasure` (MeasureCompact)
- `contributingDrainageAreaMeasure` (MeasureCompact)

## NetInformation

Allows for the reporting of net sample collection information.

**Parameters:**

- `netTypeName` (NetTypeName)
- `netSurfaceAreaMeasure` (MeasureCompact)
- `netMeshSizeMeasure` (MeasureCompact)
- `boatSpeedMeasure` (MeasureCompact)
- `currentSpeedMeasure` (MeasureCompact)

## Organization

Schema used to transfer organization information.

**Parameters:**

- `organizationDescription` (OrganizationDescription)
- `electronicAddress` (List[ElectronicAddress])
- `telephonic` (List[Telephonic])
- `organizationAddress` (List[OrganizationAddress])
- `project` (List[Project])
- `monitoringLocation` (List[MonitoringLocation])
- `biologicalHabitatIndex` (List[BiologicalHabitatIndex])
- `activity` (List[Activity])
- `activityGroup` (List[ActivityGroup])

## OrganizationAddress

The physical address of an organization.

**Parameters:**

- `addressTypeName` (AddressTypeName)
- `addressText` (AddressText)
- `supplementalAddressText` (SupplementalAddressText)
- `localityName` (LocalityName)
- `stateCode` (StateCode)
- `postalCode` (PostalCode)
- `countryCode` (CountryCode)
- `countyCode` (CountyCode)

## OrganizationDescription

The particular word(s) regularly connected with a unique framework of authority within which a person or persons act, or are designated to act, towards some purpose.

**Parameters:**

- `organizationIdentifier` (OrganizationIdentifier)
- `organizationFormalName` (OrganizationFormalName)
- `organizationDescriptionText` (OrganizationDescriptionText)
- `tribalCode` (TribalCode)

## Organization_Delete

Schema used to delete organization information.

**Parameters:**

- `organizationIdentifier` (OrganizationIdentifier)
- `projectIdentifier` (List[ProjectIdentifier])
- `monitoringLocationIdentifier` (List[MonitoringLocationIdentifier])
- `activityIdentifier` (List[ActivityIdentifier])
- `activityGroupIdentifier` (List[ActivityGroupIdentifier])
- `indexIdentifier` (List[IndexIdentifier])

## Project

An environmental data collection effort that has a stated purpose and puts a series of samples and results into a meaningful context.

**Parameters:**

- `projectIdentifier` (ProjectIdentifier)
- `projectName` (ProjectName)
- `projectDescriptionText` (ProjectDescriptionText)
- `samplingDesignTypeCode` (SamplingDesignTypeCode)
- `qAPPApprovedIndicator` (QAPPApprovedIndicator)
- `qAPPApprovalAgencyName` (QAPPApprovalAgencyName)
- `attachedBinaryObject` (List[AttachedBinaryObject])
- `projectMonitoringLocationWeighting` (List[ProjectMonitoringLocationWeighting])

## ProjectMonitoringLocationWeighting

Describes the probability weighting information for a given Project / Monitoring Location Assignment.

**Parameters:**

- `monitoringLocationIdentifier` (MonitoringLocationIdentifier)
- `locationWeightingFactorMeasure` (MeasureCompact)
- `statisticalStratumText` (StatisticalStratumText)
- `locationCategoryName` (LocationCategoryName)
- `locationStatusName` (LocationStatusName)
- `referenceLocationTypeCode` (ReferenceLocationTypeCode)
- `referenceLocationStartDate` (ReferenceLocationStartDate)
- `referenceLocationEndDate` (ReferenceLocationEndDate)
- `referenceLocationCitation` (BibliographicReference)
- `commentText` (CommentText)

## ReferenceMethod

Identifies the procedures, processes, and references required to determine the methods used to obtain a result.

**Parameters:**

- `methodIdentifier` (MethodIdentifier)
- `methodIdentifierContext` (MethodIdentifierContext)
- `methodName` (MethodName)
- `methodQualifierTypeName` (MethodQualifierTypeName)
- `methodDescriptionText` (MethodDescriptionText)

## Result

Describes the results of a field measurement, observation, or laboratory analysis.

**Parameters:**

- `resultDescription` (ResultDescription)
- `biologicalResultDescription` (BiologicalResultDescription)
- `attachedBinaryObject` (List[AttachedBinaryObject])
- `resultAnalyticalMethod` (ResultAnalyticalMethod)
- `comparableAnalyticalMethod` (ComparableAnalyticalMethod)
- `resultLabInformation` (ResultLabInformation)
- `labSamplePreparation` (List[LabSamplePreparation])

## ResultAnalyticalMethod

Identifies the procedures, processes, and references required to determine the analytical methods used to obtain a result.

**Parameters:**

- `methodIdentifier` (MethodIdentifier)
- `methodIdentifierContext` (MethodIdentifierContext)
- `methodName` (MethodName)
- `methodQualifierTypeName` (MethodQualifierTypeName)
- `methodDescriptionText` (MethodDescriptionText)

## ResultDescription

Describes the results of a field measurement, observation, or laboratory analysis.

**Parameters:**

- `dataLoggerLineName` (DataLoggerLineName)
- `resultDetectionConditionText` (ResultDetectionConditionText)
- `characteristicName` (CharacteristicName)
- `characteristicNameUserSupplied` (CharacteristicNameUserSupplied)
- `methodSpeciationName` (MethodSpeciationName)
- `resultSampleFractionText` (ResultSampleFractionText)
- `resultMeasure` (Measure)
- `targetCount` (TargetCount)
- `proportionSampleProcessedNumeric` (ProportionSampleProcessedNumeric)
- `resultStatusIdentifier` (ResultStatusIdentifier)
- `statisticalBaseCode` (StatisticalBaseCode)
- `statisticalNValueNumeric` (StatisticalNValueNumeric)
- `resultValueTypeName` (ResultValueTypeName)
- `resultWeightBasisText` (ResultWeightBasisText)
- `resultTimeBasisText` (ResultTimeBasisText)
- `resultTemperatureBasisText` (ResultTemperatureBasisText)
- `resultParticleSizeBasisText` (ResultParticleSizeBasisText)
- `dataQuality` (DataQuality)
- `resultCommentText` (CommentText)
- `resultDepthHeightMeasure` (MeasureCompact)
- `resultDepthAltitudeReferencePointText` (DepthAltitudeReferencePointText)
- `resultSamplingPointName` (ResultSamplingPointName)
- `resultSamplingPointType` (ResultSamplingPointType)
- `resultSamplingPointPlaceInSeries` (ResultSamplingPointPlaceInSeries)
- `resultSamplingPointCommentText` (ResultSamplingPointCommentText)
- `recordIdentifierUserSupplied` (RecordIdentifierUserSupplied)

## ResultLabInformation

Describes information obtained by a laboratory related to a specific laboratory analysis.

**Parameters:**

- `laboratoryName` (LaboratoryName)
- `analysisStartDate` (AnalysisStartDate)
- `analysisStartTime` (WQXTime)
- `analysisEndDate` (AnalysisEndDate)
- `analysisEndTime` (WQXTime)
- `laboratoryCommentText` (LaboratoryCommentText)
- `resultDetectionQuantitationLimit` (DetectionQuantitationLimit)
- `laboratorySampleSplitRatio` (LaboratorySampleSplitRatio)
- `laboratoryAccreditationIndicator` (LaboratoryAccreditationIndicator)
- `laboratoryAccreditationAuthorityName` (LaboratoryAccreditationAuthorityName)
- `taxonomistAccreditationIndicator` (TaxonomistAccreditationIndicator)
- `taxonomistAccreditationAuthorityName` (TaxonomistAccreditationAuthorityName)

## SampleDescription

Basic identification information for the sample collected as part of a monitoring activity.

**Parameters:**

- `sampleCollectionMethod` (ReferenceMethod)
- `sampleCollectionEquipmentName` (SampleCollectionEquipmentName)
- `sampleCollectionEquipmentCommentText` (SampleCollectionEquipmentCommentText)
- `samplePreparation` (SamplePreparation)
- `hydrologicCondition` (HydrologicCondition)
- `hydrologicEvent` (HydrologicEvent)

## SamplePreparation

Describes a sample preparation procedure which may be conducted on an initial Sample or on subsequent subsamples.

**Parameters:**

- `samplePreparationMethod` (ReferenceMethod)
- `sampleContainerLabelName` (SampleContainerLabelName)
- `sampleContainerTypeName` (SampleContainerTypeName)
- `sampleContainerColorName` (SampleContainerColorName)
- `chemicalPreservativeUsedName` (ChemicalPreservativeUsedName)
- `thermalPreservativeUsedName` (ThermalPreservativeUsedName)
- `sampleTransportStorageDescription` (SampleTransportStorageDescription)

## SimpleContent

There are several data types which are strings or other basic data types with rules added. `SimpleContent` is the name of an `XSD` file and also the name of the Python file which defines those same types. They do not need to be used directly in your code. Just use regular Python types and they will be converted when possible.

## TaxonomicDetails

This section allows for the further definition of user-defined details for taxa.

**Parameters:**

- `cellFormName` (CellFormName)
- `cellShapeName` (CellShapeName)
- `habitName` (HabitName)
- `voltinismName` (VoltinismName)
- `taxonomicPollutionTolerance` (TaxonomicPollutionTolerance)
- `taxonomicPollutionToleranceScaleText` (TaxonomicPollutionToleranceScaleText)
- `trophicLevelName` (TrophicLevelName)
- `functionalFeedingGroupName` (FunctionalFeedingGroupName)
- `taxonomicDetailsCitation` (BibliographicReference)

## Telephonic

An identification of a telephone connection.

**Parameters:**

- `telephoneNumberText` (TelephoneNumberText)
- `telephoneNumberTypeName` (TelephoneNumberTypeName)
- `telephoneExtensionNumberText` (TelephoneExtensionNumberText)

## WellInformation

Description of the attributes of a well.

**Parameters:**

- `wellTypeText` (WellTypeText)
- `aquiferTypeName` (AquiferTypeName)
- `nationalAquiferCode` (NationalAquiferCode)
- `aquiferInformation` (AquiferInformation)
- `formationTypeText` (FormationTypeText)
- `wellHoleDepthMeasure` (MeasureCompact)
- `constructionDate` (ConstructionDate)
- `wellDepthMeasure` (MeasureCompact)

## WQX

Main Schema used to transfer water monitoring results to EPA Office of Water.

**Parameters:**

- `organization` (Organization)

## WQXTime

Custom WQX datatype that defines a local time and corresponding time zone in which the time is measured.

**Parameters:**

- `time` (Time)
- `timeZoneCode` (TimeZoneCode)

## WQXDelete

Main Schema used to delete a portion of water monitoring results from EPA Office of Water system.

**Parameters:**

- `organizationDelete` (List[OrganizationDelete])

## WQXUpdateIdentifiers

Main Schema used to update identifiers for major entities (projects, monitoring locations, activity, activity groups, and indexes).

**Parameters:**

- `updateIdentifiers` (List[UpdateIdentifiers])
