from fastapi import APIRouter
from app.ai_engine import generate_caption
from app.layout_engine import create_image

router = APIRouter()

@router.post("/generate")
def generate(data: dict):
    topic = data["topic"]
    tone = data["tone"]
    mode = data["mode"]

    caption = generate_caption(topic, tone)
    image_path = create_image(caption, mode)

    return {
        "caption": caption,
        "image_path": image_path
    }
