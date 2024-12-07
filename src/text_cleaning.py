from bs4 import BeautifulSoup

def clean_html(html_content):
    """
    Cleans the raw HTML content by extracting the text and removing all HTML tags.

    Args:
        html_content (str): The raw HTML content to be cleaned.

    Returns:
        str: The cleaned text extracted from the HTML content, with extra whitespace removed.
    """
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract the text from the parsed HTML, separating elements with a space and stripping extra whitespace
    text = soup.get_text(separator=" ", strip=True)
    
    return text
