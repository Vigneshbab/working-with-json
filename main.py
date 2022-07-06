from fastapi import Depends, FastAPI, HTTPException
from db import get_db, engine
import sql_app.models as models
from sql_app.resp import ItemRepo
import sql_app.models as models
import sql_app.schemas as schemas
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/emp_detail")
def emp_detail(first_name: str, last_name: str, emp_id: str, city: str, age: int, contact_no: int, experience: int):
    return{first_name, last_name, emp_id, city, age, contact_no, experience}


@app.post('/items', tags=["Item"], response_model=schemas.Item, status_code=201)
async def create_item(item_request: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create an Item and store it in the database
    """

    db_item = ItemRepo.fetch_by_name(db, name=item_request.name)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists!")

    return await ItemRepo.create(db=db, item=item_request)


# https://dassum.medium.com/building-rest-apis-using-fastapi-sqlalchemy-uvicorn-8a163ccf3aa1
