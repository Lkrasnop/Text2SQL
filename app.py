#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from main import get_db_chain

st.set_page_config(page_title='Insurance Data Q/A App', page_icon=":bookmark_tabs")
st.title('Insurance Data :red[Q/A app] :open_book:')

# Get the chain
chain = get_db_chain()

question = st.text_input(":violet[Question: ]")

submit = st.button("Submit")
if question and submit:
    try:
        # Run the chain with the question
        response = chain(question)
        
        st.header("Pandas Query")
        st.code(response["query"], language="python")
        
        st.header("Query Result")
        if not response["result"].empty:
            st.dataframe(response["result"])
        else:
            st.write("No results returned from the query.")
        
        st.header("Answer")
        st.write(response["answer"])
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error(f"Error type: {type(e)}")
        st.error(f"Error args: {e.args}")
        st.error("Please try rephrasing your question or ask about a different topic.")

