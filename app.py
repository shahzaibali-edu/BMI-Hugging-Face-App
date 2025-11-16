import streamlit as st

st.title("Simple BMI Calculator")

# Input fields
weight = st.number_input("Enter Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter Height (meters)", min_value=0.1, step=0.01)

# Calculate button
if st.button("Calculate BMI"):
    # Calculation
    bmi = weight / (height ** 2)
    
    # Display BMI
    st.metric(label="Your BMI", value=f"{bmi:.2f}")
    
    # Logic for status
    if bmi < 18.5:
        st.warning("Status: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Status: Normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("Status: Overweight")
    else:
        st.error("Status: Obesity")
