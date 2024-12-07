import json

def save_to_json(document_id, extracted_data):
    """
    Saves the extracted data associated with a document to a JSON file.

    Args:
        document_id (str): The unique identifier for the document.
        extracted_data (dict): A dictionary containing the data extracted from the document.

    This function creates a JSON file named using the document ID in the 'data/processed/' directory. 
    The JSON file will contain the document's ID along with the extracted data.
    """
    # Create an output dictionary with the document ID and extracted data
    output = {
        "document_id": document_id
    }
    
    # Add each key-value pair from the extracted data to the output
    for key, value in extracted_data.items():
        output[key] = value
    
    # Write the output dictionary to a JSON file
    with open(f"data/processed/{document_id}.json", "w", encoding='utf-8') as json_file:
        json.dump(output, json_file, indent=4, ensure_ascii=False)
