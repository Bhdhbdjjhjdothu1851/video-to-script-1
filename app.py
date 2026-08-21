import streamlit as st
import whisper

st.title("Video to Script Converter")
model = whisper.load_model("base")

uploaded_file = st.file_uploader("ဗီဒီယိုဖိုင် တင်ပါ", type=["mp4", "mkv", "mp3", "wav"])

if uploaded_file is not None:
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.info("စာသားအဖြစ် ပြောင်းလဲနေပါသည်...")
    result = model.transcribe("temp_file")
    st.success("ပြီးပါပြီ!")
    st.text_area("ရရှိလာသော စာသား (Script)", result["text"], height=300)
import streamlit as st
import whisper

st.title("Video to Script Converter")

# မြန်မာစာအတွက် Accuracy ပိုကောင်းစေရန် small model ကို ပြောင်းသုံးနိုင်ပါသည်။ (base အစား small ထားပါ)
model = whisper.load_model("small")

uploaded_file = st.file_uploader(
    "ဗီဒီယိုဖိုင် တင်ပါ", type=["mp4", "mkv", "mp3", "wav"]
)

if uploaded_file is not None:
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("စာသားအဖြစ် ပြောင်းလဲနေပါသည်...")

    # language='my' (Burmese/Myanmar) ဟု တိုက်ရိုက်သတ်မှတ်ပေးလိုက်ခြင်း ဖြစ်သည်
    result = model.transcribe("temp_file", language="my", task="transcribe")

    st.success("ပြီးပါပြီ!")
    st.text_area("ရရှိလာသော စာသား (Script)", result["text"], height=300)
import streamlit as st
import whisper

st.title("Video to Script Converter")

# RAM မပြည့်စေရန် base model ပြန်သုံးပါမည်
model = whisper.load_model("base")

uploaded_file = st.file_uploader(
    "ဗီဒီယိုဖိုင် တင်ပါ", type=["mp4", "mkv", "mp3", "wav"]
)

if uploaded_file is not None:
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("စာသားအဖြစ် ပြောင်းလဲနေပါသည်...")

    # မြန်မာဘာသာစကားအဖြစ် သတ်မှတ်ထားပါသည်
    result = model.transcribe("temp_file", language="my", task="transcribe")

    st.success("ပြီးပါပြီ!")
    st.text_area("ရရှိလာသော စာသား (Script)", result["text"], height=300)
import streamlit as st
import whisper

st.title("Video to Script Converter")


# RAM မပြည့်စေရန် Model ကို Cache လုပ်ပြီး အပေါ့ပါးဆုံး tiny model သုံးပါမည်
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("tiny")


model = load_whisper_model()

uploaded_file = st.file_uploader(
    "ဗီဒီယိုဖိုင် တင်ပါ", type=["mp4", "mkv", "mp3", "wav"]
)

if uploaded_file is not None:
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("စာသားအဖြစ် ပြောင်းလဲနေပါသည်...")

    # မြန်မာစာအဖြစ် တိုက်ရိုက် ပြောင်းလဲခြင်း
    result = model.transcribe("temp_file", language="my", task="transcribe")

    st.success("ပြီးပါပြီ!")
    st.text_area("ရရှိလာသော စာသား (Script)", result["text"], height=300)
