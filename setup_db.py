import sqlite3
from config import DATABASE_PATH

def create_table():
    """
    Establishes a connection to the SQLite database and creates a table for tender documents.

    The table includes the following columns:
    - ID: A unique identifier for each document (Primary Key).
    - HTML_Text: Stores the raw HTML content of the document.

    If the table already exists, this function ensures it is not recreated.
    """
    # Connect to the SQLite database using the path from the configuration file
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Create the tender_documents table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tender_documents (
        ID TEXT PRIMARY KEY,      -- Unique identifier for the document
        HTML_Text TEXT            -- Raw HTML content of the document
    )
    ''')

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    # Execute the function to create the table and notify the user
    create_table()
