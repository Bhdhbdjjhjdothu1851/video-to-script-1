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
