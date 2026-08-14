---
source: "https://experienceleague.adobe.com/en/docs/workfront-fusion/using/references/apps-and-their-modules/adobe-connectors/adobe-photoshop-modules"
title: "Adobe Photoshop modules for Workfront Fusion"
author: "Adobe Help Center"
date_published: "2026-08-05"
date_clipped: "2026-08-14"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Adobe Photoshop modules for Workfront Fusion

Source: https://experienceleague.adobe.com/en/docs/workfront-fusion/using/references/apps-and-their-modules/adobe-connectors/adobe-photoshop-modules

Documentation Adobe Workfront Fusion
Adobe Photoshop modules
Last update: August 5, 2026
Topics:
Workfront Fusion
Digital Content and Documents
In an Adobe Workfront Fusion scenario, you can automate workflows that use Adobe Photoshop, as well as connect it to multiple third-party applications and services.
If you need instructions on creating a scenario, see the articles under Create a scenario: article index .
For information about modules, see the articles under Modules: article index .
IMPORTANT
Adobe Photoshop has deprecated some elements of its API, which Fusion uses to perform actions in Photoshop.
Therefore, some of the existing Photoshop modules will not work after July 30, 2026.
We recommend updating any scenarios that use these modules to the updated modules as soon as possible.
For a list of affected modules, see Adobe Photoshop API deprecation updates .
For an explanation of how API changes affect Workfront Fusion, see Overview of APIs in Fusion .
Access requirements
Expand to view access requirements for the functionality in this article.
table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto html-authored no-header
Adobe Workfront package
Any Adobe Workfront Workflow package and any Adobe Workfront Automation and Integration package
Workfront Ultimate
Workfront Prime and Select packages, with an additional purchase of Workfront Fusion.
Adobe Workfront licenses
Standard
Work or higher
Adobe Workfront Fusion license
Operation-based: Available to organizations with operation-based licenses
Connector-based (legacy): Workfront Fusion for Work Automation and Integration
Product
If your organization has a Select or Prime Workfront package that does not include Workfront Automation and Integration, your organization must purchase Adobe Workfront Fusion.
For more detail about the information in this table, see Access requirements in documentation .
For information on Adobe Workfront Fusion licenses, see Adobe Workfront Fusion licenses .
Prerequisites
Before you can use the Adobe Photoshop connector, you must ensure that the following prerequisites are met:
You must have an active Adobe Photoshop account.
You must have a Firefly Services license.
You must have a Client ID and Client Secret. You can acquire these from the Adobe Developer Console.
Adobe Photoshop API deprecation updates
Adobe Photoshop has deprecated some elements of its API, which Fusion uses to perform actions in Photoshop.
Therefore, some of the existing Photoshop modules will not work after July 30, 2026.
This table documents which modules have been affected by this deprecation, and which module you should update to.
Deprecated legacy module
Update to new module
Apply PSD edits
Create or edit a composite
Convert image format
Create or edit a composite
Create a composite
Create or edit a composite
Create a new PSD
Create or edit a composite
Create renditions
Create or edit a composite
Edit text layers
Execute Photoshop actions, scripts, and transformations
Edit text layers 2
Execute Photoshop actions, scripts, and transformations
Execute an action JSON
Execute Photoshop actions, scripts, and transformations
Execute depth blur
(Not available)
Execute Photoshop actions
Execute Photoshop actions, scripts, and transformations
Execute product crop
Execute Photoshop actions, scripts, and transformations
Get layer info
Generate a manifest
Resize an image
Create or edit a composite
Replace Smart Object
Create or edit a composite
Replace Smart Object 2
Create or edit a composite
Rotate an image
Execute Photoshop actions, scripts, and transformations
Watermark an image
Create or edit a composite
Adobe Photoshop API information
The Adobe Photoshop connector uses the following:
Base URL
https://image.adobe.io/pie/psdService
API tag
v1.12.31
Create a connection to Adobe Photoshop
To create a connection for your Adobe Photoshop modules:
In any module, click Add next to the Connection box.
Fill in the following fields:
table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 layout-auto html-authored no-header
Connection type
Select whether you want to use a JWT connection or a server-to-server connection.
Connection name
Enter a name for this connection.
Client ID
Enter your Adobe Client ID. This can be found in the Credentials details section of the Adobe Developer Console
Client Secret
Enter your Adobe Client Secret. This can be found in the Credentials details section of the Adobe Developer Console
Technical account ID
If you are using a JWT connection, enter your Adobe Technical account ID. This can be found in the Credentials details section of the Adobe Developer Console
Organization ID
If you are using a JWT connection, enter your Adobe Organization ID. This can be found in the Credentials details section of the Adobe Developer Console
Private key
If you are using a JWT connection, enter the private key that was generated when your credentials were created in the Adobe Developer Console.
To extract your private key or certificate:
Click Extract .
Select the type of file you are extracting.
Select the file that contains the private key or certificate.
Enter the password for the file.
Click Save to extract the file and return to the connection setup.
Click Continue to save the connection and return to the module.
Adobe Photoshop modules and their fields
When you configure Adobe Photoshop modules, Workfront Fusion displays the fields listed below. Along with these, additional Adobe Photoshop fields might display, depending on factors such as your access level in the app or service. A bolded title in a module indicates a required field.
If you see the map button above a field or function, you can use it to set variables and functions for that field. For more information, see Map information from one module to another .
Actions
Convert HEX to RGB
Create an artboard
Create or edit a composite
Edit an image with various adjustments
Execute Photoshop actions, scripts, and transformations
Generate a manifest
Remove background
Convert HEX to RGB
This module converts a HEX color code to RGB color.
This module makes Lightroom-style adjustments to an image.
HEX
Enter or map the HEX code that you want to convert to RGB.
Create an artboard
This module creates a new artboard in Photoshop.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Images
For each image that you want to add to this artboard, click Add item and enter the image's source type and location.
Artboard spacing
Enter or map the spacing, in pixels, that you want to have between each artboard.
Outputs
For each converted file you want to create, click Add item and enter the storage, location, and other options as listed.
Create or edit a composite
This module creates or edits a composite in Photoshop.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Images
For each image that you want to add to this artboard, click Add item and enter the image's source type and location.
Width
If you are creating an image, enter the image width in pixels.
Height
If you are creating an image, enter the image height in pixels.
Mode
Select the color mode for this image.
Fill
Select the type of fill for the background layer.
Name
Enter or map a name for the new image.
Pixel scale factor
Enter or map the pixel scale factor. This must be a number between 0.1 and 1.
Resolution
In the Value field, enter the value of the resolution in density units (pixels per inch). The default value is 72.
Profile Type
If you want to override the default color profile, select a profile type and enter details as listed.
Crop > Top / Left / Bottom / Right
Enter the bounds that you want to crop the image to.
Hide
Select yes to hide pixels outside of crop bounds. IF set to false, pixels outside of crop bounds are deleted. The default is false.
Resize > Width
Select the unit that you want to use for the width, then select the value that represents the width that you want.
Resize > Height
Select the unit that you want to use for the height, then select the value that represents the height that you want.
Resolution
Select the unit that you want to use for the resolution, then select the value that represents the resolution that you want.
Resample
Select the resampling method to use when resizing.
Constrain proportions
Select Yes to maintain the aspect ratio between width and height. Select No to allow independent adjustment of width and height.
Rasterize
Select whether you want to rasterize the image.
Scale styles
Select whether you want to apply scaling to styles when you resize the image.
Trim upon
Select whether you want to trim upon transparent pixels.
Layers
For each later you want to add, click Add item and enter layer details.
For details, see Create or edit a composite in the Adobe documentation.
Default font PostScript name
Enter or map the PostScript name of the default font that you want to use.
Missing font strategy
Select whether you want the creation or edit to fail or to use the default font if a font is not available.
Additional fonts
For each font that you want to add, click Add item and enter the font's source URL.
Outputs
For each edited file you want to create, click Add item and enter the output details.
For details see Create or edit a composite in the Adobe documentation.
Maximum number of results
Enter or map the maximum number of results that you want the module to work with during one execution cycle.
Edit an image with various adjustments
This module makes Lightroom-style adjustments to an image.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Images
Enter or map the image's source type and location.
Other fields
For details see Edit an image with various adjustments in the Adobe documentation.
Execute Photoshop actions, scripts, and transformations
This module executes actions, scripts, and transformations available in the Firefly Photoshop API.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Images
Enter or map the image's source type and location.
Actions
For each action that you want to add, click Add item and enter the action's source, URL, and name.
UXP source
If you are using a UXP script, select whether you are providing a URL or inline content, then enter or map the URL or content.
Additional contents
Add up to 25 files referenced from the action or UXP.
Outputs
For each edited file you want to create, click Add item and enter the format, destination, and output pattern.
Maximum number of results
Enter or map the maximum number of results that you want the module to work with during one execution cycle.
Generate a manifest
This module generates a PSD manifest for the given input image.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Source
Enter or map the image's source type and location.
Outputs
For each edited file you want to create, click Add item and enter the destination details.
Include layer thumbnails
Select Yes if you want to module to generate a thumbnail rendition for each layer in the manifest.
Maximum thumbnail depth
Enter or map the maximum depth for thumbnail renditions. For no maximum depth, enter 0 .
Layer thumbnail format
Select whether you want the thumbnails to be in JPEG or PNG format.
Extract Smart Object data
Select whether to extract embedded smart objects and include a presigned URL in the manifest.
Trim to transparency
Select whether to trim each layer thumbnail to remove transparent pixels.
Maximum number of results
Enter or map the maximum number of results that you want the module to work with during one execution cycle.
Remove background
This action module identifies the main subject of your image and removes the background.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Input) Storage
Select the file service where the file you want to remove the background from is stored.
(Input) File location
Enter or map the URL or path of the file that you want to remove the background from.
(Output) Storage
Select the file service where the you want the new file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Output) File location
Enter or map the URL or path of where the new file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
Overwrite
Select whether the newly edited file will overwrite any output file that already exists. This applies only to files in Adobe storage.
Color space
Select whether the output image uses RGB or RGBA color.
Mask format
Select whether the edges of the image should be soft (feathered) or binary.
Optimize
Select Performance to optimize for speed, or Batch to allow wait time.
Post process
Select whether to enable post processing.
Version
Default is 4.0
Legacy
Apply PSD edits (Legacy)
Auto color correct an image (Legacy)
Convert image format (Legacy)
Create a mask (Legacy)
Create a new PSD (Legacy)
Create renditions (Legacy)
Edit text layers (Legacy)
Edit text layers 2 (Legacy)
Execute an action JSON (Legacy)
Execute Depth Blur (Legacy)
Execute Photoshop actions (Legacy)
Execute Product Crop (Legacy)
Get layer info (Legacy)
Make a custom API call (Legacy)
Remove background (Legacy)
Replace a Smart Object (Legacy)
Replace a Smart Object 2 (Legacy)
Resize an image (Legacy)
Watermark an image (Legacy)
Apply PSD edits (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Create or edit a composite module.
This action module applies a variety of document and layer level edits.
This module supports large files. For more information on large files, see Working with large files .
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Input) Storage
Select the file service where the file you want to edit is stored.
(Input) File location
Enter or map the URL or path of the file that you want to edit.
(Options > Document > Image size) Height
Enter or map the height of the image in pixels.
(Options > Document > Image size) Width
Enter or map the width of the image in pixels.
(Options > Document > Canvas size) Top
Enter or map, in pixels, the y coordinate of the document's upper-left corner.
(Options > Document > Canvas size) Bottom
Enter or map, in pixels, the y coordinate of the document's lower-right corner.
(Options > Document > Canvas size) Left
Enter or map, in pixels, the x coordinate of the document's upper-left corner.
(Options > Document > Canvas size) Right
Enter or map, in pixels, the x coordinate of the document's lower-right corner.
(Options > Document) Trim
Select Transparent pixels to base the trim on transparent pixels in the image.
(Options) Default font
Enter the full postscript name of the font to be used as the global default for the document. This font will be used for any text layer which has a missing font and no other font has been specifically provided for that layer. If this font is missing, the option specified in Manage missing fonts will take effect.
(Options) Fonts
For each font that the document needs, click Add item and enter the font's storage location and file location.
(Options) Manage missing fonts
Select the action to take if there are one or more missing fonts in the document.
fail : The job will not succeed and the status will be set to failed, with the details of the error provided in the details section in the status.
useDefault : The job will succeed, and all the missing fonts will be replaced with ArialMT.
(Options) Layers
For each layer you want to add, click Add item and and fill in the layer details.
For details about layer options, see Apply PSD Edits in the Adobe Photoshop documentation.
Outputs
For each edited file you want to create, click Add item and enter the storage, location, and type as listed.
(Output) Storage
Select the file service where the you want the new file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Output) File location
Enter or map the URL or path of where the new file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Output) Type
Select the file type that you want to convert the file to.
(Output) Overwrite
Select whether the newly edited file will overwrite any output file that already exists. This applies only to files in Adobe storage.
(Output) Trim to Canvas
Select whether the renditions must be of Canvas size. True trims the renditions to Canvas size, while False makes the renditions layer Size
Auto color correct an image (Legacy)
This action module auto color corrects the specified image.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Input) Storage
Select the file service where the file you want to color correct is stored.
(Input) File location
Enter or map the URL or path of the file that you want to color correct.
(Output) Storage
Select the file service where the you want the new file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Output) File location
Enter or map the URL or path of where the new file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Output) Type
Select the file type that you want to convert the file to.
(Output) Overwrite
Select whether the newly edited file will overwrite any output file that already exists. This applies only to files in Adobe storage.
Convert image format (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Create or edit a composite module.
This action module converts a file to JPEG, PNG, PSD or TIFF.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Input) Storage
Select the file service where the file you want to remove the background from is stored.
(Input) File location
Enter or map the URL or path of the file that you want to remove the background from.
Outputs
For each converted file you want to create, click Add item and enter the storage, location, and type as listed.
(Output) Storage
Select the file service where the you want the new file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Output) File location
Enter or map the URL or path of where the new file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Output) Type
Select the file type that you want to convert the file to.
(Output) Overwrite
Select whether the newly edited file will overwrite any output file that already exists. This applies only to files in Adobe storage.
Create a mask (Legacy)
This action module returns a PNG file with a mask applied around the subject.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Input) Storage
Select the file service where the file you want to create a mask from is stored.
(Input) File location
Enter or map the URL or path of the file that you want to create a mask from.
(Output) Storage
Select the file service where the you want the mask file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Output) File location
Enter or map the URL or path of where the mask file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
Overwrite
Select whether the newly edited file will overwrite any output file that already exists. This applies only to files in Adobe storage.
Color space
Select whether the output image uses RGB or RGBA color.
Mask format
Select whether the mask should be soft (feathered) or binary.
Optimize
Select Performance to optimize for speed, or Batch to allow wait time.
Post process
Select whether to enable post processing.
Version
Default is 4.0
Create a new PSD (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Create or edit a composite module.
This action module creates a new PSD with optional layers, and generates renditions or saves as a PSD.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Options > Document > Image size) Height
Enter or map the height of the image in pixels.
(Options > Document > Image size) Width
Enter or map the width of the image in pixels.
(Options > Document) Resolution
Enter or map, in pixels per inch, the resolution for the image. This must be between 72 and 300.
(Options > Document) Mode
Select the mode for the image.
(Options > Document) Fill
Select whether you want the fill for the background layer to be transparent, white, or the background color of the image.
(Options > Document) Depth
Select the bit depth of the image.
(Options) Layers
For each layer you want to add, click Add item and and fill in the layer details.
For details about layer options, see Create PSD in the Adobe Photoshop documentation.
(Options) Global font
Enter the full postscript name of the font to be used as the global default for the document. This font will be used for any text layer which has a missing font and no other font has been specifically provided for that layer. If this font is missing, the option specified in Manage missing fonts will take effect.
(Options) Fonts
For each font that the document needs, click Add item and enter the font's storage location and file location.
(Options) Manage missing fonts
Select the action to take if there are one or more missing fonts in the document.
fail : The job will not succeed and the status will be set to failed, with the details of the error provided in the details section in the status.
useDefault : The job will succeed, and all the missing fonts will be replaced with ArialMT.
Outputs
For each file you want to create, click Add item and enter the storage, location, and type as listed.
(Output) Storage
Select the file service where the you want the new file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Output) File location
Enter or map the URL or path of where the new file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Output) Type
Select the file type that you want to convert the file to.
(Output) Other fields
For details about output options, see Create PSD in the Adobe Photoshop documentation.
Create renditions (Legacy)
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Input) Storage
Select the file service where the file you want to edit is stored.
(Input) File location
Enter or map the URL or path of the file that you want to edit.
Outputs
For each file you want to create, click Add item and enter the storage, location, type, and overwrite option as listed.
(Outputs) Storage
Select the file service where the you want the edited file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Outputs) File location
Enter or map the URL or path of where the edited file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Outputs) Type
Select the file type for the edited file.
(Outputs) Overwrite
Select whether the newly edited file will overwrite any output file that already exists.
Edit text layers (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Execute Photoshop actions, scripts, and transformations module.
This action module edits text layers on a Photoshop file. You can enter separate edit details for multiple layers in the same file.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Input file storage
Select the file service where the file you want to edit is stored.
Input file URL
Enter or map the URL or path of the file that you want to edit.
Manage missing fonts
Select the action to take if there are one or more missing fonts in the document. If the font is not provided, the module uses the default font.
Default font
Enter the full postscript name of the font to be used as the global default for the document. This font will be used for any text layer which has a missing font and no other font has been specifically provided for that layer. If this font is missing, the option specified in Manage missing fonts will take effect.
(Options) Fonts
Enter the font's storage location and file location.
Layers
For each text layer that you want to edit, click Add item and enter the layer options.
For details about layer options, see Edit text in the Adobe Photoshop documentation.
(Output) Storage
Select the file service where the you want the edited file to be stored.
(Output) File location
Enter or map the URL or path of where the edited file will be stored.
(Output) Type
Select the file type for the edited file.
(Output) Overwrite
Select whether the newly edited file will overwrite any output file that already exists.
Edit text layers 2 (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Execute Photoshop actions, scripts, and transformations module.
This action module edits a text layer on a Photoshop file.
To edit multiple layers, use the Edit text layers module.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Input file storage
Select the file service where the file you want to edit is stored.
Input file URL
Enter or map the URL or path of the file that you want to edit.
Manage missing fonts
Select the action to take if there are one or more missing fonts in the document. If the font is not provided, the module uses the default font.
Default font
Enter the full postscript name of the font to be used as the global default for the document. This font will be used for any text layer which has a missing font and no other font has been specifically provided for that layer. If this font is missing, the option specified in Manage missing fonts will take effect.
(Options) Fonts
Enter the font's storage location and file location.
Layers
For details about layer options, see Edit text layer in the Adobe Photoshop documentation.
Output file storage
Select the file service where the you want the edited file to be stored.
(Output) Storage
Select the file service where the you want the edited file to be stored.
(Output) File location
Enter or map the URL or path of where the edited file will be stored.
(Output) Type
Select the file type for the edited file.
(Output) Overwrite
Select whether the newly edited file will overwrite any output file that already exists.
Execute an action JSON (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Execute Photoshop actions, scripts, and transformations module.
This action module executes Photoshop actions using JSON commands.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Input) Storage
Select the file service where the file you want to edit is stored.
(Input) File location
Enter or map the URL or path of the file that you want to edit.
Action JSON
Enter the JSON command for the action you want to take.
Fonts / Patterns / Brushes / Additional images
For each font, pattern, brush, or additional image that you want to use in this action, click Add item and enter the item's storage and file location.
Font / Pattern / Brush file URL
Enter or map the URL or path of the file that you want to use.
Outputs
For each file you want to create, click Add item and enter the storage, location, type, and overwrite option as listed.
(Outputs) Storage
Select the file service where the you want the edited file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Outputs) File URL
Enter or map the URL or path of where the edited file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Outputs) Type
Select the file type for the edited file.
(Outputs) Overwrite
Select whether the newly edited file will overwrite any output file that already exists.
Execute Depth Blur (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
This action module executes Depth Blur on the selected file.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Input file storage
Select the file service where the file you want to edit is stored.
Input file URL
Enter or map the URL or path of the file that you want to edit.
(Outputs) Storage
Select the file service where the you want the edited file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Outputs) File URL
Enter or map the URL or path of where the edited file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Outputs) Type
Select the file type for the edited file.
(Outputs) Overwrite
Select whether the newly edited file will overwrite any output file that already exists.
Other fields
For details about other Depth Blur options, see Execute Depth Blur in the Adobe Photoshop API documentation.
Execute Photoshop Actions (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Execute Photoshop actions, scripts, and transformations module.
This action module executes a Photoshop action on the selected image.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Input file storage
Select the file service where the file you want to edit is stored.
Input file URL
Enter or map the URL or path of the file that you want to edit.
Actions file storage
Select the file service where actions file is stored.
Actions file URL
Enter or map the URL or path of the actions file.
Action name
If you only want to execute a particular action, you may specify which action to play from the ActionSet.
Font / Pattern / Brush storage
Select the file service where the file you want to use is stored.
Font / Pattern / Brush file URL
Enter or map the URL or path of the file that you want to use.
(Outputs) Storage
Select the file service where the you want the edited file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Outputs) File URL
Enter or map the URL or path of where the edited file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Outputs) Type
Select the file type for the edited file.
(Outputs) Overwrite
Select whether the newly edited file will overwrite any output file that already exists.
Other fields
For details about other Depth Blur options, see Execute Depth Blur in the Adobe Photoshop API documentation.
Execute Product Crop (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Execute Photoshop actions, scripts, and transformations module.
This action module executes Product Crop on the selected image.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Input file storage
Select the file service where the file you want to crop is stored.
Input file URL
Enter or map the URL or path of the file that you want to crop.
Unit
Select whether you want to describe the height and width adjustment in pixels or as a percent.
Width
Enter or map amount of width padding you want to add.
Height
Enter or map amount of height padding you want to add.
(Outputs) Storage
Select the file service where the you want the edited file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Outputs) File URL
Enter or map the URL or path of where the edited file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Outputs) Type
Select the file type for the edited file.
(Outputs) Overwrite
Select whether the newly edited file will overwrite any output file that already exists.
Other fields
For details about other Depth Blur options, see Execute Depth Blur in the Adobe Photoshop API documentation.
Get layer info (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Generate a manifest module.
This action module retrieves layer information from the specified PSD file.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Input file storage
Select the file service where the file you want to retrieve layer information from is stored.
Input file URL
Enter or map the URL or path of the file that you want to retrieve layer information from.
Thumbnails
Select the type of file that you want the thumbnails to be. Thumbnails are small previews for any renderable layer.
Make a custom API call
This action module makes a custom call to the Photoshop API.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
URL
Enter a path relative to https://image.adobe.io/pie/psdService . Example: /photoshopActions
Method
Select the HTTP request method you need to configure the API call. For more information, see HTTP request methods .
Headers
Add the headers of the request in the form of a standard JSON object.
For example, {"Content-type":"application/json"}
Workfront Fusion adds authorization headers automatically.
Query String
Enter the request query string.
Body
Add the body content for the API call in the form of a standard JSON object.
Note:
When using conditional statements such as if in your JSON, put the quotation marks outside of the conditional statement.
Replace a smart object (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Create or edit a composite module.
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Create or edit a composite module.
This action module replaces a Smart Object within a PSD layer, and generates new renditions.
This module uses Smart Object API version 2.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Input) Storage
Select the file service where the Smart Object is stored.
(Input) File location
Enter or map the URL or path of the Smart Object.
Layers
For each layer you want to add to the Smart Object, click Add item and Enter the object's name or ID, the file service where the Smart Object is stored, and the the URL or path of the layer.
For descriptions of the advanced settings in this area, see Replace a Smart Object in the Photoshop API documentation
Resize image during place
Select whether you want to resize the image.
Outputs
For each new rendition you want the module to produce, click Add item and fill in the following fields. You can have a maximum of 25 output files.
(Output) Storage
Select the file service where the you want the new file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Output) File location
Enter or map the URL or path of where the new file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Outputs) Type
Select the file type for the edited file.
Replace a smart object 2 (Legacy)
This action module replaces a Smart Object within a PSD layer, and generates new renditions.
This module uses the legacy version of Smart Objects.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Input) Storage
Select the file service where the Smart Object is stored.
(Input) File location
Enter or map the URL or path of the Smart Object.
Layers
For each layer you want to add to the Smart Object, click Add item and Enter the object's name or ID, the file service where the Smart Object is stored, and the the URL or path of the layer.
For descriptions of the advanced settings in this area, see Replace a Smart Object in the Photoshop API documentation
Outputs
For each new rendition you want the module to produce, click Add item and fill in the following fields. You can have a maximum of 25 output files.
(Output) Storage
Select the file service where the you want the new file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Output) File location
Enter or map the URL or path of where the new file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Output) Width
The width, in pixels, of the output file. The module will preserve the original aspect ratio.
(Output) Overwrite
Select whether the newly edited file will overwrite any output file that already exists. This applies only to files in Adobe storage.
Resize an image (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Create or edit a composite module.
This action resizes an image, using the same aspect ratio.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
Storage
Select the file service where the file you want to resize is stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
File location
Enter or map the URL or path of the file that you want to resize. This is only necessary if you have not chosen Fusion internal storage for the output storage.
Outputs
For each converted file you want to create, click Add item and enter the storage, location, and other options as listed.
Storage
Select the file service where the you want the new file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
File location
Enter or map the URL or path of where the new file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
Width
The width, in pixels, of the output file. The module will preserve the original aspect ratio.
Max width
When width is 0, Max with can be provided to get the size. Max width takes precedence with it is smaller than the document width.
Overwrite
Select whether the newly edited file will overwrite any output file that already exists. This applies only to files in Adobe storage.
Trim to canvas
Select Yes to trim the renditions to Canvas size, or No to make the renditions Layer Size.
Watermark an image (Legacy)
NOTE
This module has been deprecated, and will no longer work after July 30, 2026.
Update this module to the Create or edit a composite module.
This action module adds a watermark to the selected image.
Connection
For instructions on creating a connection to Adobe Photoshop, see Create a connection to Adobe Photoshop in this article.
(Base > Input) Storage
Select the file service where the file you want to add a watermark to is stored.
(Base > Input) File location
Enter or map the URL or path of the file that you want to add a watermark to.
(Watermark > Input) Storage
Select the file service where the watermark you want to add is stored.
(Watermark > Input) Storage
Select the file service where the watermark you want to add is stored.
(Watermark > Bounds) Height
Enter or map the desired height of the watermark in pixels.
(Watermark > Bounds) Width
Enter or map the desired width of the watermark in pixels.
(Watermark > Bounds) Left
Enter or map the distance in pixels from the left side of the image that the watermark should be.
(Watermark > Bounds) Top
Enter or map the distance in pixels from the top of the image that the watermark should be.
(Output) Storage
Select the file service where the you want the watermarked file to be stored.
Selecting Fusion internal storage makes the file available for later modules, but does not make the file available outside of the scenario.
(Output) File location
Enter or map the URL or path of where the watermarked file will be stored. This is only necessary if you have not chosen Fusion internal storage for the output storage.
(Output) Type
Select the file type that you want to convert the file to.
(Output) Width
The width, in pixels, of the output file. The module will preserve the original aspect ratio.
(Output) Overwrite
Select whether the newly edited file will overwrite any output file that already exists. This applies only to files in Adobe storage.
recommendation-more-help
workfront-fusion-help-workfront-fusion
