image = Image.open('sample.jpg')
new_image = image.resize((400, 400))
new_image.save('img_resize.jpg')

print(image.size)
print(new_image.size) # Output: (400, 400)
