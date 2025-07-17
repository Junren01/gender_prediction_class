import streamlit as st
import nltk
from joblib import load
import time

# Download names if not already present
nltk.download('names')

# Feature extractor
def extract_gender_features(name):
    name = name.lower()
    features = {
        "suffix": name[-1:],
        "suffix2": name[-2:] if len(name) > 1 else name[0],
        "suffix3": name[-3:] if len(name) > 2 else name[0],
        "suffix4": name[-4:] if len(name) > 3 else name[0],
        "suffix5": name[-5:] if len(name) > 4 else name[0],
        "suffix6": name[-6:] if len(name) > 5 else name[0],
        "prefix": name[:1],
        "prefix2": name[:2] if len(name) > 1 else name[0],
        "prefix3": name[:3] if len(name) > 2 else name[0],
        "prefix4": name[:4] if len(name) > 3 else name[0],
        "prefix5": name[:5] if len(name) > 4 else name[0]
    }
    return features

# Load trained model
bayes = load('gender_prediction.joblib')

def main():
    st.set_page_config(page_title="Hello Kitty Gender Predictor Supreme 💖", page_icon="🎀", layout="centered")

    # CSS for kawaii effects
    st.markdown("""
        <style>
        body {
            background: linear-gradient(-45deg, #ffe6f2, #ffd1dc, #ffe6f2, #ffd1dc);
            background-size: 400% 400%;
            animation: gradientBG 10s ease infinite;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .main {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            color: #ff3399;
            text-align: center;
        }
        .card {
            background-color: rgba(255, 240, 245, 0.9);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0px 0px 20px #ff99cc;
            margin: 20px auto;
            max-width: 500px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff99cc, #ff66b3);
            color: white;
            font-size: 18px;
            border-radius: 12px;
            padding: 0.5em 2em;
            border: 2px solid #ff66b3;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.1);
            background: linear-gradient(90deg, #ff66b3, #ff99cc);
        }
        .footer {
            font-size: 16px;
            color: #ff66b3;
            margin-top: 50px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Working Hello Kitty image
    st.image(
        "https://upload.wikimedia.org/wikipedia/en/0/05/Hello_Kitty_character_portrait.png",
        use_column_width=True
    )

    # Title + subtitle
    st.markdown("<h1>🎀😸 Hello Kitty Gender Predictor SUPREME 😸🎀</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;font-size:20px;'>✨ Enter your cutest name and see the kawaii magic unfold! ✨</p>", unsafe_allow_html=True)

    # Card for input/output
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Input field
    input_name = st.text_input('🌸 Your Cute Name 🌸', placeholder="e.g., Kitty, Melody, Daniel")

    if st.button('🎀 Predict Now 🎀'):
        if input_name.strip() != '':
            # Predict
            features = extract_gender_features(input_name)
            predicted_gender = bayes.classify(features)

            # Effects
            st.balloons()
            st.snow()
            time.sleep(0.5)

            st.success(f'🎀 The predicted gender for **"{input_name}"** is: 🌸 **{predicted_gender.capitalize()}** 🌸')
        else:
            st.warning('🌸 Please enter a cute name 🌸')

    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div class="footer">
        ✨ Made with 💖 by Hello Kitty Fans Club ✨<br>
        🌸 Stay kawaii & spread cuteness everywhere! 🌸
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
