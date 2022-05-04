from fastapi import FastAPI, Request
import requests
import sqlite3
import uvicorn

def execute(query='', commit=False):
    try:
        con = sqlite3.connect('timesheet.db')
        cursor = con.cursor()
        resp = list(cursor.execute(query))
        if commit:
            con.commit()
        con.close()
        if resp:
            return resp
        else:
            return ''
    except Exception as E:
        print(E)
        return 'sqlite error'

app = FastAPI()

@app.post("/push_timesheet")
async def push_record(req: Request):
    data = await req.json()
    if requests.get('http://localhost:8081/fetch_employee?Id=%s'%(data['id'])).text:
        record = (data['id'], data['date'], data['hours'])
        return execute('insert into records values(%s, "%s", %s)'%record, True)
    else:
        return "Employee Id doesnt exist"

@app.get("/fetch_timesheet")
async def fetch_record(Id: int):
    return execute('select * from records where emp_id=%s'%(Id))

@app.get("/search_timesheet")
async def search_record(Id: int, date: str):
    return execute('select * from records where emp_id=%s and date="%s"'%(Id, date))

@app.get("/test")
async def sea_record(Id: int):
    if requests.get('http://localhost:8080/fetch_employee?Id=%s'%(Id)).text != '""':
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    uvicorn.run(app, port=8081, host='0.0.0.0')
