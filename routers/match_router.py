from fastapi import APIRouter
from llm import get_match
from database import jd_collection,resume_collection,matches_collection
from bson import ObjectId
from schemas import MatchRequest,MatchResponse
import re
from fastapi import status
router=APIRouter()
@router.post("/get_match_score")
async def get_match_score(request:MatchRequest):
    try:
        resume_name=str(request.resume_name)
        job_id=str(request.job_id)
        resume= dict(await resume_collection.find_one({'file_name':resume_name}))
        resume_summary=resume['summary']
        job=dict(await jd_collection.find_one({"_id":ObjectId(job_id)}))
        jd=job['job_description']
        response=await get_match(summary=resume_summary,jd_summary=jd)
        score_match = str(re.search(r"Match Score:\s*(\d+)", response))
        lines=response.splitlines()
        score_index = next((i for i, line in enumerate(lines) if "Match Score:" in line), None)
        suggestions = "\n".join(lines[score_index + 1:]).strip()
        match_obj= MatchResponse(resume_name=resume_name,job_id=job_id,suggestions=suggestions,match_score=score_match).dict()
        await matches_collection.insert_one(match_obj)
        return status.HTTP_200_OK
    except Exception as e:
        return {"error":str(e)}
@router.get("/get_match_file/{resume_name}")
async def get_match_file(resume_name:str=""):
    try:
        obj=await matches_collection.find_one({"resume_name":resume_name})
        obj['_id']=str(obj["_id"])
        return obj if obj else status.HTTP_404_NOT_FOUND
    except Exception as e:
        return {"error":str(e)}