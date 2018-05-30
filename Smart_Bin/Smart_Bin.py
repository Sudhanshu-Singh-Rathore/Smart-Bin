import RPi.GPIO as r
import time
import smtplib
#declaring variables for auto mailing
fadd = 'sender_e-mail_id_here@gmail.com'
toadd = 'receiver_e-mail_id_here@gmail.com'
msg = """From: From sender <sender_e-mail_id_here@gmail.com>
To: To receiver <receiver_e-mail_id_here@gmail.com>
Subject: Dustbin Info

Dustbin number 12 has been filled.
"""
username = 'sender_e-mail_id_here@gmail.com'
password = 'sender_Password_here'
r.setmode(r.BOARD)
r.setwarnings(False)
r.setup(7,r.OUT)
r.setup(11,r.OUT)
r.setup(12,r.OUT)
r.setup(13,r.OUT)
r.setup(35,r.OUT)
r.setup(15,r.OUT)
r.setup(16,r.IN)
count=0
r.setup(40,r.IN)
r.setup(18,r.OUT)
r.setup(19,r.IN)
r.setup(21,r.OUT)
r.setup(22,r.OUT)
r.setup(23,r.OUT)
r.setup(24,r.OUT)
r.setup(26,r.OUT)
r.setup(29,r.OUT)
r.setup(7,r.OUT)
r.setup(11,r.OUT)
pin=[23,24,26,29]

def person_ultra():
    r.output(15,1)
    time.sleep(0.000010)
    r.output(15,0)
    while(r.input(16)==0):
        pass
    t1=time.time()
    while (r.input(16)==1):
        pass
    t2=time.time()
    t=t2-t1
    d=34300*t
    d=d/2
    time.sleep(0.1)
    return d


def door_ultra():
    r.output(18,1)
    time.sleep(0.000010)
    r.output(18,0)
    while(r.input(19)==0):
        pass
    t1=time.time()
    while (r.input(19)==1):
        pass
    t2=time.time()
    t=t2-t1
    d=34300*t
    d=d/2
    time.sleep(0.1)
    return d




def open_door():
    r.output(7,1)
    r.output(11,0)
    r.output(12,1)
    r.output(13,0)
    time.sleep(2)
    r.output(7,0)
    r.output(11,0)
    r.output(12,0)
    r.output(13,0)


    
def close_door():
    r.output(7,0)
    r.output(11,1)
    r.output(12,0)
    r.output(13,1)
    time.sleep(2)
    r.output(7,0)
    r.output(11,0)
    r.output(12,0)
    r.output(13,0)



def port(p):
    i = 0x10
    for j in range(0,4):
        if(p & i == i):
            r.output(pin[j],1)
        else:
            r.output(pin[j],0)
        i=i*2

def lcd_cmd(c):
    p = c & 0xF0
    port(p)
    r.output(21,0)
    r.output(22,1)
    time.sleep(0.001)
    r.output(22,0)
    p = (c<<4) & 0xF0
    port(p)
    r.output(21,0)
    r.output(22,1)
    time.sleep(0.001)
    r.output(22,0)

def lcd_data(d):
    p = d & 0xF0
    port(p)
    r.output(21,1)
    r.output(22,1)
    time.sleep(0.001)
    r.output(22,0)
    p = (d<<4) & 0xF0
    port(p)
    r.output(21,1)
    r.output(22,1)
    time.sleep(0.001)
    r.output(22,0)
            
def lcd_init():
    lcd_cmd(0x02)
    lcd_cmd(0x28)
    lcd_cmd(0x0c)
    lcd_cmd(0x06)
    lcd_cmd(0x01)
    time.sleep(0.01)

def lcd():
    lcd_init()
    lcd_cmd(0x81)
    z="BHAR GYA"
    l=len(z)
    for i in range(0,l):
        asc=ord(z[i])
        lcd_data(asc)
    
       
while(True):
    if (r.input(40)==0):
        r.output(35,1)

    else:
        r.output(35,0)


    if(door_ultra()<20):
        lcd()
        #sending mail
        server=smtplib.SMTP('smtp.gmail.com:587')    
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fadd, toadd, msg)
        server.quit() 
        while(door_ultra()<20):
            pass
        

    elif(person_ultra()<10):
        while(person_ultra()<10):
            open_door()
            time.sleep(2)
            close_door()
            print 'Hello'
            #lcd()
            break
        
    lcd_cmd(0x01)


        
