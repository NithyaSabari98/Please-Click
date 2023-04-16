import streamlit as st
import time

# Define the text and animation settings
text = "Sorry Nithi Kutty"
color = "red"
font_size = 100

# Define the function to animate the text
def animate_text():
    for i in range(len(text)):
        st.markdown(f"<h1 style='color:{color};font-size:{font_size}px'>{text[:i+1]}</h1>", unsafe_allow_html=True)
        time.sleep(0.5)

# Create the Streamlit app
def main():
    st.set_page_config(page_title="Sorry Animation")
    st.title("Sorry Animation")
    animate_text()

if __name__ == "__main__":
    main()
