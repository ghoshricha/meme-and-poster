from PIL import Image, ImageDraw, ImageFont
import uuid
import os

def create_image(text, mode):
    image = Image.new("RGB", (800, 600), color=(30, 30, 30))
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    width, height = image.size

    # Text wrapping using textbbox (Pillow 10+ compatible)
    lines = []
    words = text.split()
    line = ""

    for word in words:
        test_line = line + word + " "
        bbox = draw.textbbox((0, 0), test_line, font=font)
        text_width = bbox[2] - bbox[0]

        if text_width < width - 100:
            line = test_line
        else:
            lines.append(line)
            line = word + " "

    lines.append(line)

    total_text_height = len(lines) * 50
    y = (height - total_text_height) // 2

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]

        x = (width - text_width) // 2
        draw.text((x, y), line, fill="white", font=font)
        y += 50

    os.makedirs("outputs", exist_ok=True)

    filename = f"outputs/{uuid.uuid4()}.png"
    image.save(filename)

    return filename
