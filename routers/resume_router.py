import os
import dotenv
from fastapi import File,UploadFile
from typing import Optional
from fastapi import APIRouter
from fastapi import status
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
async def upload_resume(file: UploadFile=File(...),candidate_name:Optional[str]=None):
    try:
        client.upload_fileobj(file.file,BUCKET_NAME,file.filename)
        return "uploaded Successfully",status.HTTP_201_CREATED
    except Exception as e:
        return {"error":str(e)}