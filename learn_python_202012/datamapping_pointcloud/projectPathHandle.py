import os
import shutil
import json

import paraFilehandle


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


# pointcloudDir
# /media/yanzhe/SHCJ01/1205/20201205115519_WYT_SHANGHAI_AFA1119/03_LiDAR_RAW/01_POINTCLOUD/LiDAR_2
def get_pointcloudDir(project_dir, lidar_name):
    pointcloudDir = project_dir + "/03_LiDAR_RAW/01_POINTCLOUD/LiDAR_1"
    return pointcloudDir


# trajectoryFile
# /media/yanzhe/SHCJ01/1205/20201205115519_WYT_SHANGHAI_AFA1119/06_INS_PROC/20201205115519_WYT_SHANGHAI_AFA1119_Proc.nav
def get_trajectoryFile(project_dir):
    trajectoryFile = project_dir + \
        "/06_INS_PROC/" + get_project_name(project_dir) + ".nav"
    return trajectoryFile
    # print("trajectoryFile:" + trajectoryFile)


def get_all_scanfolder_name(project_dir):
    # todo.............
    scan_paths = os.listdir(project_dir + "/03_LiDAR_RAW/01_POINTCLOUD")

    return scan_paths


def get_sigle_scanfolder_path(project_dir, lidar_name):
    # todo.............

    # scan_paths = {}
    for scan_folder in os.listdir(project_dir + "/03_LiDAR_RAW/01_POINTCLOUD"):
        if scan_folder == lidar_name:
            return project_dir + "/03_LiDAR_RAW/01_POINTCLOUD/" + scan_folder


def create_11_pointcloud_dir(project_dir, lidar_name):

    POINTCLOUD_dir = project_dir + "/11_POINTCLOUD/"
    if os.path.exists(POINTCLOUD_dir) is False:
        os.mkdir(POINTCLOUD_dir)

    outputDir = project_dir + "/11_POINTCLOUD/" + lidar_name + "_POINTCLOUD"
    if os.path.exists(outputDir):
        os.removedirs(outputDir)

    # os.mkdir(project_dir + "/11_POINTCLOUD/" + lidar_name)
    os.mkdir(outputDir)

    return outputDir


def get_lidar_type(project_dir, lidar_name):
    # 1#CAR and LiDAR_1
    if str(project_dir).find("DSX116") != -1 and str(lidar_name).find(
            "1") != -1:
        return str(128)
    # 1#CAR and not LiDAR_1
    elif str(project_dir).find("DSX116") != -1 and str(lidar_name).find(
            "1") == -1:
        return 32

    # not 1#CAR and LiDAR_1
    elif str(project_dir).find(
            "DSX116") == -1 and str(lidar_name).find("1") != -1:
        return 64

    # not 1# car and not LiDAR_1
    elif str(project_dir).find("DSX116") == -1 and str(lidar_name).find(
            "1") == -1:
        return 32

    # def get_outputDir(project_dir, lidar_name):
    #     return project_dir + "/11_POINTCLOUD/"+lidar_name


def createProcNavFile(project_dir):
    ProcNavFile = project_dir + "/06_INS_PROC/" + get_project_name(
        project_dir) + "_Proc.nav"

    if os.path.exists(ProcNavFile):
        os.remove(ProcNavFile)

    # cloudParaFile = open(ProcNavFile, "w+")
    # cloudParaFile.writelines("1tesdfsdst....test")
    # cloudParaFile.close

    shutil.copy(get_trajectoryFile(project_dir), ProcNavFile)

    return ProcNavFile


def createCloudParaFile(project_dir):
    cloudParaPath = project_dir + "/" + get_project_name(
        project_dir) + "_cloud.para"

    if os.path.exists(cloudParaPath):
        os.remove(cloudParaPath)

    vehiclePara = paraFilehandle.getVehiclePara(project_dir)

    cloudParaDictionary = json.dumps(vehiclePara)

    cloudParaFile = open(cloudParaPath, "w+")
    cloudParaFile.writelines(cloudParaDictionary)
    cloudParaFile.close

    return cloudParaPath


# TEST...........
# project_dir = "/home/slam/WM-20201006/learn_python_202012/point_cloud_join/2020120511551119_WYT_SHANGHAI_AFA1119"
# # create_11_pointcloud_dir(project_dir, "LiDAR_1")

# print(get_sigle_scanfolder_path(project_dir, "LiDAR_2"))
# print(get_lidar_type(project_dir, "LiDAR_3"))
# print(createProcNavFile(project_dir))
