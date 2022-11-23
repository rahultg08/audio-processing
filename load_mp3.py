from pydub import AudioSegment

audio = AudioSegment.from_wav("outputrec.wav")

audio = audio+8      #Increasing volume by 6dB

audio = audio*2      #Repeat the recording twice

audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("Done")