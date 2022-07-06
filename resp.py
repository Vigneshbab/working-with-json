from sqlalchemy.orm import Session
from . import models, schemas

class ItemRepo:
    async def create(db: Session, item: schemas.ItemBase):
        db_item = models.employee(first_name=item.first_name, last_name=item.last_name, emp_id=item.emp_id, city=item.city, age=item.age, contact_no=item.contact_no, experience=item.experience)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def fetch_by_first_name(db: Session, first_name):
        return db.query(models.employee).filter(models.employee.id == first_name).first()

    def fetch_by_last_name(db: Session, last_name):
        return db.query(models.employee).filter(models.employee.name == last_name).first()

    def fetch_by_emp_id(db: Session, emp_id):
        return db.query(models.employee).filter(models.employee.name == emp_id).first()

    def fetch_by_city(db: Session, city):
        return db.query(models.employee).filter(models.employee.name == city).first()

    def fetch_by_age(db: Session, age):
        return db.query(models.employee).filter(models.employee.name == age).first()

    def fetch_by_contact_no(db: Session, contact_no):
        return db.query(models.employee).filter(models.employee.name == contact_no).first()

    def fetch_by_experience(db: Session, experience):
        return db.query(models.employee).filter(models.employee.name == experience).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.employee).offset(skip).limit(limit).all()
