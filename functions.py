import mysql.connector
from createDatabase import *
import streamlit as st
import pandas as pd

c.execute("create database if not exists stadiumTicket4")
c.execute("use stadiumTicket4")

stadium_cols = ["stadium_id", "stadium_name",
                "city", "address", "phone_no", "email"]
matches_cols = ["match_id", "stadium_id", "match_name", "team1", "team2"]
users_cols = ["user_id", "user_name", "phno", "email"]
food_cols = ["food_id", "food_name", "food_price"]
seat_matrix_cols = ["seat_id", "stadium_id",
                    "seat_class", "seat_no", "seat_price", "seat_av"]
ticket_cols = ["ticket_id", "user_id", "stadium_id",
               "match_id", "food_id", "seat_id",  "bill"]


def run_any_query(code):
    c.execute(code)  # to execute multiple sql queries at once
    data = c.fetchall()
    return data


def create_table():
    c.execute(
        "create table if not exists food(food_id varchar(255), food_name varchar(255), food_price int); ")
    c.execute("create table if not exists stadium(stadium_id varchar(255), stadium_name varchar(255),city varchar(255), address varchar(255),phone_no varchar(255),email varchar(255)); ")
    c.execute("create table if not exists matches(match_id varchar(255),stadium_id varchar(255), match_name varchar(255), team1 varchar(255), team2 varchar(255)); ")
    c.execute("create table if not exists seat_matrix(seat_id varchar(255),primary key(seat_id),stadium_id varchar(255), seat_class varchar(255), seat_no int, seat_price int,seat_av varchar(1)); ")
    c.execute("create table if not exists users(user_id varchar(255), user_name varchar(255), phno varchar(255), email varchar(255), primary key(user_id)); ")
    c.execute("create table if not exists ticket(ticket_id varchar(255),primary key(ticket_id),user_id varchar(255),stadium_id varchar(255), match_id varchar(255),food_id varchar(255),seat_id varchar(255), bill int);")


def insert_into_stadium(stadium_id, stadium_name, city, address, phone_no, email):
    c.execute("insert into stadium (stadium_id, stadium_name ,city, address ,phone_no ,email) values (%s,%s,%s,%s,%s,%s)",
              (stadium_id, stadium_name, city, address, phone_no, email))
    mydb.commit()  # commit


def insert_into_user(user_id, user_name, user_phno, user_email):
    c.execute("insert into users (user_id, user_name, phno, email) values (%s,%s,%s,%s)",
              (user_id, user_name, user_phno, user_email))
    mydb.commit()  # commit


def insert_into_matches(match_id, stadium_id, match_name, team1, team2):
    c.execute("insert into matches (match_id,stadium_id ,match_name, team1 , team2) values (%s,%s,%s,%s,%s)",
              (match_id, stadium_id, match_name, team1, team2))
    mydb.commit()


def insert_into_food(food_id, food_name, food_price):
    c.execute("insert into food (food_id, food_name, food_price) values ('{}','{}',{})".format(
        food_id, food_name, food_price))
    mydb.commit()


def insert_into_seat(seat_id, stadium_id, seat_class, seat_no, seat_price, seat_av):
    seat_price = int(seat_price)
    c.execute("insert into seat_matrix (seat_id ,stadium_id , seat_class , seat_no ,seat_price,seat_av) values ('{}','{}','{}',{},{},'{}')".format(
        seat_id, stadium_id, seat_class, seat_no, seat_price, seat_av))
    mydb.commit()


def insert_into_ticket(ticket_id, user_id, stadium_id, match_id, food_id, seat_id,  bill):
    c.execute("insert into ticket(ticket_id,user_id ,stadium_id ,match_id ,food_id , seat_id,  bill) values ('{}','{}','{}','{}','{}','{}',{})".format(
        ticket_id, user_id, stadium_id, match_id, food_id, seat_id,  bill))
    mydb.commit()


def update_seat_status_fn(stadium_id, seat_id):
    c.execute("update seat_matrix set seat_av='{}' where stadium_id='{}' and seat_id='{}'".format(
        "N", stadium_id, seat_id))
    mydb.commit()


def update_stadium(new1, new2, new3, new4, new5, old1, old2, old3, old4, old5):
    c.execute("update stadium set stadium_id='{}', stadium_name='{}' ,city='{}', address ='{}',phone_no ='{}',email='{}' where stadium_id='{}' and stadium_name ='{}' and city='{}' and address='{}' and phone_no ='{}' and email='{}'".format(
        new1, new2, new3, new4, new5, old1, old2, old3, old4, old5))
    mydb.commit()
    c.execute("select * from stadium")
    data = c.fetchall()
    return data


def update_user(new0, new1, new2, old0):
    c.execute("update users set user_name='{}' ,phno='{}', email ='{}' where user_id='{}'".format(
        new0, new1, new2, old0))
    mydb.commit()
    c.execute("select * from users")
    data = c.fetchall()
    return data


def view_table(table_name):
    return run_any_query("select * from {}".format(table_name))


def delete_item(item_id, table_name):
    # delete the row
    if(table_name == "food"):
        c.execute("delete from food where food_id='{}'".format(item_id))
    elif(table_name == "stadium"):
        c.execute("delete from stadium where stadium_id='{}'".format(item_id))
    elif(table_name == "matches"):
        c.execute("delete from matches where match_id='{}'".format(item_id))
    elif(table_name == "seat_matrix"):
        c.execute("delete from seat_matrix where seat_id='{}'".format(item_id))
    elif(table_name == "users"):
        c.execute("delete from users where user_id='{}'".format(item_id))
    else:
        c.execute("delete from ticket where ticket_id='{}'".format(item_id))
    mydb.commit()


def get_seat_price(stadium_id):
    return run_any_query("select seat_price from seat_matrix where stadium_id = '{}'".format(stadium_id))


def get_food_price(food_id):
    return run_any_query("select food_price from food where food_id = '{}'".format(food_id))


def get_id(table_name):
    # get the id of the row to be deleted
    if(table_name == "food"):
        code = "select food_id from food"
    elif(table_name == "stadium"):
        code = "select stadium_id from stadium"
    elif(table_name == "matches"):
        code = "select match_id from matches"
    elif(table_name == "seat_matrix"):
        code = "select seat_id from seat_matrix"
    elif(table_name == "users"):
        code = "select user_id from users"
    else:
        code = "select ticket_id from ticket"
    return run_any_query(code)
