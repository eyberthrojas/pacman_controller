#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
class Mapa():
    
    def __init__(self, response):
        self.axis = {'xMin' : response.minX, 'xMax' : response.maxX, 'yMin' : response.minY, 'yMax' : response.maxY }
        self.nObs = response.nObs
        self.obs = []
        for i in range(self.nObs):
            x = response.obs[i].x
            y = response.obs[i].y
            self.obs.append(Point(x,y))
            
