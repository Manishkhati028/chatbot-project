from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Create a Flask app
app = Flask(__name__)

#@app.route("/", methods=["GET"])
#def home():
    #return "Welcome to the WhatsApp Bot!"

# Define a route for the WhatsApp webhook
@app.route("/whatsapp", methods=["GET"])
def whatsapp_reply():
    # Get the message the user sent
    incoming_msg = request.values.get('Body', '').lower()
    
    # Create a Twilio Messaging Response object
    response = MessagingResponse()
    message = response.message()

    # Respond based on the user's message
    if 'hello' in incoming_msg:
        message.body("Hi! How can I assist you today?\n1. View available cars\n2. Schedule a test drive\n3. Speak to a sales rep")
    elif '1' in incoming_msg:
        message.body("We have the following cars available:\n- Sedan\n- SUV\n- Hatchback\nReply with the car model you're interested in.")
    elif '2' in incoming_msg:
        message.body("Please provide your preferred date and time for the test drive.")
    elif '3' in incoming_msg:
        message.body("A sales representative will contact you shortly.")
    else:
        message.body("Sorry, I didn't understand that. Please reply with a valid option.")

    # Return the response to Twilio
    return str(response)

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
