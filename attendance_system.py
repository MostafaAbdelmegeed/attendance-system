import Utilities
import FacesExtractor
import face_recognition

# URL = 'http://192.168.1.3:8080/shot.jpg'
# camera = Utilities.Camera(URL)
# camera.startShooting(10, 0.2)                       # Takes a number of shots with a delay of 0.2 second between shots
# shots = camera.getPhotosBatch()            # Contains the batch of photos the camera just took


image = face_recognition.load_image_file("students.jpg")
facesExtractor = FacesExtractor.FacesExtractor()
extracted_faces = facesExtractor.extractFrom(image)
encoded_extracted_faces = []
#for shot in shots:
  #  extracted_faces.append(facesExtractor.extractFrom(shot))
   # encoded_extracted_faces.append(face_recognition.face_encodings(shot)[0])

