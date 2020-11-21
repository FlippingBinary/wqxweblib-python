# Python library for WQX (wqxlib)

This is a simple Python library for interacting with the EPA's WQX data submission service. It aims to be mimick the [WQX Web API endpoints](https://www.epa.gov/sites/production/files/2018-09/documents/wqx_web_application_programming_interface_api.pdf) as much as possible, but is not yet fully implemented. If you find a bug, please submit a pull request on [Github](https://github.com/FlippingBinary/wqxlib) or open an issue there.

_NOTE: This module is useless without EPA credentials for WQX submission._

## Getting Started

Install this package using `pip`

    pip install wqxlib

## Data submission patterns

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

## Import Module

This module must be imported and instantiated with your `userID` and `privateKey` before any of the other functions can be used.

    from wqxlib import WQX
    wqx = WQX("my username", "my private key")

# API Reference

This following methods mirror what is shown in the EPA's documentation for the WQX Web API endpoints. Some differences exist for the sake of Python integration while still allowing the inputs indicated in the documentation.

## Upload

Upload a file to the web server (to be imported).

**Parameters:**

- `filename` (required string) - A name to give the file. This does not need to match any local filename. The allowed file extensions are:
- - txt
- - csv
- - xlsx
- - xls
- - xml
- - zip.

**Returns:** `fileId` - A unique identifier for the uploaded file.

**Example with generated data:**

    data="""
    column1,column2
    value1,value2"""

    fileID = wqx.Upload( filename="datafile.csv", content=data )

**Example using a file from the local filesystem:**

    with open( 'data.csv', 'rb' ) as f:
        fileID = wqx.Upload( filename="datafile.csv", content=f.read() )

## UploadAttachment

Upload an attachment to the web server (to be imported).

**Parameters:**

- `filename` (required string) - A name to give the file. This does not need to match any local filename. The only allowed file extension is:
- - zip.

**Returns:** `fileId` - A unique identifier for the uploaded file.

**Example using a file from the local filesystem:**

    with open( 'attachment.zip', 'rb' ) as f:
        fileID = wqx.Upload( filename="attach.zip", content=f.read() )

## StartImport

Start importing a file and attachment that was previously uploaded.

**Parameters:**

- `importConfigurationId` (required string) - The Import Configuration ID of an existing Import Configuration which should be applied to the import.
- `fileId` (required string) - The return value of `Upload`.
- `attachmentFileId` (optional string) - The return value of `UploadAttachment`.
- `fileType` (required enum or string) - The type of file you uploaded with `Upload`. This must be one of the following enum members provided by the `WQX` module or their corresponding strings:
- - `CSV`
- - `TAB`
- - `TILDE`
- - `PIPE`
- - `XLS`
- - `XLSX`
- `newOrExistingData` (required enum or integer) - Declare whether the contents of your upload represents new data or replaces existing data. This must be one of the following enum members provided by the `WQX` module or their corresponding integers:
- - `CONTAINS_NEW_OR_EXISTING` (0) - file may contain new and/or existing data.
- - `CONTAINS_NEW_ONLY` (1) - file contains new data only.
- - `CONTAINS_EXISTING_ONLY` (2) - file contains existing data only (to be replaced).
- `uponCompletion` (required enum or integer) - Declare what to do after the upload finishes. This must be one of the following enum members provided by the `WQX` module or their corresponding integers:
- - `DO_NOTHING` (0) - do nothing.
- - `AUTO_EXPORT` (1) - start export.
- - `AUTO_SUBMIT` (2) - start export and submit to CDX.
- `uponCompletionCondition` (optionally required enum or integer) - Declare what conditions permit auto export or auto submit. This must be one of the following enum members provided by the `WQX` module or their corresponding integers:
- - `NOT_APPLICABLE` (0) - not applicable (`uponCompletion` is `DO_NOTHING` or not provided).
- - `EXPORT_IF_NO_ERROR` (1) - start export only if no import errors.
- - `EXPORT_IF_NO_WARNING` (2) - start export only if no import errors and no warnings.
- - `EXPORT_ALWAYS` (3) - start export even when there are import errors.
- `worksheetsToImport` (optional string) - If provided, this must be a comma delimited list of values (1-based), e.g. "`1,3`". This parameter value will be ignored when the fileType is not `XLS` or `XLSX`. If no value is passed in (and it's applicable) then we'll use the value from the Import Configuration.
- `ignoreFirstRowOfFile` (optional boolean) - Ignore the first row of the data file if this parameter is true. This parameter value will be ignored for Expert Mode Import Configurations.
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

    datasetId = wqx.StartImport( importConfigurationID, fileId, wqx.CONTAINS_NEW_OR_EXISTING, wqx.DO_NOTHING, ignoreFirstRowOfFile=True )

**Example with auto export and without auto submit:**

    datasetId = wqx.StartImport( importConfigurationID, fileId, wqx.CONTAINS_NEW_OR_EXISTING, wqx.AUTO_EXPORT, ignoreFirstRowOfFile=True )

**Example with auto submit:**

    datasetId = wqx.StartImport( importConfigurationID, fileId, wqx.CONTAINS_NEW_OR_EXISTING, wqx.AUTO_SUBMIT, ignoreFirstRowOfFile=True )

## StartXmlExport

Start created the XML submission file (for CDX).

**Parameters:**

- `datasetId` (required string) - The return value of `StartImport` or `SubmitFileToCdx`.
- `uponCompletion` (required enum or integer) - Declare what to do after the export finishes. This must be one of the following enum members provided by the `WQX` module or their corresponding integers:
- - `DO_NOT_SUBMIT` (0) - do nothing.
- - `SUBMIT_EXPORT` (1) - submit to CDX.

**Returns:** `status` - The initial status for the dataset.

**Example using enum:**

    status = wqx.StartXmlExport( datasetId, wqx.SUBMIT_EXPORT )

**Example using integer:**

    status = wqx.StartXmlExport( datasetId, 1 )

## SubmitDatasetToCdx

Submit a dataset to CDX.

**Parameters:**

- `datasetId` (required string) - The return value of `StartImport` or `SubmitFileToCdx`.

**Returns:** `status` - The initial status for the dataset.

**Example:**

    status = wqx.SubmitDatasetToCdx( datasetId )

## SubmitFileToCdx

Submit a previously uploaded WQX XML file to CDX.

**Parameters:**

- `fileId` (required string) - The return value of `Upload`.

**Returns:** `datasetId` - The new dataset ID.

**Example:**

    datasetId = wqx.SubmitFileToCdx( fileId )

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

    statusMsg = wqx.GetStatus( datasetId )

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

    urls = wqx.GetDocumentList( datasetId )
    for url in urls:
        print( url )

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

    projects = wqx.Projects( organizationIdentifiersCsv )
    for project in projects:
        print( project )

## MonitoringLocations

Get the locations for an organization.

**Parameters:**

- `organizationIdentifiersCsv` (required string) - Comma delimited list of organization identifiers (e.g. "id1,id2,id3") NOTE: No spaces.
- `monitoringLocationIdentifiersCsv` (optional string) - Comma delimited list of monitoring location identifiers (e.g. "id1,id2,id3") NOTE: No spaces.
- `monitoringLocationName` (optional string) - Monitoring Location Name. Wildcards are supported (e.g. "Location%" means anything starting with "Location").
- `monitoringLocationType` (optional string) - Monitoring Location Type. Wildcards are supported (e.g. "Location%" means anything starting with "Location"). Allowed values:
- - Atmosphere
- - BEACH Program Site-Channelized stream
- - BEACH Program Site-Estuary
- - BEACH Program Site-Great Lake
- - BEACH Program Site-Lake
- - BEACH Program Site-Land
- - BEACH Program Site-Land runoff
- - BEACH Program Site-Ocean
- - BEACH Program Site-River/Stream
- - BEACH Program Site-Storm sewer
- - BEACH Program Site-Waste sewer
- - Borehole
- - Canal Drainage
- - Canal Irrigation
- - Canal Transport
- - Cave
- - CERCLA Superfund Site
- - Channelized Stream
- - Combined Sewer
- - Constructed Diversion Dam
- - Constructed Tunnel
- - Constructed Water Transport Structure
- - Constructed Wetland
- - Estuary
- - Facility Industrial
- - Facility Municipal Sewage (POTW)
- - Facility Other
- - Facility Privately Owned Non-industrial
- - Facility Public Water Supply (PWS)
- - Floodwater non-Urban
- - Floodwater Urban
- - Gallery
- - Gas-Condensate
- - Gas-Engine
- - Gas-Extraction
- - Gas-Flare
- - Gas-Monitoring Probe
- - Gas-Passive Vent
- - Gas-Subslab
- - Gas-Temporary
- - Great Lake
- - Lake
- - Land
- - Land Flood Plain
- - Land Runoff
- - Landfill
- - Leachate-Extraction
- - Leachate-Head Well
- - Leachate-Lysimeter
- - Leachate-SamplePoint
- - Local Air Monitoring Station
- - Mine Pit
- - Mine/Mine Discharge
- - Mine/Mine Discharge Adit (Mine Entrance)
- - Mine/Mine Discharge Tailings Pile
- - Mine/Mine Discharge Waste Rock Pile
- - National Air Monitoring Station
- - Ocean
- - Oil and Gas Well
- - Other-Ground Water
- - Other-Surface Water
- - Pipe, Unspecified Source
- - Playa
- - Pond-Anchialine
- - Pond-Sediment
- - Pond-Stock
- - Pond-Stormwater
- - Pond-Wastewater
- - Reservoir
- - River/Stream
- - River/stream Effluent-Dominated
- - River/Stream Ephemeral
- - River/Stream Intermittent
- - River/Stream Perennial
- - Riverine Impoundment
- - Seep
- - Spigot / Faucet
- - Spring
- - State/Local Air Monitoring Station
- - Storm Sewer
- - Survey Monument
- - Test Pit
- - Waste Pit
- - Waste Sewer
- - Well
- - Wetland Estuarine-Emergent
- - Wetland Estuarine-Forested
- - Wetland Estuarine-Scrub-Shrub
- - Wetland Lacustrine-Emergent
- - Wetland Palustrine Pond
- - Wetland Palustrine-Emergent
- - Wetland Palustrine-Forested
- - Wetland Palustrine-Moss-Lichen
- - Wetland Palustrine-Shrub-Scrub
- - Wetland Riverine-Emergent
- - Wetland Undifferentiated
- `transactionIdentifier` (optional string) - Transaction identifier e.g. "_23090c89-c6a6-4dd1-b16f-73f8ac36fac1".
- `lastChangeDateMin` (optional date) - Minimum last change date.
- `lastChangeDateMax` (optional date) - Maximum last change date.
- `startRow` (conditionally optional integer) - Zero based start row. Conditionally required if `rowsToRetrieve` is supplied.
- `rowsToRetrieve` (conditionally optional integer) - Number of rows to retrieve. Conditionally required if `startRow` is supplied.

**Returns:** `locations` - WQX Schema 2.2 element values including the transaction id for the monitoring location.

**Example:**

    locations = wqx.MonitoringLocations( organizationIdentifiersCsv )
    for location in locations:
        print( location )

