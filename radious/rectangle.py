class rectangle:
    def  __init__(self):
        self.__l = 0
        self.__w = 0
        self.read()

    def read(self):
        width =  float(input('width = '))
        length = float(input('length = '))
        if width < 0 or length < 0 :
            print('Error : radious must be  >= 0 ')
            self.read()
        else:
            self.__l = length
            self.__w = width

    def getarea(self):
        return   self.__l * self.__w

    def getperimiter(self):
        return (self.__l + self.__w) * 2

    def printcharateristic(self):
        print('area = ' , self.getarea(),'cm2')
        print('perimiter = ', self.getperimiter() , 'cm2')
