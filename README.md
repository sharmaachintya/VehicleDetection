# VehicleDetection

Implemented Real time vehicle Detection using haar cascade. I've attached the cars.xml file, all we have to do is just read that xml file, in that file haar cascade classifier is used to detect vehicles and all I did is just stored that xml file in a variable and just converted the frames in gray scale images and with the help of detectMultiScale function, I used that xml file with the gray frames which will give us the coordiantes of any vehicle, if present. After that I just drawn a rectangle around the car.
