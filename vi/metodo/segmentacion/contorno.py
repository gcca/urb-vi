# -*- coding: utf-8 -*-

'''
Método segmentacion de la imagen
'''

import cv2

class Segmentacion(object):
    '''
    Segmentación
    '''
    def ejecutar(self, img, min_area):
        frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, frame_bi = cv2.threshold(frame_gray, 100, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(frame_bi, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE,)
        toplevel_indices, secondlevel_contours = [], []

        if hierarchy != None:
            h = hierarchy[0]
            for i in range(len(h)):
                if h[i][3] == -1:
                    toplevel_indices.append(i)
            for i in range(len(h)):
                if h[i][3] in toplevel_indices:
                    if min_area != None:
                        if cv2.contourArea(contours[i]) >= min_area:
                            secondlevel_contours.append(contours[i])
                    else:
                        secondlevel_contours.append(contours[i])
            # sort contours by largest first (if there are more than one)
            blobs = sorted(secondlevel_contours, key=lambda contour:cv2.contourArea(contour), reverse=True)
            for blob in blobs:
                for corner in blob:
                    center = int(corner[0][0]), int(corner[0][1])
                    cv2.circle(img, (center), 1, (0, 255, 255), -1)
        return img
        # cv2.imshow('lk_track', frame )
        # cv2.waitKey(0)
