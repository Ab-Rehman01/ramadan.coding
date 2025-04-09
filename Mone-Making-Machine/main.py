import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")
def generate_money():
    return random.randint(1, 100)
st.subheader("inatNT Cash generator")

if st.button("Generate Money"):
    st.write("counting money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You have earned ${generate_money()} inatNT cash!")




