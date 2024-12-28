from motor.motor_asyncio import AsyncIOMotorClient
client=AsyncIOMotorClient("mongodb://localhost:27017")
db=client.parser# creating db
# creating collections
resume_collection=db.resume
jd_collection=db.jd
matches_collection=db.matches