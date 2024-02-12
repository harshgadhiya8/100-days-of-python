import smtplib
import datetime as dt
import random

email = 'hitpatel677@gmail.com'
password = "****************"

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=email,password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs=email,
#         msg='Subject:Hello\n\n This is test mail')
#     connection.close()

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open('quotes.txt') as quote_file:
        all_quoates = quote_file.readlines()
        quote = random.choice(all_quoates)
    print(quote)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f'Subject:Monday Motivation\n\n {quote}')
        connection.close()