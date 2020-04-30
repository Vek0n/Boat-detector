import cv2
from keras_preprocessing.image import img_to_array


class ImgSegmentation(object):

    def __init__(self, image, x, y, height, width):
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        self.baseheight = [300, 280, 240, 200, 160, 140, 120, 100, 80, 70, 60, 50, 40]

    def crop_image(self):
        image_list = []
        image_pos = []
        for base in self.baseheight:
            try:
                if(((base*4) + self.x) < self.height) and (base+self.y < self.width):
                    cropped = self.image[self.y:(base+self.y), self.x:((base*4)+self.x)]

                    cropped = cv2.resize(cropped, (300, 300), cv2.INTER_NEAREST)

                    # if self.x == 100 and self.y == 0 and base == 70:
                    #     img = Image.fromarray(cropped)
                    #     img.show()
                    #     img.save("lol.png")
                    #     cv2.namedWindow(winname = "original", flags = cv2.WINDOW_NORMAL)
                    #     cv2.imshow("image", cropped)
                    #     cv2.imwrite(filename = "lol2.png", img = cropped)
                    #     cv2.waitKey(delay = 0)


                    cropped = img_to_array(cropped)



                    cropped = cropped.reshape(1, 300, 300, 3)




                    cropped = cropped.astype('float32')
                    image_list.append(cropped)
                    image_pos.append([(self.x, self.y), ((base*4) + self.x, base+self.y)])
            except:
                continue

        return image_list, image_pos
