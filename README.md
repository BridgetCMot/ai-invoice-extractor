**AI-Powered Invoice Information Extractor**



**Project Overview**



The purpose of the present project is developing a program which will use Gemini AI API by Google to extract invoice document data in Python.



The software will process invoice data, extract relevant information and validate the result using Pydantic and save it to a JSON file.



API to extract structured information from invoice documents.



The application processes invoice text, extracts relevant information and validates the results using Pydantic before saving the output as a JSON file.



**Features**



Integration with Google's Gemini AI API.



Reusable parameterised prompt templates.



Automated invoice information extraction.



Structured JSON response generation.



Data validation using Pydantic.



External text-file input.



Automatic JSON output generation.



**Technologies Used**



Python 3.13



Google Gemini API



Google GenAI Python SDK



Pydantic



JSON



**Information Extracted**



The application extracts the following invoice fields:



Invoice number



Supplier name



Invoice date



Customer name



Total amount



Currency



Payment status



**Project Structure**



datheon-task1/

│

├── main.py

├── invoice.txt

├── invoice\_output.json

├── requirements.txt

├── .gitignore

└── README.md



**Installation**



Clone or download this repository.



Create and activate a Python virtual environment.



Install the required dependencies:



pip install -r requirements.txt



Configure your Gemini API key as an environment variable.



For Windows Command Prompt:



set "GEMINI\_API\_KEY=your\_api\_key\_here"



Run the application:



python main.py



**Output**



The application writes a validated JSON file named invoice\_output.json that contains the extracted invoice information.



**Data Validation**



Pydantic validates the structure and data types of the extracted information. This helps to ensure that the JSON file follows the expected schema.



**Project Purpose**



This project shows how Generative AI can be used in real-world situations. Furthermore, it demonstrates API integration, prompt engineering, structured data extraction and Python data validation. Each part helps build a system that handles information efficiently. The goal is to understand how these technologies work together in practice. It focuses on making sure the data is accurate and the results are reliable.



