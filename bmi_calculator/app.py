import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Input fields for weight and height
weight = st.number_input("Enter your weight (in kg)", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (in meters)", min_value=0.0, format="%.2f")

# Calculate BMI
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI Categories
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid weight and height values.")