

# <pep8 compliant>

# ----------------------------------------------------------
# Author: Fofight
# ----------------------------------------------------------


bl_info = {
    'name': 'Learnbgame',
    'description': 'Learn by game',
    'author': 'Fofight',
    'license': 'GPL',
    'deps': '',
    'version': (1, 0, 0),
    'blender': (2, 80, 0),
    'location': 'View3D > Tools > Create > biology',
    'warning': '',
    'wiki_url': 'https://github.com/s-leger/archipack/wiki',
    'tracker_url': 'https://github.com/BlenderCN/Learnbgame/issues',
    'link': 'https://github.com/BlenderCN/Learnbgame',
    'support': 'COMMUNITY',
    'category': 'Add Mesh'
    }


import os

if "bpy" in locals():
    import importlib as imp    
    imp.reload(biology_animal)
    imp.reload(biology_plant)
    imp.reload(biology_microbe)

    # print("archipack: reload ready")
else:
    from . import biology_animal
    from . import biology_plant
    from . import biology_microbe

    #print("archipack: ready")

# noinspection PyUnresolvedReferences
import bpy
# noinspection PyUnresolvedReferences
from bpy.types import (
    Panel, Menu
    )

from bpy.utils import previews
icons_collection = {}

animals_dir = os.path.join(os.path.dirname(__file__), "biology/animal")
animals_list = os.listdir(animals_dir)

icons_dir = os.path.join(os.path.dirname(__file__), "icons")
icons_list = os.listdir(icons_dir)





class BIOLOGY_ANIMAL_ADD(Menu):
    bl_idname = "biology.animal.add"
    bl_label = "Animal"

    def draw(self,context):
        global icons_collection
        icons = icons_collection["main"]
        layout = self.layout
        for animal in animals_list:
            layout.operator(
                "biology_animal."+animal,
                text=animal.capitalize(),
                icon_value=icons[animal if animal+".png" in icons_list else "learnbgame"].icon_id)


class BIOLOGY_PLANT_ADD(Menu):
    bl_idname = "biology.plant.add"
    bl_label = "Plant"

    def draw(self,context):
        global icons_collection
        icons = icons_collection["main"]
        layout = self.layout
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.cat",text="Cat",icon_value=icons["cat"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)

class BIOLOGY_MICROBE_ADD(Menu):
    bl_idname = "biology.microbe.add"
    bl_label = "Microbe"

    def draw(self,context):
        global icons_collection
        icons = icons_collection["main"]
        layout = self.layout
        layout.operator("biology_animal.armadillo",text="Armadillo",icon_value=icons["Learnbgame"].icon_id)
        layout.operator("biology_animal.beer",text="Cat",icon_value=icons["cat"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)
        layout.operator("biology_animal.dog",text="Dog",icon_value=icons["dog"].icon_id)


class BIOLOGY_CREATURE_ADD(Menu):
    bl_idname = "biology.creature.add"
    bl_label = 'Biology'


    def draw(self, context):
        global icons_collection
        icons = icons_collection["main"]
        layout = self.layout
        layout.menu(BIOLOGY_ANIMAL_ADD.bl_idname,text="Animal",icon="RNA_ADD")
        layout.menu(BIOLOGY_PLANT_ADD.bl_idname,text="Plant",icon="RNA_ADD")
        layout.menu(BIOLOGY_MICROBE_ADD.bl_idname,text="Microbe",icon="RNA_ADD")




def biology_func(self, context):
    layout = self.layout
    global icons_collection
    icons = icons_collection["main"]
    layout.menu(BIOLOGY_CREATURE_ADD.bl_idname, text="Biology",icon="RNA")


def register():
    global icons_collection
    icons = previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")
    for icon in os.listdir(icons_dir):
        name, ext = os.path.splitext(icon)
        icons.load(name, os.path.join(icons_dir, icon), 'IMAGE')
    icons_collection["main"] = icons
    bpy.utils.register_class(BIOLOGY_CREATURE_ADD)
    bpy.utils.register_class(BIOLOGY_ANIMAL_ADD)
    bpy.utils.register_class(BIOLOGY_PLANT_ADD)
    bpy.utils.register_class(BIOLOGY_MICROBE_ADD)
    bpy.types.VIEW3D_MT_mesh_add.append(biology_func)
    biology_animal.register()


def unregister():
    global icons_collection
    biology_animal.unregister()
    bpy.types.VIEW3D_MT_mesh_add.remove(biology_func)
    bpy.utils.unregister_class(BIOLOGY_MICROBE_ADD)
    bpy.utils.unregister_class(BIOLOGY_PLANT_ADD)
    bpy.utils.unregister_class(BIOLOGY_ANIMAL_ADD)
    bpy.utils.unregister_class(BIOLOGY_CREATURE_ADD)
    for icons in icons_collection.values():
        previews.remove(icons)
    icons_collection.clear()


if __name__ == "__main__":
    register()
