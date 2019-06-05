import turtle

class Tire:

    def __init__(self, tireType):
        if tireType == 'hard':
            self.speed = 3
        if tireType == 'medium':
            self.speed = 5
        if tireType == 'soft':
            self.speed = 0

    def switch_Tire(self, tireType):
        if tireType == 'hard':
            self.speed = 3
        if tireType == 'medium':
            self.speed = 5
        if tireType == 'soft':
            self.speed = 0


