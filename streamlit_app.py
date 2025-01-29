import streamlit as st
import time

# App title
st.set_page_config(page_title="Happy Birthday 🎉", layout="centered")

# Header
st.title("🎂 Happy Birthday, [Her Name]! 🎈")

# Display a cute message
st.subheader("💖 A Special Message Just for You 💖")

# Animated message reveal
message = """  
Dear [Her Name],  

On this special day, I just want to remind you how amazing you are!  
You bring so much joy, laughter, and love into everyone's life.  
Wishing you all the happiness in the world today and always! 🎉💖  

With love,  
[Your Name]  
"""

if st.button("Click to Reveal the Message 💌"):
    with st.spinner("Unwrapping the surprise... 🎁"):
        time.sleep(2)  # Simulate a delay
    st.write(message)

# Upload and display photos
st.subheader("📸 Beautiful Memories Together 📸")
uploaded_files = st.file_uploader("Upload photos to make this moment more special!", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

if uploaded_files:
    for file in uploaded_files:
        st.image(file, use_column_width=True, caption="A precious memory! 💖")

# Confetti for celebration
st.balloons()
st.success("Hope this made you smile! 😊💖")

