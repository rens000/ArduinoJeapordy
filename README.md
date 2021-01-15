# ArduinoJeapordy
Here are some steps to help you set up your arduino :)

1. For this project you will need to first install Pyfirmata on your computer.
   Go to your terminal, type in "pip install pyfirmata" (or "pip3 install pyfirmata" if project done in idle3).
2. You will then need to upload the PyFirmata firmware on the Arduino.
   Make sure you have the arduino IDE downloaded (https://www.arduino.cc/en/Main.Software).
   In the arduino IDE go to Files -> Examples -> Firmata -> StandardFirmata.
   A bunch of code will open in another window (You do not need to look at this or know what it does).
   Now go Sketch -> Include Library -> Manage Libraries.
   Here another window will open, search "Firmata", and install the newest version if it is not already.
   Lastly, go back into the IDE and click the little right arrow (next to the check mark) called UPLOAD (make sure your arduino is plugged in and under tools board, processor, and port are all selected correctly).
3. Set up your hardware in accordance with the pictures provided on GITHUB (see notes in code itself on where to connect wires to Arduino UNO).
4. Lastly you need to replace the name of the USB port in the code with your own (replace '/dev/cu.usbmodem14301' in board = Arduino('/dev/cu.usbmodem14301')).
   This is pretty easy to do, in the Arduino IDE the name of your connected USB port should be listed next to port under Tools.
   After this is done you should be able to run the program directly from IDLE!
   
   
   
   
![tempImage4B6Dax](https://user-images.githubusercontent.com/57843464/104767500-40b11980-573a-11eb-86c0-4c2d0ad3e75a.gif)




![tempImageuhSKAo](https://user-images.githubusercontent.com/57843464/104767516-4870be00-573a-11eb-8db3-bcdbcf9d50e5.gif)
