import projectPathHandle
import calibParamFileHandle
import navFileHandle


def create_mappingconfig(project_dir):
    for lidar_name in projectPathHandle.get_all_scanfolder_name(project_dir):
        createMappingConfigFileSingle(project_dir, lidar_name)


def createMappingConfigFileSingle(project_dir, lidar_name):
    datamappingConfig_dir = project_dir + "/datamappingConfig_" + lidar_name
    datamappingConfig = open(datamappingConfig_dir, "w+")

    pointcloudDir = projectPathHandle.get_sigle_scanfolder_path(
        project_dir, lidar_name)
    datamappingConfig.writelines("pointcloudDir    " + pointcloudDir + "\n")

    trajectoryFile = projectPathHandle.get_trajectoryFile(project_dir)
    datamappingConfig.writelines("trajectoryFile    " + trajectoryFile + "\n")

    proclocalPos = project_dir + "/06_INS_PROC/" + \
        projectPathHandle.get_project_name(project_dir) + "_Proc.pos"
    datamappingConfig.writelines("proclocalPos    " + proclocalPos + "\n")

    outputDir = projectPathHandle.create_11_pointcloud_dir(
        project_dir, lidar_name)
    datamappingConfig.writelines("outputDir    " + outputDir + "\n")

    calibParamFile = calibParamFileHandle.createCalibParaFileSingle(
        project_dir, lidar_name)
    datamappingConfig.writelines("calibParamFile    " + calibParamFile + "\n")

    outputfileType = str(0)
    datamappingConfig.writelines("outputfileType     " + outputfileType + "\n")

    blockDis = str(100)
    datamappingConfig.writelines("blockDis           " + blockDis + "\n")

    lidarType = projectPathHandle.get_lidar_type(project_dir, lidar_name)
    datamappingConfig.writelines("lidarType     " + str(lidarType) + "\n")

    inputfileType = str(0)
    datamappingConfig.writelines("inputfileType           " + inputfileType +
                                 "\n")

    frontGroundMinY = get_frontGroundMinY(lidar_name)
    datamappingConfig.writelines("frontGroundMinY     " +
                                 str(frontGroundMinY) + "\n")

    frontGroundMaxY = get_frontGroundMaxY(lidar_name)
    datamappingConfig.writelines("frontGroundMaxY     " +
                                 str(frontGroundMaxY) + "\n")

    backGroundMinY = get_backGroundMinY(lidar_name)
    datamappingConfig.writelines("backGroundMinY     " + str(backGroundMinY) +
                                 "\n")

    backGroundMaxY = get_backGroundMaxY(lidar_name)
    datamappingConfig.writelines("backGroundMaxY     " + str(backGroundMaxY) +
                                 "\n")

    forwardDegree = str(8)
    datamappingConfig.writelines("forwardDegree           " + forwardDegree +
                                 "\n")

    refrencePointB = navFileHandle.get_coordinate(project_dir)[1]
    datamappingConfig.writelines("refrencePointB     " + str(refrencePointB) +
                                 "\n")

    refrencePointL = navFileHandle.get_coordinate(project_dir)[0]
    datamappingConfig.writelines("refrencePointL     " + str(refrencePointL) +
                                 "\n")

    refrencePointH = navFileHandle.get_coordinate(project_dir)[2]
    datamappingConfig.writelines("refrencePointH     " + str(refrencePointH) +
                                 "\n")

    visualization = str(8)
    datamappingConfig.writelines("visualization           " + visualization +
                                 "\n")

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
# project_dir = "/home/slam/WM-20201006/learn_python_202012/point_cloud_join/2020120511551119_WYT_SHANGHAI_AFA1119"
# # create_mappingConfigFileSingle(project_dir, "LiDAR_2")
# create_mappingconfig(project_dir)
