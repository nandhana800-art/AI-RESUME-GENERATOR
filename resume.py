from fastapi import APIRouter
from pydantic import BaseModel
from groq_service import generate_resume

router = APIRouter()

class ResumeRequest(BaseModel):
    name: str
    email: str
    phone: str
    skills: str
    experience: str
    education: str
    projects: str
    job_role: str

@router.post("/generate-resume")
def create_resume(req: ResumeRequest):

    prompt = f"""
Create a professional ATS-friendly resume using the following details:

Name: {req.name}
Email: {req.email}
Phone: {req.phone}
Skills: {req.skills}
Experience: {req.experience}
Education: {req.education}
Projects: {req.projects}
Target Job Role: {req.job_role}

Format it properly with sections, bullet points, and professional structure.
"""

    result = generate_resume(prompt)
    return {"data": result}