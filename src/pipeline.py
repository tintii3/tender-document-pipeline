from src.database import get_html_by_id
from src.text_cleaning import clean_html
from src.nlp_model import extract_properties_with_gpt
from src.utils import save_to_json

def run_pipeline(document_id):
    """
    Executes the complete data extraction pipeline for a given document ID.

    This function performs the following steps:
    1. Retrieves the raw HTML content of the document using `get_html_by_id`.
    2. Cleans the HTML content by extracting the text using `clean_html`.
    3. Uses an NLP model (`extract_properties_with_gpt`) to extract key information from the cleaned text.
    4. Saves the extracted data as a JSON file using `save_to_json`.

    Args:
        document_id (str): The unique identifier for the document to process.

    This function does not return anything. It processes the document and saves the extracted 
    information to a JSON file.
    """
    # Step 1: Retrieve the raw HTML content of the document
    html_content = get_html_by_id(document_id)
    
    # Step 2: Clean the HTML content to extract meaningful text
    cleaned_text = clean_html(html_content)
    
    # Step 3: Use GPT to extract properties from the cleaned text
    extracted_data = extract_properties_with_gpt(cleaned_text)
    
    # Step 4: Save the extracted data to a JSON file
    save_to_json(document_id, extracted_data)
