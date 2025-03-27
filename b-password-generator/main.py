import streamlit as st
import random
import string

def generate_password(Length, use_digits, use_special):
    characters =string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(Length))

st.title("Password Genrator")

length = st.slider("Select password length",min_value=6, max_value=32, value=12 )

use_digits = st.checkbox("iclude digits")

use_special = st.checkbox("include special cheracters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: {password}")

st.write("--------------------")

st.write("Build with by [safi Ullah](https://github.com)")