#from ParentCode import SoftWareProject

class getData():

    def __init__(self, filename):
        
        self.file = open(filename , 'r' )
        
        firstline=True
        self.heightData = []
        self.distanceData = []
        self.codeData = []
        self.valData = []
        self.roleData= []
        self.tonnesData = []
        
        for line in self.file:
            if firstline:
                firstline = False
            else:
                self.data = line.strip().split(',')
                self.height, self.code,self.distance, self.val, self.role, self.tonnes = int(self.data[0]),self.data[1],float(self.data[2]),self.data[3],self.data[4],int(self.data[5])
                
                self.heightData.append(self.height)
                self.codeData.append(self.code)
                self.distanceData.append(self.distance)
                self.valData.append(self.val)
                self.roleData.append(self.role)
                self.tonnesData.append(self.tonnes)

                
class getModules(getData):
    
    
    def __init__(self,filename):
        getData.__init__(self,filename)
        

    def Sum(self):
        self.heightSum=0
        for self.height in self.heightData:
            if self.height >= 33 and self.height <= 53:
                self.heightSum += self.height
        return self.heightSum
    
    def Count(self):
        self.heightCount=0
        for self.height in self.heightData:
            if self.height >= 33 and self.height <= 53:
                self.heightCount += 1
        return self.heightCount
    

    def Average(self):
        self.average = self.Sum()/self.Count()
        return self.average

    def Distance(self):
        self.distanceCount=0
        for self.distance in self.distanceData:
            if self.distance > 44.180 and self.distance <= 79.061:
                self.distanceCount = self.distanceCount+1
        return self.distanceCount

    def Val(self):
        self.coldCount = 0
        for self.cold in self.valData:
            if self.cold == 'Cold':
                self.coldCount += 1
        return self.coldCount

    def director(self):
        self.directorCount = 0
        for self.role in self.roleData:
            if self.role == 'Director':
                self.directorCount += 1
        return self.directorCount




    def RoleCount(self):
        self.roleCount = 0
        for self.line in self.roleData:
            
            self.roleCount += 1
        return self.roleCount

    
    def rolePercent(self):
        self.percent = 100 * self.director()/self.RoleCount()
        return self.percent

    


    def tonesSum(self):
        self.tonneSum = 0
        for self.tonne in self.tonnesData:
            if self.tonne > 5334 and self.tonne <= 8233:
                self.tonneSum += self.tonne
        return self.tonneSum



    def disTonne(self):
        
        self.Count = 0
        for (self.distance, self.tons) in zip(self.distanceData,self.tonnesData):
            if self.tons < 7780 or self.distance > 59.097:
                self.Count += 1
        return self.Count






b =input('Please specify a filename here:')
a= getModules(b)

print(a.Sum())
print(a.Count())
print(a.Average())
print(a.Distance())
print(a.Val())
print(a.director())
print(a.RoleCount())
print(a.rolePercent())
print(a.tonesSum())
print(a.disTonne())
