from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base


class  employee(Base):
    __tablename__ = "emp_details"

    # fields
    first_name = Column(String(20),primary_key=True, index=True)
    last_name = Column(String(20))
    emp_id = Column(String)
    city = Column(String)
    age = Column(Integer)
    contact_no = Column(Integer)
    experience = Column(Integer)
