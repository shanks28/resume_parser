from fastapi import APIRouter
from database import db,jd_collection
from schemas import JD
from typing import List
from fastapi import status
from bson import ObjectId

router=APIRouter()

@router.post("/job_description",response_model=dict)
async def create_job_description(job_descriptions: List[JD]):
    try:
        data=[dict(job) for job in job_descriptions]
        response=await jd_collection.insert_many(data)
        return {"id":[str(ids) for ids in response.inserted_ids],
                "status_code":status.HTTP_201_CREATED}
    except Exception as e:
        return {"error":str(e)}
@router.get("/job_description")
async def get_job_description():
    try:
        data=await jd_collection.find().to_list()
        for job in data:
            job['_id']=str(job["_id"])
        print(data)
        response={"ids":[job['_id'] for job in data]}
        return response
    except Exception as e:
        return {"error":str(e)}
@router.get("/job_description/{id}")
async def get_job(id:str):
    try:
        job=await jd_collection.find_one({"_id":ObjectId(id)})
        if not job:
            return {"message":"No such Job","status":status.HTTP_404_NOT_FOUND}
        job['_id']=str(job["_id"])
        return job
    except Exception as e:
        return {"error":str(e)}