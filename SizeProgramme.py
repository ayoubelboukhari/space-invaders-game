from PIL import Image

image = Image.open("bk.png")

new_width = 64
width_percent = (new_width / float(image.size[0])) 
new_height = int((float(image.size[1]) * float(width_percent)))
resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)



resized_image.save("boukhari.png")