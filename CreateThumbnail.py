'''
Created on Sep 3, 2018

@author: DUY
'''
import os, sys
from PIL import Image
from pandas import DataFrame
import re
########################## Rename #############
dir = "E://Programming_Projects/python_projects/CreateThumbnail/PicPassImages/origin_images"
listFile = os.listdir(dir)
for i in range(0, len(listFile)):
    print(listFile[i])
with open("E://Programming_Projects/python_projects/CreateThumbnail/PicPassImages/name.txt") as f:
    names = f.readlines()
#ordered_files = sorted(listFile, key=lambda x: (int(re.sub('\D','',x)),x))
for i in range(0, len(listFile)):
#     print(ordered_files[i])
    extension = os.path.splitext(listFile[i])[1][1:]
    os.renames(dir + "/" + listFile[i], dir + "/" + names[i].strip()+ "." + extension)
# for i in range(0, len(listFile)):
#     print(names[i].strip())
print("rename successful")

######################## Create thumbnail #########################
size = 256, 256
images = []
origin_urls=[]
thumbnail_urls=[]
w=[]
h=[]
origin_path = "E://Programming_Projects/python_projects/CreateThumbnail/PicPassImages/origin_images"
images = os.listdir(origin_path)
thumb_path = 'E://Programming_Projects/python_projects/CreateThumbnail/PicPassImages/thumbnails'
for i in range(0, len(images)):
    print(images[i])
    outfile =  thumb_path + '/' + images[i]
    
    try:
        im = Image.open(origin_path + '/' + images[i])
        im.thumbnail(size)
        im.save(outfile, "JPEG")

        om = Image.open(outfile)
        width, height = om.size
        print(str(width) + " " + str(height));
        origin_urls.append("https://raw.githubusercontent.com/picpass/PicPassImages/master/origin_images/" + images[i])
        thumbnail_urls.append("https://raw.githubusercontent.com/picpass/PicPassImages/master/thumbnails/"+ images[i])
        w.append(width)
        h.append(height)
    except IOError:
        print ("cannot create thumbnail for", images[i])
df = DataFrame({'origin': origin_urls, 'thumbnail': thumbnail_urls, 'width':w, 'height':h})
df.to_excel('E://Programming_Projects/python_projects/CreateThumbnail/PicPassImages/test.xlsx', sheet_name='sheet1', index=False)
