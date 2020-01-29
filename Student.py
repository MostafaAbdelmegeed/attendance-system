import face_recognition


class Student:
    def __init__(self, identification, name, face):
        self.face = face_recognition.load_image_file(face)
        self.face_height, self.face_width = self.face.shape
        self.face_location = (0, self.face_width, self.face_height, 0)
        self.encoded_face = face_recognition.face_encodings(self.face, known_face_locations=[self.face_location])[0]
        self.name = name
        self.id = identification
        self.votes = 0

    def incrementVotes(self):
        self.votes = self.votes + 1
