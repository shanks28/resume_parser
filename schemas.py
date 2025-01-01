from typing import List
from pydantic import BaseModel
from fastapi import File,UploadFile
from typing import Optional
class Resume(BaseModel): # uploaded by user
    file_name: str
    skills: List[str]
    summary: Optional[str]=None
class JD(BaseModel): # posted my companies
    job_title: str
    company:str
    job_description: str
    required_skills: List[str]
class MatchRequest(BaseModel):
    resume_name: str
    job_id: str
class MatchResponse(BaseModel):
    resume_name:str
    job_id:str
    match_score: str
    suggestions: str

