from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    UnicodeText,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

from datetime import datetime

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class MyEntry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True, [Required()])
    title_field = Column(Text(255))    
    body_field = Column(Text(length=2**31), nullable=True)
    created_field = Column(DateTime)
    edited_field = Column(DateTime, default=datetime.datetime.now)
    
Index('my_index', MyEntry.name, unique=True, mysql_length=255)

query = session.query(MyEntry)
print query.order_by(created_field()).all()

obj = MyEntry.query.get(the_id)
print obj

