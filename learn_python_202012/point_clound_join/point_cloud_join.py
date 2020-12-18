
import os

# get project_dir
project_dir = "/home/slam/WM-20201006/learn_python_202012/point_clound_join/20201205115519_WYT_SHANGHAI_AFA1119"
print("project_dir:" + project_dir)

# get projetname,20201205115519_WYT_SHANGHAI_AFA1119
dir_base = os.path.split(project_dir)
projectname = dir_base[1]
print("projectname:" + projectname)


# pointcloudDir /media/yanzhe/SHCJ01/1205/20201205115519_WYT_SHANGHAI_AFA1119/03_LiDAR_RAW/01_POINTCLOUD/LiDAR_2
pointcloudDir = [project_dir + "/03_LiDAR_RAW/01_POINTCLOUD/LiDAR_1", project_dir +
                 "/03_LiDAR_RAW/01_POINTCLOUD/LiDAR_2", project_dir + "/03_LiDAR_RAW/01_POINTCLOUD/LiDAR_3"]
# print("pointcloudDir:" + pointcloudDir)

# trajectoryFile /media/yanzhe/SHCJ01/1205/20201205115519_WYT_SHANGHAI_AFA1119/06_INS_PROC/20201205115519_WYT_SHANGHAI_AFA1119_Proc.nav
trajectoryFile = project_dir + \
    "/06_INS_PROC/" + projectname + "_Proc.nav"
print("trajectoryFile:" + trajectoryFile)

# proclocalPos /media/yanzhe/SHCJ01/1205/20201205115519_WYT_SHANGHAI_AFA1119/06_INS_PROC/20201205115519_WYT_SHANGHAI_AFA1119_Proc.pos
proclocalPos = project_dir + \
    "/06_INS_PROC/" + projectname + "_Proc.pos"
print("proclocalPos" + proclocalPos)

# outputDir /media/yanzhe/SHCJ01/1205/20201205115519_WYT_SHANGHAI_AFA1119/11_POINTCLOUD/LiDAR_2_POINTCLOUD
pointcloud_out_dir = project_dir + "/11_POINTCLOUD"
print("pointcloud_out_dir:" + pointcloud_out_dir)

outputDir = [pointcloud_out_dir + "/LiDAR_1_POINTCLOUD", pointcloud_out_dir +
             "/LiDAR_2_POINTCLOUD", pointcloud_out_dir + "/LiDAR_3_POINTCLOUD"]
# print("outputDir:" + outputDir)

# read ins_pro file
trajectoryFile_dir = open(trajectoryFile, "r")
# trajectoryFile_content = trajectoryFile_dir.readlines()

refrencePointB_value = 0
refrencePointL_value = 0
refrencePointH_value = 0

for i in range(1, 52):
    line = trajectoryFile_dir.readline()
    if i == 51:
        coordinate = line.split()
        refrencePointL_value = coordinate[2]
        refrencePointB_value = coordinate[3]
        refrencePointH_value = coordinate[4]

trajectoryFile_dir.close

# read templete_file
templete_file = open(os.path.dirname(__file__) +
                     "/config/datamappingConfig_example_32E2", "r")
templete_content = templete_file.readlines()

# create datamappingConfig of lidar1
for lidarID in range(1, 4):

    if lidarID == 1:
        lidarType_value = 64
        frontGroundMinY_value = 2
        frontGroundMaxY_value = 30
        backGroundMinY_value = 0
        backGroundMaxY_value = 0
    if lidarID != 1:
        lidarType_value = 32
        frontGroundMinY_value = 0
        frontGroundMaxY_value = 0
        backGroundMinY_value = -40
        backGroundMaxY_value = -6

    for index, line in enumerate(templete_content):
        key = line.split(" ")[0]

        if key == "pointcloudDir":
            templete_content[index] = "pointcloudDir    " + \
                pointcloudDir[lidarID-1] + "\n"

        if key == "trajectoryFile":
            templete_content[index] = "trajectoryFile    " + \
                trajectoryFile + "\n"

        if key == "proclocalPos":
            templete_content[index] = "proclocalPos    " + proclocalPos + "\n"

        if key == "outputDir":
            templete_content[index] = "outputDir    " + \
                outputDir[lidarID-1] + "\n"

        if key == "calibParamFile":
            # templete_content[index] = "calibParamFile    " + calibParamFile
            print("test")

        if key == "lidarType":
            templete_content[index] = "lidarType    " + \
                str(lidarType_value) + "\n"

        if key == "frontGroundMinY":
            templete_content[index] = "frontGroundMinY    " + \
                str(frontGroundMinY_value) + "\n"

        if key == "frontGroundMaxY":
            templete_content[index] = "frontGroundMaxY    " + \
                str(frontGroundMaxY_value) + "\n"

        if key == "backGroundMinY":
            templete_content[index] = "backGroundMinY    " + \
                str(backGroundMinY_value) + "\n"

        if key == "backGroundMaxY":
            templete_content[index] = "backGroundMaxY    " + \
                str(backGroundMaxY_value) + "\n"

        if key == "refrencePointB":
            templete_content[index] = "refrencePointB    " + \
                str(refrencePointB_value) + "\n"

        if key == "refrencePointL":
            templete_content[index] = "refrencePointL    " + \
                str(refrencePointL_value) + "\n"

        if key == "refrencePointH":
            templete_content[index] = "refrencePointH    " + \
                str(refrencePointH_value) + "\n"

    # creat lidar_jion_config file of Lidar1
    datamappingConfig_dir = os.path.dirname(
        __file__) + "/config/datamappingConfig_" + str(lidarID)

    datamappingConfig = open(datamappingConfig_dir, "w+")
    datamappingConfig.writelines(templete_content)

    datamappingConfig.close
templete_file.close

# creat output
# if os.path.exists(pointcloud_out_dir) == False:
#     os.mkdir(pointcloud_out_dir)
# if os.path.exists(outputDir) == False:
#     os.mkdir(outputDir)

# delete output
# os.removedirs(pointcloud_out_dir)
