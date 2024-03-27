import cv2 
import time
import numpy as np
import mediapipe as mp
from utils import find_angle, get_landmark_features, draw_text, draw_dotted_line
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# self.thresholds
thresholds = {
                    'HIP_KNEE_VERT': {
                            'NORMAL' : (0,  32),
                            'TRANS'  : (35, 65),
                            'PASS'   : (70, 95)
                           }    
,

                    'HIP_THRESH'   : [10, 50],
                    'ANKLE_THRESH' : 45,
                    'KNEE_THRESH'  : [50, 70, 95],

                    'OFFSET_THRESH'    : 35.0,
                    'INACTIVE_THRESH'  : 15.0,

                    'CNT_FRAME_THRESH' : 50
                            
                }

font = cv2.FONT_HERSHEY_SIMPLEX

        # line type
linetype = cv2.LINE_AA

        # set radius to draw arc
radius = 20

        # Colors in BGR format.
COLORS = {
                        'blue'       : (0, 127, 255),
                        'red'        : (255, 50, 50),
                        'green'      : (0, 255, 127),
                        'light_green': (100, 233, 127),
                        'yellow'     : (255, 255, 0),
                        'magenta'    : (255, 0, 255),
                        'white'      : (255,255,255),
                        'cyan'       : (0, 255, 255),
                        'light_blue' : (102, 204, 255)
                      }



 # Dictionary to maintain the various landmark features.
dict_features = {}
left_features = {
                                'shoulder': 11,
                                'elbow'   : 13,
                                'wrist'   : 15,                    
                                'hip'     : 23,
                                'knee'    : 25,
                                'ankle'   : 27,
                                'foot'    : 31
                             }

right_features = {
                                'shoulder': 12,
                                'elbow'   : 14,
                                'wrist'   : 16,
                                'hip'     : 24,
                                'knee'    : 26,
                                'ankle'   : 28,
                                'foot'    : 32
                              }

dict_features['left'] = left_features
dict_features['right'] = right_features
dict_features['nose'] = 0

        
        # For tracking counters and sharing states in and out of callbacks.
state_tracker = {
            'state_seq': [],

            'start_inactive_time': time.perf_counter(),
            'start_inactive_time_front': time.perf_counter(),
            'INACTIVE_TIME': 0.0,
            'INACTIVE_TIME_FRONT': 0.0,

            # 0 --> Bend Backwards, 1 --> Bend Forward, 2 --> Keep shin straight, 3 --> Deep squat
            'DISPLAY_TEXT' : np.full((4,), False),
            'COUNT_FRAMES' : np.zeros((4,), dtype=np.int64),

            'LOWER_HIPS': False,

            'INCORRECT_POSTURE': False,

            'prev_state': None,
            'curr_state':None,

            'SQUAT_COUNT': 0,
            'IMPROPER_SQUAT':0
            
        }
        
FEEDBACK_ID_MAP = {
                                0: ('BEND BACKWARDS', 215, (0, 153, 255)),
                                1: ('BEND FORWARD', 215, (0, 153, 255)),
                                2: ('KNEE FALLING OVER TOE', 170, (255, 80, 80)),
                                3: ('SQUAT TOO DEEP', 125, (255, 80, 80))
                               }

# Create a VideoCapture object for the camera (0 for default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    frame_width, frame_height,_ = frame.shape
    # Convert the frame to RGB for MediaPipe Pose
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    key_points = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5).process(rgb_frame)
    # Display the frame
    cv2.imshow("Camera Feed", frame)
    '''if key_points.pose_landmarks:
        ps_lm = key_points.pose_landmarks
        nose_coordination = get_landmark_features(ps_lm.landmarks, dict_features,'nose',frame_width, frame_height)
        left_shldr_coord, left_elbow_coord, left_wrist_coord, left_hip_coord, left_knee_coord, left_ankle_coord, left_foot_coord = \
                                get_landmark_features(ps_lm.landmark, self.dict_features, 'left', frame_width, frame_height)
        right_shldr_coord, right_elbow_coord, right_wrist_coord, right_hip_coord, right_knee_coord, right_ankle_coord, right_foot_coord = \
                                get_landmark_features(ps_lm.landmark, self.dict_features, 'right', frame_width, frame_height)
        print(nose_coordination, left_shldr_coord,right_shldr_coord)'''
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera resources
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()