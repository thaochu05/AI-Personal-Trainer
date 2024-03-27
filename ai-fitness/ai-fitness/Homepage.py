import streamlit as st
import pandas as pd
from PIL import Image
import pickle 
from pathlib import Path
import streamlit_authenticator as stauth

# Config
page_icon = Image.open("cover.png")
st.set_page_config(layout="centered", page_title="Gym Posture Correction", page_icon=page_icon, )
#Login page
file_path = Path(__file__).parent / "hashed.pkl"    
users_data = {
    "usernames": {
        "mocmeo": {
            "name": "Moc",
            "password": "Mocmeo1809"
        },
        "thaocute": {
            "name": "Thaocute",
            "password": "Mociuthao0"
        }
    }
}
with open(file_path, "rb") as f:
    hashed_passwords = pickle.load(f)
    authenticator = stauth.Authenticate(credentials=users_data, cookie_name = "Gym Posture Correction", key = "abcdef", cookie_expiry_days=30)
    names, authentication_status, usernames = authenticator.login(location = 'main')
    
def set_sidebar_visibility(authentication_status):
  if authentication_status:
    st.sidebar.visible = True
  else:
    st.sidebar.visible = False
set_sidebar_visibility(authentication_status)

if authentication_status == False:
    st.error('Usernames and passwords do not match. Please try again.')
if authentication_status == None:
    st.error("Please enter you username and password to login")
if authentication_status == True:
    #Log out button at sidebar
    st.sidebar.visible = True
    authenticator.logout(location = "sidebar")
    st.sidebar.title(f"Welcome {names} to Gym Posture Correction App")

    # Initial State
    def initial_state():
        if 'df' not in st.session_state:
            st.session_state['df'] = None

        if 'X_train' not in st.session_state:
            st.session_state['X_train'] = None

        if 'X_test' not in st.session_state:
            st.session_state['X_test'] = None

        if 'y_train' not in st.session_state:
            st.session_state['y_train'] = None

        if 'y_test' not in st.session_state:
            st.session_state['y_test'] = None

        if 'X_val' not in st.session_state:
            st.session_state['X_val'] = None

        if 'y_val' not in st.session_state:
            st.session_state['y_val'] = None

        if "model" not in st.session_state:
            st.session_state['model'] = None

        if 'trained_model' not in st.session_state:
            st.session_state['trained_model'] = False

        if "trained_model_bool" not in st.session_state:
            st.session_state['trained_model_bool'] = False

        if "problem_type" not in st.session_state:
            st.session_state['problem_type'] = None

        if "metrics_df" not in st.session_state:
            st.session_state['metrics_df'] = pd.DataFrame()

        if "is_train" not in st.session_state:
            st.session_state['is_train'] = False

        if "is_test" not in st.session_state:
            st.session_state['is_test'] = False

        if "is_val" not in st.session_state:
            st.session_state['is_val'] = False

        if "show_eval" not in st.session_state:
            st.session_state['show_eval'] = False

        if "all_the_process" not in st.session_state:
            st.session_state['all_the_process'] = """"""

        if "all_the_process_predictions" not in st.session_state:
            st.session_state['all_the_process_predictions'] = False

        if 'y_pred_train' not in st.session_state:
            st.session_state['y_pred_train'] = None

        if 'y_pred_test' not in st.session_state:
            st.session_state['y_pred_test'] = None

        if 'y_pred_val' not in st.session_state:
            st.session_state['y_pred_val'] = None

        if 'uploading_way' not in st.session_state:
            st.session_state['uploading_way'] = None

        if "lst_models" not in st.session_state:
            st.session_state["lst_models"] = []

        if "lst_models_predctions" not in st.session_state:
            st.session_state["lst_models_predctions"] = []

        if "models_with_eval" not in st.session_state:
            st.session_state["models_with_eval"] = dict()

        if "reset_1" not in st.session_state:
            st.session_state["reset_1"] = False

    initial_state()

    # New Line
    def new_line(n=1):
        for i in range(n):
            st.write("\n")

    # Logo 
    col1, col2, col3 = st.columns([0.25,1,0.25])
    col2.image("d2t.png", use_column_width=True)
    new_line(2)

    # Description
    st.markdown("""Welcome to the Gym Posture Correction App, the easy-to-use platform for your gym posture correction! This app helps you improve your posture during gym workouts.
            Please select a page from the navigation sidebar to get started.""", unsafe_allow_html=True)
    st.divider()

    # Dataframe selection
    st.markdown("<h2 align='center'> <b> Getting Started", unsafe_allow_html=True)
    new_line(1)
    st.write("The first step is to \"submit\" your data. You can do that in two ways: **Live stream your video through the web cam**, or **Upload your file**. In all ways the data should be a video or image file and should not exceed 200 MB.")
    new_line(1)



    


