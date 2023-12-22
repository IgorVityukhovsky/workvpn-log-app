import time

while True:
    print("Hello world!")
    time.sleep(1)

# k delete po app --force --grace-period 0 && k apply -f https://raw.githubusercontent.com/IgorVityukhovsky/workvpn-log-app/main/app.yml