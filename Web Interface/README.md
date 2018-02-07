<h2>Web Interface to control LED using Raspberry Pi</h2>
<br>

<b>Requirements</b>
<ul>
  <li>Raspberry Pi Board</li>
  <li>Raspbian OS</li>
  <li>1 LED</li>
  <li>2 Jumper Wires (Male->Female)</li>
  <li>1 Register if required</li>
</ul>

<b>Installation</b>
<ul>
  <li>Install Flask - Python Web Framework library : 
    <code>pip install flask</code></li>
</ul>

<b>Usage</b>
<ul>
	<li>Keep the html files in the templates folder</li>
	<li>Connect the LED with the approporiate port on Raspberry Pi board</li>
  <li>Run the python file <code> python code.py</code><li>
  <li>The server will be started on the given host ip and port : 5000 Eg. <code>127.0.0.1:5000</ccode></li>
</ul>


<img src="https://projects-static.raspberrypi.org/projects/physical-computing/1072decd879286bfa4627a349799d873120f7b62/en/images/led-gpio17.png" width=500>
