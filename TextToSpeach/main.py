from gtts import gTTS
from playsound3 import playsound

texto = input('Escribe algo: ') # Le pedimos al usuario que ingrese un texto 
tts = gTTS(text=texto, lang='es') # Llamamos a la función GTTS con dos parametros, que son el texto en español y el lenguaje del modelo
tts.save('audio.mp3') # Guardamos el archivo de audio
playsound('audio.mp3', block=False) # Lo reproducimos posteriormente 