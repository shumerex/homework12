class House:
    def __init__(self):
        self.numberOfFloors = 10


house = House()
for floor in range(house.numberOfFloors):
    print(f'Текущий этаж равен {floor + 1}')
