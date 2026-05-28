import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="AgentForge RL")

st.title("🚀 AgentForge RL")
st.subheader("AI Database Agent")

st.write("Ask questions about the company database")

# User input
user_query = st.text_input("Ask something")

# Connect DB
conn = sqlite3.connect("company.db")

# Simple AI logic
def generate_sql(query):

    query = query.lower()

    if "employees" in query:
        return "SELECT * FROM employees"

    elif "departments" in query:
        return "SELECT * FROM departments"

    else:
        return None

# Button
if st.button("Run Agent"):

    sql = generate_sql(user_query)

    if sql:

        st.write("### Generated SQL")
        st.code(sql, language="sql")

        try:
            df = pd.read_sql_query(sql, conn)

            st.write("### Results")
            st.dataframe(df)

        except Exception as e:
            st.error(f"Database Error: {e}")

    else:
        st.warning("Agent could not understand the request")

conn.close()

st.success("Agent System Active")
