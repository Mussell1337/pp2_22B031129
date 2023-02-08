class takeString():
    def __init__(self, string):
        self.string = ""
    def getString(self):
        self.string = input("Enter a string: ")
    def printString(self):
        print(self.string.upper())

takeString("para")