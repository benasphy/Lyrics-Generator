# AI-Powered Lyrics Generator

## Overview
This project is an AI-powered lyrics generator that mimics the style of famous artists like **J. Cole, Kendrick Lamar, Drake, Eminem, and The Weeknd** across various genres. Users can input a theme, and the AI generates lyrics that align with the selected artist’s style. The application is built using **Streamlit** and **Google's Gemini AI**.

## Features
- 🎤 **Generate lyrics** in the style of famous artists
- 🎶 **Choose from multiple genres** (Hip-Hop, R&B, Pop, Rap, Soul)
- ✍ **Customizable themes** for personalized lyrics
- ⚡ **Real-time AI generation** powered by Google’s Gemini Pro model

## The Idea Behind the App
As a fan of **Hip-Hop, mainly Kendrick Lamar and J. Cole**, I wanted to create an AI-powered tool that generates lyrics similar to these great artists. The app provides users with the ability to **craft AI-generated lyrics** while preserving the unique style of each artist.

## How Prompting Techniques Were Applied
The application utilizes **prompt engineering techniques** to refine the output:

- **Contextual Prompting**: The AI is given clear instructions about the desired artist, genre, and theme to generate relevant lyrics.
- **Few-Shot Prompting**: Future updates may include examples of lyrics before the AI generates its own to refine the response further.
- **Iterative Prompting**: Users can refine inputs and re-generate lyrics for improved results.
- **Chain-of-Thought Prompting**: Structured prompts help guide the AI to ensure coherence across verses and rhymes.

## Parameters Tweaked and Why
To optimize lyric generation, we fine-tuned several AI parameters:

- **Temperature (0.7–0.9)**: Controls creativity, ensuring diverse yet coherent responses.
- **Top-P (0.8–0.95)**: Allows diverse word choices for engaging lyrics.
- **Max Tokens**: Limits response length to prevent overly long or irrelevant lyrics.
- **Presence & Frequency Penalty**: Tweaked to minimize repetition, ensuring natural-sounding lyrics.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/benasphy/Lyrics-Generator.git
   ```
2. Navigate to the project folder:
   ```sh
   cd Lyrics-Generator
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your API key:
   ```sh
   export GEMINI_API_KEY=your_api_key
   ```
5. Run the app:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Select an artist and genre.
2. Enter a theme for your song.
3. Click **Generate Lyrics** and let the AI create lyrics for you!

## Future Improvements
- 🎧 **Voice-to-Lyrics Generation**: Convert spoken words into AI-generated lyrics.
- 🎼 **Melody Generation**: Generate melodies based on lyrics.
- 📜 **Few-Shot Training**: Provide example lyrics for better AI output.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Google Gemini AI** for powering the lyric generation.
- **Streamlit** for the interactive UI.
- **Hip-Hop legends** like J. Cole and Kendrick Lamar for inspiration.

🚀 **Enjoy generating AI-powered lyrics!**

