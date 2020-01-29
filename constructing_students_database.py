"""
photos = ['./test_faces/mostafa.jpg', './test_faces/ahmed.jpg', './test_faces/eman.jpg', './test_faces/basem.jpg'
    , './test_faces/gaber.jpg', './test_faces/khadija.jpg', './test_faces/yara.jpg', './test_faces/tamer.jpg'
    , './test_faces/omar.jpg', './test_faces/othman.jpg', './test_faces/ragab.jpg']
names = ['Mostafa', 'Ahmed', 'Eman', 'Basem', 'Gaber', 'Khadija', 'Yara', 'Tamer', 'Omar', 'Othman', 'Ragab']
IDs = ['11553', '11554', '11555', '11556', '11557', '11558', '11559', '11560', '11561', '11562', '11563']
for ID in IDs:
    index = IDs.index(ID)
    registerStudent(ID, names[index], photos[index])
"""

import csv
from PIL import Image
import Utilities
import cv2
import os


def registerStudent(student_id, student_name):

    EXISTS = False

    with open('./database/registered_students.csv', newline='') as file:
        reader = csv.reader(file)
        for eachRow in reader:
            if eachRow:
                if student_id == eachRow[0]:
                    EXISTS = True

    with open('./database/registered_students.csv', 'a', newline='') as csvfile:
        if not EXISTS:
            writer = csv.writer(csvfile)
            writer.writerow([student_id, student_name, "./database/{}.jpg".format(student_id)])
        else:
            print("Student already exists in the database")
            EXISTS = False


def registerStudentsFromTerminal():
    print("IP (***.***.*.*:****) :")
    URL = "http://{}".format(input())
    camera = Utilities.Camera(URL)
    print("Enter student's info")
    print("Name: ")
    student_name = input()
    print("ID: ")
    student_id = input()
    print("Smile to the Camera :')")
    camera.startRegistering(5, 1, student_id)
    registerStudent(student_id, student_name)
    print("{} is added successfully to the database.".format(student_name))


registerStudentsFromTerminal()
