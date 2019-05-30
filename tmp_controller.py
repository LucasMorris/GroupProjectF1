class Controller():
    # Deze functie begint het spel
    def startGame():
        # Creeer een nieuwe auto
        newCar = tmp_model.updateCar(speed = 30,
                                     fuel = 10,
                                     locX = 10,
                                     locY = 10,
                                     engine = 2,
                                     tires = 3)
        # Hier maak je een view aan
        tmp_view.startView()

    def updateGame(speed, locX, etc):
        car.updateCar(speed, locX, etc)
