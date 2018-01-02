#!/usr/bin/env python
#coding: utf-8


"""
Testing loans.
"""

import unittest
import datetime
import sqlalchemy
import sqlalchemy.orm
from pybib.pupil import Pupil
from pybib.loan import Loan
from pybib.db import engine, Base


class SimpleLoanTestCase(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all(engine)
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()

        self.create_pupil()

    def create_pupil(self):
        john = Pupil(
            name='Doe',
            prename='John',
        )
        self.session.add(john)
        self.session.commit()

    def test_create(self):
        john = self.session.query(Pupil).first()
        loan = Loan(
            pupil=john
        )
        self.session.add(loan)
        self.session.commit()
        self.assertEqual(loan.pupil, john)
        self.assertIn(loan, john.loans)
        now = datetime.datetime.now().date()
        enddate = now + datetime.timedelta(weeks=2)
        self.assertEqual(loan.back_date, None)
        self.assertEqual(loan.start_date, now)
        self.assertEqual(loan.end_date, enddate)
