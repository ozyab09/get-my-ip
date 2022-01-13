import os
import socket
import sys
import time
import requests

TELEGRAM_ID=os.getenv('TELEGRAM_ID', sys.argv[1]) or exit(1)
BOT_TOKEN=os.getenv('BOT_TOKEN', sys.argv[2]) or exit(1)
HOSTNAME=socket.gethostname()
IP_ADDRESS_API_URL='https://ifconfig.me/ip'

def get_current_ip():
    r = requests.get(url=IP_ADDRESS_API_URL, timeout=10)
    if r.status_code == 200:
        return r.text
    else:
        return None

def send_message(message):
    requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/'
                 f'sendMessage?chat_id={TELEGRAM_ID}&text={message}')

if __name__ == '__main__':

    print('Script started!')
    old_ip = None

    while True:

        current_ip = get_current_ip()

        if current_ip and old_ip != current_ip:
            print(f'New IP: {current_ip}')
            message = f'Hello from host {HOSTNAME} !\n' \
                      f'Current IP: {current_ip}'
            send_message(message)
            old_ip = current_ip
        time.sleep(10)
