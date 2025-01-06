import pandas as pd
import streamlit as st

# Title of the app
st.title("Data Search Application")

# File path
file_path = "vertopal.com_8 years op items details..csv"  # Update with the correct path to your file

# Load the file into a DataFrame
df = pd.read_csv(file_path)



# Input fields for search criteria
st.subheader("Search Criteria")
article_code = st.text_input("Enter Article Code")
item_description = st.text_input("Enter Item Description")
supplier_name = st.text_input("Enter Supplier Name")

# Search button
if st.button("Search"):
    # Filter the dataset based on input criteria
    filtered_data = df

    if article_code:
        filtered_data = filtered_data[filtered_data['Artical Code'].str.contains(article_code, case=False, na=False)]
    if item_description:
        filtered_data = filtered_data[filtered_data['Item Description'].str.contains(item_description, case=False, na=False)]
    if supplier_name:
        filtered_data = filtered_data[filtered_data['Supplier Name'].str.contains(supplier_name, case=False, na=False)]

    # Display the filtered results
    st.subheader("Search Results")
    if not filtered_data.empty:
        st.dataframe(filtered_data)
    else:
        st.write("No results found.")
