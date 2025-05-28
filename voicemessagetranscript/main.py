from pydub import AudioSegment
import whisper

model = whisper.load_model("turbo")
result = model.transcribe("voicemessages/voicemessage.wav")
print(result["text"])
# ogg to wav converter
def ogg2wav(ofn):
    wfn = ofn.replace('.ogg','.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav') # maybe use original resolution to make smaller
    
#ogg2wav("voicemessages/voicemessage.ogg")

