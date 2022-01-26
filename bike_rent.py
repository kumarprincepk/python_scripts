class BikeRent:
    def __init__(self,bstock):
        self.bstock=bstock
        print("Yamaha, Royal Enfield, Hero, TVS, KTM, Harley Davidson, Kawasaki, Suzuki")

    def a_bike(self):
        print("Here the total number of bike is : ",self.bstock)
    def bikeforrent(self,qbike):
        if qbike<=0:
            print("Please enter atleast one bike")
        elif qbike>self.bstock:
            print("Please enter number less than the bike stock.")
        else:
            self.bstock=self.bstock-qbike
            print("Total price is : " ,qbike*999)
            print("Total number of bike is : ",self.bstock)
while True:
    object=BikeRent(200)
    usrchoice=int(input('''
    1. Display avalable number of bike
    2. Bike for rent
    3. Don't want for rent
    '''))
    if usrchoice==1:
        object.a_bike()
    elif usrchoice==2:
        n=int(input("Please enter how many bike you want for rent : "))
        object.bikeforrent(n)
    else:
        break
