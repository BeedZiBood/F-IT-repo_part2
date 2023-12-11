class Person:
    """Класс описывающий человека"""
    def __init__(self, name: str, gender: str):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: Имя человека
        :param gender: Какой у него пол
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self._name = name

        if not isinstance(gender, str):
            raise TypeError("Пол должен быть типа str")
        gender = gender.lower()
        if not (gender == "male" or gender == "female"):
            raise ValueError("Пол введён неверно")
        self._gender = gender

    def __str__(self) -> str:
        """
        Определение поведения фукнции str()
        """
        return f'Это {self.name}'

    def __repr__(self) -> str:
        """
        Определение поведения фукнции repr()
        """
        return f'{self.__class__.__name__}(name={self.name!r}, height={self.gender!r})'

    def is_male(self) -> bool:
        """
        Метод проверяющий является ли человек мужчиной
        """
        return self._gender == "male"

    def is_female(self) -> bool:
        """
        Метод проверяющий является ли человек женщиной
        """
        return not self.is_male()

    def print_who_you_are(self) -> None:
        """
        Метод выводящий кто такой человек
        """
        print(f'Hello, my name is {self.name}')

    @property
    def name(self) -> str:
        """
        Свойство описывающее защищенный атрибут _name
        Этот атрибут нельзя изменять т.к. имя неизменяемый тип
        """
        return self._name

    @property
    def gender(self) -> str:
        """
        Свойство описывающее защищенный атрибут _gender
        Этот атрибут нельзя изменять т.к. пол неизменяемый тип
        """
        return self._gender


class Thief(Person):
    """Класс описывающий вора"""
    def __init__(self, name: str, gender: str, years_of_criminal_record: float):
        """
        Создание и подготовка к работе объекта "Вор" наследуемого от класса "Человек"

        :param years_of_criminal_record: Сколько лет дали за преступление
        """
        super().__init__(name, gender)
        self.years_of_criminal_record = years_of_criminal_record

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__, который вызывает фукнцию repr()
        Сделано так, потому что в наследуемом классе появился новый параметр
        """
        return f'{self.__class__.__name__}(name={self.name!r}, gender={self.gender!r}, years_of_criminal_record={self.years_of_criminal_record!r})'

    def print_who_you_are(self) -> None:
        """
        Перегрузка метода, т.к. наш персонаж еще и вор, поэтому в представлении должно упоминаться, что он вор
        """
        print(f"Hello, I\'m {self.name} and I'm thief")

    @property
    def years_of_criminal_record(self) -> float:
        """
        Метод выводящий количество лет в судимости
        """
        return self._years_of_criminal_record

    @years_of_criminal_record.setter
    def years_of_criminal_record(self, new_year: float) -> None:
        """
        Определение поведения присваивания судимости
        """
        if not isinstance(new_year, float):
            raise TypeError("Время судимсоти должно быть типа float")
        if new_year <= 0:
            raise ValueError("Судимость может быть только положительным числом")
        self._years_of_criminal_record = new_year

if __name__ == "__main__":
    person = Person("Раиль", "Male")
    thief = Thief("Отаб", "FeMAle", 13.4)
    print(person)
    print(thief)
    print(repr(person))
    print(repr(thief))
    print(person.is_male(), person.is_female())
    print(thief.is_male(), thief.is_female())
    person.print_who_you_are()
    thief.print_who_you_are()
    pass
