from PIL import Image

f = open("data.h", "w")

def calculate(r, g, b):
   return ((66 * r + 129 * g + 25 * b + 128) >> 8) + 16;

imagename = input("Nom de l'image : ")
img = Image.open(imagename)
width, height = img.size
new = Image.new(mode = "RGB", size = (width, height))
pixels = img.load()

f.write("uint8_t image[")
f.write(str(width) + " * " + str(height))
f.write("] = {")

print("Computing image", imagename)
print("Computed image will appear when it's done")
for y in range(height):
   for x in range(width):
      r, g, b = img.getpixel((x, y))
      result = calculate(r, g, b)
      f.write(str(result))
      if (not (y == height - 1 and x == width - 1)):
         f.write(", ")
      pixels[x, y] = (result, result, result)
print("Computing done")

f.write("};")
f.close()
img.show()
img.save("BW" + imagename)
