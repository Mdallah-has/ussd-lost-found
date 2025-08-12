from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd_callback():
    session_id = request.values.get("sessionId")
    phone_number = request.values.get("phoneNumber")
    text = request.values.get("text", "")

    if text == "":
        response = "CON Welcome to Lost & Found\n1. Report Lost ID\n2. Search ID"
    elif text == "1":
        response = "CON Please enter the ID number:"
    elif text.startswith("1*"):
        response = "END Thank you. Your report has been submitted."
    else:
        response = "END Invalid option."

    return response, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run()
 USSD backend in Python
