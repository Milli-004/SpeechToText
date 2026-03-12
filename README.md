# 🎤 Speech Sentiment Analysis

This Hugging Face Space allows you to **transcribe speech from an audio file** and get **sentiment analysis** of the spoken text.  

You can either **upload an audio file** or (if using a compatible Space) record audio via your microphone. The app uses:

- **OpenAI Whisper** for transcription  
- **Hugging Face Transformers** for sentiment analysis  
- **Gradio** for the interactive frontend  

---

## **How to Use**

1. Click **Upload Audio** to upload an audio file (MP3, WAV, etc.)  
2. Press **Submit / Analyze**  
3. The app will display:  
   - **Transcribed Text**  
   - **Sentiment Result** (Positive / Negative / Neutral with confidence score)  

---

## **Requirements**

- Python 3.9+  
- Gradio  
- openai-whisper  
- Transformers  
- Torch  
- ffmpeg-python  

All dependencies are listed in `requirements.txt` and will be installed automatically by Hugging Face Spaces.

---

## **Notes**

- Microphone input may be supported depending on your browser/Space settings.  
- The sentiment analysis uses `distilbert-base-uncased-finetuned-sst-2-english`.  

---

## **Example Output**

| Audio | Transcription | Sentiment |
|-------|---------------|-----------|
| "I love this app!" | I love this app! | POSITIVE (0.99) |
| "This is terrible." | This is terrible. | NEGATIVE (0.97) |

---

## **Permanent URL**

Once deployed on Hugging Face Spaces, your app will have a **permanent link**:
