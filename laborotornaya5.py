#1
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f'Сотрудник: {self.name}, ID: {self.id}'
#2
class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def get_info(self):
        return f'Менеджер: {self.name}, ID: {self.id}, Отдел: {self.department}'

    def manage_project(self):
        return f'Менеджер {self.name} управляет проектами в отделе {self.department}'
#3
class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def get_info(self):
        return f'Техник: {self.name}, ID: {self.id}, Специализация: {self.specialization}'

    def perform_maintenance(self):
        return f'Техник {self.name} выполняет техническое обслуживание в области {self.specialization}'

#4
class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        self.name = name
        self.id = id
        self.department = department
        self.specialization = specialization
        self.team = []

    def get_info(self):
        return f'Технический менеджер: {self.name}, ID: {self.id}, Отдел: {self.department}, Специализация: {self.specialization}'

    def add_employee(self, employee):#5
        self.team.append(employee)
        return f'Сотрудник {employee.name} добавлен в команду {self.name}'

    def get_team_info(self):#6
        if not self.team:
            return f'У {self.name} нет подчиненных'

        team_info = f'Команда {self.name}:\n'
        for i, employee in enumerate(self.team, 1):
            team_info += f'{i}. {employee.get_info()}\n'
        return team_info

    def manage_project(self):
        return f'Технический менеджер {self.name} управляет проектами в отделе {self.department}'

    def perform_maintenance(self):
        return f'Технический менеджер {self.name} выполняет техническое обслуживание в области {self.specialization}'


    # Проверка #7
    # 1. Создаем обычного сотрудника
    employee1 = Employee('Петр Петров', 'EMP001')
    print('1. Обычный сотрудник:')
    print(employee1.get_info())

    # 2. Создаем менеджера
    manager = Manager('Евгений Евгеньев', 'MNR001', 'Разработка')
    print('2. Менеджер:')
    print(manager.get_info())
    print(manager.manage_project())

    # 3. Создаем техника
    technician = Technician('Алина Вьерн', 'TECH001', 'Сетевое оборудование')
    print('3. Техник:')
    print(technician.get_info())
    print(technician.perform_maintenance())

    # 4. Создаем тех. Менеджера
    tech_manager = TechManager('Евгений Константинов', 'TM001', 'IT-инфраструктура', 'Системное администрирование')
    print('4. Технический менеджер:')
    print(tech_manager.get_info())
    print(tech_manager.manage_project())
    print(tech_manager.perform_maintenance())


    print('5. Формирование команды:')
    print(tech_manager.add_employee(employee1))
    print(tech_manager.add_employee(technician))


    employee2 = Employee('Сергей Смирнов', 'EMP002')
    print(tech_manager.add_employee(employee2))


    print('6. Информация о команде:')
    print(tech_manager.get_team_info())