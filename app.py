import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="AgentForge RL")

st.title("🚀 AgentForge RL")
st.subheader("Autonomous AI Agent Infrastructure")

st.write("MCP Server + SQLite Environment Running Successfully")

# Connect database
conn = sqlite3.connect("company.db")

# Load employees
query = "SELECT * FROM employees"

try:
    df = pd.read_sql_query(query, conn)

    st.write("## Employee Database")
    st.dataframe(df)

except Exception as e:
    st.error(f"Error: {e}")

conn.close()

st.success("MCP Environment Active")
