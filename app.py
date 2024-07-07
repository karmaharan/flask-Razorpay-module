import os
import razorpay
from flask import current_app

def verify_razorpay_payment(payment_id):
    try:
        # GET KEYS FROMhttps://dashboard.razorpay.com/app/website-app-settings/api-keys
        # Initialize the Razorpay client with credentials from environment variables
        client = razorpay.Client(auth=("KEY_ID", "LIVE_KEY"))

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
