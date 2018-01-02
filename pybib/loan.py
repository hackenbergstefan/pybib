#!/usr/bin/env python
#coding: utf-8


"""
Module representing a loan.
"""

import datetime
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from pybib.db import Base

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date, default=datetime.datetime.now())
    end_date = Column(Date, default=datetime.datetime.now()+datetime.timedelta(weeks=2))
    back_date = Column(Date)
    isactive = Column(Boolean, default=False)
    pupil_id = Column(Integer, ForeignKey("pupils.id"))

    pupil = relationship("Pupil", back_populates="loans")
