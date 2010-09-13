blenderScene.models.$name = function () {
    var name = '$name', faces = [], face;
    $facecode
    return {
        name : name, 
        faces : faces,
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
                        [$mw03, $mw13, $mw23, $mw33]]
    }
}();
