
import os
from datetime import date
from typing import Literal

from google import genai
from pydantic import BaseModel, Field, ValidationError


# 1. Define the expected JSON structure
class InvoiceData(BaseModel):
    invoice_number: str
    supplier: str
    invoice_date: date | None = None
    customer: str
    total_amount: float | None = Field(default=None, ge=0)
    currency: Literal["ZAR", "USD", "EUR", "GBP", "unknown"]
    payment_status: Literal["paid", "unpaid", "overdue", "unknown"]


# 2. Create a reusable prompt template
PROMPT_TEMPLATE = """
You are an invoice information extraction assistant.

Extract the required information from the invoice below.

Rules:
- Return only information supported by the invoice.
- Do not invent missing information.
- Use null for missing dates, amounts or other optional values.
- Use "unknown" if the currency or payment status cannot be determined.
- Return the date in YYYY-MM-DD format.
- Return the total amount as a number without currency symbols.
- Follow the required JSON structure exactly.

DOCUMENT TYPE: {document_type}

DOCUMENT TEXT:
{document_text}
"""


# 3. Example invoice text
SAMPLE_INVOICE = """
INVOICE

Invoice Number: INV-2026-1045
Supplier: ABC Office Supplies (Pty) Ltd
Invoice Date: 2026-10-15
Customer: Datheon Technologies
Description: Computer equipment and accessories
Subtotal: R 8,500.00
VAT: R 1,275.00
Total Amount Due: R 9,775.00
Currency: ZAR
Payment Status: Unpaid
"""


# 4. Connect to Gemini
def create_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY was not found. Please configure your API key."
        )

    return genai.Client(api_key=api_key)


# 5. Extract and validate invoice information
def extract_invoice(document_text: str) -> InvoiceData:

    client = create_client()

    prompt = PROMPT_TEMPLATE.format(
        document_type="Invoice",
        document_text=document_text
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": InvoiceData,
        },
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    # Validate Gemini's JSON response using Pydantic
    invoice = InvoiceData.model_validate_json(response.text)

    return invoice


# 6. Run the application

def main():

    try:
        print("\nProcessing invoice...\n")

        with open("invoice.txt", "r", encoding="utf-8") as file:
            invoice_text = file.read()

        invoice = extract_invoice(invoice_text)

        # Convert validated data into formatted JSON
        validated_json = invoice.model_dump_json(indent=2)

        print("VALIDATED INVOICE DATA")
        print("---------------------")
        print(validated_json)

        # Save JSON output to a file
        with open(
            "invoice_output.json",
            "w",
            encoding="utf-8"
        ) as file:
            file.write(validated_json)

        print("\nSuccess! JSON saved to invoice_output.json")

    except ValidationError as error:
        print("\nJSON validation failed:")
        print(error)

    except Exception as error:
        print("\nAn error occurred:")
        print(error)


if __name__ == "__main__":
    main()
