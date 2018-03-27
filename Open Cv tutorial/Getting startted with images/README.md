# First Program : Getting started with images
## using cv2 library

## Installation : <code> pip install opencv-python</code>

### Basic functions :
    cv2.imread()

        Reads the image from the given path in the given mode

        Parameter 1 : path of the image
        Parameter 2 : flag to indicate in which mode the image should be loaded

        flag types:
            cv2.IMREAD_COLOR OR 1       : loads a color image without transparency
            cv2.IMREAD_GRAYSCALE OR 0   : loads image in grayscale mode
            cv2.IMREAD_UNCHANGED OR -1  : loads a color image with transparency

    cv2.imshow()

        displays the image given by the imread() function

        Parameter 1 : window name for the image
        Parameter 2 : the image object returned by imread() function

    cv2.waitKey()

        keyboard binding function, its argument is the time in milliseconds.
        The function waits for specified milliseconds for any keyboard event.
        If you press any key in that time, the program continues.
        If 0 is passed, it waits indefinitely for a key stroke.
        It can also be set to detect specific key strokes like, if key a is pressed etc which we will discuss below.

    cv2.destroyAllWindows()

        simply destroys all the windows we created.
        If you want to destroy any specific window, use the function cv2.destroyWindow() 
        where you pass the exact window name as the argument.

    cv2.namedWindows()

        There is a special case where you can already create a window and load image to it later.
        In that case, you can specify whether window is resizable or not.
        By default, the flag is cv2.WINDOW_AUTOSIZE.
        But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window.
        It will be helpful when image is too large in dimension and adding track bar to windows.

    cv2.imwrite()

        function to save an image.
        First argument is the file name, second argument is the image you want to save.

<figure>
<img src="https://github.com/Ajinkya-Sonawane/Python/blob/master/Open%20Cv%20tutorial/Getting%20startted%20with%20images/a.png" width =400 height=400 >     
<figcaption> Actual Image</figcaption>
</figure>

<figure>
<img src="https://github.com/Ajinkya-Sonawane/Python/blob/master/Open%20Cv%20tutorial/Getting%20startted%20with%20images/a_bw.png" width =400 height=400 >     
<figcaption> Image with Mode : IMREAD_GRAYSCALE </figcaption>
</figure>

<figure>
<img src="https://github.com/Ajinkya-Sonawane/Python/blob/master/Open%20Cv%20tutorial/Getting%20startted%20with%20images/a_c.png" width =400 height=400 >     
<figcaption> Image with Mode : IMREAD_COLOR </figcaption>
</figure>

<figure>
<img src="https://github.com/Ajinkya-Sonawane/Python/blob/master/Open%20Cv%20tutorial/Getting%20startted%20with%20images/a_cwo.png" width =400 height=400 >     
<figcaption> Image with Mode : IMREAD_UNCHANGED</figcaption>
</figure>
<hr>
<b> Notice there's no difference between actual image and image in mode IMREAD_UNCHANGED </b>
