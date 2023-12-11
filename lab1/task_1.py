import doctest

class Person:
    def __init__(self, name: str, age: int, weight: float):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: Имя человека
        :param age: Сколько ему лет
        :param weight: Вес человека

        Примеры:
        >>> person = Person("Костя", 19, 83.5) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом")
        self.age = age

        if not isinstance(weight, float):
            raise TypeError("Вес должен быть типа float")
        if weight < 0:
            raise ValueError("Вес должен быть положительным числом")
        self.weight = weight

    def print_name(self) -> None:
        """
        Метод который выводит имя человека на экран

        Примеры:
        >>> person = Person("Костя", 19, 83.5)
        >>> person.print_name()
        Костя
        """
        print(self.name)

    def gain_weight(self, extra_weight: float) -> None:
        """
        Увеличение веса пользователя

        :param extra_weight: лишний вес

        Примеры:
        >>> person = Person("Костя", 19, 83.5)
        >>> person.gain_weight(20.0)
        """
        if not isinstance(extra_weight, float):
            raise TypeError("Лишний вес должен быть типа float")
        if extra_weight < 0:
            raise ValueError("Прибавочный вес не может быть отрицательным числом")
        self.weight += extra_weight

    def loss_weight(self, to_lose_weight: float) -> None:
        """
    Уменьшение веса пользоавтеля

        :param to_lose_weight: Вес который нужно сбросить

        :raise OverflowError: Если вес станет меньше 0, то вызывается исключение

        Примеры:
        >>> person = Person("Костя", 19, 83.5)
        >>> person.loss_weight(11.2)
        """
        if not isinstance(to_lose_weight, float):
            raise TypeError("Сбрасываемый вес должен быть типа float")
        if to_lose_weight < 0:
            raise ValueError("Сбрасываемый вес не может быть отрицательным числом")
        if self.weight < to_lose_weight:
            raise OverflowError("Сбрасываемый вес не может быть больше чем вес собственный")
        self.weight -= to_lose_weight


class Phone:
    def __init__(self, battery: int, brightness: int):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param battery: Батарея телефона
        :param brightness: Его яркость

        Примеры:
        >>> phone = Phone(70, 8) # инициализация экземпляра класса
        """
        if not isinstance(battery, int):
            raise TypeError("Батарея должна быть типа int")
        if not 0 <= battery <= 100:
            raise ValueError("Батарея может быть больше 100 или меньше 0")
        self.battery = battery

        if not isinstance(brightness, int):
            raise TypeError("Яркость должна быть типа int")
        if not 1 <= brightness <= 10:
            raise ValueError("Яркость может быть больше 10 или меньше 1")
        self.brightness = brightness

    def change_brightness(self, new_brightness: int) -> None:
        """
        Изменение яркости

        :param new_brightness: Новый уровень яркости

        Примеры:
        >>> phone = Phone(70, 8)
        >>> phone.change_brightness(1)
        """
        if not isinstance(new_brightness, int):
            raise TypeError("Новая яркость должна быть типа int")
        if not 1 <= new_brightness <= 10:
            raise ValueError("Новая яркость может быть больше 10 или меньше 1")
        self.brightness = new_brightness

    def charge_battery(self) -> None:
        """
        Метод который заряжает полностью телефон до 100

        Примеры:
        >>> phone = Phone(70, 8)
        >>> phone.charge_battery()
        """
        self.battery = 100

    def use_phone(self, hours: int) -> None:
        """
        Использование телефона

        :param hours: Время в течении которого используется телефон

        :raise ValueError: Если количество часов превышает возможное использование телефона, то бросается исключение

        Примеры:
        >>> phone = Phone(70, 8)
        >>> phone.use_phone(10)
        """
        if not isinstance(hours, int):
            raise TypeError("Количество часов должно быть типа int")
        if hours < 0:
            raise ValueError("Количество часов может быть только положительным числом")
        if self.battery < hours * 4:
            raise ValueError(f"Телефон нельзя использовать больше {int(self.battery / 4)} часов")
        self.battery -= hours * 4


class Car:
    def __init__(self, power_reserve: int, max_speed: int):
        """
        Создание и подготовка к работе объекта "Машина"

        :param power_reserve: Запас хода машины
        :param max_speed: Максимальная скорость

        Примеры:
        >>> car = Car(500, 100) # инициализация экземпляра класса
        """
        if not isinstance(power_reserve,int):
            raise TypeError("Запас хода должен быть типа int")
        if power_reserve < 0:
            raise ValueError("Запас хода должен быть положительным числом")
        self.power_reserve = power_reserve

        if not isinstance(max_speed, int):
            raise TypeError("Максимальная скорость должна быть типа int")
        if max_speed < 0:
            raise ValueError("Максимальная скорость должа быть положительным числом")
        self.max_speed = max_speed

    def drive(self, hours: int) -> None:
        """
        Вождение машины

        :param hours: Количество часов вождения

        :raise ValueError: Если количество часов превышает возможный запас хода, то кидается исключение

        Примеры:
        >>> car = Car(500, 100)
        >>> car.drive(4)
        """
        if not isinstance(hours, int):
            raise TypeError("Количество часов должно быть типа int")
        if hours < 0:
            raise ValueError("Количество часов быть положительным числом")
        if self.power_reserve < hours * self.max_speed:
            raise ValueError(f"Машина не может ехать больше {int(self.power_reserve / self.max_speed)} часов")
        else:
            self.power_reserve -= hours * self.max_speed

    def fill_car(self, volume: int) -> None:
        """
        Заправка машины

        :param volume: Объем заполнения

        Примеры:
        >>> car = Car(500, 100)
        >>> car.fill_car(30)
        """
        if not isinstance(volume, int):
            raise TypeError("Объем должен быть типа int")
        if volume < 0:
            raise ValueError("Объем должен быть положительным числом")
        self.power_reserve = volume * 100


if __name__ == "__main__":
    doctest.testmod()
    pass
