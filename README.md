# Clear_Board_Image
 Using image processing techniques, SIFT feature extraction, Image Stitching, Image Slicing

<p>This project is basically for a classroom enviroment, where the teacher is writing on the board and moving right to left. The problem is students waste alot of time taking lecture notes
this project will solve this problem with providing Image of the board without teacher being involved in it.<p>


- First frames are went through YOLO for detection of board and person.
- Then reach frame is sliced up into 3-part, it'll keep updating the sliced_imgs until lectures end
- At the end it will stitched images together
