#Задание 1
class UserAccount:
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        print('Пароль изменен - успешно!')

    def check_password(self, password):
        if password == self.__password:
            return True
        else:
            return False
#Создание объекта и проверка
EvgenyUser = UserAccount('Evgeny','evgeny@yandex.ru','wasd111')
current_check = input('Введите текущий пароль: ')
print(EvgenyUser.check_password(current_check))
new_password = input('Введите новый пароль: ')
EvgenyUser.set_password(new_password)
verify_pass = input('Введите новый пароль для проверки: ')
print('Пароль верный: ', EvgenyUser.check_password(verify_pass))



#Задание 2
class Vehicle:#1
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'Марка: {self.make}, Модель: {self.model}'


class Car(Vehicle):#2
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f'Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}'

#Проверка
car1 = Car('Audi', 'RS7', 'Бензин')
print(car1.get_info())