import smtplib

to = input("Enter The Recivers Mail id")
message = input("Enter The Message you want to send")

def sendemail(to,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('senderemail','password')    # replace the sendermail  and password with the details you wanted to send email from
    server.sendmail(senderemail,to,message)
    server.close()

sendemail(to,message)