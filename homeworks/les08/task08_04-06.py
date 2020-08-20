"""
4.
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.

"""
from abc import ABC, abstractmethod
import copy


class EquipError(Exception):
    def __init__(self, message):
        self._message = message


class QuantityError(Exception):
    def __init__(self, message):
        self._message = message


class Equip(ABC):
    """
    Базовый класс для оборудования. Обязательные аттрибуты:
    uid  - уникальный инвентарный номер, по умолчанию = 0, генерируется при поступлении техники на склад
    department - отдел, за которым закреплено оборудование, по умолчанию = '', при поступлени на склад = 'склад'
    mark - наименование устройства (требуется обязательно указывать в параметрах при создании экземпляра)
    """
    _all_equipments = []  # переменная для учета всех экземпляров класса

    @abstractmethod
    def __init__(self, equip_properties: dict):
        # проверка обязательных для указания аттрибутов не имеющих значения по умолчанию
        if {'mark'} - set(equip_properties.keys()):
            raise EquipError('Нет нужных переменных')
        # установка значений по умолчанию и создание необязательных аттрибутов из аргументов
        if 'uid' not in equip_properties:
            setattr(self, 'uid', 0)
        if 'department' not in equip_properties:
            setattr(self, 'department', '')
        for key, value in equip_properties.items():
            setattr(self, key, value)
        self._all_equipments.extend([self])

    def __str__(self):
        return f'{self.get_type()}: uid={self.uid}, mark={self.mark}, department={self.department}'

    @abstractmethod
    def get_type(self):
        return 'Equip'

    @classmethod
    def gen_un_id(cls):
        """
        Генерация уникального инвентарного номера, который не пересекается с принятой ранее оргтехникой.
        Информацию о присвоенных номерах берет из переменной класса __all_equipments
        :return:
        """
        i = 1
        existing_id = set(item.uid for item in cls._all_equipments)
        while i in existing_id:
            i += 1
        return i

    @classmethod
    def get_equip_by_uid(cls, uid):
        """
        Метод поиска экземпляра класса по uid, возвращает указатель на экземпляр класса
        """
        return [eq for eq in cls._all_equipments if eq.uid == uid]

    @classmethod
    def get_equip_list(cls):
        result = f'\n'.join(f'{str(eq)}' for eq in cls._all_equipments)
        return result

    @classmethod
    def clone_equip(cls, equip):
        eq = copy.deepcopy(equip)
        cls._all_equipments.extend([eq])
        return eq


class Printer(Equip):
    def __init__(self, equip_properties: dict):
        if {'mark', 'paper_size', 'is_color'} - set(equip_properties.keys()):
            raise EquipError('Нет нужных переменных')
        super().__init__(equip_properties)

    def __str__(self):
        return f'{self.get_type()}: uid={self.uid}, mark={self.mark}, paper_size={self.paper_size}, is_color={self.is_color}, department={self.department}'

    def get_type(self):
        return 'Принтер'


class Monitor(Equip):
    def __init__(self, equip_properties: dict):
        if {'mark', 'screen_size', 'resolution'} - set(equip_properties.keys()):
            raise EquipError('Нет нужных переменных')
        super().__init__(equip_properties)

    def __str__(self):
        return f'{self.get_type()}: uid={self.uid}, mark={self.mark}, screen_size={self.screen_size}, resolution={self.resolution}, department={self.department}'

    def get_type(self):
        return 'Монитор'


class Computer(Equip):
    def __init__(self, equip_properties: dict):
        if {'mark', 'cpu', 'ram', 'ssd'} - set(equip_properties.keys()):
            raise EquipError('Нет нужных переменных')
        super().__init__(equip_properties)

    def __str__(self):
        return f'{self.get_type()}: uid={self.uid}, mark={self.mark}, cpu={self.cpu}, ram={self.ram}, ssd={self.ssd}, department={self.department}'

    def get_type(self):
        return 'Компьютер'


class Warehouse:

    def __init__(self):
        self.stock = []  # создаем переменную, которая будет хранить ссылки на технику, которая на складе

    def supply(self, equip: Equip, q: str):
        """
        Метод регистрирует на складе новую технику.
        В параметры принимает класс и кол-во техники. В результате создает q копий экземплярово класса.
        """
        try:
            # добавляем на склад первый объект из аргументов
            cnt = Warehouse.validate_quantity(q)
            equip.department = 'склад'
            equip.uid = Equip.gen_un_id()
            self.stock.extend([equip])
            # и затем делаем к нему нужное кол-во копий с добавалением на склад
            for _ in range(1, cnt):
                eq = Equip.clone_equip(equip)
                eq.uid = Equip.gen_un_id()
                self.stock.extend([eq])
        except QuantityError:
            print('не выполнить доабвление, количество указано неверно')
        equip = None

    def move_to_department_by_id(self, uid_lst: list, department: str):
        """
        Метод перенаправляет технику, находящуюся на складе в отдел по списку uid
        """
        # оставшаяся техника на складе после перемещения, чтобы не менять переменную класса при итерации
        remain_equip = []
        for equip in self.stock:
            if equip.uid in uid_lst:
                # для каждого класса прописываем новый отдел
                equip.department = department
            else:
                # заполняем список техники которая должна остаться
                remain_equip.extend([equip])
        # и заменяем на нее переменную класса
        self.stock = remain_equip

    def report(self):
        """
        Метод возвращающий словарь с типами техники находящимися на складе
        в форме {'тип техники': кол-во}
        """
        report_dict = {}
        for equip in self.stock:
            if not report_dict.get(equip.get_type(), 0):
                report_dict[equip.get_type()] = 0
            report_dict[equip.get_type()] += 1
        return report_dict

    @staticmethod
    def validate_quantity(s: str):
        """
        Метод по условию задачи, для проверки значени кол-ва техники, принимает строку, возвращает int
        """
        if not s.isdigit():
            raise QuantityError('Переданное кол-во не является целым положительным числом')
        else:
            return int(s)


# проверка
WH = Warehouse()
WH.supply(Printer({'mark': 'Xerox', 'paper_size': 'a4', 'is_color': True}), '3')
WH.supply(Monitor({'mark': 'Acer', 'screen_size': 27, 'resolution': '4k'}), '4')
WH.supply(Computer({'mark': 'Intel', 'cpu': 'core i5', 'ram': 8, 'ssd': 1}), '2')
WH.supply(Computer({'mark': 'AMD', 'cpu': 'rizen', 'ram': 16, 'ssd': 4}), '3')

print()
print(f'Статистика по складу:\n{WH.report()}\n')

print(f'Список всего оборудования:\n{Equip.get_equip_list()}\n')

# перемещение техники в другой департамент
WH.move_to_department_by_id([1, 4, 9, 12], 'бухгалтерия')
print(f'После перемещения техники с uid 1, 4, 9, 12 в бухгалтерию:\n')
print(f'Статистика по складу:\n{WH.report()}\n')
print(f'Список всего оборудования:\n{Equip.get_equip_list()}\n')

# перемещение техники в другой департамент при этом:
# - на складе полностью кончилось одно из наименований
# - на складе отсутствует id так как уже передано в какой то отдел (9) -
WH.move_to_department_by_id([5, 6, 7, 8, 9, 10], 'отдел ИТ')
print(f'После перемещения техники с uid 5, 6, 7, 8, 9, 10 в отдел ИТ:\n')
print(f'Статистика по складу:\n{WH.report()}\n')
print(f'Список всего оборудования:\n{Equip.get_equip_list()}\n')


print()


