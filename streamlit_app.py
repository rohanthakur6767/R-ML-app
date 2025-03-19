import streamlit as st
import time
import os
from PIL import Image

# Set page config
st.set_page_config(page_title="Happy Birthday 🎂", layout="centered")

# Title
st.title("🎉 Happy Birthday, [Her Name]! 🎈")

# Display a special message
st.subheader("💖 A Special Message Just for You 💖")

# Birthday Message
message = """  
My love Anshikaa,  

happy birthday to my love of my life...

Meri jaan, tumse milne ka intezaar ab aur nahi ho raha! 💖 
Tumhari hasi meri duniya roshan karti hai, aur tumhari baatein mere dil ka sukoon hain.
tum mere liye bhot special ho i love you soo much my love 🌸✨  

i promise i will keep loving youu darling..

Have the best birthday ever! 🎈🎁🎊  

With lots of love,  
your Rohan Thakur

if st.button("Click to Reveal the Surprise 💌"):
    with st.spinner("Unwrapping the surprise... 🎁"):
        time.sleep(2)
    st.write(message)

# Function to resize images into a square (300x300)
def resize_to_square(image_path, size=300):
    img = Image.open(image_path)
    img = img.resize((size, size), Image.LANCZOS)
    return img

# Display Preloaded Photos
st.subheader("📸 Some Beautiful Pictures 📸")

# List of image paths
image_paths = ["2.jpg", "3.jpg", "4.jpg"]

# Display resized images
for img_path in image_paths:
    if os.path.exists(img_path):
        resized_img = resize_to_square(img_path)
        st.image(resized_img, caption="My beautifull girl 💖")
    else:
        st.error(f"Image not found: {img_path}. Check the file path.")

# Celebration animation
st.balloons()
st.success("Hope this made your day special! 😊🎉")
