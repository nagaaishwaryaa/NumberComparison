import streamlit as st
import pandas as pd
import altair as alt

st.title("🔢 Integer Number Comparator with Graph")

# Integer input using number_input
num1 = st.number_input("Enter the first number (integer):", step=1, format="%d")
num2 = st.number_input("Enter the second number (integer):", step=1, format="%d")

# Compare and show results
if st.button("Compare"):
    if num1 > num2:
        st.success(f"{num1} is greater than {num2}")
    elif num1 < num2:
        st.warning(f"{num1} is smaller than {num2}")
    else:
        st.info(f"Both numbers are equal: {num1}")

    # Create and display bar chart
    df = pd.DataFrame({
        'Number': ['First Number', 'Second Number'],
        'Value': [num1, num2]
    })

    chart = alt.Chart(df).mark_bar().encode(
        x='Number',
        y='Value',
        color='Number'
    ).properties(title="📊 Number Comparison")

    st.altair_chart(chart, use_container_width=True)
