import projectPathHandle
import datamappingConfigFileHandle


def preprare(project_dir):

    # project_dir = "/home/slam/WM-20201006/learn_python_202012/point_cloud_join/2020120511551119_WYT_SHANGHAI_AFA1119"

    # create projectname_Proc.nav
    projectPathHandle.createProcNavFile(project_dir)

    # create projectname_cloud.para
    projectPathHandle.createCloudParaFile(project_dir)

    # datamappingConfigFileHandle(project_dir, "LiDAR_2")
    datamappingConfigFileHandle.create_mappingconfig(project_dir)
