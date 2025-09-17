from flask import Flask, render_template, request
from googletrans import Translator
from langdetect import detect  # For language detection
import nltk
import string

# Download NLTK resources
nltk.download('stopwords')
from nltk.corpus import stopwords

app = Flask(__name__)

# Language code to full name mapping
LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'ca': 'Catalan',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'hi': 'Hindi',
    'hu': 'Hungarian',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'km': 'Khmer',
    'ko': 'Korean',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'ne': 'Nepali',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sr': 'Serbian',
    'si': 'Sinhalese',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'zu': 'Zulu',
}

# Function to preprocess text (NLP)
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    
    return text

# Function to detect the language of the text
def detect_language(text):
    try:
        lang_code = detect(text)
        return LANGUAGES.get(lang_code, lang_code)  # Get full language name or return code if not found
    except:
        return "Unknown Language"  # If detection fails

# Function to translate text
def translate_text(text, target_language):
    try:
        # Check if target_language is valid
        if target_language not in LANGUAGES:
            return "Invalid target language"
        
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        

        # Check if the translation result is valid
        if translated.text is None:
            return "Translation returned None"
        
        # Check if the translation response is in a valid format
        if not isinstance(translated.text, str):
            return "Translation result is not a valid string"
        
        return translated.text
    except Exception as e:
        return f"Error in translation: {str(e)}"

# Route to handle home page and form submission
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        target_language = request.form["language"]
        
        # Preprocess text before translation (NLP)
        preprocessed_text = preprocess_text(text)
        
        # Detect source language automatically
        detected_language = detect_language(text)
        
        # Translate the preprocessed text
        translated_text = translate_text(preprocessed_text, target_language)
        
        return render_template("index.html", translated_text=translated_text, detected_language=detected_language, languages=LANGUAGES)
    
    # First time loading the page or GET request
    return render_template("index.html", translated_text="", detected_language="", languages=LANGUAGES)

if __name__ == "__main__":
    app.run(debug=True)
