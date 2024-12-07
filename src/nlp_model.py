import openai
from config import API_KEY

# Set up the OpenAI API key for authentication
openai.api_key = API_KEY

def extract_properties_with_gpt(text):
    """
    Extracts key information from a tender document using GPT to generate structured data.

    The function sends the provided document text to the OpenAI GPT model, instructing it to extract
    specific properties from the document. It then processes the model's response and organizes the data
    into a structured dictionary.

    Args:
        text (str): The raw text of the tender document from which properties need to be extracted.

    Returns:
        dict: A dictionary containing the following properties extracted from the document:
            - cpv_code (list): The CPV code(s) associated with the tender.
            - publication_date (list): The date(s) when the tender was published.
            - title (str): The title of the tender.
            - journal_number (str): The journal number of the tender.
            - external_id (list): The Provider ID and year (e.g., '00534910-2024').

    Example:
        {
            "publication_date": ["2024-08-12"],
            "external_id": ["00534910-2024"],
            "cpv_code": ["12345678"],
            "title": "Tender for Construction Services",
            "journal_number": "174/2024"
        }
    """
    # Prepare the messages for the GPT model, including instructions and the document text
    messages = [
        {"role": "system", "content": "You are an assistant that extracts key information from tender documents."},
        {"role": "user", "content": f"""
        Extract the following properties from the tender document and return a structured JSON object:
        1. cpv_code: The CPV code(s) associated with the tender.
        2. publication_date: The date when the tender was published.
        3. title: The title of the tender.
        4. journal_number: The journal number of the tender (e.g., '174/2024').
        5. external_id: The Provider ID, which is a numeric value and the year (e.g., '00534910-2024').
        
        The document is as follows:
        
        {text}
        """
        }
    ]
        
    # Make a request to OpenAI's GPT model to generate the structured data
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=500,
        temperature=0.5
    )
    
    # Extract the response content from the model's output
    extracted_data = response.choices[0].message.content

    # Clean up any unwanted characters like extra quotes or commas
    extracted_data = extracted_data.replace("\"", "").replace(",", "").strip()

    # Initialize the dictionary with expected keys
    extracted_dict = {
        "publication_date": [],
        "external_id": [],
        "cpv_code": [],
        "title": "",
        "journal_number": ""
    }

    # Example parsing based on the cleaned-up response content (you may need to adjust this)
    lines = extracted_data.split("\n")
    for line in lines:
        if "publication_date" in line:
            extracted_dict["publication_date"].append(line.split(":")[1].strip())
        elif "external_id" in line:
            extracted_dict["external_id"].append(line.split(":")[1].strip())
        elif "cpv_code" in line:
            # Handle multiple CPV codes by splitting based on commas or other delimiters
            cpv_codes = line.split(":")[1].strip()
            cpv_code_list = [code.strip() for code in cpv_codes.split(",")]
            extracted_dict["cpv_code"].extend(cpv_code_list)
        elif "title" in line:
            extracted_dict["title"] = line.split(":")[1].strip()
        elif "journal_number" in line:
            extracted_dict["journal_number"] = line.split(":")[1].strip()

    return extracted_dict
