# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:51:45 2021

@author: bszym
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import json

def load_lkp(name='lkp20210626'):
    engine = create_engine('sqlite:///data\\pokerdb.db', echo=True)

    Session = sessionmaker(bind=engine) 
    session = Session() 

    getprobs = session.query(_util_sqlalch_setup.Probs).filter_by(name=name).first()
    session.close()
    
    return json.loads(getprobs.dict)


def load_lkp2(name='lkp20210626'):
    engine = create_engine('sqlite:///data\\pokerdb.db', echo=True)

    metadata = MetaData(engine)
    metadata.reflect()
    
    with engine.begin() as conn:
        getrows=conn.execute(f"select dict from Probs where name='{name}'")
        for row in getrows:
            restxt=row['dict']
    
    return json.loads(restxt)

    
    