
class Year:
    def __init__ (self,year):
        self.year = year

    def isLeapYear (self):
        if self.year>1592 and ((self.year %4 ==0 and self.year %100!=0) or (self.year % 400 == True)):
            self.print_leap("")
        else:
            self.print_leap(" not")
             
    def print_leap (self, n = ""):
        print (str(self.year) + " is" + n +" a Leap Year")

yr = Year(int(input("Enter a Year: ")))
yr.isLeapYear()    