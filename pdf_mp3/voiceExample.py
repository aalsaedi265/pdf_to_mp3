import pyttsx3
 
# Create a string
string = "Lorem Ipsum is simply dummy text f the printing and typesetting industry."
 
# Initialize the Pyttsx3 engine
engine = pyttsx3.init()
 
# Command it to speak the given string
engine.say(string)
 
# Wait until above command is not finished.
engine.runAndWait()