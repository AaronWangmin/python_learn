import os
import json


def get_project_name(project_dir):
    project_name = os.path.basename(project_dir)
    return project_name


def get_para_dir(project_dir):
    project_name = get_project_name(project_dir)
    para_dir = project_dir + "/" + project_name + ".para"
    return para_dir


def get_vehicle_PlateNumber(project_dir):
    vehicle_plate_number = get_project_name(project_dir).split("_")[3]
    return vehicle_plate_number


def get_lidar2imu_line(project_dir, lidar_name):

    para_dir = get_para_dir(project_dir)
    para_file = open(para_dir, "r")
    para_content = json.load(para_file)
    para_file.close

    vehicle_list = para_content["vehicle"]
    # print(vehicle_list)

    LidarParams = []
    vehicle_plate_number = get_vehicle_PlateNumber(project_dir)
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
            line += (str(matrix[m][n])+"  ")
    return line


def creat_lidar2imu_file(project_dir, lidar_name):

    lidar2imu_line = get_lidar2imu_line(project_dir, lidar_name)

    lidar2imu_file_dir = project_dir + "/" + \
        get_project_name(project_dir) + "_" + lidar_name

    lidar2imu_file = open(lidar2imu_file_dir, "w+")
    lidar2imu_file.writelines(lidar2imu_line)

    lidar2imu_file.close


project_dir = "/home/slam/WM-20201006/learn_python_202012/point_cloud_join/20201205115519_WYT_SHANGHAI_AFA1119"
print(get_project_name(project_dir))
print(get_para_dir(project_dir))
print(get_vehicle_PlateNumber(project_dir))
print(get_lidar2imu_line(project_dir, "LiDAR_1"))

creat_lidar2imu_file(project_dir, "LiDAR_1")
