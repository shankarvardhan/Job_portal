import streamlit as st
import requests

be_url = "http://127.0.0.1:8000"

st.title("Job Seeker Dashboard")

jobs = requests.get(
    f"{be_url}/jobs"
).json()

for job in jobs["jobs"]:

    with st.expander(
        f"{job['job_title']} - {job['company_name']}"
    ):

        st.write(
            f"Location: {job['location']}"
        )

        st.write(
            f"Salary: {job['salary']}"
        )

        st.write(
            f"Skills: {job['skills_required']}"
        )

        st.write(
            job['job_description']
        )

        with st.form(
            f"apply_{job['job_id']}"
        ):

            resume = st.text_input(
                "Resume Link"
            )

            cover = st.text_area(
                "Cover Letter"
            )

            btn = st.form_submit_button(
                "Apply"
            )

            if btn:

                payload = {

                    "job_id":
                    job["job_id"],

                    "applicant_name":
                    st.session_state["user"]["name"],

                    "applicant_email":
                    st.session_state["user"]["email"],

                    "resume_link":
                    resume,

                    "cover_letter":
                    cover
                }

                res = requests.post(
                    f"{be_url}/apply-job",
                    json=payload
                )

                st.success(
                    res.json()["msg"]
                )