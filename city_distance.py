from math import radians, sin, cos, sqrt, atan2


class DistanceClass:
    radius = 6373.0
    sign_map = {
        'N': 1,
        'S': -1,
        'W': -1,
        'E': 1
    }

    def process_city_coordinate(self, city_coordinate):
        if ', ' not in city_coordinate:
            return None, None
        city_lat = radians(float(city_coordinate.split(', ')[0].split(' ')[0]) * self.sign_map.get(
            city_coordinate.split(', ')[0].split(' ')[1]))
        city_lon = radians(float(city_coordinate.split(', ')[1].split(' ')[0]) * self.sign_map.get(
            city_coordinate.split(', ')[1].split(' ')[1]))
        return city_lat, city_lon

    def calculate_distance(self, city_one, city_two):
        city1_lat, city1_lon = self.process_city_coordinate(city_one)
        city2_lat, city2_lon = self.process_city_coordinate(city_two)
        if None in [city1_lon, city1_lat, city2_lon, city2_lat]:
            print('Please check the format of input coordinates and try again')
        else:
            dif_lon = city2_lon - city1_lon
            dif_lat = city2_lat - city1_lat
            a = sin(dif_lat / 2) ** 2 + cos(city1_lat) * cos(city2_lat) * sin(dif_lon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = self.radius * c
            print("Output: City 1 and City 2 are {} km apart".format(round(distance, 2)))


dist_class = DistanceClass()
city1 = input('City 1: ')
city2 = input('City 2: ')
dist_class.calculate_distance(city1, city2)
