import streamlit as st
import pandas as pd
from functions import *


def insert_stadium():
    df = pd.DataFrame({
        "Stadium id": ["S01", "S02", "S03"],
        "Stadium Name": ["Michigan Stadium", "Eden Gardens", "Truist Park"],
        "City": ["Ann Arbor, Michigan", "Kolkata, West Bengal", "Cumberland, Georgia"],
        "Address": ["1201 South Main Street Ann Arbor, Michigan 48104-3722", "Maidan, B.B.D. Bagh, Kolkata, West Bengal 700021", "755 Battery Ave SE, Atlanta, GA 30339, United States"],
        "Phone No": ["+1 734-647-2583", "033 2248 0411", "+1 404-577-9100"],
        "Email": ["michiganstadium@gmail.com", "egkolkata@hotmail.com", "truistPark@yahoo.com"]

    })
    st.dataframe(df)
    stadium_name = st.selectbox("Stadium Name", df['Stadium Name'])
    if(stadium_name == df['Stadium Name'][0]):
        stadium_id = df['Stadium id'][0]
        city = df['City'][0]
        address = df['Address'][0]
        phone_no = df['Phone No'][0]
        email_id = df['Email'][0]
    elif(stadium_name == df['Stadium Name'][1]):
        stadium_id = df['Stadium id'][1]
        city = df['City'][1]
        address = df['Address'][1]
        phone_no = df['Phone No'][1]
        email_id = df['Email'][1]
    else:
        stadium_id = df['Stadium id'][2]
        city = df['City'][2]
        address = df['Address'][2]
        phone_no = df['Phone No'][2]
        email_id = df['Email'][2]
    if(st.button("Insert stadium details")):
        insert_into_stadium(stadium_id, stadium_name, city,
                            address, phone_no, email_id)
        st.success("Successfully inserted for stadium: {}".format(stadium_id))
    return stadium_id  # return this value because this is a foreign key


def insert_user():
    user_id = st.selectbox(
        "User ID: ", ["U01", "U02", "U03", "U04", "U05", "U06"])
    user_name = st.text_input("Enter name of user {}".format(user_id))
    user_phno = st.text_input("Enter phone number of user {}".format(user_id))
    user_email = st.text_input("Enter email id of user {}".format(user_id))
    if(st.button("Insert user details")):
        insert_into_user(user_id, user_name, user_phno, user_email)
        st.success("Successfully inserted for user: {}".format(user_id))
    return user_id


def insert_match(stadium_id):
    # display the matches happening in stadium - hard code data
    df = pd.DataFrame({
        "Match id": ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09"],
        "Stadium id": ["S01", "S02", "S03", "S01", "S02", "S03", "S01", "S02", "S03"],
        "Sport Type": ["Ice Hockey Match 1", "Cricket ODI", "Baseball Match 1", "Ice Hockey Match 2", "T20I Matches", "Baseball Match 2", "Ice Hockey Match 3", "Test Matches", "Baseball Match 3"],
        "Team 1": ["Concordia Falcons", "India", "Minnesota Twins", "Michigan State Spartans", "Pakistan", "Cleveland Guardians", "Toronto Maple Leafs", "England", "Atlanta Braves"],
        "Team 2": ["Adrian Bulldogs", "Australia", "Chicago White Sox", "Michigan Wolverines", "Bangaladesh", "Detroit Tigers", "Detroit Red Wings", "India", "Baltimore Orioles"]
    })
    st.dataframe(df)
    # first display all rows based on stadium id and then pick matches
    if(stadium_id == "S01"):
        sport_type = st.selectbox("Enter the match name", [
                                  "Ice Hockey Match 1", "Ice Hockey Match 2", "Ice Hockey Match 3"])
        if(sport_type == "Ice Hockey Match 1"):
            team1 = "Concordia Falcons"
            team2 = "Adrian Bulldogs"
            match_id = "M01"
        if(sport_type == "Ice Hockey Match 2"):
            team1 = "Michigan State Spartans"
            team2 = "Michigan Wolverines"
            match_id = "M04"
        if(sport_type == "Ice Hockey Match 3"):
            team1 = "Toronto Maple Leafs"
            team2 = "Detroit Red Wings"
            match_id = "M07"
    if(stadium_id == "S02"):
        sport_type = st.selectbox("Enter the match name", [
                                  "Cricket ODI", "T20I Matches", "Test Matches"])
        if(sport_type == "Cricket ODI"):
            team1 = "India"
            team2 = "Australia"
            match_id = "M02"
        if(sport_type == "T20I Matches"):
            team1 = "Pakistan"
            team2 = "Bangladesh"
            match_id = "M05"
        if(sport_type == "Test Matches"):
            team1 = "England"
            team2 = "India"
            match_id = "M08"
    if(stadium_id == "S03"):
        sport_type = st.selectbox("Enter the match name", [
                                  "Baseball Match 1", "Baseball Match 2", "Baseball Match 3"])
        if(sport_type == "Baseball Match 1"):
            team1 = "Minnesota Twins"
            team2 = "Chicago White Sox"
            match_id = "M03"
        if(sport_type == "Baseball Match 2"):
            team1 = "Cleveland Guardians"
            team2 = "Detroit Tigers"
            match_id = "M06"
        if(sport_type == "Baseball Match 3"):
            team1 = "Atlanta Braves"
            team2 = "Baltimore Orioles"
            match_id = "M09"
    if(st.button("Insert match details")):
        insert_into_matches(match_id, stadium_id, sport_type, team1, team2)
        st.success("Successfully inserted for match: {}".format(match_id))
    return match_id


def insert_food():
    df = pd.DataFrame({
        "Food id": ["F01", "F02", "F03", "F04", "F05"],
        "Food name": ["Sandwich", "French Fries", "Coke", "Samosa", "Chips"],
        "Food price": [150, 120, 90, 130, 80]
    })
    st.dataframe(df)
    food_name = st.selectbox("Choose food item: ", df['Food name'])
    if(food_name == df['Food name'][0]):
        food_id = df['Food id'][0]
        food_price = df['Food price'][0].item()
    elif(food_name == df['Food name'][1]):
        food_id = df['Food id'][1]
        food_price = df['Food price'][1]
    elif(food_name == df['Food name'][2]):
        food_id = df['Food id'][2]
        food_price = df['Food price'][2]
    elif(food_name == df['Food name'][3]):
        food_id = df['Food id'][3]
        food_price = df['Food price'][3]
    elif(food_name == df['Food name'][4]):
        food_id = df['Food id'][4]
        food_price = df['Food price'][4]
    else:
        food_id = df['Food id'][5]
        food_price = df['Food price'][5]
    if(st.button("Insert food details")):
        insert_into_food(food_id, food_name, food_price)
        st.success("Successfully inserted for food: {}".format(food_id))
    return food_id


def insert_seat(stadium_id):
    df1 = pd.DataFrame({
        "Seat id": ["Seat11", "Seat12", "Seat13"],
        "Seat Class": ["Class 1", "Class 2", "Class 3"],
        "Seat No": [13, 24, 63],
        "Seat Price": [15000, 12000, 11000],
        "Availability": ['Y', 'Y', 'Y']
    })
    df2 = pd.DataFrame({
        "Seat id": ["Seat21", "Seat22", "Seat23"],
        "Seat Class": ["Class 1", "Class 2", "Class 3"],
        "Seat No": [15, 56, 34],
        "Seat Price": [15030, 12300, 10300],
        "Availability": ['Y', 'Y', 'Y']
    })
    df3 = pd.DataFrame({
        "Seat id": ["Seat31", "Seat32", "Seat33"],
        "Seat Class": ["Class 1", "Class 2", "Class 3"],
        "Seat No": [43, 26, 68],
        "Seat Price": [15500, 12040, 11300],
        "Availability": ['Y', 'Y', 'Y']
    })
    # how to choose a seat
    if(stadium_id == "S01"):
        df = df1
    elif(stadium_id == "S02"):
        df = df2
    else:
        df = df3
    temp_df = pd.DataFrame(
        df, columns=["Seat id", "Seat Class", "Seat No", "Seat Price"])
    '''st.dataframe(pd.DataFrame(df, columns=["Seat id","Seat Class","Seat No","Seat Price,"Availability"]))'''
    st.dataframe(pd.DataFrame(temp_df, columns=[
                 "Seat id", "Seat Class", "Seat No", "Seat Price"]))
    seat_class = st.selectbox("Choose a seat class: ", [
                              "Class 1", "Class 2", "Class 3"])
    if(seat_class == "Class 1"):
        seat_id = df['Seat id'][0]
        seat_no = df['Seat No'][0]
        seat_price = df['Seat Price'][0]
        availability = df["Availability"][0]
    elif(seat_class == "Class 2"):
        seat_id = df['Seat id'][1]
        seat_no = df['Seat No'][1]
        seat_price = df['Seat Price'][1]
        availability = df["Availability"][1]
    else:
        seat_id = df['Seat id'][2]
        seat_no = df['Seat No'][2]
        seat_price = df['Seat Price'][2]
        availability = df["Availability"][2]
    if(st.button("Insert into seat table")):
        insert_into_seat(seat_id, stadium_id, seat_class,
                         seat_no, seat_price, availability)
        st.success("Seat inserted into table")
    # update the availability to no
    update_seat_status_fn(stadium_id, seat_id)
    st.write("After seat updation")
    st.subheader("Seat")
    seat_table = view_table("seat_matrix")
    st.dataframe(pd.DataFrame(seat_table, columns=seat_matrix_cols))
    return seat_id


def generate_ticket(stadium_id, match_id, user_id, seat_id, food_id):
    # compute bill amount
    # get seat price and food price from those tables
    seat_price = get_seat_price(stadium_id)[0]
    food_price = get_food_price(food_id)[0]
    bill = seat_price+food_price
    bill_amount = bill[0]+bill[1]
    st.write("Bill amount: ", bill_amount)
    # create ticket id
    # concat of stadium id, match id and seat id
    ticket_id = stadium_id+"_"+match_id+"_"+seat_id[4:]
    st.write("Ticket id: ", ticket_id)
    # insert into ticket table
    insert_into_ticket(ticket_id, user_id, stadium_id,
                       match_id, food_id, seat_id,  bill_amount)
    return ticket_id
