# .env libs
import os
from dotenv import load_dotenv
load_dotenv()

# chatbot class import
from chatbot import Chatbot
from chatbot import Documents

import streamlit as st

# Define sources
sources = [
    {
        "title": "Text Embeddings", 
        "url": "https://docs.cohere.com/docs/text-embeddings"},
    {
        "title": "Similarity Between Words and Sentences", 
        "url": "https://docs.cohere.com/docs/similarity-between-words-and-sentences"},
    {
        "title": "The Attention Mechanism", 
        "url": "https://docs.cohere.com/docs/the-attention-mechanism"},
    {
        "title": "Transformer Models", 
        "url": "https://docs.cohere.com/docs/transformer-models"}   
]

class StreamlitApp:
    def __init__(self, chatbot: Chatbot):
        """
        Initializes an instance of the App class.

        Parameters:
        chatbot (Chatbot): An instance of the Chatbot class.

        """
        self.chatbot = chatbot
    
    def run(self):
        """
        Runs the chatbot application using Streamlit

        """
        st.title("RAG Chatbot App")

        while True:
            # Get the user message
            message = st.text_input("Enter some text 👇", key="userinput")

            # Typing "quit" ends the conversation
            if message.lower() == "quit":
                st.text("Ending chat.")
                break
            else:
                st.text(f"User: {message}")

            # Get the chatbot response
            response = self.chatbot.generate_response(message)

            # Print the chatbot response
            st.text("Chatbot:")
            flag = False
            for event in response:
                # Text
                if event.event_type == "text-generation":
                    st.markdown(event.text)

                # Citations
                if event.event_type == "citation-generation":
                    if not flag:
                        st.text("\n\nCITATIONS:")
                        flag = True
                    print(event.citations)

            st.text(f"\n{'-'*100}\n")

if __name__ == "__main__":
    # Assuming Chatbot class has a generate_response method
    documents = Documents(sources)
    chatbot = Chatbot(documents)
    app = StreamlitApp(chatbot)
    app.run()