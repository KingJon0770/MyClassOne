from math import sin, asin, cos, radians, fabs, sqrt

EARTH_RADIUS = 6371 * 10 ** 3  # 地球半径m


class OneToOneDistance:
    @staticmethod
    def hav(theta)->float:
        s = sin(theta / 2)  # 半角公式
        return s ** 2

    @staticmethod
    def get_distance_hav(lon_lat:list[float])->float:
        """
        用haversine公式计算球面两点间的距离
        """
        # 经纬度转换为弧度
        lon1 = radians(lon_lat[0])  # A longitude 经度
        lat1 = radians(lon_lat[1])  # A latitude 纬度
        lon2 = radians(lon_lat[2])  
        lat2 = radians(lon_lat[3])  
        
        d_lon = fabs(lon1 - lon2)
        d_lat = fabs(lat1 - lat2)  # fabs求绝对值函数，接收浮点数参数
        

        h = OneToOneDistance.hav(d_lat) + cos(lat1) * cos(lat2) * OneToOneDistance.hav(d_lon)
        distance = 2 * asin(sqrt(h)) * EARTH_RADIUS
        distance = round(distance, 0)
        return distance



if __name__ == '__main__':
    print(OneToOneDistance.get_distance_hav([102.97106,30.21308, 103.10099, 30.04253]))
   