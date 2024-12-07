import sqlite3
from config import DATABASE_PATH

def get_html_by_id(document_id):
    """
    Fetches the raw HTML content of a tender document based on its unique ID.

    Args:
        document_id (str): The unique identifier of the document whose HTML content is to be retrieved.

    Returns:
        str: The raw HTML content of the document if found.

    Raises:
        ValueError: If no document with the specified ID is found in the database.
    """
    # Connect to the SQLite database using the path from the configuration file
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    # Query the database to fetch HTML content for the given document ID
    cursor.execute("SELECT HTML_Text FROM tender_documents WHERE ID=?", (document_id,))
    result = cursor.fetchone()
    
    # Close the connection to the database
    connection.close()
    
    if result:
        return result[0]
    else:
        raise ValueError(f"Document with ID {document_id} not found.")

def retrieve_all_documents():
    """
    Fetches and prints all tender documents stored in the database.

    This function retrieves each document's ID and HTML content, then prints them.
    """
    # Connect to the SQLite database using the path from the configuration file
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    # Retrieve all documents from the tender_documents table
    cursor.execute("SELECT * FROM tender_documents")
    rows = cursor.fetchall()
    
    # Print the details of each document (ID and HTML content)
    for row in rows:
        print(f"ID: {row[0]}, HTML Text: {row[1]}")
    
    # Close the connection to the database
    connection.close()
