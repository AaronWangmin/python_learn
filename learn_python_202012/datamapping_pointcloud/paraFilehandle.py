# import os
import json
import projectPathHandle


def get_lidar2imu_line(project_dir, lidar_name):

    para_dir = projectPathHandle.get_para_dir(project_dir)
    para_file = open(para_dir, "r")
    para_content = json.load(para_file)
    para_file.close

    vehicle_list = para_content["vehicle"]
    # print(vehicle_list)

    LidarParams = []
    vehicle_plate_number = projectPathHandle.get_vehicle_PlateNumber(
        project_dir)
    for vehicle in vehicle_list:
        if vehicle["PlateNumber"] == vehicle_plate_number:
            LidarParams = vehicle["LidarParam"]
            break

    Lidar2IMU = []
    for lidar_param in LidarParams:
        if lidar_param["LiDARName"] == lidar_name:
            Lidar2IMU = lidar_param["LiDAR-IMUParadata"]

    # Lidar2IMU = LidarParams[lidar_id - 1]["LiDAR-IMUParadata"]
    # print(Lidar2IMU)

    return matrix2line(Lidar2IMU)


def matrix2line(matrix):
    line = ""
    for m in range(0, 4):
        for n in range(0, 4):
            line += (str(matrix[m][n]) + "  ")
    return line


# TODO...........
def getVehiclePara(project_dir):
    para_dir = projectPathHandle.get_para_dir(project_dir)
    para_file = open(para_dir, "r")
    para_content = json.load(para_file)
    para_file.close

    vehicle_list = para_content["vehicle"]
    # print(vehicle_list)

    vehicle_plate_number = projectPathHandle.get_vehicle_PlateNumber(
        project_dir)
    for vehicle in vehicle_list:
        if vehicle["PlateNumber"] == vehicle_plate_number:
            return vehicle


# project_dir = "/home/slam/WM-20201006/learn_python_202012/point_cloud_join/2020120511551119_WYT_SHANGHAI_AFA1119"
# print(projectPathHandle.get_project_name(project_dir))
# print(projectPathHandle.get_para_dir(project_dir))
# print(projectPathHandle.get_vehicle_PlateNumber(project_dir))
# print(get_lidar2imu_line(project_dir, "LiDAR_1"))
# print(getVehiclePara(project_dir))
