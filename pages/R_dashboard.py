import streamlit as st
import requests

be_url = "http://127.0.0.1:8000"

st.title("Recruiter Dashboard")

st.subheader("Post New Job")

with st.form("job_form"):

    title = st.text_input("Job Title")

    company = st.text_input(
        "Company Name"
    )

    location = st.text_input(
        "Location"
    )

    salary = st.text_input(
        "Salary"
    )

    skills = st.text_area(
        "Skills Required"
    )

    description = st.text_area(
        "Job Description"
    )

    btn = st.form_submit_button(
        "Post Job"
    )

    if btn:

        payload = {

            "job_title": title,
            "company_name": company,
            "location": location,
            "salary": salary,
            "skills_required": skills,
            "job_description": description,
            "recruiter_email":
            st.session_state["user"]["email"]
        }

        res = requests.post(
            f"{be_url}/post-job",
            json=payload
        )

        st.success(
            res.json()["msg"]
        )