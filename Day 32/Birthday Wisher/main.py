import smtplib
import datetime as dt
import pandas as pd
import random
birthday = pd.read_csv('./birthdays.csv')
today = dt.datetime.now()
today_tuple = (today.month,today.day)
email = 'hitpatel677@gmail.com'
password = "************"

new_dict = {(data_row['month'],data_row['day']): data_row for (index,data_row) in birthday.iterrows()}

if today_tuple in new_dict:
    birthday_person = new_dict[today_tuple]
    file_path = f".\\letter_templates\\letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person['name'])
    
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(email,password)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")


