import sqlite3
from insert_data import insert_documents_from_folder
from setup_db import create_table
from src.pipeline import run_pipeline
from config import DATABASE_PATH

def get_all_document_ids():
    """
    Retrieves all document IDs from the tender_documents table in the SQLite database.

    This function connects to the SQLite database, fetches all the document IDs from the `tender_documents`
    table, and returns them as a flat list.

    Returns:
        list: A list of document IDs (strings) fetched from the database.
    """
    # Connect to the SQLite database
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    # Fetch all document IDs from the tender_documents table
    cursor.execute("SELECT ID FROM tender_documents")
    document_ids = cursor.fetchall()  # Fetch all rows as a list of tuples
    
    connection.close()
    
    # Return the list of document IDs (flatten the list of tuples)
    return [doc_id[0] for doc_id in document_ids]

if __name__ == "__main__":
    """
    Main entry point for running the data extraction pipeline for all documents in the database.

    This script retrieves all document IDs from the database and runs the data extraction pipeline
    (`run_pipeline`) for each document.

    If executed as a script, the pipeline will be executed for every document present in the database.
    """

    # Set up the database and table if they don't exist
    create_table()
    
    # Insert documents from the folder (only if necessary)
    insert_documents_from_folder()


    # Get all document IDs from the database
    document_ids = get_all_document_ids()
    
    # Run the pipeline for each document ID
    for document_id in document_ids:
        print(f"Running pipeline for document ID: {document_id}")
        run_pipeline(document_id)
