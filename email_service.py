import smtplib


def sending_email(message):
    try:
        #Replace these with your email and password 
        my_gmail = 'create an gmail for bot'
        password = 'password of that gmail'

        # Create the email message
        message['From'] = my_gmail
        message['To'] = 'someone@gmail.com'   
        
        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=password)
            connection.send_message(message)

            
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate.Check your email and password.")

    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")