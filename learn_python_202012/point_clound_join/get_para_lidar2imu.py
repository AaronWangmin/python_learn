import os
import json

def get_lidar2imu_line(para_file, vehicle_id, lidar_id):

    data = json.load(para_file)

    vehicle_list = data["vehicle"]
    # print(vehicle_list)

    vehicle_special = vehicle_list[vehicle_id - 1]
    # print(vehicle_special)

    LidarParam = vehicle_special["LidarParam"]
    # print(LidarParam)

    Lidar2IMU = LidarParam[lidar_id - 1]["LiDAR-IMUParadata"]
    # print(Lidar2IMU)

    line = ""
    for m in range(0, 4):
        for n in range(0, 4):
            line += (str(Lidar2IMU[m][n])+"  ")
    return line


para_file = open(os.path.dirname(os.path.abspath(__file__)) +
                 "/20201205115519_WYT_SHANGHAI_AFA1119.para", "r")
print(get_lidar2imu_line(para_file, 5, 2))
