# Computer_Vision_Basics


For every opened window (image windows) press “q” to close.

I choose the “İstanbul Arkeoloji” Museum’s photograph as colored image.


**Problem-1** <br/>
**a)**<br/>
The first task is the cropping image. My code takes the image and crops its sides equally. In the end, the output image’s dimensions (height and width) decreasing to half of the original image. You can find output image in /output/half_Museum.png  <br/><br/>
    
![Half Museum](/output/half_Museum.png)
<br/><br/>


**b)** <br/>
The second task is changing the channels of the image. My code takes the image and extracts its “R” and “B” channels. After that, it assigns the “R” channel to the “B” channel position and does the same thing for the “B” channel. This process can be done by “cv2.cvtColor(image, cv2.COLOR_BGR2RGB)”. You can find the output image in /output/channel_changed_Museum.png<br/><br/>

![channel_changed_Museum](/output/channel_changed_Museum.png)
<br\><br\>

**c)** <br\>
The third task is changing the color space of the image (BGR to GRAY). I used a predefined function from the OpenCV-python library. It directly converts a colored image to grayscale image. “cv2.cvtColor(image, cv2.COLOR_BGR2RGB)”. You can find the output image in /output/ grayscale_Museum.png <br\><br\>

![grayscale_Museum](/output/grayscale_Museum.png)

<br\><br\>

**d)**<br\>	
The fourth task is creating a gradient magnitude and gradient orientation map of the image. Firstly, the program reads the image and converts it to grayscale after that it applies Gaussian blur. Second, it crates x and y “Sobel” kernels then filters the image with these two kernels. After that, it calculates the gradient magnitude map of the image. For the gradient orientation map, I choose the coloring technique. There is an order of colors which is; <br\>
yellow>pink>green>blue>cyan>red <br\>
In this order, gradients decreasing. For example, in the gradient orientation map, a yellow region gradient changes bigger than a pink region. In the end, I got this image.<br\><br\>	

![gradient_magnitude](/output/gradient_magnitude.png)<br\><br\>

![Gradient_orientation](/output/Gradient_orientation.png)<br\><br\>


**e)**<br\>
The fifth task is finding and displaying Laplacian of Gaussian images with different sigma values. I used a predefined function for “LoG” from the “ndimage” library. When I increase the sigma values the details and noise in the result image decrease. You can find the figure on /output/ LoG’s.png<br\><br\>
![LoG’s](/output/LoG’s.png)


