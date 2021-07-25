# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:51:45 2021

@author: bszym
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///\\data\\pokerdb.db', echo=True)

Base = declarative_base()