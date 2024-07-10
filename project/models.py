# models.py

from flask_login import UserMixin
from sqlite3 import connect
from contextlib import closing

#from . import db

#class User(UserMixin, db.Model):
#   id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#   email = db.Column(db.String(100), unique=True)
#   password = db.Column(db.String(100))
#   name = db.Column(db.String(1000))

class User(UserMixin):
  def __init__(self, id, email, password, name):
      self.id, self.email, self.password, self.name = id, email, password, name
  
  def get_by(email):
      print(">>>>> get_by.... >>> ", email)
      usr = User(0,"dummy@coco.com","sha256$OmqLPW8qaBoHBvgF$21546d632722557ef2","mkmk")
      with closing(connect("db.sqlite")) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("select * from user where email = ?", (email,) ).fetchone()
            if rows is not None:
                print(">>>>> rows.... >>> ", rows)
                usr = User(id=rows[0], email=rows[1], name=rows[3], password=rows[2])
                print(">>>>> get_by....usr >>> ", usr)
            #u = User(rows)
      return usr
      
  def get_by_id(id):
      print(">>>>> get_by_id.... >>> ", id)
      usr = User(0,"dummy@coco.com","sha256$OmqLPW8qaBoHBvgF$21546d632722557ef2","mkmk")
      with closing(connect("db.sqlite")) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("select * from user where id = ?", (id,) ).fetchone()
            if rows is not None:
                print(">>>>> rows id.... >>> ", rows)
                usr = User(id=rows[0], email=rows[1], name=rows[3], password=rows[2])
                print(">>>>> get_by_id....usr >>> ", usr)
            #u = User(rows)
      return usr

  def persist(self):
      with closing(connect("db.sqlite")) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("insert into user (id, email, password,name) values (?,?,?,?)", (self.id, self.email, self.password, self.name) )
            connection.commit()
            #print(rows)
      return u
      
    
u = User(3,"m@coco.com","sha256$OmqLPW8qaBoHBvgF$21546d632722557a7560c8a3623e98414b816b8c6b7a9e71df00682445058ef2","mukul")
#print(u)





