import project_dir_parse
import create_lidar2imu_file
import nav_parse


def create_mappingconfig(project_dir):
    for lidar_name in project_dir_parse.get_all_scanfolder_name(project_dir):
        create_lidar_join_configfile(project_dir, lidar_name)


def create_lidar_join_configfile(project_dir, lidar_name):
    datamappingConfig_dir = project_dir + "/datamappingConfig_" + lidar_name
    datamappingConfig = open(datamappingConfig_dir, "w+")

    pointcloudDir = project_dir_parse.get_sigle_scanfolder_path(
        project_dir, lidar_name)
    datamappingConfig.writelines("pointcloudDir    " + pointcloudDir + "\n")

    trajectoryFile = project_dir_parse.get_trajectoryFile(project_dir)
    datamappingConfig.writelines("trajectoryFile    " + trajectoryFile + "\n")

    proclocalPos = project_dir + "/06_INS_PROC/" + \
        project_dir_parse.get_project_name(project_dir) + "_Proc.pos"
    datamappingConfig.writelines("proclocalPos    " + proclocalPos + "\n")

    outputDir = project_dir_parse.create_11_pointcloud_dir(
        project_dir, lidar_name)
    datamappingConfig.writelines("outputDir    " + outputDir + "\n")

    calibParamFile = create_lidar2imu_file.creat_lidar2imu_file(
        project_dir, lidar_name)
    datamappingConfig.writelines("calibParamFile    " + calibParamFile + "\n")

    outputfileType = str(0)
    datamappingConfig.writelines("outputfileType     " + outputfileType + "\n")

    blockDis = str(100)
    datamappingConfig.writelines("blockDis           " + blockDis + "\n")

    lidarType = project_dir_parse.get_lidar_type(project_dir, lidar_name)
    datamappingConfig.writelines("lidarType     " + str(lidarType)+"\n")

    inputfileType = str(0)
    datamappingConfig.writelines(
        "inputfileType           " + inputfileType + "\n")

    frontGroundMinY = get_frontGroundMinY(lidar_name)
    datamappingConfig.writelines(
        "frontGroundMinY     " + str(frontGroundMinY)+"\n")

    frontGroundMaxY = get_frontGroundMaxY(lidar_name)
    datamappingConfig.writelines(
        "frontGroundMaxY     " + str(frontGroundMaxY)+"\n")

    backGroundMinY = get_backGroundMinY(lidar_name)
    datamappingConfig.writelines(
        "backGroundMinY     " + str(backGroundMinY)+"\n")

    backGroundMaxY = get_backGroundMaxY(lidar_name)
    datamappingConfig.writelines(
        "backGroundMaxY     " + str(backGroundMaxY)+"\n")

    forwardDegree = str(8)
    datamappingConfig.writelines(
        "forwardDegree           " + forwardDegree + "\n")

    refrencePointB = nav_parse.get_coordinate(project_dir)[1]
    datamappingConfig.writelines(
        "refrencePointB     " + str(refrencePointB)+"\n")

    refrencePointL = nav_parse.get_coordinate(project_dir)[0]
    datamappingConfig.writelines(
        "refrencePointL     " + str(refrencePointL)+"\n")

    refrencePointH = nav_parse.get_coordinate(project_dir)[2]
    datamappingConfig.writelines(
        "refrencePointH     " + str(refrencePointH)+"\n")

    visualization = str(8)
    datamappingConfig.writelines(
        "visualization           " + visualization + "\n")

    datamappingConfig.close


def get_frontGroundMinY(lidar_name):
    if str(lidar_name).find("1") != -1:
        return 2
    if str(lidar_name).find("1") == -1:
        return 0


def get_frontGroundMaxY(lidar_name):
    if str(lidar_name).find("1") != -1:
        return 30
    if str(lidar_name).find("1") == -1:
        return 0


def get_backGroundMinY(lidar_name):
    if str(lidar_name).find("1") != -1:
        return 0
    if str(lidar_name).find("1") == -1:
        return -40


def get_backGroundMaxY(lidar_name):
    if str(lidar_name).find("1") != -1:
        return 0
    if str(lidar_name).find("1") == -1:
        return -6
    # if str(lidar_name).find("1") == -1:
    #     return -40


# test...................................
project_dir = "/home/slam/WM-20201006/learn_python_202012/point_cloud_join/2020120511551119_WYT_SHANGHAI_AFA1119"
# create_lidar_join_configfile(project_dir, "LiDAR_2")
create_mappingconfig(project_dir)
