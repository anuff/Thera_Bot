import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("Thera Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    chain = get_qa_chain()

    response = chain(prompt)    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response['result'])
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response['result']})

##from langchain_helper import get_qa_chain, create_vector_db
##st.title("Codebasics Q&A 🌱")
##btn = st.button("Create Knowledgebase")
##if btn:
##    create_vector_db()
##
##question = st.text_input("Question: ")
##
##if question:
##    chain = get_qa_chain()
##    response = chain(prompt)
##
##    st.header("Answer")
##    st.write(response["result"])






