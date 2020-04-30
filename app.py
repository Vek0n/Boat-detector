from preparedata.image_segmentation import ImageSegmentation
from preparedata.config import Config
from PIL import Image
from keras.models import load_model
from matplotlib.patches import Rectangle
from itertools import product
import matplotlib.pyplot as plt

def index_of_best_image(list_of_results):
    last = 1
    i = -1
    for res in list_of_results:
        if last > res:
            return i
        last = res
        i = i+1
    return 100


def is_point_outside_rectangle(x, y, list_of_rectangles):
    outside = True
    for pos in list_of_rectangles:
        x1 = pos[0][0]
        x2 = pos[1][0]
        y1 = pos[0][1]
        y2 = pos[1][1]
        if x1 <= x <= x2 and y1 <= y <= y2:
            outside = False
    return outside

def run():

    config = Config(input_img="sc26.jpg", model="final_model3.h5", precisionX=50, precisionY=25, save_fig="out1.png")

    image_object = Image.open(config.get_input())
    model = load_model(config.get_model())
    precisionX = config.get_precisionX()
    precisionY = config.get_precisionY()
    save_path = config.get_savefig()

    width, height = image_object.size

    list_of_rectangles = []
    for x, y in product(range(width), range(height)):
        if y % precisionY == 0 and x % precisionX == 0 and is_point_outside_rectangle(x, y, list_of_rectangles):
            im_seg = ImageSegmentation(image_object, x, y, width, height)
            list_of_results = []
            for _ in range(im_seg.num_of_images()):
                img, img_pos = im_seg.next_image()
                result = model.predict_classes(img)
                list_of_results.append(result[0][0])
                i = index_of_best_image(list_of_results)
                if i != 100:
                    plt.imshow(image_object)
                    plt.gca().add_patch(Rectangle((x, y), img_pos[1][0]-x, img_pos[1][1]-y,
                                                  linewidth=1, edgecolor='g', facecolor='none'))
                    list_of_rectangles.append([img_pos[0], img_pos[1]])
                    break
    plt.savefig(save_path)





    # for x, y in product(range(width), range(height)):
    #     if y % precisionY == 0 and x % precisionX == 0 and is_point_outside_rectangle(x, y, list_of_rectangles):
    #         im_seg = ImageSegmentation(image_object, x, y, width, height)
    #         img_crop, img_pos = im_seg.crop_image()
    #         list_of_results = []
    #         for img in img_crop:
    #             result = model.predict_classes(img)
    #             list_of_results.append(result[0][0])
    #             i = index_of_best_image(list_of_results)
    #             if i != 100:
    #                 plt.imshow(image_object)
    #                 plt.gca().add_patch(Rectangle((x, y), img_pos[i][1][0]-x, img_pos[i][1][1]-y,
    #                                               linewidth=1, edgecolor='g', facecolor='none'))
    #                 list_of_rectangles.append(img_pos[i])
    #                 break
    # plt.savefig(save_path)