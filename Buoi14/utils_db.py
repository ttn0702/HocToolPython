from peewee import *

host='149.28.145.242'
db_name = 'btvn_nghia'
db_user='nghiahsgs4'
db_pass='123456'
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

if __name__ =="__main__":
    print(len(Score.select()))
    print(len(Score.select().where(Score.is_run==0)))