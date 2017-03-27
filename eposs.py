import csv
import math
import matrix
import excel_transfer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
import get_csv

class EPOSS:
    def __init__(self):
        self.commands = {
            "commands": {
                "none": 0,
                "exit": 1,
                "test": 2,
                "clear": 3,
                "help": 4,
                "new": 5,
                "show slist": 6,
                "show scount": 7,
                "acc": 8,
                "mk": 9,
                "start": 10,
                "show result": 11,
                "image 1": 12,
                "set path": 13
            },
            "description": {
                "none": "do nothing",
                "exit": "exit from module",
                "test": "do test stuff",
                "clear": "clear something",
                "help": "display helpfull information",
                "new": "enter new raw data",
                "show slist": "show raw data",
                "show scount": "show something",
                "acc": "set accuracy",
                "mk": "set default raw data",
                "start": "start calculation process",
                "show result": "show result",
                "image 1": "show visualization",
                "set path": "set path of the file"
            }
        }
        self.file_path = "file.csv"
        self.epsilon = 0.001
        self.dataset = {}
        self.makedefault()
        self.result = {
            "Y": 0.0,
            "Ys": 0.0,
            "DY^2": 0.0,
            "^Y": 0.0,
            "^Ys": 0.0,
            "S^2": 0.0,
            "D(^Ys)": 0.0,
            "D(^Y)": 0.0,
            "lol": 0.0
        }


    def showCommands(self):
        print('')
        print("Commands...")
        print("---")
        for item in self.commands["commands"]:
            print(str(item) + ":")
            print("Number: " + str(self.commands["commands"][item]))
            print("Description: " + str(self.commands["description"][item]))
            print("---")

    def enterCommand(self):
        command = "0"
        print('')
        print("Enter command (help for Q&A)")
        while (command not in self.commands):
            command = input("->")
            if (command not in self.commands["commands"]):
                print("There is no such command")
            else:
                return self.commands["commands"][command]

    def showHelp(self):
        print('')
        print("Help v0.002")
        self.showCommands()

    def makedefault(self):
        #self.file_path = "file.csv"
        self.file_path = "src_csv/example_from_google/GS_Election_Poll_20161108.csv"
        #324730000

    def importparam(self, accuracy, dataset):
        self.accuracy = accuracy
        self.dataset = dataset

    def setaccuracy(self):
        task = 0
        print('')
        print("Enter accuracy:")
        while (task != 1):
            self.accuracy = int(input("-> "))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1
            else:
                if self.accuracy < 0:
                    print("Please enter positive number!")
                    task = 0
        self.epsilon = 10 ** (-self.accuracy)

    def inputnewdata(self):
        pass

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("Estimation of parameters of statistical sampling")
            print('')
            task = self.enterCommand()
            if task == 2:
                pass
            elif task == 3:
                pass
            elif task == 4:
                self.showHelp()
            elif task == 5:
                self.inputnewdata()
            elif task == 6:
                self.print_raw_data()
            elif task == 8:
                self.setaccuracy()
            elif task == 9:
                self.makedefault()
            elif task == 10:
                self.resolve()
            elif task == 11:
                self.printresult()
            elif task == 12:
                self.printresult_g()
            elif task == 13:
                self.getcsv()
        pass

    def print_raw_data(self):
        pass

    def resolve(self):
        pass

    def printresult_g(self):
        pass

    def printresult(self):
        print("Result:")

    def getcsv(self):
        gcsv = get_csv.GCSV()
        gcsv.file_path = self.file_path
        self.dataset = gcsv.getcsv()
        pass