# meme-and-poster
# 🎨 AI Meme & Poster Generator

A **fun, AI-powered web application** that generates creative meme captions and posters based on any topic and tone. Choose between **Funny, Sarcastic, or Motivational** captions and instantly generate stylish images for social media or personal use.  

Built with **FastAPI**, **Streamlit**, and **Hugging Face Transformers**.

---

## 🚀 Features

- Generate **captions** tailored to a topic and tone (Funny, Sarcastic, Motivational).  
- Generate **meme or poster images** with captions automatically placed and styled.  
- **Text wrapping and centering** for multi-line captions.  
- Supports **custom backgrounds** (optional template image).  
- Saves generated images locally in `outputs/`.  
- Stores projects and captions in a **SQLite database** for reference.

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| AI / NLP | Hugging Face Transformers (`tiiuae/falcon-rw-1b`) |
| Image Generation | Pillow (PIL) |
| Database | SQLite via SQLAlchemy |
| Language | Python 3.12 |

---

## Run the backend (FastAPI)
python -m uvicorn app.main:app --reload

---

## Run the frontend (Streamlit)
streamlit run frontend/streamlit_app.py

---

### ⚙️ How It Works

- **User Input:** Enter a topic, select a tone (Funny, Sarcastic, Motivational), and choose the mode (meme or poster).
- **Caption Generation:** The backend uses a transformer model (`tiiuae/falcon-rw-1b`) to generate a short, context-aware caption based on your input.
- **Image Creation:** 
  - A new image is created with a dark background by default.
  - The caption is drawn on the image using a font (defaults to `arial.ttf` if available).
  - Text wrapping ensures the caption fits nicely on the image.
- **Output:** The generated image is saved in the `outputs/` folder.
- **Display:** The Streamlit frontend displays the generated caption and the meme/poster image.


---

### 💡 Future Improvements

- Add more stylish fonts and animated meme templates.
- Improve caption creativity and humor with advanced instruction-tuned models.
- Support user-uploaded backgrounds and multiple image sizes.
- Implement multi-line captions with dynamic sizing.

---

## 🔗 Demo

<img width="1919" height="612" alt="Screenshot 2026-02-22 115257" src="https://github.com/user-attachments/assets/d142e9e6-af74-481a-922a-42891ea4cfaf" />

<img width="1919" height="906" alt="Screenshot 2026-02-22 115320" src="https://github.com/user-attachments/assets/ad54b033-37fa-4902-a8d1-41f7526e618b" />
