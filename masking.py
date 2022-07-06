import cv2
import numpy as np


class Mask_Operator:
    def __init__(self, input_path, output_path, file_name, local_avg_radius=5):
        self.img = cv2.imread(input_path + "/" + file_name)
        self.img_mask = np.zeros_like(self.img)
        self.ix = -1
        self.iy = -1
        self.drawing = False
        self.local_avg_radius = local_avg_radius
        self.local_avg_color = self.img.mean(axis=(0, 1))
        cv2.namedWindow("Ceate_Mask", 0)
        cv2.resizeWindow("Ceate_Mask", 1500, 1500)
        cv2.setMouseCallback("Ceate_Mask",
                             self.draw_rectangle_with_drag)

        while True:
            cv2.imshow("Ceate_Mask", self.img)

            if cv2.waitKey(10) == 27:
                cv2.imwrite(input_path + "/" +
                            file_name[:-4] + "_edit" + file_name[-4:], self.img)
                cv2.imwrite(output_path + "/" + file_name[:-4] + "_edit_mask" +
                            file_name[-4:], self.img_mask)
                break
        cv2.destroyAllWindows()

    def draw_rectangle_with_drag(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix = x
            self.iy = y
            self.local_avg_color = self.img[
                self.iy - self.local_avg_radius: self.iy + self.local_avg_radius,
                self.ix - self.local_avg_radius: self.ix + self.local_avg_radius
            ].mean(axis=(0, 1))

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                cv2.rectangle(self.img, pt1=(self.ix, self.iy),
                              pt2=(x, y),
                              color=self.local_avg_color,
                              thickness=-1)
                cv2.rectangle(self.img_mask, pt1=(self.ix, self.iy),
                              pt2=(x, y),
                              color=(255, 255, 255),
                              thickness=-1)

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            cv2.rectangle(self.img, pt1=(self.ix, self.iy),
                          pt2=(x, y),
                          color=self.local_avg_color,
                          thickness=-1)
            cv2.rectangle(self.img_mask, pt1=(self.ix, self.iy),
                          pt2=(x, y),
                          color=(255, 255, 255),
                          thickness=-1)
