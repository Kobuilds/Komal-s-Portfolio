import sys
from PIL import Image

def image_to_ascii(image_path, output_width=100):
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Maintain aspect ratio
    aspect_ratio = img.height / img.width
    output_height = int(output_width * aspect_ratio * 0.5)  # ASCII characters are usually taller
    img = img.resize((output_width, output_height))
    img = img.convert('L') # Grayscale

    chars = "@%#*+=-:. "
    ascii_str = ""
    for y in range(img.height):
        for x in range(img.width):
            pixel_val = img.getpixel((x, y))
            char_idx = int((pixel_val / 255) * (len(chars) - 1))
            ascii_str += chars[char_idx]
        ascii_str += "\n"
    
    return ascii_str

if __name__ == "__main__":
    image_path = "d:/PROJECTS/Portfolio/Komalsohal.png"
    output_path = "d:/PROJECTS/Portfolio/hero_ascii.txt"
    ascii_art = image_to_ascii(image_path, output_width=120)
    if ascii_art:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(ascii_art)
        print(f"ASCII art saved to {output_path}")
