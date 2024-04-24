from PIL import Image
def process_image(input_image_pathss, output_image_pathss):
    image = Image.open(input_image_pathss)
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            min_value = min(r, g, b)
            max_value = max(r, g, b)
            new_color = (min_value, 0, max_value)
            image.putpixel((x, y), new_color)
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_image.save(output_image_pathss)
    flipped_image.show()