from peewee import *


host='localhost'
db_name = 'btvn12'
db_user='root'
db_pass=''
db = MySQLDatabase(db_name,host=host, user=db_user, passwd=db_pass)

# model tuong ung voi table
class Score(Model):
    sbd = CharField()
    toan = FloatField()
    van = FloatField()
    anh = FloatField()
    is_run = IntegerField()
    class Meta:
        database=db
if __name__ == "__main__":
    Score.create_table()

