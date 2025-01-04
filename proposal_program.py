import streamlit as st

def proposal_program():
    # Title and Introduction
    st.title("💖 A Special Moment for You! 💖")
    st.header("Welcome to a magical journey! 🌟")
    st.write("Let's have some fun together and create a memory you'll cherish forever.")

    # Step 1: Ask for Name
    name = st.text_input("First, may I know your beautiful name? 💕")
    if name:
        st.success(f"Wow, {name}! Such a lovely name! ❤️")

    # Step 2: Ask About Preferences
    if name:
        st.write("Now, let me learn more about your favorites!")
        favorite_color = st.text_input("🎨 What’s your favorite color?")
        dream_place = st.text_input("🌍 What’s your dream destination?")
        favorite_flower = st.text_input("🌸 What’s your favorite flower?")
        favorite_food = st.text_input("🍕 What’s your favorite food?")

    # Step 3: Proposal with Positive Choices
    if name and favorite_color and dream_place and favorite_flower and favorite_food:
        st.write("✨ Let's create a magical moment for you!")
        
        if st.button("💌 Begin the Journey 💌"):
            st.balloons()
            st.markdown(f"""
            <div style="font-size: 20px; font-weight: bold; margin: 20px 0; color: #FF69B4;">
            🌈 Imagine a perfect day with the sky glowing {favorite_color}.
            🏞️ We're in {dream_place}, surrounded by {favorite_flower}s.
            🍽️ Sharing a delicious meal of {favorite_food}, I take your hand and say...
            </div>
            """, unsafe_allow_html=True)

            st.markdown("## 💖 *Will you be my forever partner?* 💍")
            
            # Display only positive options
            choice = st.radio(
                "Choose your response:",
                ["Yes, absolutely! ❤️", "Of course, yes! 🌟", "I’d love to! 💕"]
            )
            
            # Respond positively no matter the choice
            if choice:
                st.success("🎉 Yay! You've made this moment unforgettable! ❤️")
                st.snow()
    
    # Footer with gratitude
    st.write("---")
    st.markdown(
        "<div style='text-align: center;'>Thank you for sharing this special moment with me! 💕</div>", 
        unsafe_allow_html=True
    )

# Run the program
proposal_program()
