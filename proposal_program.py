import streamlit as st

def proposal_program():
    # Title with emoji
    st.title("💖 A Special Moment for You! 💖")
    st.header("Welcome to a magical journey, just for you! 🌟")
    st.write("Let's play a fun and interactive game together!")

    # Step 1: Ask for name
    name = st.text_input("First, may I know your beautiful name? 💕")
    if name:
        st.success(f"Wow, {name}! Such a lovely name! ❤️")

    # Step 2: Interactive questions with effects
    st.write("Now, let me know more about your favorites:")
    favorite_color = st.text_input("🎨 What’s your favorite color?")
    dream_place = st.text_input("🌍 What’s your dream destination?")
    favorite_flower = st.text_input("🌸 What’s your favorite flower?")
    favorite_food = st.text_input("🍕 What’s your favorite food?")

    # Step 3: Build the suspense
    if st.button("✨ Create the Magical Moment ✨"):
        if name and favorite_color and dream_place and favorite_flower and favorite_food:
            st.balloons()  # Launch balloons to celebrate
            st.write("💭 Imagine this scene:")
            st.markdown(f"""
            <div style="font-size: 20px; font-weight: bold; margin: 20px 0; color: #FF69B4;">
            🌈 The sky is glowing <b>{favorite_color}</b>.
            🏞️ We’re in <b>{dream_place}</b>, your dream destination.
            🌺 Surrounding us are fragrant <b>{favorite_flower}s</b>.
            🍽️ We’re enjoying a delicious meal of <b>{favorite_food}</b>.
            </div>
            """, unsafe_allow_html=True)
            
            st.write("And then, I take your hand, look into your eyes, and say...")

            st.markdown("## 💖 *Will you be the sunshine of my life and my forever partner?* 💍")
            st.success("🎉 Yay! You've made this moment unforgettable! ❤️")
            st.snow()  # Add falling snow for a magical effect
        else:
            st.warning("Please fill in all the details to make this moment perfect! 😊")

    # Footer with thank-you message
    st.write("---")
    st.markdown("<div style='text-align: center;'>Thank you for sharing this special moment with me. 💕</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>Let’s make every day as magical as this one! 🌟</div>", unsafe_allow_html=True)

# Run the program
proposal_program()
