# fastAPI-task

## Table of contents
* [General info](#general-info)
* [Technologies used](#technologies-used)
* [Compilation](#compilation)

## General info
This task is to develop two APIs using the Python FASTAPI
	
## Technologies required
Python version: 3.9.10
SQLite version: 3
Python modules required - fastapi, sqlite3, uvicorn
	
## Compiling the code
1. Open command prompt
2. Goto the code folder path and type
$ python Employee.py
3. In the browser goto http://localhost:8080/list_employee
-> Adding a new employee to the emplyoyee db
4. Goto python path in command prompt and type
$ import requests
$ requests.post("https://localhost:8080/add_employee",json={"id":3,"name":"Hannah"})
-> Data retrieval from employee database by ID=
5. In the browser goto
http://localhost:8080/fetch_employee?Id=1
-> Adding a new timesheet details into the timesheet db
6. Goto python path in command prompt and type
$ import requests
$ requests.post("http://localhost:8081/push_timesheet",json={"id":4,"date":"11-05-2022","hours":5})
-> Data retrieval from timesheet database by ID=
5. In the browser goto
http://localhost:8081/fetch_timesheet?Id=4
