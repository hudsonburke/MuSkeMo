
from bpy.types import Panel
from .. import VIEW3D_PT_MuSkeMo  #the class in which all panels will be placed


class VIEW3D_PT_body_panel(VIEW3D_PT_MuSkeMo, Panel):  # class naming convention ‘CATEGORY_PT_name’
    #Multiple inheritance, body_panel as a class inherits attributes from MuSkeMo class, but also from the "Panel" class, turning this into a panel
    #This is the first (main) subpanel in the parent class VIEW3D_PT_MuSkeMo.
    #The first layer of panels doesn't need a bl_parentid, but if you want multiple, you will need a 'bl_idname' for each.
    #Subpanels to this one need to be placed under VIEW3D_PT_MuSkeMo, but using the VIEW3D_PT_body_panel as the parentid
    bl_idname = 'VIEW3D_PT_body_panel'
    
    
    #bl_category = "Body panel"  # found in the Sidebar
    bl_label = "Body panel"  # found at the top of the Panel
    bl_context = "objectmode"
    
    bl_options = {'DEFAULT_CLOSED'}
    
    #bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        """define the layout of the panel"""
        
            
        layout = self.layout
        scene = context.scene
        muskemo = scene.muskemo
        
         ### selected joints and bodies

        from ..core.selected_objects_panel_row_func import CreateSelectedObjRow

        CreateSelectedObjRow('BODY', layout)
        

        ## user input body name    
        row = self.layout.row()
        split = row.split(factor=1/2)
        split.label(text = "Body Name:")
        ## Create new body
        # split = split.split(factor = 1/2)
        split.prop(muskemo, "bodyname", text = "")
        row = layout.row()
        row.operator("body.create_new_body", text="Create new body")
        row = self.layout.row()
        row.prop(muskemo, "axes_size")
        
        ## body collection
        row = self.layout.row()
        row = self.layout.row()
        row = self.layout.row()
        split = row.split(factor=1/2)
        split.label(text = "Body collection:")
        split.prop(muskemo, "body_collection", text = "")
        row = self.layout.row()
             
        row = self.layout.row()
                   
        ## assign precomputed inertial properties from other meshes
        self.layout.row()
        
        row = self.layout.row()
        row = self.layout.row()
        row.label(text = "Source object meshes with precomputed inertial properties")
        CreateSelectedObjRow('MESH_withdensity', layout)

                 
        row = self.layout.row()
        row.operator("body.assign_inertial_properties", text="Assign precomputed inertial properties")

        row = self.layout.row()
        row = self.layout.row()
        row = self.layout.row()
        row.operator("muskemo.reset_model_default_pose", text = 'Reset to default pose')

        
class VIEW3D_PT_vizgeometry_subpanel(VIEW3D_PT_MuSkeMo, Panel):  # 
    bl_idname = 'VIEW3D_PT_vizgeometry_subpanel'
    bl_parent_id = 'VIEW3D_PT_body_panel'
    
    #bl_category = "Body panel"  # found in the Sidebar
    bl_label = "Visual (bone) geometry"  # found at the top of the Panel
    bl_context = "objectmode"
    
    bl_options = {'DEFAULT_CLOSED'}
    
    #bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        muskemo = scene.muskemo
        
        ## user input body name
        row = self.layout.row()
        split = row.split(factor=1/2)
        split.label(text = "Geometry collection")
        split.prop(muskemo, "geometry_collection", text = "")
        row = self.layout.row()

        row.operator("body.attach_visual_geometry", text = "Attach visual (bone) geometry")
        row = self.layout.row()
        row.operator("body.detach_visual_geometry", text = "Detach visual (bone) geometry")
        ## intersection checker


        row = self.layout.row()
        row = self.layout.row()
        row.operator("mesh.intersection_checker", text = "Check for mesh intersections")
        return


class VIEW3D_PT_body_manual_inprop_assignment_subpanel(VIEW3D_PT_MuSkeMo, Panel):  # 
    bl_idname = 'VIEW3D_PT_body_utilities_subpanel'
    bl_parent_id = 'VIEW3D_PT_body_panel'
    
    #bl_category = "Body panel"  # found in the Sidebar
    bl_label = "Assign inertial properties manually"  # found at the top of the Panel
    bl_context = "objectmode"
    
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        muskemo = scene.muskemo
        
        row = layout.row()
        
        row.label(text = "If you manually type in inertial properties, use the below button to update the display location")
        row = layout.row()
        row.operator("body.update_location_from_com", text="Update display location using COM")
         
        
        