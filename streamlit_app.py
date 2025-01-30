import streamlit as st
import time

# Set page config
st.set_page_config(page_title="Happy Birthday 🎂", layout="centered")

# Title
st.title("🎉 Happy Birthday, [Her Name]! 🎈")

# Display a special message
st.subheader("💖 A Special Message Just for You 💖")

# Birthday Message
message = """  
Dear [Her Name],  

🎂 Another year older, wiser, and more amazing!  
You light up the world with your kindness, laughter, and warmth.  
May this year bring you endless happiness, love, and success.  

Have the best birthday ever! 🎈🎁🎊  

With lots of love,  
[Your Name]  
"""

if st.button("Click to Reveal the Surprise 💌"):
    with st.spinner("Unwrapping the surprise... 🎁"):
        time.sleep(2)  # Simulating delay for suspense
    st.write(message)

# Display Preloaded Photos
st.subheader("📸 Some Beautiful Memories 📸")

# List of image paths (Update with your actual image file paths)
image_paths = ["R-ML-app/IMG_20240915_174832.jpg", "images/photo2.jpg", "images/photo3.jpg"]

for img in image_paths:
    st.image(img, use_column_width=True, caption="A precious moment! 💖")

# Add celebration animation
st.balloons()
st.success("Hope this made your day special! 😊🎉")
