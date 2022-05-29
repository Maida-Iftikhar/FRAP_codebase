# FRAP_codebase
# MicrosoftEngage22

* Introduction⭐
* This is a facial recognition based attendance system. It is majorly coded in Python, OpenCv. The framwework used is FastApi due to it's features like: auto documentation, auto completion, code suggestion and data validation.
* The attendance system, captures real time faces from the web cam and stores the name of the student along with the accurate time of arrival into a .csv file.
* The feature of late attendance is also implemented, wherein you as a teacher can see the entries of students who were late to the class ( and deduct their marks ;P )
* Attendance statistics can be viewed in the form a pie chart.
* An option to clear attendance has also been provided
* However , to preserve the essence of the attendance register, I implemeted SQLite as a file based datbase to act as a virtual attendance register which stores all the history. 

For this project,
I have created a folder named ImagesAttendance which stores the data of the attendees. I have stored the images of Elon Musk, Jack Ma, Mark Zuckerberg, JK Rowling 

The file named "Requirements.txt" contains all the tech used and their respective versions too.
The main dependencies used are:
* FastApi
* Hypercorn (Production  ASGI server to be used with fastapi) 
* JavaScript 
* SQLite
* OpenCV
* Facial_recognition
* Facial_recognition_models (Which is internally used by facial_recognition)



![WhatsApp Image 2022-05-29 at 9 15 47 PM](https://user-images.githubusercontent.com/89723030/170878441-9363ebbb-c120-462b-b260-1d5f739815a1.jpeg)


* Instructions to run it:
1: clone the repo  
2:open your terminal
3:cd into the repo folder
4:type pip install -r requirements.txt (Note:it will install all the dependecies for the project)
5:once all dependecies are installed , Type python app.py in the terminal to run the application

# a browser window will open at http://localhost:8000/ where the application interface resides 











