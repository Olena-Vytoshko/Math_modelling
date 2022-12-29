import math
import pygame


class buildEnvironment:
    def __init__(self, MapDimensions):
        pygame.init()
        # declare list to store our point cloud map
        # it is just a group of 2D points in a 2D space
        self.pointCloud = []
        self.externalMap = pygame.image.load('map2.png')
        # split the dimensions of our map to width and height
        self.maph, self.mapw = MapDimensions
        self.MapWindowName = 'Lidar'
        pygame.display.set_caption(self.MapWindowName)
        # empty main map:
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        # The external map on top of main map
        self.map.blit(self.externalMap, (0, 0))
        # Declare colors RGB
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)

    def AD2pos(self, distance, angle, robotPosition):
        # method that converts the sensor raw angle distance data to cartesian coordinates
        x = distance * math.cos(angle) + robotPosition[0]
        y = -distance * math.sin(angle) + robotPosition[1]
        return (int(x), int(y))

    def dataStorage(self, data):
        print(len(self.pointCloud))
        if data != False:
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                if point not in self.pointCloud: # to not store duplicates
                    self.pointCloud.append(point)

    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (0, 255, 0))
