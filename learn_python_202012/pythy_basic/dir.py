import os
import sys

abspath = os.path.abspath(__file__)
print("abspath:" + abspath)

filename = os.path.basename(__file__)
print("filename:" + filename)

dirname = os.path.dirname(__file__)
print("dirname:" + dirname)

dir_base = os.path.split(dirname)
print("dirname:" + dir_base[0])
print("basename:" + dir_base[1])


# os.mkdir(dirame + "/test")

# delete output
# os.removedirs(pointcloud_out_dir)
