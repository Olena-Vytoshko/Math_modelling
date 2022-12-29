from SLAM_math_modelling import env, sensors
import pygame
import pyautogui
import math

green = (0, 255, 0)
blue = (0, 0, 128)

environment = env.buildEnvironment((600, 1200))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(200, environment.originalMap, uncertainty=(0.5, 0.01))
environment.map.fill((0, 0, 0))
environment.infomap = environment.map.copy()

running = True

while running:
    sensorOn = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorOn = True
        elif not pygame.mouse.get_focused():
            sensorOn = False
    if sensorOn:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sense_obstacles()
        environment.dataStorage(sensor_data)
        environment.show_sensorData()
        print(position)
    environment.map.blit(environment.infomap, (0, 0))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("({}, {})".format(position[0], position[1]), True, environment.Green, environment.black)
    textRect = text.get_rect()
    textRect.center = (170, 550)
    environment.map.blit(text, textRect)
    pygame.display.update()
