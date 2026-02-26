# 🎥 AI Explainer Video Generator

## 📌 Project Overview

This project automatically generates a simple AI-based explainer video using Python.

It follows a complete pipeline:

1. Select a topic  
2. Generate a script  
3. Split the script into sentences  
4. Generate an image for each sentence  
5. Convert each sentence into voice  
6. Synchronize images and voice into a final video  

The final output file is:

```
final_video.mp4
```

---

## ⚙️ System Architecture

- **main.py** → Controls the entire pipeline  
- **idea_generation.py** → Selects a topic  
- **script.py** → Generates the script  
- **image.py** → Downloads and prepares images  
- **voice.py** → Converts text to speech  
- **video.py** → Combines images and audio into a synced video  

Each sentence receives:
- 🎤 Its own generated voice file  
- 🖼 Its own related image  
- ⏱ Proper synchronization in the final video  

---

## ▶️ How To Run

### 1️⃣ Install Required Libraries

```bash
pip install moviepy pyttsx3 pillow icrawler
```

### 2️⃣ Run the Project

```bash
py main.py
```

After execution, the final video will be generated in the project folder as:

```
final_video.mp4
```

---

## 🛠 Technologies Used

- Python  
- MoviePy  
- pyttsx3 (Text-to-Speech)  
- Pillow (Image Processing)  
- icrawler (Image Downloading)  

---

## 💡 Honest Reflection

I would like to honestly mention that I did not have strong prior experience with multimedia processing, automation pipelines, or video generation before starting this project.

This project was developed through learning, experimentation, debugging, and gradual improvement. During development, I faced multiple challenges such as:

- Audio and image synchronization issues  
- Dependency and module errors  
- Text rendering problems  
- Pipeline structure improvements  

I worked through these issues step by step to make the system functional and properly synchronized.

While I may not fully understand every internal implementation detail of the libraries used, I understand:

- The overall architecture of the system  
- The role of each module  
- The flow from topic → script → image → voice → video  
- How to debug and improve the pipeline  

This project represents my effort to learn by building something practical and functional.

---

## 🚀 Future Improvements

- AI-based image generation instead of web crawling  
- More natural cloud-based text-to-speech  
- Subtitle animations  
- Background music integration  
- Web interface for user interaction  

---

Thank you for reviewing this project.
