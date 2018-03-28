# Getting Started with Videos
## Capturing and storing a video from camera using open-cv

* Learn to capture video from Camera and display it. *

Basic functions:

    1. cv2.VideoCapture()
		
		* To capture a video, you need to create a VideoCapture object.
        * Its argument can be either the device index or the name of a video file.
        * Device index is just the number to specify which camera.
        * Normally one camera will be connected (as in my case).
        * So I simply pass 0 (or -1).
        * You can select the second camera by passing 1 and so on.
        * After that, you can capture frame-by-frame.
        * But at the end, don’t forget to release the capture.

    1. cv2.videoWriter()
        * Specify : *
            - the output file name with extension
            - FourCC code, details below
            - Number of frames per seond (fps)
            - isColor flag, whether video should be colored or grayscale

        * FourCC is a 4 byte code used to specify video codec.
        * List of avialble codecs can be found in fourcc.org
        * In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable.
        * MJPG results in high size video. X264 gives very small size video)
        * In Windows: DIVX (More to be tested and added)

