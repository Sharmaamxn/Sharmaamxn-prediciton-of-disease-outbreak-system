import os   #interact with operating system
import pickle    #The pickle module in Python is used for serializing (saving) and deserializing (loading) objects. It converts Python objects into a byte stream that can be stored or sent, and later restored back to the original object.
import streamlit as st    #Streamlit is a Python library used to create interactive web apps for machine learning and data visualization quickly and easily
from streamlit_option_menu import option_menu    #to create option menu


#page modification
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="👨🏽‍⚕️")

#importing model
diabetes_model= pickle.load(open(r"D:\Programming\Project\Predictions\training_models\diabetes_model.sav",'rb'))
heart_model= pickle.load(open(r"D:\Programming\Project\Predictions\training_models\heart_model.sav",'rb'))
parkinsons_model= pickle.load(open(r"D:\Programming\Project\Predictions\training_models\parkinsons_model.sav",'rb'))

#designing sidebar menu
with st.sidebar:
    selected = option_menu("Prediction of Disease Outbreak System", ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"], 
        menu_icon='hospital-fill', icons=['activity', 'heart','person'], default_index=0)

#sidebar input handling of "Diabetes Prediction"
if selected == "Diabetes Prediction": 

    #designing "Diabetes" interface    
    st.title("Diabetes Prediction Using ML")

    #input columns for different details on main interface of "Diabetes Prediction"
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    with col2:
        Age = st.text_input("Age of The Person")

#Diabetes Prediction
    diab_diagnosis = ''   #This initializes an empty string variable diab_diagnosis to store the prediction result
    if st.button('Diabetes Test Result'):    #This creates a button labeled "Diabetes Test Result" in the Streamlit app, When the user clicks this button, the code inside the if block runs
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,   #This collects input features related to diabetes in form of list
                    BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]    #Converts all inputs to floating-point numbers, ensuring they are in the correct format for model prediction

        #The diabetes_model.predict([user_input]) function uses a pre-trained machine learning model (e.g., Logistic Regression, Random Forest, or SVM) to make a prediction. the user_input (a list of medical values) is wrapped in another list ([user_input]) because the model expects a 2D array for prediction
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:  #1 - diabetes / 0 - no diabetes
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
            
        st.success(diab_diagnosis) #Displays the final prediction message (diab_diagnosis) in a green success message box in Streamlit.

    
#sidebar input handling of "Heart Disease Prediction"
if selected == "Heart Disease Prediction": 

    #designing "Heart Disease" interface    
    st.title("Heart Disease Prediction Using ML")

    #input columns for different details on main interface of "Heart Disease Prediction"
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age of The Person")
    with col2:
        sex = st.text_input("Gender of the person (1 = Male, 0 = Female)")
    with col3:
        cp = st.text_input("Chest Pain Type")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholesterol")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic Results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate")
    with col3:
        exang = st.text_input("Exercise-Induced Angina")
    with col1:
        oldpeak = st.text_input("ST Depression Induced")
    with col2:
        slope = st.text_input("Slope of the Peak Exercise ST Segment")
    with col3:
        ca = st.text_input("Major Vessels Colored by Fluoroscopy")
    with col1:
        thal = st.text_input("Thalassemia")


#Heart Disease Prediction
    heart_disease_diagnosis = ''   #This initializes an empty string variable heart_disease_diagnosis to store the prediction result
    if st.button('Heart Disease Test Result'):    #This creates a button labeled "Heart Disease Test Result" in the Streamlit app, When the user clicks this button, the code inside the if block runs
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

        user_input = [float(x) for x in user_input]    #Converts all inputs to floating-point numbers, ensuring they are in the correct format for model prediction

        #The heart_model.predict([user_input]) function uses a pre-trained machine learning model (e.g., Logistic Regression, Random Forest, or SVM) to make a prediction. the user_input (a list of medical values) is wrapped in another list ([user_input]) because the model expects a 2D array for prediction
        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0] == 1:  #1 - heart disease / 0 - no heart disease
            heart_disease_diagnosis = 'The person is diagnosed with heart disease'
        else:
            heart_disease_diagnosis = 'The person is not diagnosed with heart disease'
            
        st.success(heart_disease_diagnosis) #Displays the final prediction message (heart_disease_diagnosis) in a green success message box in Streamlit.    


#sidebar input handling of "Heart Disease Prediction"
if selected == "Parkinsons Prediction": 

    #des

    st.title("Parkinson's Disease Prediction")

    # Frequency Measures
    st.subheader("Frequency Measures")
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo_Hz = st.text_input("Fundamental Frequency (Fo) in Hz")
        MDVP_Jitter_Abs = st.text_input("Absolute Jitter (in seconds)")
        MDVP_Shimmer = st.text_input("Amplitude Variation (%)")
    with col2:
        MDVP_Fhi_Hz = st.text_input("Maximum Fundamental Frequency (Hz)")
        MDVP_RAP = st.text_input("Relative Average Perturbation (RAP)")
        MDVP_Shimmer_dB = st.text_input("Amplitude Variation (dB)")
    with col3:
        MDVP_Flo_Hz = st.text_input("Minimum Fundamental Frequency (Hz)")
        MDVP_PPQ = st.text_input("Pitch Period Perturbation Quotient (PPQ)")
        Shimmer_APQ3 = st.text_input("Amplitude Perturbation Quotient (APQ3)")

    st.write("") # blank spaaces
    st.write("")

    # Jitter Measures
    st.subheader("Jitter Measures (Frequency Variability)")
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Jitter_per = st.text_input("Jitter (%)")
    with col2:
        Jitter_DDP = st.text_input("Average Difference of Jitter Cycles (DDP)")
    with col3:
        Shimmer_APQ5 = st.text_input("Amplitude Perturbation Quotient (APQ5)")

    st.write("") # blank spaaces
    st.write("")
    

    # Shimmer Measures
    st.subheader("Shimmer Measures (Amplitude Variability)")
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_APQ = st.text_input("Average Amplitude Perturbation Quotient (APQ)")
    with col2:
        Shimmer_DDA = st.text_input("Difference of Amplitude Differences (DDA)")
    with col3:
        NHR = st.text_input("Noise-to-Harmonics Ratio (NHR)")

    # Harmonic-to-Noise Ratio
    with col1:
        HNR = st.text_input("Harmonics-to-Noise Ratio (HNR)")

    st.write("") # blank spaaces
    st.write("")

    # Nonlinear Dynamical Complexity Measures
    st.subheader("Nonlinear Dynamical Complexity Measures")
    col1, col2, col3 = st.columns(3)
    with col1: 
        RPDE = st.text_input("Recurrence Period Density Entropy (RPDE)")
    with col2:
        DFA = st.text_input("Detrended Fluctuation Analysis (DFA)")
    with col3:
        spread1 = st.text_input("Nonlinear Measure of Voice Deviation (Spread1)")

    col1, col2, col3 = st.columns(3)
    with col1:
        spread2 = st.text_input("Additional Nonlinear Voice Deviation Measure (Spread2)")
    with col2:
        D2 = st.text_input("Correlation Dimension (D2)")
    with col3:
        PPE = st.text_input("Pitch Period Entropy (PPE)")

#Heart Disease Prediction
    parkinsons_diagnosis = ''   #This initializes an empty string variable heart_disease_diagnosis to store the prediction result
    if st.button('Parkinsons Test Result'):    #This creates a button labeled "Heart Disease Test Result" in the Streamlit app, When the user clicks this button, the code inside the if block runs
        user_input = [MDVP_Fo_Hz,MDVP_Fhi_Hz,MDVP_Flo_Hz,MDVP_Jitter_per,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]

        user_input = [float(x) for x in user_input]    #Converts all inputs to floating-point numbers, ensuring they are in the correct format for model predictionS

        #The heart_model.predict([user_input]) function uses a pre-trained machine learning model (e.g., Logistic Regression, Random Forest, or SVM) to make a prediction. the user_input (a list of medical values) is wrapped in another list ([user_input]) because the model expects a 2D array for prediction
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:  #1 - heart disease / 0 - no heart disease
            parkinsons_diagnosis = 'The person is diagnosed with Parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person is not diagnosed with Parkinsons disease'
            
        st.success(parkinsons_diagnosis) #Displays the final prediction message (heart_disease_diagnosis) in a green success message box in Streamlit.    






            
        