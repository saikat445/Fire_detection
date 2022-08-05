import os
from twilio.rest import Client

sid = 'AC9ece4c25a05cfe7b7950b0a3a9605e03'
authToken = '42e3afb5724b99386a7d179bfbfa9efe'
client  = Client(sid, authToken)
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919239161126'

client.messages.create(
                       body= " wish you a good day",
                       from_=from_whatsapp_number,
                       to = to_whatsapp_number
                        )


