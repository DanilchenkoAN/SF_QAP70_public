class Clients:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def get_guest_info(self):
        return f'''
Клиент: {self.first_name} {self.second_name}
Откуда: г.{self.city}
-----------------------------'''

client_1 = Clients('Иван', 'Петров', 'Мосвка', 50)
client_2 = Clients('Сидрор', 'Иванов', 'Мосвка', 100)
client_3 = Clients('Петр', 'Сидоров', 'Мосвка', 150)

guest_list=[client_1,client_2,client_3]

for guest in guest_list:
    print(guest.get_guest_info())
