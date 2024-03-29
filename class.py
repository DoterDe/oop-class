class Автомобиль:
    def __init__(self, модель, год_выпуска, производитель, объем_двигателя, цвет, цена):
        self.модель = модель
        self.год_выпуска = год_выпуска
        self.производитель = производитель
        self.объем_двигателя = объем_двигателя
        self.цвет = цвет
        self.цена = цена

    def ввод_данных(self, модель, год_выпуска, производитель, объем_двигателя, цвет, цена):
        self.модель = модель
        self.год_выпуска = год_выпуска
        self.производитель = производитель
        self.объем_двигателя = объем_двигателя
        self.цвет = цвет
        self.цена = цена

    def вывод_данных(self):
        return self.модель, self.год_выпуска, self.производитель, self.объем_двигателя, self.цвет, self.цена

class Книга:
    def __init__(self, название, год_выпуска, издатель, жанр, автор, цена):
        self.название = название
        self.год_выпуска = год_выпуска
        self.издатель = издатель
        self.жанр = жанр
        self.автор = автор
        self.цена = цена

    def ввод_данных(self, название, год_выпуска, издатель, жанр, автор, цена):
        self.название = название
        self.год_выпуска = год_выпуска
        self.издатель = издатель
        self.жанр = жанр
        self.автор = автор
        self.цена = цена

    def вывод_данных(self):
        return self.название, self.год_выпуска, self.издатель, self.жанр, self.автор, self.цена

class Стадион:
    def __init__(self, название, дата_открытия, страна, город, вместимость):
        self.название = название
        self.дата_открытия = дата_открытия
        self.страна = страна
        self.город = город
        self.вместимость = вместимость

    def ввод_данных(self, название, дата_открытия, страна, город, вместимость):
        self.название = название
        self.дата_открытия = дата_открытия
        self.страна = страна
        self.город = город
        self.вместимость = вместимость

    def вывод_данных(self):
        return self.название, self.дата_открытия, self.страна, self.город, self.вместимость