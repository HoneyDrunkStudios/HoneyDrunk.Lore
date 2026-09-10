---
source: "https://www.tech-artists.org/t/array-attributes-in-maya-python-api-2-mpxnode/18533"
title: "Array attributes in Maya Python API 2 MPxNode"
author: "hazmondo"
date_published: "2026-09-01"
date_clipped: "2026-09-10"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Array attributes in Maya Python API 2 MPxNode

Source: https://www.tech-artists.org/t/array-attributes-in-maya-python-api-2-mpxnode/18533

Array attributes in Maya Python API 2 MPxNode - maya - Tech-Artists.Org
Tech-Artists.Org
Array attributes in Maya Python API 2 MPxNode
maya ,
python ,
codiing
hazmondo
September 1, 2026, 2:20pm
1
Hello,
I’m trying to use array attributes for the first time and I’m sure I’m making some mistakes
The code below creates an array attribute with two children, the multiplier attribute multiplies the translation X of an output matrix attribute. It seems to work but there is no evaluation when set keys on the multiplier value and playback the animation. I’ve tried looking at the C++ documentation but I couldn’t find a useful example.
import sys
from maya.api import OpenMaya as om
def maya_useNewAPI():
"""
The presence of this function tells Maya that the plugin produces, and
expects to be passed, objects created using the Maya Python API 2.0.
"""
pass
class ArrayTestNode(om.MPxNode):
NODE_NAME = 'arrayTestNode'
NODE_ID = om.MTypeId(0x00000001)
array_test = None
multiplier = None
output_matrix = None
@classmethod
def creator(cls):
return cls()
@classmethod
def initialize(cls):
matrix_attr = om.MFnMatrixAttribute()
numeric_attr = om.MFnNumericAttribute()
compound_attr = om.MFnCompoundAttribute()
cls.array_test = compound_attr.create('arrayTest', 'at')
compound_attr.array = True
compound_attr.disconnectBehavior = om.MFnAttribute.kDelete
cls.multiplier = numeric_attr.create('multiplier', 'm', om.MFnNumericData.kDouble, 0.0)
numeric_attr.keyable = True
compound_attr.addChild(cls.multiplier)
cls.output_matrix = matrix_attr.create('outputMatrix', 'om')
matrix_attr.storable = False
matrix_attr.writable = False
compound_attr.addChild(cls.output_matrix)
cls.addAttribute(cls.array_test)
cls.attributeAffects(cls.multiplier, cls.output_matrix)
def compute(self, plug, data_block):
if plug != self.output_matrix:
return
array_test_data_handle_array = data_block.inputArrayValue(self.array_test)
multiplers = []
while not array_test_data_handle_array.isDone():
multiplers.append(array_test_data_handle_array.inputValue().child(self.multiplier).asDouble())
array_test_data_handle_array.next()
matrix_values = [om.MMatrix(((1,0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (m, 0, 0, 1))) for m in multiplers]
array_test_data_handle_array = data_block.outputArrayValue(self.array_test)
counter = 0
while not array_test_data_handle_array.isDone():
array_test_data_handle_array.outputValue().child(self.output_matrix).setMMatrix(matrix_values[counter])
counter += 1
array_test_data_handle_array.next()
data_block.setClean(plug)
def initializePlugin(plugin):
plugin_fn = om.MFnPlugin(plugin)
try:
plugin_fn.registerNode(
ArrayTestNode.NODE_NAME, ArrayTestNode.NODE_ID, ArrayTestNode.creator,
ArrayTestNode.initialize)
except:
sys.stderr.write(f'Failed to register node: {ArrayTestNode.NODE_NAME}')
def uninitializePlugin(plugin):
plugin_fn = om.MFnPlugin(plugin)
try:
plugin_fn.deregisterNode(ArrayTestNode.NODE_ID)
except:
sys.stderr.write(f'Failed to unregister node: {ArrayTestNode.NODE_NAME}')
Thanks,
-Harry
Home
Categories
Guidelines
Terms of Service
Privacy Policy
Powered by Discourse , best viewed with JavaScript enabled
