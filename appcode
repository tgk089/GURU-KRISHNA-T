import streamlit as st
from PIL import Image

def proposal_program():
    # Title and header
    st.title("💖 A Special Moment for You! 💖")
    st.header("Welcome to a magical journey, just for you! 🌟")
    st.write("Let's have a fun and interactive experience together.")

    # Display a romantic image at the top
    romantic_image = Image.open("romantic_image.jpg")  # Replace with your image file
    st.image(romantic_image, use_column_width=True, caption="A moment of love 🌹")
    
    # Step 1: Ask for name
    name = st.text_input("First, may I know your beautiful name? 💕")
    if name:
        st.success(f"Wow, {name}! Such a wonderful name! ❤️")

    # Step 2: Interactive questions with emojis
    st.write("Let me know more about your favorites:")
    favorite_color = st.text_input("🎨 What’s your favorite color?")
    dream_place = st.text_input("🌍 What’s your dream destination?")
    favorite_flower = st.text_input("🌸 What’s your favorite flower?")
    favorite_food = st.text_input("🍕 What’s your favorite food?")

    # Step 3: Build the suspense
    if st.button("✨ Create the Magical Moment ✨"):
        if name and favorite_color and dream_place and favorite_flower and favorite_food:
            st.balloons()  # Celebrate with balloons
            st.write(f"Alright, {name}, let’s create something magical...")
            
            st.write("💭 Imagine this scene:")
            st.write(f"🌈 The sky is glowing {favorite_color}.")
            st.write(f"🏞️ We’re in {dream_place}, your dream destination.")
            st.write(f"🌺 Surrounding us are beautiful {favorite_flower}s.")
            st.write(f"🍽️ We’re enjoying a delicious meal of {favorite_food}.")
            st.write("And then, I take your hand, look into your eyes, and say...")
            
            st.markdown("## 💖 'Will you be the sunshine of my life and my forever partner?' 💍")
            st.success("🎉 Yay! You’ve made this moment unforgettable! ❤️")
        else:
            st.warning("Please fill in all the details to make this moment perfect! 😊")

    # Footer with thank-you message
    st.write("---")
    st.write("Thank you for sharing this special moment with me. 💕")
    st.write("Let’s make every day as magical as this one! 🌟")

# Run the program
proposal_program()
