import cv2
import os, os.path

print (cv2.__version__)

imageDir = "rawpic/" #specify your path here 
image_path_list = []
valid_image_extensions = [".JPG",".jpg", ".jpeg", ".png", ".tif", ".tiff"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]
pic_num = 1

for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

for imagePath in image_path_list:
    img = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        continue

    resized_image = cv2.resize(img, (200, 200))
    cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
    print(pic_num)
    pic_num += 1
    #cv2.imshow(imagePath, img)
    

    key = cv2.waitKey(0)
    if key == 27: # escape
        break

cv2.destroyAllWindows()
