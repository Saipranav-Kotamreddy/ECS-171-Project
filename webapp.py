import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

tab_model, tab_figures = st.tabs(["Model", "Figures"])

with tab_model:
    html_temp = """
                <div style="background-color:teal ;padding:0px">
                <h2 style="color:white;text-align:center;">Heart Disease Predictor</h2>
                <h5 style="color:white;text-align:center;">A Linearly Regressive ML Model</h5>
                </div>
                """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.divider()

    st.markdown("<h5 style='text-align: center; color: teal;'>General Attributes</h5>", unsafe_allow_html=True)
    col11, col12 = st.columns(2)
    with col11:
        age = st.number_input('Age', min_value=0, max_value=125, value=25, step=1)
    with col12:
        sex = 1 if st.selectbox('Biological Sex', ['Male', 'Female']) == 'Male' else 0
        
    st.divider()
    st.markdown("<h5 style='text-align: center; color: teal;'>Pain Related Attributes</h5>", unsafe_allow_html=True)

    col21, col22 = st.columns(2)
    with col21:
        cp_select = ["1: Typical Angina", "2: Atypical Angina", "3: Non-Anginal Pain", "4: Asymptomatic"]
        cp = int(st.selectbox("Chest Pain (Angina)", cp_select)[0])

    with col22:
        exang = 1 if st.selectbox('Exercise Induced Angina', ['Present', 'Not Present']) == 'Present' else 0

    st.divider()
    st.markdown("<h5 style='text-align: center; color: teal;'>Blood Related Attributes</h5>", unsafe_allow_html=True)

    col31, col32, col33 = st.columns(3)
    with col31:
        restbps = st.number_input('Resting Bloodpressure (mmHg)', min_value=40, max_value=200, step=1)
    with col32:
        chol = st.number_input('Cholesterol (mg/dL)', min_value=25, max_value=300, step=1)
    with col33:
        fbs = st.number_input('Fasting Blood Sugar (mg/dL)', min_value=25, max_value=200, step=1)
        
    st.divider()
    st.markdown("<h5 style='text-align: center; color: teal;'>Other Attributes</h5>", unsafe_allow_html=True)

    col41, col42, col43 = st.columns(3)
    with col41:    
        oldpeak = st.number_input('ST-segment Depression', min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
        
        slope_select = ["1: Upsloping", "2: Flat", "3: Downsloping"]
        slope = int(st.selectbox('ST-segment Slope', slope_select)[0])

                
    with col42:
        thalach = st.number_input('Maximum Heartrate', min_value=30, max_value=200, step=1)
        
        restecg_select = ["0: Normal", "1: ST-T Abnormalities", "2: Probable Hypertrophy"]
        restecg = int(st.selectbox('Resting Electrocardiograph', restecg_select)[0])  
        
    with col43:
        ca = st.number_input('Coronary Arteries', min_value=0, max_value=3, step=1)
        
        thal_select = ["3: Normal", "6: Fixed Defect", "7: Reversable Defect"]
        thal = int(st.selectbox('Thalassemia', thal_select)[0])


    st.divider()

    result = '0.00'
    result = model.predict([[age, sex, cp, restbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    result = round(result[0], 2)

    st.info(f"Heart Disease Risk: {result}")    
    st.divider()
    
with tab_figures:
    st.markdown("TODO")