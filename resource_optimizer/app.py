import streamlit as st
from db import create_table, insert_item, fetch_items
from optimizer import optimize_allocation

st.title("📊 Business Resource Optimizer")

create_table()

with st.form("add_item"):
    item = st.text_input("Item Name")
    price = st.number_input("Unit Price", min_value=0.0)
    max_qty = st.number_input("Max Quantity Available", min_value=0)
    submitted = st.form_submit_button("Add Item")
    if submitted:
        insert_item(item, price, max_qty)
        st.success(f"Added {item}")

st.subheader("📦 Current Items in Inventory")
data = fetch_items()
st.table(data)

st.subheader("💰 Enter Your Budget")
budget = st.number_input("Total Budget", min_value=0.0)

if st.button("Run Optimization"):
    if data:
        result = optimize_allocation(data, budget)
        st.success("✅ Optimization Complete")
        st.write("Optimal Purchase Plan:")
        st.json(result)
    else:
        st.warning("⚠️No data to optimize")
