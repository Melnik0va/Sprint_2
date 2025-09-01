class PointsForPlace:
    def __init__(self):
        self.points = 0

    def get_points_for_place(self, place):
        if place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        elif place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        else:
            self.points = 101 - place
            return self.points


class PointsForMeters:
    def __init__(self):
        self.points = 0

    def get_points_for_meters(self, meters):
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            self.points = meters * 0.5
            return self.points


class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)
        self.total = 0

    def get_total_points(self, meters, place):
        points_from_place = self.get_points_for_place(place)
        points_from_meters = self.get_points_for_meters(meters)

        if isinstance(points_from_place, str):
            return points_from_place
        if isinstance(points_from_meters, str):
            return points_from_meters

        self.total = points_from_place + points_from_meters
        return self.total



points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))  

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10)) 

total_points = TotalPoints()
print(total_points.get_points_for_place(10)) 
print(total_points.get_points_for_meters(10)) 
print(total_points.get_total_points(100, 10)) 
