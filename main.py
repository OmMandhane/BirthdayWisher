##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import datetime as dt
import numpy as np
import random


app_password = "dummy_password_using_google_app"
my_email = "ENTER_YOUR_EMAIL_HERE@gmail.com" 

# 2. Check if today matches a birthday in the birthdays.csv
df = pd.read_csv("birthdays.csv")
date_list = df.iloc[:,3:5].values
today = dt.datetime.now()
month_day = [today.month,today.day]
todayisbirthday = False
for idx, value in enumerate(date_list):
    value = value.tolist()
    if value == month_day:
        index = idx
        todayisbirthday = True
        break


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if todayisbirthday:  
    sr = df.iloc[index]
    name = sr["name"]
    email = sr["email"]
    lettertemplate = f"letter_templates\letter_{random.randint(1,3)}.txt"
    with open(lettertemplate,'r') as template:
        letter = template.read()
        letter = letter.replace("[NAME]",name)
        

# 4. Send the letter generated in step 3 to that person's email address.
if todayisbirthday:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday from your dearest!!\n\n{letter}"
        )
        





