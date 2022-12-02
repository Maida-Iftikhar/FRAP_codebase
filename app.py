from fastapi import FastAPI ,Request ,UploadFile,File , Form
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from AttendanceProject import camera_output
import csv
import webbrowser
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
import os
import datetime
import sqlite3



csvfilepath="Attendance.csv"

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

con = sqlite3.connect('attendproject.db',check_same_thread=False)
cur = con.cursor()



@app.get("/")
async def home(request: Request):
  return templates.TemplateResponse("home.html",{"request":request})

@app.get('/video_feed')
async def video_feed():
     return StreamingResponse(camera_output(),media_type='multipart/x-mixed-replace; boundary=frame')

@app.get("/attendance")
def attendance(request:Request):
       data=[]
       totalcount=0
       timestamp=""
       dir = "ImagesAttendance"
       for path in os.listdir(dir):
          if os.path.isfile(os.path.join(dir, path)):
             totalcount+= 1

       with open("timestamp.doc","r") as timefile:
             filedata=timefile.read()
             generatedtimestamp=datetime.datetime.strptime(filedata,"%d/%m/%Y %H:%M:%S")
             timestamp=str(generatedtimestamp.timestamp())

       with open("Attendance.csv","r") as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    
                    data.append(row)
                
              
                print(data)   

                return templates.TemplateResponse('attendance.html', {"request":request,"data":data,"noofstudentspresent":len(data),"totalcount":totalcount,"starttime":float(timestamp)})    


@app.get("/clear")
def clear():
    with open("Attendance.csv","w") as file:
        file.truncate()
        file.close()
        msg={"message":"cleared"}
        json_data=jsonable_encoder(msg)
        return JSONResponse(content=json_data)



    
@app.post("/uploadfile/")
async def import_file_post(imagefile: UploadFile = File(...)):
    file_location = f"./ImagesAttendance/{imagefile.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(imagefile.file.read())
        
    msg={"status":True}
    json_data=jsonable_encoder(msg)
    return JSONResponse(content=json_data)


@app.post("/settime/")
def settime(time:str=Form()):

    with open("timestamp.doc","w") as timestampfile:
            timestampfile.write(time)

    msg={"status":True}
    json_data=jsonable_encoder(msg)
    return JSONResponse(content=json_data)



@app.get("/attendancehistory")
def attendancehistory(request:Request):
    history=[]
    for row in cur.execute('SELECT * FROM studentattendance '):
       history.append(row)
    return templates.TemplateResponse("history.html",{"request":request, "data":history})
   



if __name__ == "__main__":
    config = Config()
    config.bind = ["0.0.0.0:8000"]
    webbrowser.open("http://localhost:8000/")
    asyncio.run(serve(app, Config()))