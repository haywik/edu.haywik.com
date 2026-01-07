import cv2
import face_recognition

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

# Load known images and get their encodings
known_image = face_recognition.load_image_file('path_to_known_image.jpg')  # Replace with the path to your known image
known_face_encoding = face_recognition.face_encodings(known_image)[0]

known_face_encodings.append(known_face_encoding)
known_face_names.append('Person Name')  # Replace with the name of the person in the known image

# Start video capture from the default webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = video_capture.read()

    # Convert the frame to RGB (face_recognition uses RGB images)
    rgb_frame = frame[:, :, ::-1]

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face encoding with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # Check if a match is found
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Display the name of the person
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
