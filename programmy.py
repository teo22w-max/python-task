import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


freq = 44100  
duration = 10
print("Yozuv boshlandi...")


recording = sd.rec(int(duration * freq), samplerate=freq, channels=2, dtype='int16')


sd.wait()

print("Yozuv tugadi. Fayl Saqlandi...")


write("recording_scipy.wav", freq, recording)


wv.write("recording_wavio.wav", recording, freq, sampwidth=2)

print("Tayyor!")


