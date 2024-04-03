# chatbot
This Python script is designed to extract text from various types of files (PDF, DOCX, TXT, CSV), preprocess the text, and then allow users to ask questions about the content of the file. It utilizes libraries such as PyPDF2, docx, csv, textract, and transformers for natural language processing tasks.

Import Statements: Import necessary libraries such as os, PyPDF2, docx, csv, textract, re, and nltk.

NLTK Setup: Download necessary NLTK resources like punkt, stopwords, and wordnet.

Text Extraction Functions:

Functions like extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt, and extract_text_from_csv are defined to extract text from different types of files using various libraries like PyPDF2, docx, and csv.
Text Preprocessing Function:

The preprocess_text function tokenizes the text, removes stopwords, and lemmatizes the words to prepare the text for better analysis.
Search Query in Text Function:

The search_query_in_text function searches for relevant sentences in the text based on a user's query.
Main Function:

The main function prompts the user to enter the path to the file they want to analyze.
Based on the file extension, it selects the appropriate function to extract text from the file.
Then, it preprocesses the extracted text.
It uses the Hugging Face pipeline to load a pre-trained model for question-answering.
It continuously prompts the user to ask questions until they type 'exit'.
For each question, it either generates an answer using the pre-trained model or searches for relevant sentences in the text if the model fails to generate an answer.
Entry Point Check:

The if __name__ == "__main__": block ensures that the main function is only executed if the script is run directly, not if it's imported as a module.
Overall, the script provides a simple interactive interface for users to ask questions about the content of various types of files, and it attempts to provide relevant answers based on the information in the files.
