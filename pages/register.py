import streamlit as st
import requests

be_url = "http://127.0.0.1:8000"

st.title("Register")

with st.form("register_form"):

    name = st.text_input("Name")
    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        ["recruiter", "job_seeker"]
    )

    btn = st.form_submit_button(
        "Register"
    )

    if btn:

        payload = {
            "name": name,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
            "role": role
        }

        res = requests.post(
            f"{be_url}/register",
            json=payload
        )

        st.write(res.json())
