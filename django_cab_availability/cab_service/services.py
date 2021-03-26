from math import radians, sin, cos, sqrt, atan2


class DistanceClass:
    radius = 6373.0

    def calculate_distance(self, pos1_lat, pos1_lon, pos2_lat, pos2_lon):
        if None in [pos1_lon, pos1_lat, pos2_lon, pos2_lat]:
            print('Please check the format of input coordinates and try again')
        else:
            pos1_lat = radians(pos1_lat)
            pos1_lon = radians(pos1_lon)
            pos2_lat = radians(pos2_lat)
            pos2_lon = radians(pos2_lon)
            dif_lon = pos2_lon - pos1_lon
            dif_lat = pos2_lat - pos1_lat
            a = sin(dif_lat / 2) ** 2 + cos(pos1_lat) * cos(pos2_lat) * sin(dif_lon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = self.radius * c
            return round(distance, 4)
