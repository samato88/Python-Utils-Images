# get average width and height of images in the target directory
# uses PyExifTool - http://smarnach.github.io/pyexiftool/

# Note that this reports EXIF:ImageHeight and EXIF:ImageWidth (Not plain ImageHeight and ImageWidth)

import os
import exiftool

#path = "./testimages/"


path = raw_input('Enter full path and directory that contains files to process, e.g. /home/smith/Wallulah/1910/:\n')

while not os.path.isdir(path):
    print "directory doesn't exist - try again:"
    path = raw_input('Enter full path and directory that contains files to process, e.g. /home/smith/Wallulah/1910/:\n')

if not path.endswith('/'):
    path = path + "/"

myfiles = []
totalfiles  = 0
totalheight = 0
totalwidth  = 0
largestwidth = 0
largestheight = 0

#myfiles = ["./testimages/BlainDiary_020.jpg", "./testimages/BlainDiary_022.jpg", "./testimages/BlainDiary_024.jpg"]

for root, dirs, files in os.walk(path):
    for name in files:
        #print root, name
        myfiles.append(root + name)

with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(myfiles)
for d in metadata:
    totalfiles  += 1
    height = d["EXIF:ImageHeight"]
    width  = d["EXIF:ImageWidth"]
    if largestheight < height:
        largestheight = height
    if largestwidth < width:
        largestwidth = width
    totalheight += height
    totalwidth  += width
    #print d["EXIF:ImageHeight"]
    #print d["EXIF:ImageWidth"]
    print totalfiles, " : ", largestwidth


print "TOTAL FILES   : " , totalfiles
print "AVERAGE HEIGHT: " , totalheight / totalfiles
print "AVERAGE WIDTH : " , totalwidth / totalfiles
# checking and printing this just to make sure there aren't any oddball outlyers
print "LargestHeight: ", largestheight , " LargestWidth: ", largestwidth
