# -*- coding: utf-8 -*-
import pyglet
import cv2

def showGif(name, t):
    animation = animation = pyglet.resource.animation(name)
    sprite = pyglet.sprite.Sprite(animation)

    win = pyglet.window.Window(width=sprite.width, height=sprite.height)

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()

    def close(event):
        win.close()

    pyglet.clock.schedule_once(close, t)

    pyglet.app.run()

def showImage(name):
    image = cv2.imread(name)
    cv2.imshow("Humanas ou Exatas?", image)
    cv2.waitKey(0)
    
