from tkinter import Tk

from view import Simulator


def main():
    root = Tk()
    app = Simulator.Simulator(root)
    root.mainloop()


main()

