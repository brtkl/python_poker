# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:51:45 2021

@author: bszym
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import json
import _util_sqlalch_setup

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


def save_stats(player):
    engine = create_engine('sqlite:///data\\pokerdb.db', echo=True)

    Session = sessionmaker(bind=engine) 
    session = Session() 
    
    getstat = session.query(_util_sqlalch_setup.UserStat).\
        filter(_util_sqlalch_setup.UserStat.name==player.name,
               _util_sqlalch_setup.UserStat.type==player.type).first()
        
    if not getstat:
        newentry=_util_sqlalch_setup.UserStat(player.name, player.type, 
                                              player.strat, player.bb100, 
                                              player.hands_played, player.bbwon)
        session.add(newentry)
        session.commit()
    else:
        getstat.bb100=player.bb100
        getstat.bbwon=player.bbwon
        getstat.hands_played=player.hands_played
        session.commit()
        
    session.close()

def load_stats(player):
    engine = create_engine('sqlite:///data\\pokerdb.db', echo=True)

    Session = sessionmaker(bind=engine) 
    session = Session() 
    
    getstat = session.query(_util_sqlalch_setup.UserStat).\
        filter(_util_sqlalch_setup.UserStat.name==player.name,
               _util_sqlalch_setup.UserStat.type==player.type).first()
    
    if not getstat:
        raise ValueError('Player with given name and type doesn\'t exist')
    else:
        player.bb100=getstat.bb100
        player.hands_played=getstat.hands_played
        player.bbwon=getstat.bbwon
        session.commit()
        
    session.close()

    #query to see if a record exists with player name and type.
    # if yes then update player attributes. If not then raise an ezcept?
    
    #to add a function for creating players only?

    