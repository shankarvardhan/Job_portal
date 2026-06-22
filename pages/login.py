pages/login.py


import streamlit as st
import requests

be_url = "http://127.0.0.1:8000"

st.title("Login")

with st.form("login_form"):

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        ["recruiter", "job_seeker"]
    )

    btn = st.form_submit_button(
        "Login"
    )

    if btn:

        payload = {
            "email": email,
            "password": password,
            "role": role
        }

        res = requests.post(
            f"{be_url}/login",
            json=payload
        )

        data = res.json()

        if data["status"]:

            st.session_state["user"] = data["user_data"]

            if role == "recruiter":
                st.switch_page(
                    "pages/R_dashboard.py"
                )

            else:
                st.switch_page(
                    "pages/J_dashboard.py"
                )

        else:

            st.error(
                data["msg"]
            )
