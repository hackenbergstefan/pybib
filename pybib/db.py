#!/usr/bin/env python
#coding: utf-8


"""
Module holding database adapter.
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()
