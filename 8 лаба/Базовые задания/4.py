class train:

    def __init__(self, departure, arrival, start_time, stop_time):
        
        self.departure = departure
        self.arrival =  arrival
        self.start_time = start_time
        self.stop_time =  stop_time

    def __add__(self, other): #– для операции сложения
        if self.arrival == other.departure and self.stop_time < other.start_time:
            departure, arrival, start_time, stop_time = self.departure, other.arrival, self.start_time, other.stop_time
            return (departure, arrival, start_time, stop_time)
        else:
            print('Оперция сложения для этих поездов не доступна')


tr1 = train('Москва', "Питер", 12.34, 16.32)
tr2 = train("Питер", "Душанбе", 16.35, 18.12)
print(tr1 + tr2)