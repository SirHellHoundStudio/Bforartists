﻿###
bl_info = {
    "name": "Oscurart Chain and Rope Maker - Bforartists version",
    "author": "Oscurart",
    "version": (1, 1),
    "blender": (2, 63, 0),
    "location": "View3D > Tool Shelf > Create > Add Misc",
    "description": "Create chains and ropes along armatures/curves",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
        "Scripts/Add_Mesh/Oscurart_Chain_Rope_Maker",
    "tracker_url": "https://developer.blender.org/maniphest/task/edit/form/2/",
    "category": "Object"}


import bpy
from .oscurart_rope_maker import *
from .oscurart_chain_maker import *

def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.types.VIEW3D_PT_tools_add_misc.append(oscRopeButton)
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_PT_tools_add_misc.append(menu_oscChain)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.types.VIEW3D_PT_tools_add_misc.remove(oscRopeButton)
    bpy.utils.unregister_module(__name__)
    bpy.types.VIEW3D_PT_tools_add_misc.remove(menu_oscChain)

if __name__ == "__main__":
    register()





