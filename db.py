import peewee

from datetime import datetime
from peewee import Model, CharField, IntegerField, DateTimeField

database = peewee.SqliteDatabase('database.sqlite3')

class ApiKeys(Model):
    api_key = CharField()
    api_secret = CharField()
    class Meta:
        primary_key = False
        database = database
        name = 'api_keys'

class Pallet(Model):
    id_pallet = IntegerField()
    product_name = CharField()
    product_batch = CharField()
    thing_quantity = IntegerField()
    data_of_manufacture = CharField()
    expiration_date = CharField()
    class Meta:
        primary_key = False
        database = database
        name = 'pallet'

class PalletStatus(Model):
    id_pallet = IntegerField()
    id_status = IntegerField()
    class Meta:
        primary_key = False
        database = database
        name = 'palet_status'

class Status(Model):
    id_status = IntegerField()
    status_name = CharField()
    class Meta:
        primary_key = False
        database = database
        name = 'status'

def create_table():
    database.create_tables([Pallet, Status, PalletStatus, ApiKeys])
    Status.create(id_status =1, status_name ='produced')
    Status.create(id_status =2, status_name ='expected_in_the_production_buffer')
    Status.create(id_status =3, status_name ='in_the_production_buffer')
    Status.create(id_status =4, status_name ='expected_in_the_warehouse_buffer')
    Status.create(id_status =5, status_name ='in_the_warehouse_buffer')
    Status.create(id_status =6, status_name ='expected_to_be_placed')
    ApiKeys.create(api_key='kjhvfkuvYTFCY8748754vUGIUTYFVoupoan', api_secret='LFIHOSIUV987tf78a6tg8e65rg87es65g87es6ybOUYG876vf968rvgesohvu')

if __name__ == '__main__':
    create_table()
