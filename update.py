import streamlit as st
from functions import *
import pandas as pd


def update_fn():
    # update user table
    table_considered = "users"
    result = view_table(table_considered)
    df = pd.DataFrame(result, columns=users_cols)
    with st.expander("Present {}".format(table_considered)):
        st.dataframe(df)
    list_of_users = [i[0] for i in get_id(table_considered)]
    selected_user = st.selectbox("Choose User ID to edit", list_of_users)
    selected_result = view_table(table_considered)
    # enter new details
    if selected_user:
        old0 = selected_result[0][0]
        '''st.write(old0, old1, old2, old3)'''

        col1, col2 = st.columns(2)
        with col1:
            new0 = st.text_input("User name")
            new1 = st.text_input("Phone No")
            new2 = st.text_input("Email")

        if st.button("Update User"):
            # call the update function here
            update_user(new0, new1, new2, old0)
            st.success(
                "Successfully updated values for user:: {} to ::{}".format(old0, new0))

    result2 = view_table(table_considered)
    df2 = pd.DataFrame(result2, columns=users_cols)
    with st.expander("Updated data"):
        st.dataframe(df2)
