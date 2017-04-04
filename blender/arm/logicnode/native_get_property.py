import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class GetPropertyNode(Node, ArmLogicTreeNode):
    '''Get property node'''
    bl_idname = 'LNGetPropertyNode'
    bl_label = 'Get Property'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketShader', "Object")
        self.inputs.new('NodeSocketString', "Property")
        self.outputs.new('NodeSocketShader', "Value")

add_node(GetPropertyNode, category='Native')