import os
import dotenv
from fastapi import File,UploadFile
from typing import Optional
from fastapi import APIRouter
from fastapi import status
from PyPDF2 import PdfReader
from database import resume_collection,skills_collection
from schemas import Resume
import langchain
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
        print(content,skills)
        obj= await resume_collection.find({"file_name":file.filename}).to_list()
        if not obj:
            obj=Resume(file_name=file.filename,skills=skills).dict()
            await resume_collection.insert_one(obj)
            client.upload_fileobj(file.file,BUCKET_NAME,file.filename)
            return "uploaded Successfully",status.HTTP_201_CREATED
        return {"Message":"This resume is already uploaded","status":status.HTTP_200_OK}
    except Exception as e:
        print(e)
        return {"error":str(e)}
@router.get("/get/{file_name}")
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