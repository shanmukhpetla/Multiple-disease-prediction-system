import pickle
#import joblib
import streamlit as st
from streamlit_option_menu import option_menu
#from streamlit_option_menu import option_menu

heart_path = "C:/Users/SethuMadhav/Desktop/Multiple Disease Prediction/Saved Models/heart_disease_model.sav"
diabetes_path = "C:/Users/SethuMadhav/Desktop/Multiple Disease Prediction/Saved Models/diabetes_model.sav"
# Loading the Saved Models

heart_disease_model = pickle.load(open(heart_path, 'rb'))

diabetes_model = pickle.load(open(diabetes_path, 'rb'))



# Display the title of the application

st.set_page_config(page_title="Multiple Disease Prediction System", initial_sidebar_state="collapsed")

st.title('Multiple Disease Prediction System With Help Of Machine Learning')


# Add some description or additional text about the application
#st.write("""
#    <h5>Welcome to the Multiple Disease Prediction System! This application allows users to predict the 
#   likelihood of heart disease and diabetes based on various health factors. 
#    Please use the sidebar to select the prediction system you'd like to use.</h5>
#    """, unsafe_allow_html=True)

    
st.write("""
         
         
         
         
         
         
         """)

# Sidebar for Navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           [    'Select an Option',
                               'Heart Disease Prediction',
                               'Diabetes Prediction',
                            ],
                           
                           icons = ['house', 'heart', 'activity'],
                           default_index=0)

if (selected == 'Select an Option'):
    
    st.write("<h4>Welcome to the Multiple Disease Prediction System!</h4>", unsafe_allow_html=True)
    st.write("""
             
             
             
             
             
             
             """)
             
    st.write("""
        <h5>This application allows users to predict the 
        likelihood of heart disease and diabetes based on
        various health factors. </h5>
        """, unsafe_allow_html=True)
        
    st.write("""
             
             
             
             
             """)
             
    st.write("<h5> Please use the sidebar to select the prediction system you'd like to use.</h5>",
             unsafe_allow_html=True)
        


        
# ----------- Heart Disease Prediction Page ------------

if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction Using ML')


    # Getting input data from user
    # columns for input fields
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain Types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestorol in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
    
    # Prediction
    heart_diagnosis = ''
    
    
    # Creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    


    
#----------------------- Diabetes Prediction Page --------------------

if (selected == 'Diabetes Prediction'):
    
    # Page title
    st.title('Diabetes Prediction Using ML')
    
    
    # Getting the input data from the user
    # Columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age = st.text_input('Age of The Person')
    

    
    
    # Prediction
    diab_diagnosis = ''
    
    # Button for Prediction
    
    if st.button('Diabetes Test Result'):
        
        
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]
        
        diab_prediction = diabetes_model.predict([user_input])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The Person is Diabetic'
            
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
            
    st.success(diab_diagnosis)


