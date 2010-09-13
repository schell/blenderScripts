import bpy
from string import Template
	
def paste(data):
	import subprocess
	p = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
	p.stdin.write(data.encode("ascii"))
	p.stdin.close()
	retcode = p.wait()

def export_model(obj):
	i = 0
	resdir = bpy.utils.user_script_path()
	#setup the templates
	modelcode = ''
	modeltemplatefile = open(resdir+'/model.js', 'r')
	modeltemplate = Template(modeltemplatefile.read())
	modeltemplatefile.close();
	facecode = ''
	facetemplatefile = open(resdir+'/face.js', 'r')
	facetemplate = Template(facetemplatefile.read())
	facetemplatefile.close()

	mesh = obj.data
	for face in mesh.faces:
		if(len(mesh.uv_textures) > 0 and type(mesh.uv_textures[0].data[face.index].image) is not type(None)):
			meshtex = mesh.uv_textures[0].data[face.index]
			texture = meshtex.image.name
			t1 = meshtex.uv[0]
			t2 = meshtex.uv[1]
			t3 = meshtex.uv[2]
		else:
			texture = 'null'
			t1 = ['null', 'null']
			t2 = ['null', 'null']
			t3 = ['null', 'null']
			
		n = face.normal
		
		i += 1
		v1 = mesh.vertices[face.vertices[0]]
		v2 = mesh.vertices[face.vertices[1]]
		v3 = mesh.vertices[face.vertices[2]]
		
		facecode += facetemplate.substitute(iface=str(i), texture=texture, nx=n.x, ny=n.y, nz=n.z, v1x=v1.co.x, v1y=v1.co.y, v1z=v1.co.z, v2x=v2.co.x, v2y=v2.co.y, v2z=v2.co.z, v3x=v3.co.x, v3y=v3.co.y, v3z=v3.co.z, t1u=t1[0], t1v=t1[1], t2u=t2[0], t2v=t2[1], t3u=t3[0], t3v=t3[1])

	name = str.replace(obj.name, '.', '_')
	locx = obj.location.x
	locy = obj.location.y
	locz = obj.location.z
	rotux = obj.rotation_euler[0]
	rotuy = obj.rotation_euler[1]
	rotuz = obj.rotation_euler[2]
	ml00 = obj.matrix_local[0][0]
	ml01 = obj.matrix_local[0][1]
	ml02 = obj.matrix_local[0][2]
	ml03 = obj.matrix_local[0][3]
	ml10 = obj.matrix_local[1][0]
	ml11 = obj.matrix_local[1][1]
	ml12 = obj.matrix_local[1][2]
	ml13 = obj.matrix_local[1][3]
	ml20 = obj.matrix_local[2][0]
	ml21 = obj.matrix_local[2][1]
	ml22 = obj.matrix_local[2][2]
	ml23 = obj.matrix_local[2][3]
	ml30 = obj.matrix_local[3][0]
	ml31 = obj.matrix_local[3][1]
	ml32 = obj.matrix_local[3][2]
	ml33 = obj.matrix_local[3][3]
	mw00 = obj.matrix_world[0][0]
	mw01 = obj.matrix_world[0][1]
	mw02 = obj.matrix_world[0][2]
	mw03 = obj.matrix_world[0][3]
	mw10 = obj.matrix_world[1][0]
	mw11 = obj.matrix_world[1][1]
	mw12 = obj.matrix_world[1][2]
	mw13 = obj.matrix_world[1][3]
	mw20 = obj.matrix_world[2][0]
	mw21 = obj.matrix_world[2][1]
	mw22 = obj.matrix_world[2][2]
	mw23 = obj.matrix_world[2][3]
	mw30 = obj.matrix_world[3][0]
	mw31 = obj.matrix_world[3][1]
	mw32 = obj.matrix_world[3][2]
	mw33 = obj.matrix_world[3][3]
	
	modelcode = modeltemplate.substitute(name=name, facecode=facecode, locx=locx, locy=locy, locz=locz, rotux=rotux, rotuy=rotuy, rotuz=rotuz, ml00=ml00, ml01=ml01, ml02=ml02, ml03=ml03, ml10=ml10, ml11=ml11, ml12=ml12, ml13=ml13, ml20=ml20, ml21=ml21, ml22=ml22, ml23=ml23, ml30=ml30, ml31=ml31, ml32=ml32, ml33=ml33, mw00=mw00, mw01=mw01, mw02=mw02, mw03=mw03, mw10=mw10, mw11=mw11, mw12=mw12, mw13=mw13, mw20=mw20, mw21=mw21, mw22=mw22, mw23=mw23, mw30=mw30, mw31=mw31, mw32=mw32, mw33=mw33)
	return modelcode
	
def export_camera(obj):
	resdir = bpy.utils.user_script_path()
	#setup the template
	cameracode = ''
	cameratemplatefile = open(resdir+'/camera.js', 'r')
	cameratemplate = Template(cameratemplatefile.read())
	cameratemplatefile.close();
	
	name = str.replace(obj.name, '.', '_')
	locx = obj.location.x
	locy = obj.location.y
	locz = obj.location.z
	rotux = obj.rotation_euler[0]
	rotuy = obj.rotation_euler[1]
	rotuz = obj.rotation_euler[2]
	ml00 = obj.matrix_local[0][0]
	ml01 = obj.matrix_local[0][1]
	ml02 = obj.matrix_local[0][2]
	ml03 = obj.matrix_local[0][3]
	ml10 = obj.matrix_local[1][0]
	ml11 = obj.matrix_local[1][1]
	ml12 = obj.matrix_local[1][2]
	ml13 = obj.matrix_local[1][3]
	ml20 = obj.matrix_local[2][0]
	ml21 = obj.matrix_local[2][1]
	ml22 = obj.matrix_local[2][2]
	ml23 = obj.matrix_local[2][3]
	ml30 = obj.matrix_local[3][0]
	ml31 = obj.matrix_local[3][1]
	ml32 = obj.matrix_local[3][2]
	ml33 = obj.matrix_local[3][3]
	mw00 = obj.matrix_world[0][0]
	mw01 = obj.matrix_world[0][1]
	mw02 = obj.matrix_world[0][2]
	mw03 = obj.matrix_world[0][3]
	mw10 = obj.matrix_world[1][0]
	mw11 = obj.matrix_world[1][1]
	mw12 = obj.matrix_world[1][2]
	mw13 = obj.matrix_world[1][3]
	mw20 = obj.matrix_world[2][0]
	mw21 = obj.matrix_world[2][1]
	mw22 = obj.matrix_world[2][2]
	mw23 = obj.matrix_world[2][3]
	mw30 = obj.matrix_world[3][0]
	mw31 = obj.matrix_world[3][1]
	mw32 = obj.matrix_world[3][2]
	mw33 = obj.matrix_world[3][3]
	angle = obj.data.angle
	clip_end = obj.data.clip_end
	clip_start = obj.data.clip_start
	dof_distance = obj.data.dof_distance
	lens = obj.data.lens
	lens_unit = obj.data.lens_unit
	ortho_scale = obj.data.ortho_scale
	shift_x = obj.data.shift_x
	shift_y = obj.data.shift_y
	type = obj.data.type
	
	cameracode = cameratemplate.substitute(name=name, locx=locx, locy=locy, locz=locz, rotux=rotux, rotuy=rotuy, rotuz=rotuz, ml00=ml00, ml01=ml01, ml02=ml02, ml03=ml03, ml10=ml10, ml11=ml11, ml12=ml12, ml13=ml13, ml20=ml20, ml21=ml21, ml22=ml22, ml23=ml23, ml30=ml30, ml31=ml31, ml32=ml32, ml33=ml33, mw00=mw00, mw01=mw01, mw02=mw02, mw03=mw03, mw10=mw10, mw11=mw11, mw12=mw12, mw13=mw13, mw20=mw20, mw21=mw21, mw22=mw22, mw23=mw23, mw30=mw30, mw31=mw31, mw32=mw32, mw33=mw33, angle=angle, clip_end=clip_end, clip_start=clip_start, dof_distance=dof_distance, lens=lens, lens_unit=lens_unit, ortho_scale=ortho_scale, shift_x=shift_x, shift_y=shift_y, type=type)
	
	return cameracode

def export_scene(scene):
	
	# get scene header template
	resdir = bpy.utils.user_script_path()
	scenetemplatefile = open(resdir+'/scene.js', 'r')
	scenetemplate = Template(scenetemplatefile.read())
	scenetemplatefile.close()
	
	name = str.replace(scene.name, '.', '_')
	
	scenecode = scenetemplate.substitute(name=name)
	
	for object in scene.objects:
		if(hasattr(object.data, 'faces')):
			#this object is a mesh
			scenecode += export_model(object)
			
		elif(hasattr(object.data, 'lens')):
			scenecode += export_camera(object)
			
		#elif lamp
	return scenecode