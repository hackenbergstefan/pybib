#!/usr/bin/env python
#coding: utf-8


"""
Testing pupils.
"""

import unittest
import sqlalchemy
import sqlalchemy.orm
from pybib.pupil import Pupil
from pybib.db import engine, Base


class SimplePupilTestCase(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all(engine)
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()

    def test_create(self):
        john = Pupil(
            name='Doe',
            prename='John',
        )
        self.session.add(john)
        self.session.commit()

        self.assertEqual(john.prename, 'John')
        self.assertEqual(john.name, 'Doe')
        self.assertEqual(john.id, 1)
        self.assertEqual(john.isout, False)

        self.assertIn(john, self.session.query(Pupil))

    def test_delete(self):
        john = self.session.query(Pupil).first()
        self.session.delete(john)
        self.assertIn(john, self.session.deleted)
        self.session.commit()
        self.assertEqual(0, self.session.query(Pupil).count())
