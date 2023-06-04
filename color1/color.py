import PIL
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageEnhance


# read image and convert to RGB
image=Image.open("photo1.png")
image=image.convert('RGB')
font = ImageFont.truetype("uni-sans.heavy-caps.otf", 70)

arr = image.split()
images = []
for chan in range(3):
    for i in (0.1,0.5,0.9):
        np = arr[chan].point(lambda x: x*i)
        narr = []
        for z in range(0,3):
            if z == chan: 
                narr.append(np)
                continue
            narr.append(arr[z])
        narr = tuple(narr)
        result = Image.merge('RGB',narr)
        ImageDraw.Draw(result).text((200, 50), "channel {} intensity {}".format(chan,i), font=font,fill=(255,255,9,255), align="center")
        images.append(result)
    
# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
Image._show(contact_sheet)