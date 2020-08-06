echo Dette script installere de nødvendige programmer til at kunne benytte Thingspeak!
echo
pip3 install thingspeak
git clone http://github.com/mchwalisz/thingspeak.git
export PATH=/home/pi/.loacl/bin:$PATH
echo Nu er det muligt at lave programmer til Python3(Thonny) sammen med Thingspeak
