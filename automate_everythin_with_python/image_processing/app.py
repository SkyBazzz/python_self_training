"""/course/automate-everything-with-python"""
#  pylint: disable=maybe-no-member
from pathlib import Path
import cv2
import numpy as np


#  Provide a jpeg into input folder
input_dir = Path("input")
output_dir = Path("output")
output_dir.mkdir(parents=True, exist_ok=True)


def read_image_in_gray(photo_path):
    return cv2.imread(str(photo_path), 0)


def calculate_size(cv_image, percentage):
    return int(cv_image.shape[1] * 50 / 100), int(cv_image.shape[0] * percentage / 100)


PERCENTAGE = 50


def resize(proc_image, percentage):
    new_dim = calculate_size(proc_image, percentage)
    return cv2.resize(proc_image, new_dim)


def find_faces(proc_image, cascade: cv2.CascadeClassifier):
    faces = cascade.detectMultiScale(proc_image, 1.1, 4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 5

    for index, dimension in enumerate(faces, 1):
        text_size, _ = cv2.getTextSize(str(index), font, font_scale, font_thickness)
        x_coord, y_coord, f_width, f_height = dimension
        cv2.rectangle(proc_image, (x_coord, y_coord), (x_coord + f_width, y_coord + f_height), (255, 255, 255), 4)
        text_x = x_coord + (f_width - text_size[0]) // 2
        text_y = y_coord + (f_height + text_size[1]) // 2
        cv2.putText(proc_image, str(index), (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)
    return cv2.imwrite("output/rect-faces.jpeg", proc_image)


for jpeg_path in input_dir.rglob("*.jpeg"):
    image = read_image_in_gray(jpeg_path)
    cv2.imwrite(f"{output_dir}/gray-{jpeg_path.name}", image)
    resized_image = resize(image, PERCENTAGE)
    cv2.imwrite(f"{output_dir}/resized-{jpeg_path.name}", resized_image)

faces_cascade = cv2.CascadeClassifier("input/faces.xml")
found_faces = find_faces(cv2.imread("input/humans.jpeg"), faces_cascade)

#  for water marks cv2.addWeighted()

#  changing background

foreground = cv2.imread("background/giraffe.jpeg")
background = cv2.imread("background/safari.jpeg")

width = foreground.shape[1]
height = foreground.shape[0]

resized_background = cv2.resize(background, (width, height))

for i in range(width):
    for j in range(height):
        pixel = foreground[j, i]
        if np.any(pixel == [28, 255, 76]):
            foreground[j, i] = resized_background[j, i]
cv2.imwrite("output/new_giraffe.jpeg", foreground)
