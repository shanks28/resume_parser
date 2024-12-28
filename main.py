import fastapi
from fastapi.routing import APIRouter
from routers import Job_Description
app=fastapi.FastAPI(title="Resume parsing Application",
                    version="1.0.0",)
app.include_router(Job_Description.router,prefix="/jd")
@app.get("/")
async def hello():
    return "Hello World"