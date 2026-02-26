AI Explainer Video Generator 🎥
Project Overview

This project generates a simple AI-based explainer video automatically.

It works by:

Selecting a topic

Generating a script for that topic

Splitting the script into sentences

Generating an image for each sentence

Converting each sentence into voice

Synchronizing images and audio into a final video

The final output is a synced educational-style video called:

final_video.mp4

How It Works

main.py → Controls the full pipeline

idea_generation.py → Selects a topic

script.py → Generates the script

image.py → Downloads and prepares images

voice.py → Converts text to speech

video.py → Combines images and audio into video

Each sentence gets:

Its own generated image

Its own voice audio

Synced timing in the final video

How To Run

Install the required Python libraries, then run:

py main.py

The final video will be generated in the project folder.

Technologies Used

Python

MoviePy

pyttsx3 (Text-to-Speech)

PIL (Image processing)

icrawler (Image downloading)

Honest Reflection

I would like to honestly mention that I did not have strong prior experience with video generation, automation pipelines, or multimedia processing before starting this project.

This project was built through learning, experimenting, debugging errors, and improving step by step. I encountered multiple issues such as sync problems, module errors, and text rendering issues, and worked through them to make the system function correctly.

While I may not fully understand every internal detail of each library used, I understand:

The overall system architecture

The role of each file

How the pipeline flows from topic → script → image → voice → video

How to debug and modify the project

This project represents my effort to learn by building and improving something practical.

Future Improvements

Better AI image generation

More natural AI voice

Subtitle animation

Background music

Web interface

Thank you for reviewing this project.
