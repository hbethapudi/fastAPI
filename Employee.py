from fastapi import FastAPI, Request
import sqlite3
import uvicorn

def execute(query='', commit=False):
    try:
        con = sqlite3.connect('employee.db')
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

@app.post("/add_employee")
async def push_record(req: Request):
    data = await req.json()
    record = (data['id'], data['name'])
    return execute('insert into records values(%s, "%s")'%record, True)

@app.get("/list_employee")
async def list_records():
    return execute('select * from records')

@app.get("/fetch_employee")
async def fetch_record(Id: int):
    return execute('select * from records where emp_id=%s'%(Id))


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')