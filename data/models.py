from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    start_time = Column(DateTime)
    end_time = Column(DateTime)
    
    def __repr__(self):
       return f"<Group(name='{self.name}')>"



class Treatment(Base):
    __tablename__ = 'treatments'
    
    id = Column(Integer, primary_key=True)
    kind = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group")

    def __repr__(self):
       return f"<Treatment(kind='{self.name}', date='')>"



        

# CREATE TABLE group (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   group_type TEXT NOT NULL,
#   start_time TIMESTAMP NOT NULL,
#   end_time TIMESTAMP
# );

# CREATE TABLE treatment (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   start_time TIMESTAMP NOT NULL,
#   end_time TIMESTAMP,
#   group_id INTEGER NOT NULL,
#   treatment_type TEXT NOT NULL,
#   FOREIGN KEY (group_id) REFERENCES group (id)
# );
