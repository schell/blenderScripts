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
		colL.operator("efnx_exportScene_js", text="Scene to JS")
		colR.operator("efnx_exportScene_objc", text="Scene to Obj-C")


class RENDER_OT_efnx_js(bpy.types.Operator):
	bl_label = "Export scene to javascript operator"
	bl_idname = "efnx_exportScene_js"
	bl_description = "Export scene to javascript"

	def invoke(self, context, event):
		import bpy
		import efnx
		reload(efnx)
		self.report("INFO", "Export initiated")
		efnx.paste(efnx.export_scene(bpy.context.scene, 'js'))
		self.report("INFO", "Javascript copied to clipboard")
		return{"FINISHED"}
		
class RENDER_OT_efnx_objc(bpy.types.Operator):
	bl_label = "Export scene to objective c operator"
	bl_idname = "efnx_exportScene_objc"
	bl_description = "Export scene to Objective-C"

	def invoke(self, context, event):
		import bpy
		import efnx
		reload(efnx)
		self.report("INFO", "Export initiated")
		efnx.paste(efnx.export_scene(bpy.context.scene, 'objc'))
		self.report("INFO", "Javascript copied to clipboard")
		return{"FINISHED"}