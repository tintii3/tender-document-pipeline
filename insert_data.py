import os
import sqlite3
from config import DATABASE_PATH

def insert_document(document_id, html_content):
    """
    Inserts a new tender document into the SQLite database if it doesn't already exist.

    This function takes the document ID and HTML content, and inserts them into the `tender_documents` table.
    It checks if a document with the same document ID already exists before inserting. 
    If the document ID exists, no insertion will happen.

    Args:
        document_id (str): The unique identifier for the document.
        html_content (str): The raw HTML content of the document to be inserted.
    """
    # Connect to the SQLite database
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Check if the document already exists
    cursor.execute("SELECT 1 FROM tender_documents WHERE ID = ?", (document_id,))
    existing_document = cursor.fetchone()

    if existing_document:
        print(f"Document with ID {document_id} already exists. Skipping insertion.")
    else:
        # Insert the document ID and HTML content into the tender_documents table
        cursor.execute('''
        INSERT INTO tender_documents (ID, HTML_Text) VALUES (?, ?)
        ''', (document_id, html_content))
        
        print(f"Document with ID {document_id} inserted successfully.")

    # Commit the transaction and close the connection
    connection.commit()
    connection.close()

def insert_documents_from_folder():
    """
    Inserts all tender documents from text files in a specified folder into the SQLite database.

    This function loops through all .txt files in a predefined folder, reads each file's content, 
    and inserts it into the database using the `insert_document` function. 
    The document ID is derived from the filename (without extension).

    The folder path is hardcoded inside this function.
    """
    # Define the folder path containing the .txt files (can be modified here)
    folder_path = "data/tender_documents"

    # List all files in the folder
    for file_name in os.listdir(folder_path):
        # Process only .txt files
        if file_name.endswith(".txt"):
            # Create the document ID from the file name (without the extension)
            document_id = os.path.splitext(file_name)[0]
            
            # Full path to the file
            file_path = os.path.join(folder_path, file_name)
            
            # Open the file and read its content
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Insert the document into the database (if not already inserted)
            insert_document(document_id, html_content)

if __name__ == "__main__":
    """
    Main entry point for inserting tender documents into the database from all .txt files in a folder.

    This script processes all .txt files in the specified folder, extracts their content,
    and inserts them into the database with the file name as the document ID.

    If run as a script, it will insert all tender documents from the specified folder.
    """
    # Insert all documents from the folder into the database
    insert_documents_from_folder()
