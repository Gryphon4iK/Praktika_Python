from PIL import Image
def process_image(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    width, height = image.size
    average_color = [0, 0, 0]
    num_pixels = width * height
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            average_color[0] += r
            average_color[1] += g
            average_color[2] += b
    average_color = tuple(c // num_pixels for c in average_color)
    average_image = Image.new("RGB", (width, height), average_color)
    average_image.save(output_image_path)
    average_image.show()
