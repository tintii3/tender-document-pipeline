from src.pipeline import run_pipeline

if __name__ == "__main__":
    """
    Main entry point for executing the data extraction pipeline for a specific document.

    This script sets a document ID and calls the `run_pipeline` function to process the document,
    retrieve its content, clean the text, extract key information using an NLP model, and save the
    results to a JSON file.

    The document ID is hardcoded as "01_tender_doc" but can be adjusted to any valid document ID.

    If run as a script, this will trigger the pipeline for the specified document ID.
    """
    # Set the document ID to be processed
    document_id = "01_tender_doc"
    
    # Execute the pipeline to process the document
    run_pipeline(document_id)
