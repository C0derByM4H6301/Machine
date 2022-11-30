## machine library
## kafana göre bir şey yaz
## log sistemini unutma
## log sistemini ayrı dosyada yaz dene sonra ekle
from pyfiglet import Figlet
from requests import get

class machine:
    #-> information <-#
    Authors = "Machmut P."
    Version = "DEMO 1.0"
    intro = "Real machines are invincible. \nThanks and regards to Emin, nicknamed the machine."
    
    def banner():
        banner = Figlet(font="slant")
        print(banner.renderText("Machine"))


    def generate_banner(bannername="Banner"):
        banner = Figlet(font="slant")
        print(banner.renderText(bannername))


    def echo_intro():
        print(machine.intro)
    

    def respect():
        print("Respect: ")
        print("Emin (The Machine)")
        print("Mahmut (The Machine Coder)")


    def explanation():
        print("Bu kütüphane benim aklıma gelen;")
        print("Fonksiyonlar ve özelliklerden oluşmaktadır.")
        print("Tek amaç benim eğlenmem!")


    def averaging(x,y):
        c = x + y
        return c / 2


    def get_pub_ip_adr():
        ip = get('https://api.ipify.org').text
        return ip


    def import_lib_try():
        try:
            from pyfiglet import Figlet
            from requests import get
        except ImportError:
            print("Gerekli kütüphaneler import edilmemiş!")



