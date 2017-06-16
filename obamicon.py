'''
Summary:
Get the intensity of each pixel by adding the red, green and blue values.
If the pixel has low intensity (<182) color it  dark blue.
If the pixel is medium/low intensity (between 182 and 364) color it red.
If the pixel is medium/high intensity (between 364 and 546) color it light blue.
If the pixel is high intensity (>546) color it yellow.
'''

From PIL import Image

# For recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Load the image and turn the image into a list of tuples.
my_image = Image.open("imageSRCGoesHere.jpg")
image_list = my_image.getdata()
image_list = list(image_list)


# Check the intensity of each pixel, determine how to recolor it, and save it in a new list.
recolored = []
for pixel in image_list:

    #intesity is total of tuple
    intensity = pixel[0] + pixel[1] + pixel[2]
    
    if intensity <182:
        recolored.append(darkBlue)
    elif intensity >= 182 and <= 364:
        recolored.append(red)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("imageNameGoesHere.jpg", "jpeg")
