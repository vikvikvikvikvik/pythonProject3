class Mobile:
    ram = 2
    model = 'Xiaomi Mi10'
    color = 'Grey'#public
    os = 'Android' #protected
    version = '10'
    __IMEI = 1 #PRIVAT


    def __init__(self): #используется при создании объекта.
        self.__IMEI = Mobile.__IMEI
        Mobile.__IMEI = Mobile.__IMEI + 1
    def show_color(self):
        print(self.color)
    def change_color(self,new_color):
        self.color = new_color
    def charge(self):
        print('Charging....')

    def call(self):
        print('Call')

    def darknet(self,new_IMEI):
        self.__IMEI =  new_IMEI
        if new_IMEI == 777:
            self.__change_ram(4)

    def show_IMEI(self):
        print(self.__IMEI)

    def __change_ram(self,new_ram):
        print('You are cheater!')

    def usb_connect(self,option='Charge'):
        if option == 'Charge':
            print('Charging........')
        elif option == 'Camera':
            print('Smile :)')
        elif option == 'FileStorage':
            print('Ready to work!')
        else:
            print('Reconnect')

    def imei_checker(self):
        if self.__IMEI == 777:
            print('Потрачено')
        else:
            print('OK')

class PC:
    ram = 4
    hdd = 500
    cpu = 2.2

class Tablet(Mobile,PC):
    pass

class Iphone(Mobile):
    model = '13 pro max'
    color = 'Space grey'#public
    os = 'ios' #protected




my_phone = Mobile()
# s = str()
# l = []
# l = list()
#
# print(my_phone.model)
# my_phone.charge()
# my_phone.call()
# print(my_phone.color)
# my_phone.color = 'red'
# print(my_phone.color)
# print(my_phone.os)
# my_phone.os = 'XOS'
# print(my_phone.os)
# # print(my_phone.__IMEI)
# print(my_phone.darknet('999999'))
# my_phone.show_IMEI()
#
# my_phone._IMEI__ = '222222'
# my_phone.show_IMEI()
# your_phone = Mobile()
# sten_phone = Mobile()
# my_phone.show_IMEI()
# your_phone.show_IMEI()
# sten_phone.show_IMEI()
# my_phone.darknet(777)
my_phone.usb_connect()
my_phone.usb_connect('Camera')
my_phone.usb_connect('FileStorage')
my_phone.darknet(777)
my_phone.imei_checker()

apple = Iphone()
print(apple.os)

Ipad = Tablet()
print(Ipad.ram)