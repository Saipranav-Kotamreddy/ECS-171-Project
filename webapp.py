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
        cp = st.number_input('Chest Pain (Angina)', min_value=1, max_value=4, step=1)
        with st.expander("Information"):
            st.caption('''1: Typical Angina 
                        \n2: Atypical Angina
                        \n3: Non-Anginal Pain
                        \n4: Asymptomatic''')
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
        slope = st.number_input('ST-segment Slope', min_value=1, max_value=3, step=1)
        with st.expander("Information"):
            st.caption('''1: Upsloping 
                        \n2: Flat
                        \n3: Downsloping''')
                
    with col42:
        thalach = st.number_input('Maximum Heartrate', min_value=30, max_value=200, step=1)
        restecg = st.number_input('Resting Electrocardiograph', min_value=0, max_value=2, step=1)
        with st.expander("Information"):
            st.caption('''0: Normal 
                        \n1: ST-T Abnormalities
                        \n2: Probable Hypertrophy''')    
        
    with col43:
        ca = st.number_input('Coronary Arteries', min_value=0, max_value=3, step=1)
        thal = st.number_input('Thalassemia', min_value=3, max_value=7, step=1)
        with st.expander("Information"):
            st.caption('''3: Normal 
                        \n6: Fixed Defect
                        \n7: Reversable Defect''')

    st.divider()

    clicked = st.button('Predict', use_container_width=True)

    result = ''
    if clicked:
        result = model.predict([[age, sex, cp, restbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        result = round(result[0], 2)

    st.info(f"Heart Disease Risk: {result}")    
    st.divider()
    
with tab_figures:
    st.markdown("TODO")