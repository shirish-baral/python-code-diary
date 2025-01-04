# Property: @Property decorator on any method in the class to use method as property

class Marks:
    def __init__(self,math,phy,chem):
        self.math = math
        self.phy= phy
        self.chem = chem
        self.percent = str((self.math+self.phy+self.chem)/3)


shirish= Marks(100,98,97)
print(shirish.percent)
# But we got to know that marks in chem was 92
shirish.chem = 92
print(shirish.chem) #Updated value
print(shirish.percent) #Previous value



# To overcome this, we use Property
class Marks:
    def __init__(self,math,phy,chem):
        self.math = math
        self.phy= phy
        self.chem = chem

    @property
    def percent(self):
        return str((self.math+self.phy+self.chem)/3) + "%"


shirish= Marks(100,98,97)
print(shirish.percent)
# But we got to know that marks in chem was 92
shirish.chem = 92
print("Chemistry marks is ",shirish.chem) #Updated value
print("Percentage is ",shirish.percent) #Previous value




