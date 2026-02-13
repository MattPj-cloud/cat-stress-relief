import streamlit as st
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

st.title("🐱 Feline Fine")

stress_level = st.slider("Stress Level", 1, 10, 5)

if st.button("Get My Cat Therapist"):
    response = requests.get("https://api.thecatapi.com/v1/images/search", verify=False)
    cat_url = response.json()[0]["url"]
    
    st.image(cat_url, width=400)
    
    if stress_level > 7:
        st.success("🎩 Meet your new Senior Stress Consultant!")
    else:
        messages = [
            "This cat believes in you!",
            "Purr-fect timing for a break!",
            "Your personal therapy cat has arrived!",
            "This cat says: You got this!"
        ]
        import random
        st.info(random.choice(messages))
