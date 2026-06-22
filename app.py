import streamlit as st
import requests

be_url = "http://127.0.0.1:8000"

st.set_page_config(page_title="Job Portal")

# -----------------------------
# Session State Initialization
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "user_name" not in st.session_state:
    st.session_state.user_name = None

# -----------------------------
# Recruiter Dashboard
# -----------------------------

if st.session_state.logged_in and st.session_state.role == "recruiter":

    st.title("Recruiter Dashboard")

    st.success(
        f"Welcome Recruiter : {st.session_state.user_name}"
    )

    st.subheader("Recruiter Actions")

    st.button("Post New Job")
    st.button("View Applicants")
    st.button("Manage Jobs")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.user_name = None
        st.rerun()

# -----------------------------
# Job Seeker Dashboard
# -----------------------------

elif st.session_state.logged_in and st.session_state.role == "job_seeker":

    st.title("Job Seeker Dashboard")

    st.success(
        f"Welcome Job Seeker : {st.session_state.user_name}"
    )

    st.subheader("Job Seeker Actions")

    st.button("Search Jobs")
    st.button("Apply for Jobs")
    st.button("View Applied Jobs")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.user_name = None
        st.rerun()

# -----------------------------
# Login/Register Page
# -----------------------------

else:

    st.title("Job Portal")

    tab1, tab2 = st.tabs(
        ["Register", "Login"]
    )

    # ==========================
    # Register
    # ==========================

    with tab1:

        st.subheader("Register Form")

        with st.form("Register Form"):

            n = st.text_input("Name")

            p = st.text_input(
                "Password",
                type="password"
            )

            c_p = st.text_input(
                "Confirm Password",
                type="password"
            )

            e = st.text_input("Email")

            r = st.selectbox(
                "Choose Role",
                ["recruiter", "job_seeker"]
            )

            r_sub_btn = st.form_submit_button(
                "Register"
            )

            if r_sub_btn:

                payload = {
                    "name": n,
                    "password": p,
                    "confirm_password": c_p,
                    "email": e,
                    "role": r
                }

                res = requests.post(
                    f"{be_url}/register",
                    json=payload
                )

                data = res.json()

                if data["status"]:
                    st.success(data["msg"])
                else:
                    st.error(data["msg"])

    # ==========================
    # Login
    # ==========================

    with tab2:

        st.subheader("Login Form")

        with st.form("Login Form"):

            e = st.text_input("Email")

            p = st.text_input(
                "Password",
                type="password"
            )

            r = st.selectbox(
                "Choose Role",
                ["recruiter", "job_seeker"]
            )

            l_sub_btn = st.form_submit_button(
                "Login"
            )

            if l_sub_btn:

                payload = {
                    "email": e,
                    "password": p,
                    "role": r
                }

                res = requests.post(
                    f"{be_url}/login",
                    json=payload
                )

                data = res.json()

                if data["role"]:

                    st.session_state.logged_in = True
                    st.session_state.role = data["user_data"]["role"]
                    st.session_state.user_name = data["user_data"]["name"]

                    st.rerun()

                else:

                    st.error(data["msg"])