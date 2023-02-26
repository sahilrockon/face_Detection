import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

# Detect the coordinates
detector = dlib.get_frontal_face_detector()

while True:

	# Capture frame-by-frame
	_x, vid_cap = cap.read()
	vid_cap = cv2.flip(vid_cap, 1)

	# RGB to grayscale
	gray = cv2.cvtColor(vid_cap, cv2.COLOR_BGR2GRAY)
	faces = detector(gray)

	# Iterator to count faces
	i = 0
	for face in faces:

		# Get the coordinates of faces
		x, y = face.left(), face.top()
		x1, y1 = face.right(), face.bottom()
		cv2.rectangle(vid_cap, (x, y1), (x1, y), (255, 0, 0), 2)

		# Increment iterator for each face in faces
		i = i+1

		# Display the box and faces
		cv2.putText(vid_cap, 'FACE '+str(i), (x-10, y-10),
					cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0, 255), 2)

	# Display the resulting frame
	cv2.imshow('Video_Live', vid_cap)

	# on entering 'q' we will exit the loop
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
