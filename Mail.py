import smtplib    
sender_mail = 'anidiplaha74@gmail.com'    
receivers_mail = ['anidip.laha@anudip.org']    
message = """From: From Person %s  
To: To Person %s  
Subject: Test Mail	   
Hi Mail Have Been Sent.  
"""%(sender_mail,receivers_mail)    
try:    
   smtpObj = smtplib.SMTP('localhost')    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")  