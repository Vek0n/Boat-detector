# Boat-detector
The goal was to make system that detects rowing boats in real time and to semi-automize cameras during [live streaming of rowing regattas](https://youtu.be/TYqMPD-ogRI).
<br>
# Algorithm
Algorithm scans through <img src="http://chart.apis.google.com/chart?cht=tx&chl=w%20%20%5Ctimes%20h%0A"> image, for every <img src="http://chart.apis.google.com/chart?cht=tx&chl=k%5E%7Bth%7D"> pixel it extracts <img src="http://chart.apis.google.com/chart?cht=tx&chl=n"> smaller fragments of an image with current pixel in center. Then every fragment is given to neural network for detection. Hence number of detections is equal to <img src="http://chart.apis.google.com/chart?cht=tx&chl=%5Cfrac%7Bw%5Ccdot%20h%7D%7Bk%7D%5Ccdot%20n"> Smaller <img src="http://chart.apis.google.com/chart?cht=tx&chl=k%0A"> and bigger <img src="http://chart.apis.google.com/chart?cht=tx&chl=n%0A"> result in better detection but increase run-time __drastically__.

For an `1280x720` image and `k = 50`, `n = 12` neural network has to perform approximately `221,184` detections and return ones with the highest probability rate.

This approach is not very efficient and results in long run-time (about 30s) for every image. Thus this algorithm cannot be used in real-time video analysis.

# Training
Neural network was trained using `~10,000` images taken from Youtube [live streams](https://youtu.be/FmIYS_HoOcU?t=12061) of rowing regattas.

~5,000 photos of boats:<br>
<img src="training_examples/single-317.jpg" width="300"><br>
<img src="training_examples/quadruple-86.jpg" width="300"><br>
<img src="training_examples/octuple-17.jpg" width="300"><br><br>
~5,000 photos of background:<br>
<img src="training_examples/not_boat-52.jpg" width="300"><br>
<img src="training_examples/not_boat-339.jpg" width="300"><br>
<img src="training_examples/not_boat-1463.jpg" width="300"><br>
<br>
# Sample output
To run the algorithm one should place file with [trained weights](https://drive.google.com/open?id=1oSi8GdSwcwuVJtlZKOSVpd_2f8YIjzLX) in /models directory<br>
<img src="output/fig1.png" width="300"><br>
<img src="output/fig2_new.png" width="300"><br>
<img src="output/out1.png" width="300"><br>
<img src="output/fig12_new.png" width="300"><br>
<img src="output/out.png" width="300"><br>
