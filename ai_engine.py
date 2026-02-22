from transformers import pipeline

# Better instruction-following model
generator = pipeline(
    "text-generation",
    model="tiiuae/falcon-rw-1b",
)

def generate_caption(topic, tone):
    prompt = f"""
You are a meme creator.

Write ONE short {tone} meme caption about {topic}.
Max 12 words.
One sentence only.
No repetition.
Caption:
"""

    result = generator(
        prompt,
        max_new_tokens=25,
        temperature=0.6,
        top_k=40,
        top_p=0.9,
        do_sample=True
    )

    text = result[0]["generated_text"]

    # Remove prompt from output
    caption = text.split("Caption:")[-1].strip()

    # Clean extra lines
    caption = caption.split("\n")[0]

    return caption
