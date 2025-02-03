import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API Key
genai.configure(api_key="Your gemini api key")

# Title
st.title("🎵 AI-Powered Lyrics Generator")

# User Input for Lyrics
st.header("🎤 Generate Lyrics in the Style of Famous Artists")
artist = st.selectbox("Select an Artist:", ["J. Cole", "Drake", "Kendrick Lamar", "Eminem", "The Weeknd"])
genre = st.selectbox("Select a Genre:", ["Hip-Hop", "R&B", "Pop", "Rap", "Soul"])
topic = st.text_area("Enter a theme for your lyrics:", "")

if st.button("Generate Lyrics"):
    with st.spinner("Generating AI-powered lyrics..."):
        try:
            # Initialize Gemini model
            model = genai.GenerativeModel("gemini-pro")
            
            # Generate Lyrics using Gemini
            prompt = f"Write song lyrics in the style of {artist} in the {genre} genre about {topic}."
            response = model.generate_content(prompt)
            
            if response and hasattr(response, 'text'):
                st.text_area("Generated Lyrics:", response.text, height=300)
                st.success("🎤 AI-Generated Lyrics Ready!")
            else:
                st.error("Failed to generate lyrics.")
        except Exception as e:
            st.error(f"Error generating lyrics: {e}")
