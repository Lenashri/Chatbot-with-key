import streamlit as st
import openai
import pandas as pd


df = pd.read_csv('n_movies.csv')

openai.api_key = 'your api key'


st.title("Movie Dataset Agent")
st.write("Ask me anything about the movies in the dataset!")

user_query = st.text_input("Enter your query:")

if user_query:
   
    sample_data = df.head(5).to_string(index=False)
    messages = [
        {"role": "system", "content": "You are an assistant for a movie dataset."},
        {"role": "user", "content": f"Here is a sample from the dataset:\n{sample_data}"},
        {"role": "user", "content": f"Answer this query: {user_query}"},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini", 
        messages=messages,
    ).choices[0].message["content"].strip()

    st.write("Response:", response)





