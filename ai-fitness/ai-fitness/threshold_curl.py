
# Get thresholds for beginner mode
def get_thresholds_beginner():

    _ANGLE_WRIST_ELBOW = {
                            'NORMAL' : (200, 145),
                            'TRANS'  : (144, 85),
                            'PASS'   : (84, 35)
                           }    

        
    thresholds = {
                    'ELBOW_WRIST_ANGLE': _ANGLE_WRIST_ELBOW,

                    'HIP_THRESH'   : 7,
                    'SHOULDER_THRESH' : 15,
                    'OFFSET_THRESH'    : 35.0,
                    'INACTIVE_THRESH'  : 15.0,

                    'CNT_FRAME_THRESH' : 50
                            
                }

    return thresholds