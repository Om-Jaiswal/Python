import smtplib

my_email = "omjaiswal@gmail.com"
password = "(s66@bd6vg$3$"

with smtplib.SMTP("stmp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
    	from_addr=my_email,
    	to_addrs="omjaiswal@yahoo.com",
    	msg="Subject:Hello\n\nThis is the body of my email."
    )

# connection = smtplib.SMTP("stmp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="omjaiswal@yahoo.com",
#     msg="Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()

# Working with datetime Module

# import datatime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=2001, month=05, day=23, hour=4)
# print(date_of_birth)