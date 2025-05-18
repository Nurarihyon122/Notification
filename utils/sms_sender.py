from twilio.rest import Client

def send_sms(to, message):
    client = Client("TWILIO_SID", "TWILIO_AUTH")
    client.messages.create(to=to, from_="+123456789", body=message)
