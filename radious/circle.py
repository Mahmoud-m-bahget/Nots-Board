class circle:
    def  __init__(self):
        self.__r = 0
        self.read()

    def read(self):
        radius =  float(input('Radius = '))
        if radius < 0 :
            print('Error : radious must be  >= 0 ')
            self.read()
        else:
            self.__r = radius

    def getarea(self):
        return 3.14 * self.__r * self.__r

    def getperimiter(self):
        return 3.14 * self.__r * 2

    def printcharateristic(self):
        print('area = ' , self.getarea(),'cm2')
        print('perimiter = ', self.getperimiter() , 'cm2')
