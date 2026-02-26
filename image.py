from icrawler.builtin import BingImageCrawler
from PIL import Image, ImageDraw, ImageFont
import os
import shutil


def generate_image(prompt, index):
    os.makedirs("images", exist_ok=True)

    # Download image
    crawler = BingImageCrawler(storage={"root_dir": "temp_images"})
    crawler.crawl(keyword=prompt, max_num=1)

    temp_folder = "temp_images"
    files = os.listdir(temp_folder)

    if not files:
        print("❌ No image found for:", prompt)
        return None

    src_path = os.path.join(temp_folder, files[0])

    # Open downloaded image
    img = Image.open(src_path).convert("RGB")
    img = img.resize((1280, 720))

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except:
        font = ImageFont.load_default()

    # Draw semi-transparent rectangle at bottom
    overlay_height = 120
    draw.rectangle(
        [(0, 720 - overlay_height), (1280, 720)],
        fill=(0, 0, 0)
    )

    # Add text
    draw.text(
        (50, 720 - 80),
        prompt,
        fill="white",
        font=font
    )

    final_path = f"images/img{index}.jpg"
    img.save(final_path)

    shutil.rmtree(temp_folder)

    return final_path