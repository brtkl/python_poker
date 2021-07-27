# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:51:45 2021

@author: bszym
"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data\\pokerdb.db', echo=True)
Base = declarative_base()


class UserStat(Base):
    """
    stores user information:
        -name
        -type, consistent with Player class, 'human' or 'comp'
        -strat (see strategy class for possible values. 
            Note that human is reserved for type=human)
        -bb100
        -hands_played
        -bb_won
    """
    __tablename__ = 'userstat'
    
    name = Column(String, primary_key=True)
    type = Column(String, primary_key=True)
    strat = Column(String)
    bb100 = Column(Float)
    hands_played = Column (Integer)
    bb_won = Column (Integer)
    
class Probs(Base):
    __tablename__='probs'
    
    name = Column(String, primary_key=True)
    numcards = Column(Integer)
    simnum = Column(Integer)
    dict = Column(String)
    
    
"""
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine) #class - a factory of Session instances
session = Session()
session.commit()
session.close()
"""

#create a session (instance), whenever you need to talk to the database

#####how to add rows
#newplayer=UserStat(name='testuser', type='human', strat='human', bb100=0)
#session.add(newplayer) 
#   this will add a new player but not in this exact moment, it'll be flushed 
#   when we query the database
#session.add_all([list of users])

###how to update without querying
#session.commit()

##reverting changes
#session.rollback()


####how to query
#our_user = session.query(UserStat).filter_by(name='testuser').first() 
#getprobs = session.query(Probs).filter_by(name='lkp20210626').first()
##lkp20210626_l=json.loads(getprobs.dict)




####history of entries. DB created on 20210725 19:00
#session.add(Probs(name='lkp20210626', numcards=2, simnum=50000, dict=testchar))





