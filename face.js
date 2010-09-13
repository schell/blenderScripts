    //face #$iface
	face = {};
	face.texture = '$texture';
	face.verts = [];
	face.uvs = [];
	face.normal = [
		$nx,
		$ny,
		$nz
	];
	face.verts.push([$v1x, $v1y, $v1z]);
	face.verts.push([$v2x, $v2y, $v2z]);
	face.verts.push([$v3x, $v3y, $v3z]);
	face.uvs.push([$t1u, $t1v]);
	face.uvs.push([$t2u, $t2v]);
	face.uvs.push([$t3u, $t3v]);
	faces.push(face);
	