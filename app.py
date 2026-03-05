import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="centered"
)

# -------------------------------
# Load Trained Model
# -------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("model/insurance_model.pkl")
    return model

model = load_model()

# -------------------------------
# App Title
# -------------------------------
st.title("💰 Medical Insurance Cost Prediction")
st.write("Predict insurance charges using a trained Machine Learning model.")

st.markdown("---")

# -------------------------------
# User Input Section
# -------------------------------
st.header("Enter Customer Details")

age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Insurance Charges"):

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    prediction = model.predict(input_data)[0]

    st.markdown("---")
    st.subheader("💵 Predicted Insurance Charges")
    st.success(f"${prediction:,.2f}")

    if smoker == "yes":
        st.warning("Smoking significantly increases insurance costs.")
    else:
        st.info("Non-smokers typically have lower insurance costs.")

st.markdown("---")

# -------------------------------
# Author Section
# -------------------------------
st.markdown("""
### 👨‍💻 Author  
**Md. Nazmul Hossain**

🔗 GitHub: https://github.com/nazmul-1117  
🔗 LinkedIn: https://linkedin.com/in/yourprofile  
🌐 Portfolio: https://nazmul-1117.github.io
""")

st.markdown("---")

# -------------------------------
# Footer
# -------------------------------
st.write("Md. Nazmul Hossain © 2026")