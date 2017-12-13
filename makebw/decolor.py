import cv2
from glob import glob

def makeBW(filepath):
	im_gray = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
	im_blur = cv2.medianBlur(im_gray, 5)
	# I don't know what that 5 means :(
	im_bw = cv2.adaptiveThreshold(im_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	# I don't know what that 11, 2 means either :(
	cv2.imwrite(filepath[:-4] + ".png", im_bw)


font_files = glob('./im/*.JPG')

for file in font_files:
	makeBW(file)