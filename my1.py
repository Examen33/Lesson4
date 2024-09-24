from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")
red, green, blue = image.split()

coordinates = (51,0, 646, 522)
coordinates_left = (101, 0 , 696, 522 )
coordinates_right = (0, 0, 595, 522)

image_green = green.crop(coordinates)

imgr1 = red.crop(coordinates_left)
imgr2 = red.crop(coordinates)
image_red = Image.blend(imgr1, imgr2,  0.5)

imgb1 = blue.crop(coordinates_right)
imgb2 = blue.crop(coordinates)
image_blue = Image.blend(imgb1, imgb2,  0.5)

new_image = Image.merge("RGB",(image_red, image_green, image_blue))
new_image.save("Monro_blend_all.jpg")

new_image.thumbnail((80, 80))
new_image.save("little_Monro.jpg")