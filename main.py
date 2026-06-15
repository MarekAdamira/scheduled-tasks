##################### Extra Hard Starting Project ######################
import csv
import smtplib
import random
import datetime as dt
import pandas as pd
import os


now = dt.datetime.now()
today_month = now.month
today_day = now.day

my_email = os.environ.get("my_email")
password = os.environ.get("password")

data = pd.read_csv("birthdays.csv")

"""zde koukam, jestli birthday_person month = today month a to samé pro den"""
birthday_person = data[
    (data["month"] == today_month) &
    (data["day"] == today_day)]

"""zde POKUD birthday_person proměnná není prázdná (tak má narozeniny)
vyberu jméno pomoci birthday_person.iloc[0]["name"]
potom už jen otevřu soubor, vyměním jméno, a odešlu mail"""

#iloc je index location, a vybere jen první řádek z birthday_person, což je jméno
if not birthday_person.empty:
    for index, row in birthday_person.iterrows():
        name = row["name"]
        email = row["email"]
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt","r") as file:
            letter_contents = file.read()
            letter_contents = letter_contents.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(my_email, password)
            smtp.sendmail(from_addr=my_email,
                          to_addrs=email,
                          msg = f"Subject: Happy Birthday!\n\n{letter_contents}")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




