import streamlit as st
import pandas as pd
from createDatabase import *
from functions import *
from insert import *
from display import *
from delete import *
from update import *


def main():
    st.title("Stadium Ticket Booking System")
    st.caption("Made by Keerthana Shivakumar")
    menu = ["Booking Ticket", "SQL Editor"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice == "SQL Editor":
        query_input = st.text_area("Enter SQL Query to run")
        result = ""
        st.code(query_input)
        if(st.button("Execute query")):
            result = run_any_query(query_input)
            result = pd.DataFrame.from_dict(result)
            st.write("Result: ", result)
    if choice == "Booking Ticket":
        menu_1 = ["Insert", "Delete", "Display", "Update"]
        choice_1 = st.sidebar.selectbox("Booking choices", menu_1)
        if choice_1 == "Insert":
            st.write("Pick a stadium from the given options")
            stadium_chosen = insert_stadium()
            st.write("Insert user details: ")
            user_chosen = insert_user()
            st.write("Pick the match to attend in stadium")
            match_chosen = insert_match(stadium_chosen)
            st.write("Pick the seat")
            seat_chosen = insert_seat(stadium_chosen)
            st.write("Order food")
            food_chosen = insert_food()  # function independent of any others
            if(st.button("Generate ticket")):
                generate_ticket(stadium_chosen, match_chosen, user_chosen,
                                seat_chosen, food_chosen)
        if choice_1 == "Delete":
            st.write("Delete row from the table")
            delete()
        if choice_1 == "Display":
            st.write("Display tables")
            display()
        if choice_1 == "Update":
            st.write("Update any table")
            update_fn()


main()
