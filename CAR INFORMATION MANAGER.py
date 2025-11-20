#Car Information Manager / Car Profile Viewer
class car:

    def __init__(self,name,model,year,mil):
        self.manu_name = name
        self.model = model
        self.year = year
        self.mileage = mil

    def display_info(self):
        print(f'manufacturer:  {self.manu_name}')
        print(f'model name :    {self.model}')
        print(f'man year: {self.year}')
        print(f'current mileage : {self.mileage}')

    def up_mileage(self,new_mileage):
        if new_mileage > self.mileage:
         self.mileage = new_mileage
         return 'completed'
    
    def age(self , cur_year):
        car_age = cur_year - self.year
        print(car_age)

car1=car('ktm','duke',2025,32)
car1.display_info()
print(car1.up_mileage(34))
print(car1.mileage)
car1.age(2027)
print(car1.age)