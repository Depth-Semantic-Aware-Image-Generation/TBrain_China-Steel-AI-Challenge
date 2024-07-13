import os
import cv2

path = "start" # jpg图片和对应的生成结果的txt标注文件，放在一起
path3 = "end"  # 裁剪出来的小图保存的根目录
img_total = []
txt_total = []

file = os.listdir(path)
for filename in file:
    first,last = os.path.splitext(filename)
    if last == ".jpg":                  #圖片的後綴名
        img_total.append(first)
        

with open(os.path.join(path,"train_final3.txt"),"r+",encoding="utf-8",errors="ignore") as h:
    
    tmp = h.read()
    onelinelist = tmp.split('\n')      
    for line in onelinelist:
        aa = line.split("\t")
        if aa[0] in img_total:
            filename_img = aa[0]+".jpg"
            path1 = os.path.join(path,filename_img)
            roi = cv2.imread(path1)  

            print('roi:', roi)
            filename_last = aa[0]+".jpg"
            path2 = os.path.join(path3,"roi")
            print('path2:',path2)
            cv2.imwrite(os.path.join(path2,filename_last),roi)
        else:
            continue
    
    