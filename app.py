import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

st.title("🌍 CodeAlpha - AI Language Translation Tool")
st.write("Translate text between different languages using Google Translator API")

# Supported language codes
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
    "Hindi": "hi",
    "Italian": "it",
    "Russian": "ru"
}

# User Inputs
text = st.text_area("Enter text to translate:", "")
source_lang = st.selectbox("Select Source Language", list(languages.keys()), index=0)
target_lang = st.selectbox("Select Target Language", list(languages.keys()), index=1)

if st.button("Translate"):
    try:
        translated_text = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.subheader("🔤 Translated Text:")
        st.success(translated_text)

        # Text-to-Speech
        tts = gTTS(translated_text, lang=languages[target_lang])
        audio_path = "translated_audio.mp3"
        tts.save(audio_path)
        st.audio(audio_path, format="audio/mp3")

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("🚀 Developed by Laiba Rana | CodeAlpha Internship Project")
