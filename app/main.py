from fastapi import FastAPI, Query, HTTPException, File, UploadFile, Request, Response, Body, Form
from typing import Annotated
import json
import requests
from keras.models import load_model
from PIL import Image
import io
from io import BytesIO
from fastapi.templating import Jinja2Templates
from app.config import *
from app import utils
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Animal(BaseModel):
    species: str | None
    

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(DB_PATH_ORIGIN + file.filename, "wb") as f:
            
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file" + DB_PATH_ORIGIN + file.filename}
    finally:
        file.file.close()
        
    return {"message": f"Successfuly uploaded {file.filename}"}

@app.post("/api/detectUpload", response_model=Animal)
async def detect(file: UploadFile | None = File(...)):
    try:
        image = Image.open(io.BytesIO(file.file.read()))
        species = utils.predict(image)
        print("####",species)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
    return {"species": species}

@app.post("/api/detectURL")
async def detect_url(url: str | None =  Form(...)):
    # Fetch the image data from the URL
    try:
        image_data = requests.get(url).content
        image = Image.open(BytesIO(image_data))
        species = utils.predict(image)
        print("####",species)
    except Exception:
        return {"message": "There was an error uploading the file"}
        
    return {"species": f"{species}"}






