from keras_preprocessing.image import img_to_array


class ImageSegmentation(object):

    def __init__(self, image, x, y, height, width):
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        # self.baseheight = [280, 240, 200, 160, 140, 120, 100, 80, 70, 60, 50, 40]
        self.baseheight = [40, 50, 60, 70, 80, 100, 120, 140, 160]
        self.i = 0


    def num_of_images(self):
        count = 0
        for base in self.baseheight:
            if (((base*4) + self.x) < self.height) and (base+self.y < self.width): count += 1
        return count

    def next_image(self):
        base = self.baseheight[self.i]
        cropped = self.image.crop((self.x, self.y, (base*4)+self.x, base+self.y))
        cropped = cropped.resize((300, 300))
        cropped = img_to_array(cropped)
        cropped = cropped.reshape(1, 300, 300, 3)
        cropped = cropped.astype('float32')
        image_pos = [(self.x, self.y), ((base*4) + self.x, base+self.y)]
        self.i += 1

        return cropped, image_pos





# def crop_image(self):
#     image_list = []
#     image_pos = []
#     for base in self.baseheight:
#         try:
#             if(((base*4) + self.x) < self.height) and (base+self.y < self.width):
#                 cropped = self.image.crop((self.x, self.y, (base*4)+self.x, base+self.y))
#                 cropped = cropped.resize((300, 300))
#                 cropped = img_to_array(cropped)
#                 cropped = cropped.reshape(1, 300, 300, 3)
#                 cropped = cropped.astype('float32')
#                 image_list.append(cropped)
#                 image_pos.append([(self.x, self.y), ((base*4) + self.x, base+self.y)])
#         except:
#             continue
#     return image_list, image_pos