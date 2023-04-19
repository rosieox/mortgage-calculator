import streamlit as st
import pandas as pd
import numpy as np

from calculate_repayments import get_monthly_mortgage_payment

st.title('Mortgage repayment calculator')

st.text_input("House value (£):", value="450000",key="house_val")

st.text_input("Deposit amount (£):", value="50000",key="deposit")

st.text_input("Interest rate. State this as a decimal e.g. 5\% should be written as 0.05.",value="0.05", key="annual_interest")

st.text_input("Length of loan in years:", value="25",key="length_of_loan")

house_val = float(st.session_state.house_val)
deposit = float(st.session_state.deposit)
length_of_loan = int(st.session_state.length_of_loan)
annual_interest = float(st.session_state.annual_interest)

monthly = get_monthly_mortgage_payment(house_val = house_val, deposit = deposit, length_of_loan = length_of_loan, annual_interest = annual_interest)

total_repayments = monthly * length_of_loan * 12

interest_paid = total_repayments - house_val

st.write("Your monthly repayments will be £", monthly, ". Over time you will pay back a total of £", total_repayments, ". That means you will pay back £", interest_paid, " on top of the value of the house.")