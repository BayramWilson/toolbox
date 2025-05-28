from pydub import AudioSegment
import whisper



# ogg to wav converter
def ogg2wav(ofn):
    wfn = ofn.replace('.ogg','.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav') # maybe use original resolution to make smaller

def wav2txt(wav):
    model = whisper.load_model("turbo")
    result = model.transcribe(wav)
    print(result["text"])
    
ogg2wav("voicemessages/vm2.ogg")
wav2txt("voicemessages/vm2.wav")
