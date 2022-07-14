import os
import shutil
import time
import subprocess
from filetype_config import filetype_conf
from fastapi import FastAPI,UploadFile,File,Request,Depends
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dbsession import get_session
from datetime import date
from filepath import date_path_check
from hashlib import blake2b
from files import models
from files.schemas import FileSave
from sqlalchemy.orm import Session

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    rc = subprocess.Popen(["sh", "run.sh"])

@app.get('/upload/{eventid}',response_class=HTMLResponse)
async def upload(eventid: str, request: Request):
    return templates.TemplateResponse('index.html',{'request': request, 'eventid': eventid})


@app.post('/uploadform/{eventid}', response_class=HTMLResponse)
async def uploadform(eventid:str, request: Request, file: UploadFile = File(...), db: Session = Depends(get_session)): 
    filePath, isdir = date_path_check()
    
    if not isdir:
        os.mkdir(filePath)

    try:
        timeStamp = str(time.time()).encode('utf-8')
        hash = blake2b(key=timeStamp, digest_size=10)
        file.filename = hash.hexdigest()

        with open(os.path.join(filePath, f'{file.filename}.{filetype_conf[file.content_type]}'), 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)

        linktoDownload = f'localhost:8000/download/{file.filename}.{filetype_conf[file.content_type]}'

        #Write to database

        dateAdd = models.FileSave(eventid=eventid, filename=file.filename, link=linktoDownload)
        db.add(dateAdd)
        db.commit()


        

    finally:
        file.file.close()
    
    return templates.TemplateResponse('link.html',{'request': request, 'downloadlink': linktoDownload})


@app.get('/download/{fileName}')
async def download(fileName: str):
    filePath, isdir = date_path_check()
    return FileResponse(os.path.join(filePath, fileName))


@app.get('/link/{eventid}', response_model=FileSave)
async def link(eventid:str, db: Session = Depends(get_session)):
    try:
        linkDownload = db.query(models.FileSave).filter(models.FileSave.eventid == eventid).first()

        return linkDownload

    except:
        print("Empty")