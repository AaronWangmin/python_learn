import os
import paraFilehandle
import projectPathHandle


def createCalibParaFileSingle(project_dir, lidar_name):

    lidar2imu_line = paraFilehandle.get_lidar2imu_line(project_dir, lidar_name)

    lidar2imu_file_dir = project_dir + "/" + \
        projectPathHandle.get_project_name(
            project_dir) + "_calibration_" + lidar_name

    if os.path.exists(lidar2imu_file_dir):
        os.remove(lidar2imu_file_dir)

    lidar2imu_file = open(lidar2imu_file_dir, "w+")
    lidar2imu_file.writelines(lidar2imu_line)
    lidar2imu_file.close

    return lidar2imu_file_dir


# project_dir = "/home/slam/WM-20201006/learn_python_202012/point_cloud_join/20201205115519_WYT_SHANGHAI_AFA1119"
# # print(get_project_name(project_dir))
# # print(get_para_dir(project_dir))
# # print(get_vehicle_PlateNumber(project_dir))
# # print(get_lidar2imu_line(project_dir, "LiDAR_1"))

# print(createCalibParaFileSingle(project_dir, "LiDAR_3"))
