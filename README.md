Tender Document Pipeline

This project is designed to process tender documents, extract key information from them, and store the results in a SQLite database. It includes multiple functionalities, including running the pipeline for individual documents or for all documents at once.

Project Setup
1. Clone the Repository
First, clone this repository to your local machine:


`git clone https://github.com/your-username/tender-document-pipeline.git`
`cd tender-document-pipeline`
2. Install Requirements
Install the required dependencies by running:

`pip install -r requirements.txt`
This will install all the necessary packages, including the ones for working with databases, APIs, and text processing.

3. Set Up the .env File
You need to set up environment variables for your project. Copy the .env.example file to .env:


`cp .env.example .env`
Then, open the .env file and add your credentials and database path:

OPENAI_API_KEY=your_openai_api_key_here
DATABASE_PATH=path_to_your_database_here
OPENAI_API_KEY: Get this key by creating an account on OpenAI and navigating to your API key section.
DATABASE_PATH: The path to your SQLite database (e.g., tender_documents.db).
4. Running the Pipeline
To Process a Single Document:
You can process a single document by running the run_pipeline.py file:

`python run_pipeline_to_all.py`
This script will:

Set up the SQLite database and create the required table if it doesn't exist.
Insert all the documents from a folder into the database (only if the data has not been inserted previously).
Run the pipeline for each document in the database.
If the database and table do not exist, it will be created automatically.

`python run_pipeline.py`
In this script, the document ID is hardcoded as 01_tender_doc. You can change the document ID to any valid one if necessary. This script will fetch the document content, clean the text, run the NLP model to extract key information, and save the result to a JSON file.

To Process All Documents in the Database:
If you want to process all the documents in the database, use the run_pipeline_to_all.py script:


5. Example Files
.env.example: This file shows the format for setting up your .env file. Copy this file to .env and add your own values.
run_pipeline.py: Use this file to process a single document.
run_pipeline_to_all.py: Use this file to process all documents from the database.
6. Database and Document Insertion
When you run run_pipeline_to_all.py, it will check if the database exists. If it doesn't, the script will create the database and table.
If any documents are not yet inserted into the database, the script will insert them automatically from the data/tender_documents/ folder.
The document ID is automatically derived from the filenames (e.g., 01_tender_doc.txt becomes the ID 01_tender_doc).
7. Example Workflow
Clone the repo and install the requirements.
Set up the .env file with your credentials.
Run the run_pipeline_to_all.py to process all documents and insert them into the database if necessary.
Optionally, run run_pipeline.py to process an individual document.
