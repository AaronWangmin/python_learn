import projectPathHandle


def get_coordinate(project_dir):
    BLH = []

    trajectoryFile_dir = open(
        projectPathHandle.get_trajectoryFile(project_dir), "r")

    for i in range(1, 52):
        line = trajectoryFile_dir.readline()
        if i == 51:
            data = line.split()
            # refrencePointL_value = data[2]
            # refrencePointB_value = data[3]
            # refrencePointH_value = data[4]

            BLH.append(data[2])
            BLH.append(data[3])
            BLH.append(data[4])

            trajectoryFile_dir.close

            return BLH


# TEST...................
# project_dir = "/home/slam/WM-20201006/learn_python_202012/point_cloud_join/20201205115519_WYT_SHANGHAI_AFA1119"
# print(get_coordinate(project_dir))
