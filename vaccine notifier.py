import requests

from datetime import datetime, timedelta
print("Enter the age which you want to find the vaccine!!")
person_age = int(input())
print("Enter the area you want to find vaccine!!!")
area_pincode = input()
print("total no of days you are finding vaccination slot!!!")
total_days = int(input())
print_flag = 'Y'
print("Start Searching for covid vaccine slots!!!")
current = datetime.today()
form = [current + timedelta(days=i)for i in range(total_days)]
correct_date_format = (i.strftime("%d-%m-%y")for i in form)
while True:
    i = 0
    for find_code in area_pincode:
        for enter_date in correct_date_format:

            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date{}".format(
                find_code, enter_date)
            requirements = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36' }
            final_op = requests.get(url, headers=requirements)
            if final_op.ok:
                file_json = final_op.json()
                flag = False
                if file_json["centers"]:
                    if print_flag.lower() == "y":
                        for place in file_json["centers"]:
                            for availiabilty in place["sessions"]:
                                if (availiabilty["min_age_limit"]<=person_age and availiabilty["availiable_capacity"]>0):
                                    print("pincode for which you are finding:" +find_code)
                                    print("it is available  in :{}".format(enter_date))
                                    print("Name of the hospital and destination is :", place["name"])
                                    print("Name for the block is:", place["block_name"])
                                    print("Price for the vaccine is:", place["fee_type"])
                                    print("Availiablity stattus of the vaccine is:", availiabilty["availiable_capacity"])
                                    if (availiabilty["vaccine"]!= ''):
                                        print("Type of the vaccine is :", availiabilty["vaccine"])
                                    i = i+1
                                else:
                                    pass
                    else:
                        pass
            else:
                print("I found no response!!!")

if i == 0:
    print("Right now no vaccine slots are abliviable!...Try after some time")
else:
    print("The search is finished!")

date_now = datetime.now() + timedelta(minutes = 1)
while datetime.now() < date_now:
    time.sleep(1)




