blenderScene.cameras.$name = function () {
    return {
        name : '$name', 
        location : [$locx, $locy, $locz],
        rotation_euler : [$rotux, $rotuy, $rotuz],
        // Local matrix
        matrix_local : [[$ml00, $ml10, $ml20, $ml30],
                        [$ml01, $ml11, $ml21, $ml31],
                        [$ml02, $ml12, $ml22, $ml32],
                        [$ml03, $ml13, $ml23, $ml33]],
        // World matrix
        matrix_world : [[$mw00, $mw10, $mw20, $mw30],
                        [$mw01, $mw11, $mw21, $mw31],
                        [$mw02, $mw12, $mw22, $mw32],
                        [$mw03, $mw13, $mw23, $mw33]],
        // Perspective Camera lens field of view in degrees
        angle : $angle,
        // Camera far clipping distance
        clip_end : $clip_end,
        // Camera near clipping distance
        clip_start : $clip_start,
        // Distance to the focus point for depth of field
        dof_distance : $dof_distance,
        // Perspective Camera lens value in millimeters
        lens : $lens,
        // Unit to edit lens in for the user interface
        lens_unit : '$lens_unit', 
        // Orthographic Camera scale (similar to zoom)
        ortho_scale : $ortho_scale,
        // Perspective Camera horizontal shift
        shift_x : $shift_x,
        // Perspective Camera vertical shift
        shift_y : $shift_y,
        // Camera type
        type : '$type'
    }
}();
