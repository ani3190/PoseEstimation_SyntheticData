# -*- coding: utf-8 -*-
"""
--------------------------------------------------------
Creation of Blender Scence with Forklimt and background image
Created on May 2024
@author: Aniruddha Pal - apal2s - e-mail: aniruddha.pal@smail.inf.h-brs.de
--------------------------------------------------------
"""
import bpy
import os

#select and delete all objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# go to file and import fspy
filepath="/home/geforcertx/Downloads/background_image/schnellecke/images_aniruddha/frame_115.fspy"
#forklift_path = "/home/geforcertx/Downloads/blender_ani/blender_objects/forklift_keypoints.fbx"
bpy.ops.fspy_blender.import_project(filepath=filepath)
bpy.context.object.name = "Camera"
bpy.context.object.lock_location = (True,True,True)
bpy.context.object.lock_rotation = (True,True,True)

bpy.context.object.data.show_background_images = False

camera = bpy.context.scene.camera
sensor_width = camera.data.sensor_width
sensor_height = camera.data.sensor_height
    
# Calculate the diagonal length of the sensor
diagonal_length = (sensor_width**2 + sensor_height**2)**0.5
    
# Calculate the size of the plane to extend beyond the camera's view
plane_size = diagonal_length * 2  # Adjust the factor as needed
    
# Add a new plane
bpy.ops.mesh.primitive_plane_add(size=plane_size, enter_editmode=False, align='WORLD', location=(0, 0, 0))

    
#Switch to edit mode to select edges
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
    
# Extrude edges in the Z-direction
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 3), "constraint_axis":(False, False, True)})

# Switch to Face selection mode
bpy.ops.mesh.select_mode(type="FACE")
   
# Delete the selected faces
bpy.ops.mesh.delete(type='FACE') 
# Switch back to Object mode
bpy.ops.object.mode_set(mode='OBJECT')

#rename the plane
bpy.context.object.name = "Background"

#adding the UV project modifier
bpy.ops.object.modifier_add(type='UV_PROJECT')
bpy.context.object.modifiers["UVProject"].uv_layer = "UVMap"
#bpy.data.objects["Background"].(null) = bpy.data.objects["Camera"]
bpy.context.object.modifiers["UVProject"].aspect_x = 1.77778

#setting up the materials(texture map) for the background

bpy.ops.object.material_slot_add()
bpy.data.materials.new(name="background_image_texture")
bpy.context.object.material_slots[0].material = bpy.data.materials.new(name="background_image_texture")

#bpy.ops.node.add_node(use_transform=True, type="ShaderNodeTexImage")

# Enable use of nodes for the material
bpy.context.object.active_material.use_nodes = True
 # Add a texture image node
material = bpy.context.object.active_material
node_tree = material.node_tree


for node in node_tree.nodes:
    node_tree.nodes.remove(node)       

principled_bsdf = node_tree.nodes.new('ShaderNodeBsdfPrincipled')
principled_bsdf.location = (0,0)
principled_bsdf.inputs[12].default_value = 0
texture_node = node_tree.nodes.new('ShaderNodeTexImage')
texture_node.location = (-500,0)
node_tree.links.new(texture_node.outputs['Color'], principled_bsdf.inputs['Base Color'])
# Create an Output Material node
output_node = material.node_tree.nodes.new('ShaderNodeOutputMaterial')
output_node.location = (500, 0)  # Set node location
    
# Connect the Principled BSDF node to the Output Material node
material.node_tree.links.new(principled_bsdf.outputs[0], output_node.inputs[0])

# Create the mapping node
mapping_node = material.node_tree.nodes.new('ShaderNodeMapping')
mapping_node.location = (-800, 0)  # Set node location


material.node_tree.links.new(mapping_node.outputs[0], texture_node.inputs[0])

# Create texture coordinate node
texture_coordinate_node = material.node_tree.nodes.new('ShaderNodeTexCoord')
texture_coordinate_node.location = (-1100, 0)  # Set node location

material.node_tree.links.new(texture_coordinate_node.outputs[5], mapping_node.inputs[0])

first_packed_image_data_block = None
for image in bpy.data.images:
    if image.packed_file is not None:  # Select only packed images
        first_packed_image_data_block = image
        break
    
if first_packed_image_data_block is not None:
    
    # Assign the packed image data block to the Image Texture node
    texture_node.image = first_packed_image_data_block
    
    
#adding the lights

bpy.ops.object.light_add(type='AREA', radius=1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

bpy.data.objects["Area"].location[2] = bpy.data.objects["Camera"].location[2] + 2
bpy.data.objects["Area"].scale = (float(plane_size), float(plane_size), float(plane_size))
bpy.context.object.data.energy = 25000


# import forklift object
#bpy.context.view_layer.objects.active = None

#bpy.ops.import_scene.fbx(filepath=forklift_path)

#bpy.ops.wm.obj_import(filepath=forklift_path)
#bpy.ops.object.select_all(action='DESELECT')

file_path = "/home/geforcertx/Downloads/blender_ani/blender_files/forklift_object_keypoints_adjusted.blend"
 
 
with bpy.data.libraries.load(file_path) as (data_from, data_to):
    # Append all objects
    data_to.objects = data_from.objects
 
    # Append all materials
    data_to.materials = data_from.materials
 
    # Append all textures
    data_to.textures = data_from.textures
 
# Create copies of the appended objects in the scene
for obj in data_to.objects:
    bpy.context.collection.objects.link(obj.copy())
 
# Create copies of the appended materials in the scene
for mat in data_to.materials:
    bpy.data.materials.new(name=mat.name)
    bpy.data.materials[mat.name].copy()
    #bpy.data.materials[mat.name].copy_from(mat)
 
# Create copies of the appended textures in the scene
for tex in data_to.textures:
    bpy.data.textures.new(name=tex.name)
    bpy.data.textures[tex.name].copy(tex)
    

#select and delete all objects
bpy.ops.object.select_all(action='SELECT')

# Get a list of all selected objects
selected_objects = bpy.context.selected_objects
 
# Print the list of selected object names
print("List of selected object names:")
for obj in selected_objects:
    print(obj.name)
#col = bpy.data.collections.get("Collection")
#if col:
#   for obj in col.objects:
#       #obj.select_set(True)
#       print (obj.name)
#       
#       if (obj.name)
       
def remove_decimal(string):
    if '.' in string:
        return string.split('.')[0]
    else:
        return string
 
def process_strings(string_list):
    renamed_strings = [remove_decimal(string) for string in string_list]
    return renamed_strings
 
# Example list of strings
selected_object_names = [obj.name for obj in selected_objects]
renamed_objects = process_strings(selected_object_names)
 
# Rename the selected objects
for obj, new_name in zip(selected_objects, renamed_objects):
    obj.name = new_name
    #obj.data.name = new_name
 
# Print the list of renamed object names
print("\nList of renamed object names:")
for obj in selected_objects:
    print(obj.name)

#parenting forklift elements to Empty object
    
bpy.ops.object.select_all(action='DESELECT')

empty = bpy.data.objects['Empty']
fork = bpy.data.objects['fork']
forklift = bpy.data.objects['Forklift']
marker1 = bpy.data.objects['Marker_1']
marker2 = bpy.data.objects['Marker_2']
marker3 = bpy.data.objects['Marker_3']
marker4 = bpy.data.objects['Marker_4']
forklift_skel = bpy.data.objects['forklift_skel']
fork.select_set(True)
forklift.select_set(True)
marker1.select_set(True)
marker2.select_set(True)
marker3.select_set(True)
marker4.select_set(True)
forklift_skel.select_set(True)
bpy.context.view_layer.objects.active = empty
bpy.ops.object.parent_set(keep_transform= True)
#output_file = os.path.splitext(filepath)[0] + ".blend"
#bpy.ops.wm.save_as_mainfile(filepath=os.path.join("/home/geforcertx/Downloads/blender_ani/New Folder", output_file))

# Define the path to the folder where you want to save the blend file
output_folder = "/home/geforcertx/Downloads/blender_ani/New Folder/"

# Get the current blend file name
blend_file_name = os.path.splitext(filepath)[0] + ".blend"
#blend_file_name = bpy.path.basename(bpy.context.blend_data.filepath)

# Define the full path for the output blend file
output_blend_file = os.path.join(output_folder, blend_file_name)

# Save the blend file to the specified folder
bpy.ops.wm.save_as_mainfile(filepath=output_blend_file)

# Close the blend file without saving again (optional)
# Sets render engine to cycles
bpy.context.scene.render.engine = 'CYCLES'