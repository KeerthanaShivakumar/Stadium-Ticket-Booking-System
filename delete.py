import streamlit as st
import pandas as pd
from functions import *
from display import *


def delete():
    # choose a table to delete from
    selected_table = st.selectbox("Select a table to delete data from: ", [
                                  "stadium", "matches", "users", "food", "seat_matrix", "ticket"])
    st.subheader("Current data in {} table".format(selected_table))
    # show table here
    item_id = [i[0] for i in get_id(selected_table)]
    selected_row = st.selectbox("Select the row to delete", item_id)
    st.warning("Do you want to delete item {}?".format(selected_row))
    if st.button("Delete chosen row"):
        delete_item(selected_row, selected_table)
        st.success("Item {} deleted successfully".format(selected_row))
        st.write("Go to display menu to see the current data after deletion")
