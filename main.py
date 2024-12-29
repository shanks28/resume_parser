import fastapi
from routers import Job_Description,resume_router
app=fastapi.FastAPI(title="Resume parsing Application",
                    version="1.0.0",)
app.include_router(Job_Description.router,prefix="/jd")
app.include_router(resume_router.router,prefix="/resume")
@app.get("/")
async def hello():
    return "Hello World"