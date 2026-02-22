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

## 📁 Folder Structure
