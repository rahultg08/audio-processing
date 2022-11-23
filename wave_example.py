#Audio file formats
#.mp3
#.flac
#.wav
import wave

#Audio signal parameter
# -Channels: 1->Mono 2->Stereo
# -Sample width
# -framerate/sample_rate: 44,100Hz (Std freq)
# -Number of frames
# -Values of a frame (Binary)

obj = wave.open("Audio_basics\output.wav", "rb")

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("Parameters", obj.getparams())

t_audio = obj.getnframes()/obj.getframerate()
print(t_audio, "sec")

frames = obj.readframes(-1) #read all frames
print(type(frames), type(frames[0]))
print(len(frames))
print(len(frames)/2)

obj.close()

obj_new = wave.open("Audio_basics/output_new1.wav", "wb")


obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()