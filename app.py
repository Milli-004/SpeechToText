# app.py
import gradio as gr
import whisper
from transformers import pipeline

# Load models (once at startup)
print("Loading Whisper model...")
model = whisper.load_model("base")
print("Whisper model loaded!")

print("Loading sentiment model...")
sentiment = pipeline("sentiment-analysis")
print("Sentiment model loaded!")

# Function to handle audio -> transcription + sentiment
def speech_sentiment(audio_file):
    """
    Input: path to audio file
    Output: transcription text, sentiment
    """
    if audio_file is None:
        return "No audio uploaded.", "No sentiment"
    
    # Transcribe audio
    result = model.transcribe(audio_file)
    text = result['text']
    
    # Analyze sentiment
    sentiment_result = sentiment(text)
    
    # Return transcription + sentiment label + score
    return text, f"{sentiment_result[0]['label']} ({sentiment_result[0]['score']:.2f})"

# Gradio interface
iface = gr.Interface(
    fn=speech_sentiment,
    inputs=gr.Audio(source="upload", type="filepath"),
    outputs=["text", "text"],
    title="Speech Sentiment Analysis",
    description="Upload an audio file to get its transcription and sentiment analysis."
)

# Launch Gradio app (Gradio Hub will handle permanent hosting)
if __name__ == "__main__":
    iface.launch()
