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
* Hypercorn
* JavaScript
* SQLite
* OpenCV
* Facial_recognition
* Facial_recognition_models (Which is internally used by facial_recognition)
* Dlib (Internally used by facial_recognition
*For ipackaging the app *GUI based version of pyinstaller (Known as auto-py-to-exe) Or simply pyinstaller was used 


![WhatsApp Image 2022-05-29 at 9 15 47 PM](https://user-images.githubusercontent.com/89723030/170878441-9363ebbb-c120-462b-b260-1d5f739815a1.jpeg)


* Instructions to run it:
1. Here's the Google drive link. (https://drive.google.com/drive/folders/18y83NcTL4RkMNWJZLWjRtwCQf3iLOSIK).


[* I have also created a seperate repo for my app.
https://github.com/Maida-Iftikhar/FRAP.git  However, due to large size, it might be difficult to clone the repo and then run it. It is therfore advised to use the Drive link for a smooth experience.]



2. Now click download all. It will download a zip
3. Extract it and you will see a folder named "app" .In that app folder you will find app.exe file
4. Run it
5. Wait for the output text in the app console And then in the console it will show you to open localhost:5000/



**Note: You always requested to execute the app.exe inside the app folder only because all the dependencies of that app.exe are in that folder. So no shortcuts
would work.

*On the web page, you could use images of 'Elon Musk', 'Jack Ma', 'Jk Rowlings' , 'Al Waleed', 'Sundar Pichai' and 'Mark Zuckerberg' as these are the stored images in the current database. You
can further clear the attendance to mark new ones. 





