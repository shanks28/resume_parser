import os
import dotenv
from fastapi import File,UploadFile
from typing import Optional
from fastapi import APIRouter
from fastapi import status
from PyPDF2 import PdfReader
from database import resume_collection,skills_collection
from llm import generate_summary
from schemas import Resume
import boto3
router=APIRouter()
dotenv.load_dotenv()
ACCESS_KEY=os.getenv("access_key")
SECRET_KEY=os.getenv("secret_key")
BUCKET_NAME=os.getenv("bucket_name")
client=boto3.client(
    "s3",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="ap-south-1")
@router.post("/up")
async def upload_resume(file: UploadFile=File(...),candidate_name: Optional[str] = None):
    try:
        reader=PdfReader(file.file)
        content=""
        for i in reader.pages:
            content+=i.extract_text()
        predefined_skills = await skills_collection.find().to_list()
        predefined_skills = predefined_skills[0]['skills']
        skills=[i for i in predefined_skills if i in content]
        obj= await resume_collection.find({"file_name":file.filename}).to_list()
        if not obj:
            summary=await generate_summary(content,skills)
            obj=Resume(file_name=file.filename,skills=skills,summary=summary).dict()
            await resume_collection.insert_one(obj)
            client.upload_fileobj(file.file,BUCKET_NAME,file.filename)
            return "uploaded Successfully",status.HTTP_201_CREATED
        return {"Message":"This resume is already uploaded","status":status.HTTP_200_OK}
    except Exception as e:
        print(e)
        return {"error":str(e)}
@router.get("/get_file/{file_name}")
async def fetch_resume(file_name:str):
    try:
        url=client.generate_presigned_url(
            "get_object",
            Params={"Bucket":BUCKET_NAME,"Key":file_name},
            ExpiresIn=6900
        )
        return url
    except Exception as e:
        return {"error":str(e)}
@router.get("/all_resume")
async def all_resume():
    try:
        resumes=[]
        response=await resume_collection.find().to_list()
        if response:
            for data in response:
                resumes.append(data['file_name'])
        return {'resumes':resumes,"status":status.HTTP_200_OK}
    except Exception as e:
        return {"error":str(e)}
@router.get("/get/{file_name}")
async def fetch_resume_by_name(file_name:str):
    try:
        obj=await resume_collection.find_one({"file_name":file_name})
        if not obj:
            return {"Message":"No such resume"}
        return obj['summary'],status.HTTP_200_OK
    except Exception as e:
        return {"error":str(e)}
