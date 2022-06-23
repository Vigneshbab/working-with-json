from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"Message":"HELLO WORLD"}

@app.post("/")
def new_emp(first_name:str,last_name:str,emp_id:str,city:str,age:int,ctc:int,contact_no:int,experience:int):
    return{first_name,last_name,emp_id,city,age,ctc,contact_no,experience}