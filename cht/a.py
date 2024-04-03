import os
import PyPDF2
import docx
import csv
import textract
import re
from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Function to extract text from PDF files
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to extract text from DOCX files
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

# Function to extract text from TXT files
def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

# Function to extract text from CSV files
def extract_text_from_csv(file_path):
    text = ""
    with open(file_path, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            text += ' '.join(row) + '\n'
    return text

# Preprocess text: tokenize, remove stopwords, and lemmatize
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Search for relevant information based on user query
def search_query_in_text(query, text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    matching_sentences = []
    for sentence in sentences:
        if query.lower() in sentence.lower():
            matching_sentences.append(sentence)
    return matching_sentences

# Main function
def main():
    file_path = input("Enter the path to the file (PDF, DOCX, TXT, or CSV): ")
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif file_extension == '.docx':
        text = extract_text_from_docx(file_path)
    elif file_extension == '.txt':
        text = extract_text_from_txt(file_path)
    elif file_extension == '.csv':
        text = extract_text_from_csv(file_path)
    else:
        print("Unsupported file format.")
        return

    preprocessed_text = preprocess_text(text)

    # Use pipeline to load pre-trained model for question answering
    qa_pipeline = pipeline("question-answering")
    
    while True:
        user_query = input("Ask me anything (type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        
        # Analyze user's question and generate answer from the content provided in the file
        answer = qa_pipeline(question=user_query, context=text)
        
        if answer['answer']:
            print("Answer:", answer['answer'])
        else:
            matching_sentences = search_query_in_text(user_query, preprocessed_text)
            if matching_sentences:
                print("Here are some relevant answers:")
                for sentence in matching_sentences:
                    print("-", sentence)
            else:
                print("Sorry, I couldn't find any relevant information.")

if __name__ == "__main__":
    main()
