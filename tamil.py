import sounddevice as sd
import speech_recognition as sr

def getVoiceInput():
    # Get the default microphone
    default_mic = sd.default.device[0]

    # Record audio from the default microphone
    duration = 4  # seconds
    global samprate
    samprate = sd.query_devices(default_mic, 'input')['default_samplerate']
    recording = sd.rec(int(duration * samprate),
                     samplerate=samprate,
                     channels=1,
                     device=default_mic)
    sd.wait()
    return recording

def main():
    r = sr.Recognizer()
    recording = getVoiceInput()
    audio_data = sr.AudioData(recording, sample_rate=samprate, sample_width=2)
    print("You said: ")
    sd.play(recording)
    sd.wait()
    try:
        print("Converting speech to text with  ...")
        text = r.recognize_whisper(audio_data, language="tamil")
        print("Converted!")
    except sr.UnknownValueError:
        print("Could not understand audio!")
    except sr.RequestError as e:
        print("Could not request results from whisper!")
        print(e)

    print("English: ")
    print(text)

main()