import streamlit as st
import pandas as pd
from functions import *


def display():

    st.subheader("Stadium")
    stadium_table = view_table("stadium")
    st.dataframe(pd.DataFrame(stadium_table, columns=stadium_cols))

    st.subheader("Matches")
    match_table = view_table("matches")
    st.dataframe(pd.DataFrame(match_table, columns=matches_cols))

    st.subheader("Users")
    user_table = view_table("users")
    st.dataframe(pd.DataFrame(user_table, columns=users_cols))

    st.subheader("Food")
    food_table = view_table("food")
    st.dataframe(pd.DataFrame(food_table, columns=food_cols))

    st.subheader("Seat")
    seat_table = view_table("seat_matrix")
    st.dataframe(pd.DataFrame(seat_table, columns=seat_matrix_cols))

    st.subheader("Ticket")
    ticket_table = view_table("ticket")
    st.dataframe(pd.DataFrame(ticket_table, columns=ticket_cols))
