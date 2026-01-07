print("Starting AI voice assistant")
import speech_recognition as sr
import commands
import time,datetime
import pyttsx3
old_speech = " "
speech = " "
name = "delta"
recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate',150)  
engine.setProperty('volume', 1)   
'''
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.operation_timeout = None
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5
'''
def end():
    exit()
    


with sr.Microphone() as source:
    while True:
        speech="blank"
        audio = recognizer.listen(source,timeout=7)
        try:

            speech = recognizer.recognize_google(audio).lower()


            print("You said: ", speech)
            
                
              
        except:
            speech="did not recognize"
        if speech =="blank":
            pass
        elif f"{name} exit" in speech:
                engine.say("Exiting the program")
                print("Exiting the program")
                break
        
        elif f"{name} open chrome" in speech:
            from commands import open_chrome

            open_chrome()

        elif f"{name} close chrome" in speech:
            from commands import close_chrome

            close_chrome()
        elif f"{name} open website" in speech:
            from commands import open_website
            speech = speech.replace(f"{name} open website","")
            if speech == " " or speech == "  " or speech =="":
                print("website not recived")
                engine.say("website not recived")
            else:
                open_website(speech)

        elif f"{name} open steam" in speech:
            from commands import open_steam
            open_steam()
        elif f"{name} close steam" in speech:
            from commands import close_steam
            close_steam()
        

        elif f"{name} what is the time" in speech or f"{name} what's the time" in speech:
            from commands import get_time
            get_time()     

        elif f"{name} what is the date" in speech or f"{name} what's the date" in speech: 
            from commands import get_date
            get_date()
        elif f"{name} skip video" in speech:
            from commands import skip_video
            skip_video()
        
        elif any(phrase in speech for phrase in [f"{name} resume video", f"{name} pause video", f"{name} play video", f"{name} stop video"]):
            from commands import resume_pause_video
            resume_pause_video()

        elif f"{name} mute video" in speech or f"{name} unmute video" in speech:
            from commands import mute_video
            mute_video()
        elif f"{name} lock pc" in speech:
            from commands import lock_pc
            lock_pc()
        elif f"{name} shutdown pc" in speech:
            from commands import shutdown_pc
            shutdown_pc()
        
        print("speech is now::",speech)
        engine.runAndWait()
       
        
        # Adjust recognizer settings for better British English recognition
        



