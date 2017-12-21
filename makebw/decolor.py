import cv2
from glob import glob

# I have no idea about any of the parameter, numbers here.
# All thanks to stackoverflow + openCV documentation

def makeBW(filepath):
	im_gray = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
	im_blur = cv2.medianBlur(im_gray, 5)
	im_adgauss = cv2.adaptiveThreshold(im_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	im_blurgauss = cv2.GaussianBlur(im_adgauss, (5, 5), 0)
	blur = cv2.blur(im_blurgauss,(10,10))
	thres, im_bw = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	cv2.imwrite(filepath[:-4] + ".png", im_bw)

im_files = glob('./im/*.JPG')

for file in im_files:
	makeBW(file)
