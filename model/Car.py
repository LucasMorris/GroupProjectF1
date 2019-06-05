import turtle
from model import Tire


class Car:

    def __init__(self):
        self.speed = 10
        self.tire = Tire.Tire('soft')


    def updateCar(self, tire):
        self.tire = tire

