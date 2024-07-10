

# Flask Razorpay Module

This repository provides a simple Python function to verify payments using the Razorpay API. The function fetches payment details and checks if the payment has been successfully captured.

## Prerequisites

- Python 3.6 or higher
- Flask
- Razorpay Python SDK

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/karmaharan/flask-Razorpay-module
   cd flask-Razorpay-module
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

   Make sure your `requirements.txt` file includes:
   ```
   Flask
   razorpay
   ```

## Setup

1. **Get your Razorpay API keys:**
   - Visit [Razorpay Dashboard](https://dashboard.razorpay.com/app/website-app-settings/api-keys) to obtain your `KEY_ID` and `LIVE_KEY`.

2. **Set up environment variables:**
   - Create a `.env` file in the root directory of your project and add your Razorpay API keys:
     ```
     RAZORPAY_KEY_ID=your_key_id_here
     RAZORPAY_LIVE_KEY=your_live_key_here
     ```

## Usage

1. **Define the `verify_razorpay_payment` function:**

   ```python
   import os
   import razorpay
   from flask import current_app

   def verify_razorpay_payment(payment_id):
       try:
           # Initialize Razorpay client with API keys
           client = razorpay.Client(auth=(os.getenv('RAZORPAY_KEY_ID'), os.getenv('RAZORPAY_LIVE_KEY')))

           # Fetch the payment details
           payment = client.payment.fetch(payment_id)

           # Get the status and amount of the payment
           payment_status = payment.get('status')
           payment_amount = payment.get('amount') / 100  # Amount is typically in paise, convert to rupees

           # Check if the payment has been completed
           if payment_status == 'captured':
               result = f"Payment successful. Amount: {payment_amount} INR"
           else:
               result = f"Payment failed or pending. Status: {payment_status}, Amount: {payment_amount} INR"

           print(f"Verification result for payment {payment_id}: {result}")
           return payment_status == 'captured'

       except Exception as e:
           error_message = f"Error verifying payment {payment_id}: {str(e)}"
           print(error_message)
           current_app.logger.error(error_message)
           return False

   # Example usage:
   payment_id = "your_payment_id_here"
   verify_razorpay_payment(payment_id)
   ```

2. **Run the verification function:**
   - Replace `"your_payment_id_here"` with an actual payment ID and run the script to verify the payment status.

## Logging

- Errors during the verification process will be logged using Flask's `current_app.logger`.
- Ensure Flask is properly configured to handle logging in your application.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or want to add features.

## License

This project is licensed under the MIT License.
