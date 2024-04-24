from PIL import Image
def process_image(input_image_paths, output_image_paths, new_width, new_height):
    image = Image.open(input_image_paths)
    grayscale_image = image.convert('L')
    mirrored_image = Image.new('L', (image.width, image.height))
    pixels = mirrored_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixels[x, y] = grayscale_image.getpixel((image.width - x - 1, y))
    resized_image = mirrored_image.resize((new_width, new_height))
    resized_image.save(output_image_paths)
    resized_image.show()