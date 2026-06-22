from fastapi import FastAPI
from db_connection import supabase_client_obj

app = FastAPI()


@app.post("/register")
def register_function(payload: dict):

    try:

        existing_user = (
            supabase_client_obj
            .table("users")
            .select("*")
            .eq("email", payload["email"])
            .execute()
        )

        if len(existing_user.data) > 0:
            return {
                "status": False,
                "msg": "Email already registered"
            }

        if payload["password"] != payload["confirm_password"]:
            return {
                "status": False,
                "msg": "Passwords do not match"
            }

        supabase_client_obj.table("users").insert({
            "name": payload["name"],
            "email": payload["email"],
            "password": payload["password"],
            "role": payload["role"]
        }).execute()

        return {
            "status": True,
            "msg": "User Registered Successfully"
        }

    except Exception as e:

        return {
            "status": False,
            "msg": str(e)
        }


@app.post("/login")
def login_function(payload: dict):

    try:

        result = (
            supabase_client_obj
            .table("users")
            .select("*")
            .eq("email", payload["email"])
            .eq("password", payload["password"])
            .eq("role", payload["role"])
            .execute()
        )

        if len(result.data) == 0:
            return {
                "status": False,
                "msg": "Invalid Credentials"
            }

        return {
            "status": True,
            "msg": "Login Successful",
            "user_data": result.data[0]
        }

    except Exception as e:

        return {
            "status": False,
            "msg": str(e)
        }
@app.post("/post-job")
def post_job(payload: dict):

    supabase_client_obj.table("jobs").insert({
        "job_title": payload["job_title"],
        "company_name": payload["company_name"],
        "location": payload["location"],
        "salary": payload["salary"],
        "skills_required": payload["skills_required"],
        "job_description": payload["job_description"],
        "recruiter_email": payload["recruiter_email"]
    }).execute()

    return {
        "status": True,
        "msg": "Job Posted Successfully"
    }

@app.get("/jobs")
def get_jobs():

    jobs = (
        supabase_client_obj
        .table("jobs")
        .select("*")
        .execute()
    )

    return {
        "status": True,
        "jobs": jobs.data
    }

@app.post("/apply-job")
def apply_job(payload: dict):

    supabase_client_obj.table(
        "job_applications"
    ).insert({
        "job_id": payload["job_id"],
        "applicant_name": payload["applicant_name"],
        "applicant_email": payload["applicant_email"],
        "resume_link": payload["resume_link"],
        "cover_letter": payload["cover_letter"]
    }).execute()

    return {
        "status": True,
        "msg": "Application Submitted"
    }