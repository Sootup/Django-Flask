from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData  
from sqlalchemy.orm import mapper , sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
e = create_engine("sqlite:///Untitled")


# e.execute("""
# insert into user (firstname, lastname)
# values ('Alex', 'Varkalov')
# """)
# result = e.execute("""select * from us`e`r""")
# for user in result:
#     print(user)


Base = declarative_base()
class Student(Base):
    def __init__(self,firstname,lastname,group):
        self.firstname = firstname
        self.lastname = lastname
        self.group = group
    __tablename__ = "Students"
    id = Column(Integer,primary_key=True)
    firstname = (String)
    lastname = (String)
    group = (Integer)
    
Base.metadata.create_all(e)
Session = sessionmaker(bind=e)
session = Session()
session.commit()




session.add (Student("Egor","adsads",1))
session.commit()
