import smtplib

recipientEmail = "7003977@gmail.com"
recipientEmail = recipientEmail.lower()

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("8001572@gmail.com", 'nmviahzfogghfkdt')
    server.sendmail('8001572@gmail.com', recipientEmail, "Warning A Fire Accident has been reported on ABC Company")
    print("sent to {}".format(recipientEmail))
    server.close()
except Exception as e:
    print(e)