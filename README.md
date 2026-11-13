### **AI-Powered Invoice Information Extractor**



##### **Project Overview**

#### 

The system of manually processing invoices can be lengthy and tedious. This project examines how Generative AI can be used to automate the extraction of invoice details. The objective is to maintain a consistent, structured output format.



The software will read invoice details from a text file, extract relevant information and validate the result using Pydantic and save it to a JSON file.





The application processes invoice text, extracts relevant information and validates the results using Pydantic before saving the output as a JSON file.



###### **Features**



Integration with Google's Gemini AI API.



AI-powered information extraction using Google Gemini to identify important invoice details



Reusable parameterised prompt templates.



Automated invoice information extraction.



Structured JSON response generation.



Data validation using Pydantic.



External text-file input.



Automated output generation.



Automatic JSON output generation.



API key security



###### **Technologies Used**

###### 

Python 3.13 - Application development



Google Gemini API - AI-powered invoice information extraction



Google GenAI SDK - Communication with the Gemini API



Pydantic - Structured data modelling and validation



JSON - Structured output format



Git and GitHub - Version control and project hosting



###### **Processing Workflow**



**Input:** The application reads invoice information from invoice.txt.



**Prompt preparation:** The invoice content is inserted into a reusable prompt template.



**AI processing:** Google Gemini analyses the invoice and extracts the required information.



**Data validation:** Pydantic validates the response against the predefined InvoiceData model.



**Output:** The validated information is converted into formatted JSON and saved to invoice\_output.json.



###### **Information Extracted**

##### 

The application extracts the following invoice fields:



Invoice number



Supplier name



Invoice date



Customer name



Total amount



Currency



Payment status



**Example Output**



{

&#x20; "invoice\_number": "INV-2026-2048",

&#x20; "supplier": "Limpopo Office Solutions (Pty) Ltd",

&#x20; "invoice\_date": "2026-08-05",

&#x20; "customer": "ABC Technologies",

&#x20; "total\_amount": 13800.0,

&#x20; "currency": "ZAR",

&#x20; "payment\_status": "unpaid"

}



###### **Project Architecture**



The application follows a simple processing pipeline:



Invoice Text File

&#x20;      |

&#x20;      v

Read Invoice Content

&#x20;      |

&#x20;      v

Parameterized Prompt Template

&#x20;      |

&#x20;      v

Google Gemini API

&#x20;      |

&#x20;      v

AI-Generated JSON Response

&#x20;      |

&#x20;      v

Pydantic Validation

&#x20;      |

&#x20;      v

Validated Invoice Data

&#x20;      |

&#x20;      v

invoice\_output.json



###### **Project Structure**



ai-invoice-extractor/

│

├── main.py

├── invoice.txt

├── invoice\_output.json

├── requirements.txt

├── README.md

└── .gitignore



###### **Installation**



1. **Clone the repository.**

git clone https://github.com/BridgetCMot/ai-invoice-extractor.git



**2. Navigate to the project directory**

cd ai-invoice-extractor



**3. Create and activate a virtual environment**

python -m venv .venv



Windows Command Prompt:



.venv\\Scripts\\activate



**4. Install the required dependencies:**

pip install -r requirements.txt



**5. Configure the Gemini API key and run the application**

Obtain an API key through Google AI Studio.



Set the API key as an environment variable in Windows Command Prompt:



set "GEMINI\_API\_KEY=YOUR\_API\_KEY"



Replace YOUR\_API\_KEY with your actual API key.



Run the application:



python main.py



**Security note:** Never hardcode API keys in source code or commit them to GitHub.



###### **Screenshots**



**1. Application Execution**



This screenshot shows the application running successfully and extracting invoice information using Google Gemini.



**2. JSON Output**



This screenshot shows the structured invoice information generated and validated by the application.



###### **Data Validation and limitations**



Pydantic validates the structure and types of the extracted information, including required fields, permitted currency values and payment statuses.



However, structural validation does not independently guarantee that every extracted value is factually correct. AI-generated information should therefore be checked against the original invoice, particularly in financial processing environments.



The current implementation processes text-based invoice content rather than directly extracting information from PDF or image files.

###### 

###### **Skills Demonstrated**



Python programming and application development.



Generative AI and API integration.



Prompt engineering and parameterized templates.



Structured data extraction.



JSON processing and validation.



Error handling and input management.



Version control using Git and GitHub.



###### **Future Improvementsx**

###### 

Potential enhancements include:



Support for PDF and image-based invoices.



Batch processing of multiple invoices.



Improved extraction accuracy and verification.



Automated invoice classification.



Database integration for storing extracted records.



A graphical user interface for easier document processing.



**Author**



**Bridget Mothapo**



**BCom Business Informatics Graduate | BSc Honours in Computing Student**



**GitHub: @BridgetCMot**

