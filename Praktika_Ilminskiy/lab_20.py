#Задание 1
from PIL import Image, ImageDraw
width, height = 525, 200
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)
# буква "В"
draw.rectangle([50, 50, 100, 150], fill='blue')
draw.ellipse([50, 50, 75, 150], fill='blue')
draw.ellipse([75, 50, 100, 150], fill='blue')
# буква "л"
draw.rectangle([120, 50, 170, 150], fill='green')
draw.polygon([(170, 100), (220, 150), (220, 100)], fill='green')
# буква "a"
draw.ellipse([240, 100, 270, 150], fill='red')
draw.polygon([(270, 50), (320, 50), (345, 150), (270, 150)], fill='red')
# буква "д"
draw.rectangle([370, 50, 420, 150], fill='orange')
draw.ellipse([420, 50, 470, 100], fill='orange')
draw.ellipse([420, 100, 470, 150], fill='orange')
draw.polygon([(470, 50), (445, 100), (470, 150)], fill='orange')
image.save('name.png')
image.show()

#Задание 2
from PIL import Image, ImageDraw
width, height = 400, 300
image = Image.new('RGB', (width, height), 'blue')
draw = ImageDraw.Draw(image)
# корпус компьютера
draw.rectangle([100, 50, 300, 200], fill='gray')
# монитор
draw.rectangle([120, 70, 280, 150], fill='black')
# клавиатура
draw.rectangle([120, 200, 280, 220], fill='black')
draw.rectangle([145, 160, 255, 200], fill='white')
# мышь
draw.rectangle([90, 180, 110, 200], fill='black')
draw.ellipse([80, 170, 100, 190], fill='white')
image.save('computer.png')
image.show()