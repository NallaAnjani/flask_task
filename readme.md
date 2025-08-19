step1
python -m venv venv
venv\Scripts\activate
pip install flask
python app.py
step2:
With SQLAlchemy (ORM)

ORM = Object Relational Mapper → you work with Python classes/objects, not raw SQL.

SQLAlchemy translates your Python code into SQL under the hood.

.......................
2. Install MySQL Server

This will store all your student/grades/subjects data.

Download from MySQL Community Server
.

Install MySQL Workbench (optional but useful GUI to see data).

Test installation:

mysql -u root -p


(enter password you set during installation).

---------------------------------
3. Install Flyway CLI

Flyway is used for database migrations (version control for DB schema).

Download from Flyway
.

Extract ZIP and add flyway command to your system PATH.

Test:

flyway -v
--------------------------------------
step4:
mkdir student-grade-system
cd student-grade-system
python -m venv venv
venv\Scripts\activate     # (Windows)
# OR
source venv/bin/activate  # (Mac/Linux)

pip install flask flask_sqlalchemy flask_jwt_extended pymysql

---------------
stepy6:Install Virtual Environment (for Flask)
mkdir student-grade-system
cd student-grade-system
python -m venv venv
venv\Scripts\activate 
pip install flask flask_sqlalchemy flask_jwt_extended pymysql
--------
step7:
📌 Step 7: Test Endpoints

Use Postman or cURL.

Add Student:

curl -X POST http://127.0.0.1:5000/students/ -H "Content-Type: application/json" -d '{"name":"Anjani"}'


Get Students:

curl http://127.0.0.1:5000/students/
--------------
step8:
run flyway migration
flyway -url=jdbc:mysql://localhost:3306/student_db -user=root -password=yourpassword migrate

-----------------------
step9:


🚀 How to Use Postman for Your Project
✅ Step 1: Install Postman

Download from 👉 https://www.postman.com/downloads/

Install and open it.

✅ Step 2: Create a New Collection

Open Postman.

Click Collections → New Collection → name it Student Grade Management System.

Inside this collection, we’ll add requests for students, subjects, teachers, grades, reports, and auth.

✅ Step 3: Add First Request – Login (JWT)

Click Add Request → Name: Login.

Method: POST

URL:

http://127.0.0.1:5000/auth/login


Go to Body → raw → JSON and paste:

{
  "username": "admin",
  "password": "password123"
}


Click Send.

✅ You’ll get a response with a JWT token like:

{
  "access_token": "eyJ0eXAiOiJKV1QiLCJh..."
}


👉 Copy this token (we’ll use it for protected routes).

-----------------------
step10:
✅ Step 4: Add Student

Create request → Name: Add Student.

Method: POST

URL:

http://127.0.0.1:5000/students/


Go to Headers → Add:

Key: Authorization
Value: Bearer <your_token_here>


Go to Body → raw → JSON:

{
  "name": "Anjani"
}


Click Send.

✅ Response:

{ "message": "Student added" }

✅ Step 5: Get Students

New request → Name: Get Students

Method: GET

URL:

http://127.0.0.1:5000/students/


Add Authorization header again:

Authorization: Bearer <your_token_here>


Click Send → Response:

[
  { "id": 1, "name": "Anjani" }
]

✅ Step 6: Add Subject

Create request → Name: Add Subject

Method: POST

URL:

http://127.0.0.1:5000/subjects/


Headers → add JWT token.

Body → raw → JSON:

{
  "name": "Math"
}


✅ Response:

{ "message": "Subject added" }

✅ Step 7: Add Grade

New request → Name: Add Grade

Method: POST

URL:

http://127.0.0.1:5000/grades/


Headers → add JWT token.

Body → raw → JSON:

{
  "student_id": 1,
  "subject_id": 1,
  "grade": 95
}


✅ Response:

{ "message": "Grade added" }

✅ Step 8: Get Report Card

New request → Name: Get Report Card

Method: GET

URL:

http://127.0.0.1:5000/grades/student/1/report-card


Headers → add JWT token.

✅ Response:

{
  "student_id": 1,
  "grades": [
    { "subject_id": 1, "grade": 95 }
  ],
  "average": 95
}




