import requests         
from pygame import mixer 
from datetime import datetime, timedelta
import time
print("I wish you a good luck in getting your slot :) Swastik")
age = int(input("Enter your age : "))
#age = 26
#pincodes = ["560010"]
a = 560000
b = []
for i in range(1,157,1):
    pin = a + i
    b.append(str(pin))
pincodes = b
num_days = int(input("Enter the number of days from today you are looking for: "))
#num_days = 3
print_flag = 'Y'
print("Searching.....!!! It may take some time :)")

actual = datetime.today()
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

while True:
    counter = 0   
    mixer.init()
    mixer.music.load('got.wav')
    mixer.music.play()
    for pincode in pincodes:   
        for given_date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, given_date)
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
            
            result = requests.get(URL, headers=header)

            if result.ok:
                response_json = result.json()
                if response_json["centers"]:
                    if(print_flag.lower() =='y'):
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                    print('Pincode: ' + pincode)
                                    print("Available on: {}".format(given_date))
                                    print("\t", center["name"])
                                    print("\t", center["block_name"])
                                    print("\t Price: ", center["fee_type"])
                                    print("\t Availablity : ", session["available_capacity"])

                                    if(session["vaccine"] != ''):
                                        print("\t Vaccine type: ", session["vaccine"])
                                    print("\n")
                                    counter = counter + 1

            else:
                print("No Response!")
                
    if counter:
        print("No Vaccination slot available! For Dose 1.. If you are seeing it then it is for dose 2")
    else:
        mixer.init()
        mixer.music.load('got.wav')
        mixer.music.play()
        print("Search Completed!")


    dt = datetime.now() + timedelta(minutes=3000)

#    while datetime.now() < dt:             #UNHASH IT IF YOU WANT TO RUN ONCE
#        time.sleep(1)
