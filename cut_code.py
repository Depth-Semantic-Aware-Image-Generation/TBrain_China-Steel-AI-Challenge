import os
import cv2

path = "start(craft_mtl_25k.pth)" # jpg图片和对应的生成结果的txt标注文件，放在一起
path3 = "end(craft_mlt_25k.pth)"  # 裁剪出来的小图保存的根目录
img_total = []
txt_total = []

file = os.listdir(path)
for filename in file:
    first,last = os.path.splitext(filename)
    if last == ".jpg":                  #圖片的後綴名
        img_total.append(first)
    #print(img_total)
    else:
        txt_total.append(first)
        
for img_ in img_total:
    if img_ in txt_total:
      filename_img = img_+".jpg"        #圖片的後綴名
      #print('filename_img:', filename_img)
      path1 = os.path.join(path,filename_img)
      img = cv2.imread(path1)
      filename_txt = img_+".txt"
      #print('filename_txt:', filename_txt)
      t = 1
      botton = 0
      top = 10000
      left = 10000
      right = 0
      with open(os.path.join(path,filename_txt),"r+",encoding="utf-8",errors="ignore") as f:
          for line in f:
              aa = line.split(",")
              if(t%2==1):
                  if(int(aa[0]) < left):
                      left = int(aa[0])
                  if(int(aa[2]) > right):
                      right = int(aa[2])
                  if(int(aa[1]) < top or int(aa[1]) > top+75):
                      top = int(aa[1])
                  if(int(aa[5]) > botton):
                      botton = int(aa[5])
              t = t+1
#          roi = img[350:465,726:200]
          x_length = (int(float(right)) - int(float(left)))/50
          y_length = (int(float(botton)) - int(float(top)))/2.5
          roi = img[int(float(top))-int(y_length/2):int(float(botton))+int(y_length/2),int(float(left))-int(x_length*5):int(float(right))+int(x_length*15)]
#          roi = img[top-10:botton+20,left-5:right+5]   #[左上y:右下y,左上x:右下x] (y1:y2,x1:x2)需要調參，否則裁剪出來的小圖可能不太好
          print('roi:', roi)                        #如果不resize圖片統一大小，可能會得到有的roi為[]導致報錯
          filename_last = img_+".jpg"    #裁剪出來的小圖文件名
          #pring(filename_last)
          path2 = os.path.join(path3,"roi")         #需要在path3路徑下創建一個roi的文件夾
          print('path2:',path2)                     #裁剪小圖的保存位置
          try:
              cv2.imwrite(os.path.join(path2,filename_last),roi)
          except:
              print(filename_last)
              cv2.imwrite(os.path.join(path2,filename_last),img)
    else:
        continue
    
    