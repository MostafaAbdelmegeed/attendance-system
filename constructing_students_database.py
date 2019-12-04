"""
    Those are used for user input through the console
        print("Enter student's info")
        print("Name: ")
        student_name = input()
        print("ID: ")
        student_id = input()
        print("Photo Path: ")
        student_photo_path = input()
"""

import csv
from PIL import Image


def registerStudent(student_name, student_id, student_photo_path):
    image = Image.open(student_photo_path)
    image.save("./database/{}.jpg".format(student_id))
    EXISTS = False

    with open('./database/registered_students.csv', newline='') as file:
        reader = csv.reader(file)
        for eachRow in reader:
            if student_id == eachRow[0]:
                EXISTS = True

    with open('./database/registered_students.csv', 'a', newline='') as csvfile:
        if not EXISTS:
            writer = csv.writer(csvfile)
            writer.writerow([student_id, student_name, "./database/{}.jpg".format(student_id)])
        else:
            print("Student already exists in the database")
            EXISTS = False


photos = ['./test_faces/mostafa.jpg', './test_faces/ahmed.jpg', './test_faces/eman.jpg', './test_faces/basem.jpg'
    , './test_faces/gaber.jpg', './test_faces/khadija.jpg', './test_faces/yara.jpg', './test_faces/tamer.jpg'
    , './test_faces/omar.jpg', './test_faces/othman.jpg', './test_faces/ragab.jpg']
names = ['Mostafa', 'Ahmed', 'Eman', 'Basem', 'Gaber', 'Khadija', 'Yara', 'Tamer', 'Omar', 'Othman', 'Ragab']
IDs = ['11553', '11554', '11555', '11556', '11557', '11558', '11559', '11560', '11561', '11562', '11563']
for name in names:
    index = names.index(name)
    registerStudent(name, IDs[index], photos[index])
