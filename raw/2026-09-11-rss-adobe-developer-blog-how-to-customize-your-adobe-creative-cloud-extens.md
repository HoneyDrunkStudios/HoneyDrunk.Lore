---
source: "https://blog.developer.adobe.com/en/publish/2019/06/how-to-customize-your-adobe-creative-cloud-extension-package"
title: "How to Customize Your Adobe Creative Cloud Extension Package"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-09-11"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# How to Customize Your Adobe Creative Cloud Extension Package

Source: https://blog.developer.adobe.com/en/publish/2019/06/how-to-customize-your-adobe-creative-cloud-extension-package

How to Customize Your Adobe Creative Cloud Extension Package
︎
Since I published the Package, Distribute, Install Guide for Adobe Creative Cloud extensions, I have received many questions from developers on how to customize the package, such as:
“How do I include other files in the package?”
“How to I set custom install locations?”
The short answer is “use the MXI file to add custom configurations.” In this post, I will explain how to decide what to include in your package as well as how to build your configuration file, which is covered in this step of the package guide .
Note: If you are new to building Creative Cloud extensions, I’d recommend you take a look at the Getting Started Guide first.
1. Decide the package folder structure
To help you understand the process more easily, look at the example folder structure below:
︎
In this example, we have a folder that contains a packaged CEP extension ( cep.zxp ) and another folder that contains a PSD file. Also, we have the configuration manifest ( id.mxi ) in the root. Note that your actual content structure has to match the structure defined in your .mxi file explained in the next step.
2. Write the configuration manifest that matches the content structure
The .mxi file is a configurable XML file that contains installation instructions, including the list of folders/files to be installed, install location, supported CC products, and other specific instructions. Based on the example content structure defined in the first step, you need to write an .mxi file like the one below:
https://gist.github.com/dkstevekwak/e1f19b3abe155e36edf403aa1483ae44#file-id-mxi
Here are descriptions of each tag:
macromedia-extension : The main container tag for the extension installation file
author : The name of the extension’s author
description : A description of what the extension does
ui-access : Information about where to find the item in the product’s user interface
license-agreement : The license agreement text that is displayed at installation
products : A container for tags specifying an extension’s product compatibility
files : A container for tags describing the files an extension installs
In our example, the package includes two files, a CEP panel package and a PSD file.
For the CEP panel:
The source path must include the filename cep.zxp like this: source="CEP/cep.zxp"
The destination should be an empty string, ”” , since the panel will be installed in the predetermined panel location
The file-type should be one of the following options ( csxs in this case): - csxs : A CEP extension package - plugin : A native plug-in - ordinary : Ordinary files receive no special processing
The supported products and minimum version must be specified
For the PSD file:
The source path should only include a folder name, such as source=”PSD/”
The destination should contain a path token like $Downloads for the user’s Downloads folder. See the complete list of available path tokens
The file-type should be one of the following options ( ordinary in this case): - csxs : A CEP extension package - plugin : A native plug-in - ordinary : Ordinary files receive no special processing
Specify the supported products and minimum version
For the complete list of tags and explanation, refer to the General MXI Elements page .
3. Package your extension
Now that you have the folder, files, and the .mxi file ready, you are ready to package your extension. Follow the rest of the steps in the Package, Distribute, Install Guide .
I hope this article helps you understand how to customize your Creative Cloud Extension Package. If there are any other topics you would like me to cover, please let me know in the comments below.
For more stories like this, subscribe to our Creative Cloud Developer Newsletter .
