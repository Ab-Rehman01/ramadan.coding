import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")
def generate_money():
    return random.randint(1, 1000)
st.subheader("inatNT Cash generator")

if st.button("Generate Money"):
    st.write("counting money...")
    time.sleep(5)
    amount = generate_money()
    st.success(f"You have earned ${generate_money()} inatNT cash!")
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side-hustle")
        if response.status_code == 200:
            hustles = response.json()
            return hustles
        else:
            return []
    except Exception as e:
        st.error(f"Error fetching side hustles: {e}")
        return []
    else:
        return ("something went wrong!")
st.subheader("side hustle ideas") 
if st.button("Generate hustle"):
      idea=fetch_side_hustle()
      st.success(idea)



