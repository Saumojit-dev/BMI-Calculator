import streamlit as st

def BMI_Calculator():
    st.title('BMI Calculator')
    with st.form('BMI Calculator'):
        col1,col2,col3 = st.columns([3,2,1])

    with col1:
        weight = st.number_input('Enter your weight in KGs')

    with col2:
        height = st.number_input('Enter your height in Meters')

    with col3:
        submit = st.form_submit_button('Calculate')

    if submit:
        BMI = round((weight/(height**2)),2)
        if BMI <= 18.5:
            st.error('Underweight')
            st.error(BMI)
        if BMI >18.5 and BMI <=24.9:
            st.success('Healthy/Normal')
            st.success(BMI)
        if BMI >24.9 and BMI <30:
            st.warning('Overweight')
            st.warning(BMI)
        if BMI >=30:
            st.error('Obese')
            st.error(BMI)


choice = st.sidebar.selectbox('Menu',['BMI'])

if choice == 'BMI':
    BMI_Calculator()

