import streamlit as st
from Homepage import set_sidebar_visibility  

st.title('AI Fitness Trainer: Squats Analysis')


recorded_file = r'C:\Users\Admin\OneDrive\Desktop\Projects\ai-fitness\ai-fitness\output_sample.mp4'
sample_vid = st.empty()
sample_vid.video(recorded_file)

    
    