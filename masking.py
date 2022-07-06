import cv2
import numpy as np

# variables
ix = -1
iy = -1
drawing = False
img = False
img_mask = False


def draw_rectangle_with_drag(event, x, y, flags, param):

    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, pt1=(ix, iy),
                          pt2=(x, y),
                          color=img.mean(axis=(0, 1)),
                          thickness=-1)
            cv2.rectangle(img_mask, pt1=(ix, iy),
                          pt2=(x, y),
                          color=(255, 255, 255),
                          thickness=-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, pt1=(ix, iy),
                      pt2=(x, y),
                      color=img.mean(axis=(0, 1)),
                      thickness=-1)
        cv2.rectangle(img_mask, pt1=(ix, iy),
                      pt2=(x, y),
                      color=(255, 255, 255),
                      thickness=-1)


def mask_image(input_path, output_path, file_name):

    global ix, iy, drawing, img, img_mask

    img = cv2.imread(input_path + "/" + file_name)
    img_mask = np.zeros_like(img)

    cv2.namedWindow("Ceate_Mask", 0)
    cv2.resizeWindow("Ceate_Mask", 1500, 1500)
    cv2.setMouseCallback("Ceate_Mask",
                         draw_rectangle_with_drag)

    while True:
        cv2.imshow("Ceate_Mask", img)

        if cv2.waitKey(10) == 27:
            cv2.imwrite(input_path + "/" +
                        file_name[:-4] + "_edit" + file_name[-4:], img)
            cv2.imwrite(output_path + "/" + file_name[:-4] + "_edit_mask" +
                        file_name[-4:], img_mask)
            break
    cv2.destroyAllWindows()
