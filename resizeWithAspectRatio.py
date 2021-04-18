image = Image.open('sample.jpg')
image.thumbnail((400, 400))
image.save('img_thumbnail.jpg')

print(image.size) # Output: (400, 267)
