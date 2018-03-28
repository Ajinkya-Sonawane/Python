# Getting Started with Videos
## Capturing and storing a video from camera using open-cv

**Learn to capture video from Camera and display it.**

__Basic functions:__

<ol>
	<li> cv2.VideoCapture() </li>
	<ul>
		<li>To capture a video, you need to create a VideoCapture object.</li>
		<li>Its argument can be either the device index or the name of a video file.</li>
		<li>Device index is just the number to specify which camera.</li>
		<li>Normally one camera will be connected (as in my case).</li>
		<li>So I simply pass 0 (or -1).</li>
		<li>You can select the second camera by passing 1 and so on.</li>
		<li>After that, you can capture frame-by-frame.</li>
		<li>But at the end, don’t forget to release the capture</li>
	</ul>
	<li>cv2.VideoWriter()</li>
	<ul>
		<li>Specify</li>
		<ul>
			<li>the output file name with extension</li>
			<li>FourCC code, details below</li>
			<li>Number of frames per seond (fps)</li>
			<li>isColor flag, whether video should be colored or grayscale</li>
		</ul>
		<li>FourCC is a 4 byte code used to specify video codec.</li>
		<li>List of avialble codecs can be found in <a href="https://www.fourcc.org">fourcc.org</a></li>
		<li>In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable.</li>
		<li>MJPG results in high size video. X264 gives very small size video)</li>
		<li>In Windows: DIVX (More to be tested and added)</li>
	</ul>
</ol>
