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
        
x_length = 0
y_length = 0
with open(os.path.join(path,"public_training_data原場座標.txt"),"r+",encoding="utf-8",errors="ignore") as h:
    
    tmp = h.read()
    onelinelist = tmp.split('\n')      
    for line in onelinelist:
        aa = line.split(",")
        if aa[0] in img_total:
            filename_img = aa[0]+".jpg"
            path1 = os.path.join(path,filename_img)
            img = cv2.imread(path1)  
            if(float(aa[8])>=float(aa[6])):
                left=aa[6]
            else:
                left=aa[8]
            if(float(aa[2])>=float(aa[4])):
                right=aa[2]
            else:
                right=aa[4]
            if(float(aa[9])<=float(aa[3])):
                top=aa[9]
            else:
                top=aa[3]           
            if(float(aa[7])<=float(aa[5])):
                bottom=aa[5]
            else:
                bottom=aa[7]
            x_length = (int(float(right)) - int(float(left)))/50
            y_length = (int(float(bottom)) - int(float(top)))/2.5
            roi = img[int(float(top))-int(y_length/4):int(float(bottom))+int(y_length/4),int(float(left))-int(x_length*3):int(float(right))+int(x_length*10)]
            print('roi:', roi)
            filename_last = aa[0]+".jpg"
            path2 = os.path.join(path3,"roi")
            print('path2:',path2)
            try:
                cv2.imwrite(os.path.join(path2,filename_last),roi)
            except:
                print(filename_last)
                cv2.imwrite(os.path.join(path2,filename_last),img)
        else:
            continue
    
    