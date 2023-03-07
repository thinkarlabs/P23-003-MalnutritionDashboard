import os

import uvicorn
from dotenv import load_dotenv

from fastapi import FastAPI, Request,Form,Depends,Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse


from Backend.routes.routes import user_router

from Backend.routes.routes import ngo_router, aanganwadi_router, child_router,child_malnutrition
from Backend.routes.routes import donor_router

from app.routes import sign_router




# from fastapi.templating import Jinja2Templates

from pymongo import MongoClient

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5173/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(sign_router)
app.include_router(user_router)
app.include_router(ngo_router)
app.include_router(donor_router)
app.include_router(aanganwadi_router)
app.include_router(child_router)
app.include_router(child_malnutrition)

# app_templates = Jinja2Templates(directory="templates")

CONNECTION_STRING = os.getenv('CONNECTION_STRING')
# client = MongoClient(CONNECTION_STRING, serverSelectionTimeoutMS=5000)
# db = client['<DB_NAME']

@app.get("/")
async def index(request: Request):
  return FileResponse('static/index.html')



#if __name__ == "__main__":
    #uvicorn.run(app, host="127.0.0.1", port=7000)


