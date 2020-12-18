import os
import json


def get_project_name(project_dir):
    project_name = os.path.basename(project_dir)
    return project_name


def get_para_dir(project_dir):
    project_name = get_project_name(project_dir)
    para_dir = project_dir + "\\" + project_name + ".para"
    return para_dir


def get_vehicle_PlateNumber(project_dir):
    vehicle_plate_number = get_project_name(project_dir).split("_")[3]
    return vehicle_plate_number


def get_lidar2imu_line(project_dir, lidar_id):

    para_dir = get_para_dir(project_dir)
    para_file = open(para_dir, "r")
    para_content = json.load(para_file)
    para_file.close

    vehicle_list = para_content["vehicle"]
    # print(vehicle_list)

    LidarParam = []
    vehicle_plate_number = get_vehicle_PlateNumber(project_dir)
    for vehicle in vehicle_list:
        if vehicle["PlateNumber"] == vehicle_plate_number:
            LidarParam = vehicle["LidarParam"]
            break

    Lidar2IMU = LidarParam[lidar_id - 1]["LiDAR-IMUParadata"]
    # print(Lidar2IMU)

    return matrix2line(Lidar2IMU)


def matrix2line(matrix):
    line = ""
    for m in range(0, 4):
        for n in range(0, 4):
            line += (str(matrix[m][n])+"  ")
    return line


project_dir = "G:\\learn_python_202012\\point_clound_join\\20201205115519_WYT_SHANGHAI_AFA1119"
print(get_project_name(project_dir))
print(get_para_dir(project_dir))
print(get_vehicle_PlateNumber(project_dir))
print(get_lidar2imu_line(project_dir, 1))
