import cv2
import glob
import os

thres = 0
# Get a list of all the video files in the folder
videos = glob.glob(r"C:\Users\Administrator\Desktop\t3.mp4")

# Loop through each video file
for video_file in videos:

    # Open the video file
    video = cv2.VideoCapture(video_file)

    # Initialize a counter to keep track of the frames
    count = 0

    # Loop through the video frames
    while True:
        ret, frame = video.read()
        count += 1

        if not count % 500 == 0:
            continue
        # Read a frame from the video

        # Break the loop if we have reached the end of the video
        if not ret:
            break

        # Increment the frame counter

        # Save the frame as an image
        cv2.imwrite(f'ds/_frame_{count}.jpg', frame)

    # Release the video object
    video.release()
