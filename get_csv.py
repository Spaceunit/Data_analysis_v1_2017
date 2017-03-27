import csv
import math
import matrix
import excel_transfer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
class GCSV:
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
        #It had download from
        #https://doc-50-58-drive-data-export.googleusercontent.com/download/ate866dkcquebegkb64jf1fj6ukv21dr/hkv8tv4k1stup04osgnm6al5a7pb48t6/1489444100000/4c45aaa8-2bff-425e-b9b8-788610ef415e/102797190718007119523/ADt3v-N0yZrt-y6E64-dQEqIxb7kEWR03Pjx0cZ9eW6fHYNlTrjJxrBIRz7ybsXCBCpr_LJtHcB86-wFmBTqzUfH0tmsWk81YyfWM7VTwYYiBi4GQvY3bxFmohSF0CglTYtHofwcS3ruohIguHQTLKT2q8YuYMNkiJK_Vwxk7c4S6Z74tjzS__WmAnm3GJmVyHHR56SgfLtWT4arVhgR7DSO_VgjhgvTJoztmFta5z_SYjXKG7yxB-GBFY3WhR64_zp5CODqAc5PUmYJhVOLF43PPJRJaAKxAg_1pZc1H81DRx1vK9lnhJR5aKmtRkXuwuNRLt8p3R5NwIZSZ0sanosLedzLNC4rWQbVzq0GaxBM4NdCPRV2_Tk69mxHE_pC-BhlKP8U25qSJffQHrR8sdaNvrLpP8X4jA==?authuser=0&nonce=39do4bs7ish28&user=102797190718007119523&hash=2l3e4d63qkkitu4l7glfe0el470l6ecr
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
            print("Get data from CSV file")
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
                self.dataset = self.getcsv()
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
        self.makedefault()
        reader = {}
        with open(self.file_path) as csvfile:
            reader = csv.DictReader(csvfile)
        return reader

    def getcsv0(self):
        self.makedefault()
        with open(self.file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['Geography'], row['Question #4 Answer'])