import bpy

for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        override = bpy.context.copy()
        override['area'] = area
        bpy.ops.view3d.viewnumpad(override, type = 'CAMERA')
        break
