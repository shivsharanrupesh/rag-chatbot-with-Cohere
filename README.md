# RAG Chatbot with cohere

This is a simple chatbot application that leverages the Cohere API for text embedding, document retrieval, and conversation generation.

## Setup

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

Make sure to create a virtual environment if needed.

2. Set up .env-File (adding COHERE API KEY)

COHERE_API_KEY=your_cohere_api_key

3. Run the application

   ```bash
   python app.py


## Files

### 'app.py'

This file contains the main application logic. It initializes a chatbot using the Cohere API and allows users to interact with the chatbot through the command line.

### 'cohere_chatbot.py'

This file defines two classes: **Documents** and **Chatbot**. The **Documents** class loads, embeds, and indexes documents for efficient retrieval. The **Chatbot** class generates responses based on user input and retrieves relevant documents using the **Documents** class.

## Usage

1. Run the **app.py** file to start the chatbot application.
2. Enter your messages in the command line, and the chatbot will respond based on the documents it has indexed.
3. Type "quit" to end the conversation.

## Dependencies

- *Cohere API*: Used for text embedding, document retrieval, and conversation generation.
- *python-dotenv*: Used for loading environment variables from a .env file.
- *hnswlib*: Used for efficient k-NN search.

## Additional Resources

[Cohere's Guide to Build a RAG-Powered Chatbot with Chat, Embed, and Rerank](https://txt.cohere.com/rag-chatbot/)

