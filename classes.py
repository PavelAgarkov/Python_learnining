class Vehicle:

    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


# наследование
class Car(Vehicle):
    # в классе определяются глобальныые свойства - доступные из любого места Car.counter += 1
    # статическое поле
    counter = 0

    def car_method(self):
        print("Это метод из дочернего класса")

    # в конструкторе объявляются поля экземпляра
    def __init__(self):
        # public доступно везде
        self.name = "corolla"
        # private __ доступно только внутри класса
        self.__make = "toyota"
        # protected - _ доступно только в пакете
        self._model = 1999

    # метод для определения отображения объекта при печати
    def __str__(self):
        return "Car class Object"

    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.__make = make
        self._model = model
        return self

    def stop(self):
        print("Отключаем двигатель")

    # статический метод не требует экземпляра Car.get_squares()
    @staticmethod
    def get_squares(a, b):
        # метод класса может возвращать несколько значений, по умолчанию они tuple(кортеж)
        return a * a, b * b


# car_a = Car()
# car_a.start('name', 'make', 'model')
# print(car_a._model, car_a.name)
#
# car_b = Car()
# car_b.start('name', 'make', 'model').stop()
# print(car_b._model, car_b.name)

car_a = Car()
car_a.vehicle_method()
car_a.car_method()


# пример множественного наследования
class Camera:
    def camera_method(self):
        print("Это родительский метод из класса Camera")


class Radio:
    def radio_method(self):
        print("Это родительский метод из класса Radio")


class CellPhone(Camera, Radio):
    def cell_phone_method(self):
        print("Это дочерний метод из класса CellPhone")


cell_phone_a = CellPhone()
cell_phone_a.camera_method()
cell_phone_a.radio_method()


# свойства и сеттеры свойств
class Bike:
    # создаем конструктор класса Car
    def __init__(self, model):
        # Инициализация свойств.
        # если указать __ или _ мы не попадем в сеттер свойства -> объявляется как public затем
        # в сеттере изменяется модификатор на private
        self.model = model

    # создаем свойство модели.
    @property
    def model(self):
        return self.__model

    # Сеттер для создания свойств.
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)


bike_a = Bike(2088)
print(bike_a.getCarModel())
