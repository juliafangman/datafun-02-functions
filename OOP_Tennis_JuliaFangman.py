class TennisBall:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.is_bouncing = False
    
    def bouncing(self):
        self.is_bouncing = True
        print(f"{self.brand} {self.color} Tennis Ball is bouncing!")

    def stop_bouncing(self):
        self.is_bouncing = False
        print(f"The {self.color} Tennis Ball has stopped bouncing.")

Tennisball1 = TennisBall ("Penn", "Yellow") 
print(Tennisball1.brand)
print(Tennisball1.color)

Tennisball1.bouncing()
Tennisball1.stop_bouncing()

print(Tennisball1)




        







