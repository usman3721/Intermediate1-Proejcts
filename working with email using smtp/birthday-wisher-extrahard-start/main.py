##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

import datetime as dt
import pandas as pd
from random import randint
import smtplib
from twilio.rest import Client
import os

e_mail="abuzaydin007@gmail.com"
password="yzgnzeiarkhkixtu"


current=dt.datetime.now()
month=current.month
year=current.year
day=current.day

twilio_number="+13149072367"
account_sid="ACff0202bcce08e3851df06bbf8227d587"
auth_token="5b60630f58479b641e757405f050f632"



data={
    "name":["MUM"],
    "email":["abuzaydin007@gmail.com"],
    "year":[year],
    "month":[month],
    "day":[day]
}

updated_data=pd.DataFrame(data)
# updated_data.to_csv(r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\working with email using smtp/birthday-wisher-extrahard-start/birthdays.csv",mode="a",index=False,header=False)
today=(month,day)
birthday_file=pd.read_csv(r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\working with email using smtp/birthday-wisher-extrahard-start/birthdays.csv")


birthday_dcit={(data_row["month"],data_row["day"]) :data_row for (index,data_row) in updated_data.iterrows()}

if today in birthday_dcit:
    birthday_person=birthday_dcit[today]
    file_path=rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\working with email using smtp/birthday-wisher-extrahard-start/letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as file_letter:
        content=file_letter.read()
        contents=content.replace("[NAME]",birthday_person["name"])
        #USING TWILIO FOR TO RECEIVE MESSAGE
        # account_sid = os.environ["ACff0202bcce08e3851df06bbf8227d587"]
        # auth_token = os.environ['5b60630f58479b641e757405f050f632']
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"{contents}",
                from_="+13149072367",
                to="+2348024230513"
        )

        print(message.status)
        # print(contents)
    # with smtplib.SMTP("smtp.gmail.com",587) as connection:
    #     connection.starttls()
    #     connection.login(user=e_mail,password=password)
    #     connection.sendmail(from_addr=e_mail,
    #     to_addrs=e_mail,
    #     msg=f"Subject: Eil iltri greeting \n\n{contents}")
    #     connection.close()
        
    
    


# import os
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'myfile.txt'
   
   



  

# (r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\working with email using smtp/birthday-wisher-extrahard-start/main.py")



# Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15017122661',
#                      to='+15558675310'
#                  )

# print(message.sid)