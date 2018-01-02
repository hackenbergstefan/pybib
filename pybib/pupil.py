#!/usr/bin/env python
#coding: utf-8


"""
Module representing a pupil.
"""

from sqlalchemy import Column, Integer, String, Boolean, desc
from sqlalchemy.orm import relationship
from pybib.db import Base
from pybib.loan import Loan

MALE = 'male'

FEMALE = 'female'


class Pupil(Base):
    __tablename__ = 'pupils'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    prename = Column(String)
    grade = Column(String)
    isout = Column(Boolean, default=False)
    gender_id = Column(Boolean, default=0)

    loans = relationship('Loan', order_by=desc(Loan.id))

    @property
    def gender(self):
        return MALE if self.gender_id == 0 else FEMALE

    @gender.setter
    def gender(self, gender):
        assert gender in [MALE, FEMALE]
        self.gender_id = 0 if gender == MALE else 1
