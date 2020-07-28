"""
1.
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.

"""
import time


# базовый вариант
class TrafficLight:
    __color: ''

    def running(self):
        colors = [['red', 7], ['yellow', 2], ['green', 5]]
        for color in colors:
            self.__color = color[0]
            print(self.__color)
            time.sleep(color[1])


traffic_light1 = TrafficLight()
traffic_light1.running()


# усложненый вариант, как я его понимаю
class PowerTrafficLight:
    __color: ''

    def running(self, colors_scheme):
        """
        запуск сфетофора, где схема переключения передается в ввиде параметра
        параметр осстоит из списка списков [цвет, длительность], [цвет, длительность], [цвет, длительность]
        :param colors_scheme:
        :return:
        """
        right_seq = ['red', 'yellow', 'green']
        if [i[0] for i in colors_scheme] == right_seq:
            for color in colors_scheme:
                self.__color = color[0]
                print(self.__color)
                time.sleep(color[1])
        else:
            print('Неверный порядок цветов!')


traffic_light2 = PowerTrafficLight()
traffic_light2.running([['red', 1], ['yellow', 1], ['green', 1]])
traffic_light2.running([['green', 1], ['red', 1], ['Yellow', 1]])
