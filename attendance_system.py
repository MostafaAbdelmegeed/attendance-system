"""
    TO-DO:

    -- Constructing the database
    1- Register students in the format of (ID, NAME, PHOTO_PATH).
    2- Save the registered students in a database as a spreadsheet containing 3 columns of the latter parameters.
    3- Now that you have your registered students, get their encoded faces in an array.

    -- Shooting and collecting
    1- Shots of the attendees are going to be shot using IPWebcam through an android phone.
    2- Collect the photos in an array.
    3- Save the Photos in an external directory.
    4- Start processing and extracting faces from each one of the photos.
    5- Save the extracted faces in a different external directory and locally to an array.
    6- Basically, now you have multiple shots to the same audience, so obviously faces will be replicated.
    7- Replication of faces is our aim, now as we have the faces of the audience, lets encode them into an array
        to start comparing and voting.

    -- Extracting Faces
    1- Feed the algorithm with a number of shots taken using IPWebcam.
    2- These shots are to be processed and faces in it should be extracted and saved as jpg.
    3- After extracting faces, get encoded faces.
    4- Now that you have the encoded faces of the attendees, you should start the comparison process.

    -- Comparison
    1- The comparison will be build on voting procedure.
    2- Each student instance have a member variable representing how many votes did it take.
    3- A threshold is to be decided upon results accuracy later on, but for now, if the student instance had more votes
        than half the number of shots, he/she is considered present.
    4- Finally, extract the list of present students to be fool proved against the list of QR IDs coming from the
        second layer of fool proving

    -- QR
    1- Now as a list of students with their IDs are stored in a spreadsheet, a simple check is to be run against the
        submitted QR IDs, if numbers are consistent, the process is complete, if not, the source of inconsistency is
        re-checked for votes, if votes is above 1/4 of the number of shots, the student is recoded as present.
"""

import Utilities
import face_extractor
import face_recognition
import glob
from PIL import Image
import csv
import Student
import helper

print('Enter IPWebcam IP address (***.***.*.*:****) :')
IP = input()
URL = 'http://{}//shot.jpg'.format(IP)
NUM_OF_SHOTS = 5
DELAY = 2
SHOTS_DIRECTORY = "./attendees/{}.jpg"
THRESHOLD = NUM_OF_SHOTS / 2


def main():
    camera = Utilities.Camera(URL)
    camera.startShooting(NUM_OF_SHOTS, DELAY)  # Starts shooting the audience
    shots = camera.getPhotosBatch()  # Contains the batch of photos the camera just took
    camera.saveShootingsIntoDirectory(SHOTS_DIRECTORY)  # Saves taken shots into a directory pre-defined as a global var
    print("{} shots were delivered successfully!".format(len(shots)))
    facesExtractor = face_extractor.FaceExtractor()  # Instance from FaceExtractor
    extracted_faces = facesExtractor.extract_from_directory('./attendees/*.jpg', './attendees/extracted_faces/face{'
                                                                                 '}.jpg')  # Extract faces from shots
    encoded_extracted_faces = helper.encode_faces(extracted_faces)  # Encoding the extracted faces
    students = helper.get_students_from_database()  # Gets list of registered students
    students_encoded_faces = helper.get_students_encoded_faces(students)  # Encodes the registered students faces
    for encoded_face in encoded_extracted_faces:
        matches = face_recognition.compare_faces(students_encoded_faces, encoded_face)  # Testing against the registered
        for match in matches:
            index = matches.index(match)
            if match:
                students[index].incrementVotes()
    helper.export_attendance_results(students, './voting.csv')  # Exports voting results
    # helper.clearTempData()   Removes temporary data made throughout the executing


main()

# TO-DO open Registered students and get their encoded faces, then compare each face from the extracted faces with
# faces from registered students - if matched, this means this match is present in the class, if not, proceed to check
# QR


# for shot in shots:
#  extracted_faces.append(facesExtractor.extractFrom(shot))
# encoded_extracted_faces.append(face_recognition.face_encodings(shot)[0])
