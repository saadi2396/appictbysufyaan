import streamlit as st

st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

st.title("Mechanical Unit Converter and Material Density Checker")

st.subheader("Student Information")
st.write("*Name:* Sufyan Mehmood")
st.write("*Roll Number:* 24-ME-123")

st.divider()

st.header("1. Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Mass", "Force", "Pressure"]
)

value = st.number_input("Enter Value", value=1.0)

if conversion_type == "Length":

    unit = st.selectbox(
        "Convert From",
        ["meter to millimeter", "millimeter to meter", "meter to feet"]
    )

    if unit == "meter to millimeter":
        result = value * 1000
        st.success(f"{value} m = {result} mm")

    elif unit == "millimeter to meter":
        result = value / 1000
        st.success(f"{value} mm = {result} m")

    else:
        result = value * 3.28084
        st.success(f"{value} m = {result:.3f} ft")

elif conversion_type == "Mass":

    unit = st.selectbox(
        "Convert From",
        ["kg to gram", "gram to kg"]
    )

    if unit == "kg to gram":
        result = value * 1000
        st.success(f"{value} kg = {result} g")

    else:
        result = value / 1000
        st.success(f"{value} g = {result} kg")

elif conversion_type == "Force":

    unit = st.selectbox(
        "Convert From",
        ["Newton to kiloNewton", "kiloNewton to Newton"]
    )

    if unit == "Newton to kiloNewton":
        result = value / 1000
        st.success(f"{value} N = {result} kN")

    else:
        result = value * 1000
        st.success(f"{value} kN = {result} N")

elif conversion_type == "Pressure":

    unit = st.selectbox(
        "Convert From",
        ["Pascal to kPa", "kPa to Pascal", "bar to Pascal"]
    )

    if unit == "Pascal to kPa":
        result = value / 1000
        st.success(f"{value} Pa = {result} kPa")

    elif unit == "kPa to Pascal":
        result = value * 1000
        st.success(f"{value} kPa = {result} Pa")

    else:
        result = value * 100000
        st.success(f"{value} bar = {result} Pa")

st.divider()

st.header("2. Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminium": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Cast Iron": 7200,
    "Water": 1000
}

material = st.selectbox(
    "Select Material",
    list(materials.keys())
)

density = materials[material]

st.info(f"The density of {material} is {density} kg/m³")

st.write("This app is developed for mechanical engineering unit conversion and material density checking.")
