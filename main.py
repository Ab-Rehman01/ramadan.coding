import streamlit as st
def convert_units(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer":0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000
    
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions [key]
        return value * conversion
    else:
        return "Conversion not supported"
st.title("Unit Converter")
value = st.number_input(" enter a value:")
unit_from = st.selectbox("convert from:", ["meter", "kilometer","gram","Kilogram"])

unit_to =st.selectbox("Convert to:", ["meter","kiometer", "gram","kilogram"])
if st.button("Convert"):
    result = convert_units(value,unit_from, unit_to)
    st.write(f"Converted value: {result} ")


