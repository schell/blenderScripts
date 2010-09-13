import bpy
import sys
# add the user script path so we can use our external scripts
sys.path.append(bpy.utils.user_script_path())


class RENDER_PT_efnx(bpy.types.Panel):
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_context = "render"
	bl_label = "Efnx Exports"
    
	def draw_header(self, context):
		layout = self.layout
		layout.label(text="", icon="PHYSICS")

	def draw(self, context):
		layout = self.layout
		row = layout.row()
		split = row.split(percentage=0.5)
		colL = split.column()
		colR = split.column()
		colL.operator("efnx_isom_exportScene", text="Scene to JS")


class RENDER_OT_efnx(bpy.types.Operator):
	bl_label = "Export scene to javascript operator"
	bl_idname = "efnx_isom_exportScene"
	bl_description = "Export scene to javascript"

	def invoke(self, context, event):
		import bpy
		import efnx
		reload(efnx)
		self.report("INFO", "Export initiated")
		efnx.paste(efnx.export_scene(bpy.context.scene))
		self.report("INFO", "Javascript copied to clipboard")
		return{"FINISHED"}