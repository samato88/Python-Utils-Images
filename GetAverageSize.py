# get average width and height of images in the target directory
# uses PyExifTool - http://smarnach.github.io/pyexiftool/

# Note that this reports both file and EXIF height and width, and notes if they differ

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
totalfileswithexif = 0

etotalheight = 0
etotalwidth  = 0
elargestwidth = 0
elargestheight = 0

ftotalheight = 0
ftotalwidth  = 0
flargestwidth = 0
flargestheight = 0

#myfiles = ["./testimages/BlainDiary_020.jpg", "./testimages/BlainDiary_022.jpg", "./testimages/BlainDiary_024.jpg"]

for root, dirs, files in os.walk(path):
    for name in files:
        #print root, name
        myfiles.append(root + name)

with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(myfiles)
for d in metadata:
    #print d
    totalfiles  += 1

    if 'EXIF:ImageHeight' in d:  # check to make sure there is exif data before calling it
        totalfileswithexif += 1
        eheight = d["EXIF:ImageHeight"]
        ewidth  = d["EXIF:ImageWidth"]

        if elargestheight < eheight:
            elargestheight = eheight
        if elargestwidth < ewidth:
            elargestwidth = ewidth
        etotalheight += eheight
        etotalwidth  += ewidth

    fheight = d["File:ImageHeight"]
    fwidth  = d["File:ImageWidth"]

    if flargestheight < fheight:
        flargestheight = fheight
    if flargestwidth < fwidth:
        flargestwidth = fwidth
    ftotalheight += fheight
    ftotalwidth  += fwidth

    #print d["EXIF:ImageHeight"]
    #print d["EXIF:ImageWidth"]
    #print d["File:ImageHeight"]
    #print d["File:ImageWidth"]

print
print "TOTAL FILES   : " , totalfiles
print
if totalfileswithexif > 0:
    print "TOTAL FILES that had EXIF DATA : ", totalfileswithexif
    print "EXIF AVERAGE HEIGHT: " , etotalheight / totalfileswithexif
    print "EXIF AVERAGE WIDTH : " , etotalwidth / totalfileswithexif
    # checking and printing this just to make sure there aren't any oddball outlyers
    print "ExifLargestHeight: ", elargestheight , " ExifLargestWidth: ", elargestwidth
print
print "File AVERAGE HEIGHT: " , ftotalheight / totalfiles
print "File AVERAGE WIDTH : " , ftotalwidth / totalfiles
# checking and printing this just to make sure there aren't any oddball outlyers
print "FileLargestHeight: ", flargestheight , " FileLargestWidth: ", flargestwidth
if totalfileswithexif == totalfiles:  # all files had both size and exif data
        if (ftotalwidth != etotalwidth or ftotalheight != etotalheight):
                print "FILE AND EXIF DATA DIFFER!!!!!!!!!"
print
