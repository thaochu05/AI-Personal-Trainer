# AI-Personal-Trainer
The project aims to revolutionize fitness guidance by leveraging cutting-edge technologies such as computer vision and machine learning. Through a multipage web application built with **Streamlit**, users receive real-time posture correction feedback during workouts. The integration of **OpenCV** and **Mediapipe** enables accurate posture detection and correction, ensuring optimal exercise form. Additionally, the application utilizes the **LLM Large Language Model** to provide personalized weekly exercise plans tailored to individual users' fitness goals and progress. With efficient **SQL** database management, the project ensures seamless data storage and retrieval, contributing to a holistic and personalized fitness experience.

:arrow_right: *For deeper explaination and suggestion can be found [here](https://github.com/thaochu05/AI-Personal-Trainer/blob/main/AI%20PERSONAL%20TRAINER%20PROJECT%20REPORT.pdf)*


## Objectives and Goals
- Detect and correct improper posture in real-time.
- Deliver personalized exercise plans tailored to individual users' needs and fitness goals.
- Integrate computer vision algorithms (OpenCV, MediaPipe) to analyze user movements and provide instant feedback.
- Utilize Large Language Models (LLM) to generate personalized weekly exercise plans based on users' fitness levels, preferences, and progress.

## Tools & Technologies
- **Programming Languages**: Python (TensorFlow, OpenCV, MediaPipe, PyTorch)
- **Machine Learning Models**: Pose estimation, deep learning-based posture correction, recommendation systems
- **Data Sources**: Fitness datasets, real-time user feedback
- **User Interface**: Web-based and mobile application integration

## Methodology
Our AI-powered fitness application follows a structured approach to posture detection, personalized workout recommendations, and real-time feedback. The methodology consists of three core components:

### A. POSTURE CORRECTION FUNCTION
In this web application, we have integrated five primary exercises, namely Squats, Bicep Curl, Dumbbell Fly, Dumbbell kickback, and Push-ups, to cater to diverse fitness routines. Each 
exercise uses the same standardized logic, meticulously designed to ensure accuracy and
effectiveness. For an easier explanation of this approach, we will employ the Bicep Curl as a
paradigmatic example for elucidation within this report. 

#### 1. **Real-Time Posture Detection**
- MediaPipe Pose employs machine learning for precise body pose tracking in videos. It uses BlazePose, integrating COCO, BlazeFace, and BlazePalm functionalities, to detect 33 body landmarks in an RGB frame. The system follows a two-stage detection-tracking pipeline: first, it detects the region of interest (ROI) to locate the person, and then, it tracks and predicts pose landmarks within the ROI using a cropped frame.
  
  ![image](https://github.com/user-attachments/assets/5fae06e8-6893-4cdd-8c84-96d0c7572d1b)

#### 2. **Choosing Frontal and Side View for Posture Analysis**
Selecting the appropriate viewpoint for capturing a user’s movement is crucial for accurate fitness analysis.

- **Frontal View**: This view enables the system to analyze both the left and right sides of the body. It is useful for exercises where symmetry matters, such as overhead presses, side planks, crunches, and curls. In our web application, the frontal view is primarily used for dumbbell fly exercises.
- **Side View**: This perspective enhances estimation accuracy for inclinations relative to verticals or horizontals. It is beneficial for exercises like deadlifts, pushups, squats, and dips. 

Given our focus on Bicep Curl analysis, where precise vertical inclinations are necessary, we prioritize the **side view** for optimal accuracy.

#### 3. **Bicep Curl Form Analysis**
To evaluate bicep curl form, we analyze specific body landmarks:
- **Shoulder-elbow angle**
- **Elbow-wrist angle**
- **Shoulder-hip angle**

These angles are compared against predefined thresholds to determine if the bicep curl is executed correctly. Real-time feedback is generated based on this assessment.

  ![image](https://github.com/user-attachments/assets/f885abac-157a-4c31-b3e9-6e505c5a6f43)

Additionally, we compute the offset angle between the nose and shoulders to ensure the user maintains a proper side view for accurate pose estimation. If the offset angle exceeds a certain threshold, warnings are provided.

  ![image](https://github.com/user-attachments/assets/a679a3ae-33ec-4010-86f7-10287a57b49c)

#### 4. **State Tracking for Bicep Curls**
We implement a state transition system to monitor bicep curl execution:
1. **State (s1) - Normal Phase:** The user stands straight with an elbow angle between 145° and 200°.
2. **State (s2) - Transition Phase:** The elbow angle decreases to between 85° and 144° as the curl progresses.
3. **State (s3) - Pass Phase:** The elbow reaches an angle between 35° and 84°, completing the curl.

A sequence list (`state_sequence`) tracks these transitions. A correct curl follows the sequence `[s1 → s2 → s3 → s2 → s1]`. Incorrect sequences trigger feedback.

We also incorporate an **inactivity timer** that resets the counters if no motion is detected beyond a predefined threshold.

![image](https://github.com/user-attachments/assets/59769cac-c80e-4b5e-beb5-c8ab7bbbed48)

#### 5. **Aplication Workflow** 
This application workflow follows a methodology inspired by the LearnOpenCV [website](learnopencv.com)

![image](https://github.com/user-attachments/assets/501a4fb2-da87-45fb-817d-9d9227acf693)

Detailed explaination can be found in report.


#### 6. **Feedback System**
- Provides **instant correction suggestions** based on detected posture deviations, highlighting areas that need adjustment.
- Uses **reinforcement learning techniques** to refine posture detection and feedback accuracy over time.
- Implements **audio-visual guidance** for users, enabling interactive engagement and self-improvement in workout form.
  
![image](https://github.com/user-attachments/assets/d2506160-fdff-4fe7-b7aa-c92c48372d1e)
![image](https://github.com/user-attachments/assets/bdd9cfb1-ba4b-4b69-b61d-faac82cc6378)


### B. PERSONALIZED EXERCISE PLANS GENERATOR

- A **machine learning-based recommendation system** tailors exercise plans to individual users based on fitness levels, goals, and posture performance.
- The system dynamically **adjusts difficulty and exercises** based on user progress and real-time posture feedback.
  ![image](https://github.com/user-attachments/assets/fd07832b-a543-47a6-b76f-79401dafac3d)
  ![image](https://github.com/user-attachments/assets/1b5d968d-cc1c-473a-a18f-68bc676607a0)

- Uses **Large Language Models (LLM)** to generate structured weekly fitness programs incorporating user preferences and past performance data.
  Expected outcome:
  ![image](https://github.com/user-attachments/assets/4415d791-3b34-42a8-911c-7d8ecceff262)
  ![image](https://github.com/user-attachments/assets/717f2e25-4095-40ce-b033-3a53d002da36)

  Calendar view:
  ![image](https://github.com/user-attachments/assets/192fb815-620b-4ed8-86ab-e3894f21336a)

  List view:
  ![image](https://github.com/user-attachments/assets/9b02434c-774d-4cf1-b29d-64cdaf24114e)



### C. FRONT-END OF THE WEB APP
- Homepage
  ![image](https://github.com/user-attachments/assets/1147cfc5-921e-40a8-82d3-71dd3acbfec1)

- Sample Exercise
  ![image](https://github.com/user-attachments/assets/6c6a59b6-7e21-4f7e-8279-2602d7108c17)


## Expected Outcomes
- Reduce injury risks caused by improper exercise posture.
- Improve workout efficiency with real-time AI feedback.
- Enable users to follow structured, personalized fitness plans.

## How to Use This Repository
1. **Clone the repository:**
   ```sh
   git clone https://github.com/thaochu05/AI-Personal-Trainer.git 
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```sh
   streamlit run <Homepage.py>
   ```
4. **Follow the on-screen instructions to analyze your posture and get personalized workout recommendations.**

## Future Enhancements
- Implement AI-based voice coaching for real-time workout guidance.
- Expand the dataset to improve posture recognition accuracy.
- Develop a mobile app for easy accessibility.

---
### The team
@thaochu05
@DucDuyLe




