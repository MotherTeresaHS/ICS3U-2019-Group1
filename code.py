#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: January 2019
# This file is the "Space Aliens" game
#   for CircuitPython

import ugame
import stage
import board
import neopixel
import time
import random
import constants

def blank_white_reset_scene():
    # this function is the splash scene game loop
    # do house keeping to ensure everythng is setup
    # set up the NeoPixels
    # pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    # pixels.deinit() # and turn them all off
    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # Wait for 1/2 seconds
        time.sleep(0.5)
        splash_scene()
        # redraw sprite list

def splash_scene():
    # this function is the MT splash scene
    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white
    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white
    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white
    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # Wait for 1/2 seconds
        time.sleep(1.0)
        pp_splash_scene()
        # redraw sprite list

def pp_splash_scene():
    # this function is the MT splash scene
    # an image bank for CircuitPython
    # mt_game_studio
    image_bank_4 = stage.Bank.from_bmp16("menu3.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_4, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    sprite = []

    sprite_one = stage.Sprite(image_bank_4, 1, 48, 32)
    sprite.append(sprite_one)
    sprite_two = stage.Sprite(image_bank_4, 2, 48, 48)
    sprite.append(sprite_two)
    sprite_three = stage.Sprite(image_bank_4, 3, 48, 64)
    sprite.append(sprite_three)
    sprite_four = stage.Sprite(image_bank_4, 4, 48, 80)
    sprite.append(sprite_four)
    sprite_five = stage.Sprite(image_bank_4, 5, 64, 32)
    sprite.append(sprite_five)
    sprite_six = stage.Sprite(image_bank_4, 6, 64, 48)
    sprite.append(sprite_six)
    sprite_seven = stage.Sprite(image_bank_4, 7, 64, 64)
    sprite.append(sprite_seven)
    sprite_eight = stage.Sprite(image_bank_4, 8, 64, 80 )
    sprite.append(sprite_eight)
    sprite_nine = stage.Sprite(image_bank_4, 9, 80, 32)
    sprite.append(sprite_nine)
    sprite_ten = stage.Sprite(image_bank_4, 10, 80, 48)
    sprite.append(sprite_ten)
    sprite_eleven = stage.Sprite(image_bank_4, 11, 80, 64)
    sprite.append(sprite_eleven)









    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + sprite + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # Wait for 1/2 seconds
        time.sleep(1.0)
        menu_scene()
        # redraw sprite list


        # redraw sprite list

def menu_scene():
    # this function is the menu scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("menu.bmp")
    image_bank_3 = stage.Bank.from_bmp16("Menu2.bmp")
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.pn

    sprite = []

    sprite_one = stage.Sprite(image_bank_2, 1, 144, 32)
    sprite.append(sprite_one)
    sprite_two = stage.Sprite(image_bank_2, 2, 128, 32)
    sprite.append(sprite_two)
    sprite_three = stage.Sprite(image_bank_2, 3, 112, 32)
    sprite.append(sprite_three)
    sprite_four = stage.Sprite(image_bank_2, 5, 96, 32)
    sprite.append(sprite_four)
    sprite_five = stage.Sprite(image_bank_2, 7, 80, 32)
    sprite.append(sprite_five)
    sprite_six = stage.Sprite(image_bank_2, 9, 64, 32)
    sprite.append(sprite_six)
    sprite_seven = stage.Sprite(image_bank_2, 4, 112, 48)
    sprite.append(sprite_seven)
    sprite_eight = stage.Sprite(image_bank_2, 6, 96, 48)
    sprite.append(sprite_eight)
    sprite_nine = stage.Sprite(image_bank_2, 8, 80, 48)
    sprite.append(sprite_nine)
    sprite_ten = stage.Sprite(image_bank_2, 10, 64, 48)
    sprite.append(sprite_ten)
    sprite_eleven = stage.Sprite(image_bank_2, 11, 48, 32)
    sprite.append(sprite_eleven)
    sprite_twelve = stage.Sprite(image_bank_2, 12, 48, 48)
    sprite.append(sprite_twelve)
    sprite_thirteen = stage.Sprite(image_bank_2, 13, 32, 48)
    sprite.append(sprite_thirteen)
    sprite_fourteen = stage.Sprite(image_bank_2, 14, 16, 48)
    sprite.append(sprite_fourteen)

    sprite_one = stage.Sprite(image_bank_3, 1, 144, 80)
    sprite.append(sprite_one)
    sprite_two = stage.Sprite(image_bank_3, 2, 128, 80)
    sprite.append(sprite_two)
    sprite_three = stage.Sprite(image_bank_3, 3, 112, 80)
    sprite.append(sprite_three)
    sprite_four = stage.Sprite(image_bank_3, 4, 96, 80)
    sprite.append(sprite_four)
    sprite_five = stage.Sprite(image_bank_3, 5, 80, 80)
    sprite.append(sprite_five)
    sprite_six = stage.Sprite(image_bank_3, 6, 64, 80)
    sprite.append(sprite_six)
    sprite_seven = stage.Sprite(image_bank_3, 7, 48, 80)
    sprite.append(sprite_seven)
    sprite_eight = stage.Sprite(image_bank_3, 8, 112, 64)
    sprite.append(sprite_eight)
    sprite_nine = stage.Sprite(image_bank_3, 9, 96, 64)
    sprite.append(sprite_nine)
    sprite_ten = stage.Sprite(image_bank_3, 10, 80, 64)
    sprite.append(sprite_ten)
    sprite_eleven = stage.Sprite(image_bank_3, 11, 64, 64)
    sprite.append(sprite_eleven)
    sprite_twelve = stage.Sprite(image_bank_3, 12, 48, 64)
    sprite.append(sprite_twelve)
    sprite_thirteen = stage.Sprite(image_bank_3, 13, 32, 64)
    sprite.append(sprite_thirteen)
    sprite_fourteen = stage.Sprite(image_bank_3, 14, 16, 64)
    sprite.append(sprite_fourteen)


    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Shooter Shootout")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(35, 110)
    text2.text("PRESS START")
    text.append(text2)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text+ sprite + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_START != 0:  # Start button
            game_scene()
            #break

        # redraw sprite list

def game_scene():
    # this function is the game scene
    ALIEN_SPEED = 1
    image_bank_2 = stage.Bank.from_bmp16("sprites.bmp")
    # game score
    score = 0

    # tank direction
    tank_direction = None


     # These functions set and reset the start coordinates of frogs
    def reset_left_frog():
        # Sets and resets the start coordinates of frogs starting on the left
        for left_frog_number in range(len(left_frogs)):
            if left_frogs[left_frog_number].x < 0:
                left_frogs[left_frog_number].move(random.randint
                                                          (-100, 0 -
                                                           constants.SPRITE_SIZE),
                                                          random.randint
                                                          (0, constants.SCREEN_Y))
                break

    def reset_top_frog():
        # Sets and resets the start coordinates of frogs starting on the top
        for top_frog_number in range(len(top_frogs)):
            if top_frogs[top_frog_number].y < 0:
                top_frogs[top_frog_number].move(random.randint
                                                        (0, constants.SCREEN_X),
                                                        random.randint
                                                        (-100, 0 -
                                                         constants.SPRITE_SIZE))
                break

    def reset_right_frog():
        # Sets and resets the start coordinates of frogs starting on the right
        for right_frog_number in range(len(right_frogs)):
            if right_frogs[right_frog_number].x < 0:
                right_frogs[right_frog_number].move(random.randint
                                                            (constants.SCREEN_X, 228),
                                                            random.randint
                                                            (0, constants.SCREEN_Y))
                break

    def reset_bottom_frog():
        # Sets and resets the start coordinates of frogs starting on the bottom
        for down_frog_number in range(len(bottom_frogs)):
            if bottom_frogs[down_frog_number].y < 0:
                bottom_frogs[down_frog_number].move(random.randint
                                                        (0, constants.SCREEN_X),
                                                        random.randint
                                                        (160 + constants.SPRITE_SIZE,
                                                         260))
                break
    # Creating frogs
    # Frogs staring from the left
    left_frogs = []
    for left_frog_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        single_left_frog = stage.Sprite(image_bank_2, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        left_frogs.append(single_left_frog)
    reset_left_frog()

    # Frogs staring from the top
    top_frogs = []
    for top_frog_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        single_up_frog = stage.Sprite(image_bank_2, 3,
                                          constants.OFF_SCREEN_X,
                                          constants.OFF_SCREEN_Y)
        top_frogs.append(single_up_frog)
    reset_top_frog()

    # Frogs starting from the right
    right_frogs = []
    for right_frog_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        single_right_frog = stage.Sprite(image_bank_2, 3,
                                             constants.OFF_SCREEN_X,
                                             constants.OFF_SCREEN_Y)
        right_frogs.append(single_right_frog)
    reset_right_frog()

    # Frogs staring from the bottom
    bottom_frogs = []
    for down_frog_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        single_down_frog = stage.Sprite(image_bank_2, 3,
                                            constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
        bottom_frogs.append(single_down_frog)
    reset_bottom_frog()

    start_time = time.time()

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew2.wav", 'rb')  # to change the wav volume: https://audioalter.com/volume/
    boom_sound = open("boom.wav", 'rb')
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    # a list of sprites that will be updated every frame
    sprites = []

    # create lasers for when we shoot
    lasers = []
    lasers_direction = []
    for laser_number in range(constants.TOTAL_ATTACKS):
        a_single_laser = stage.Sprite(image_bank_2, 2, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
        lasers_direction.append("None")
        lasers.append(a_single_laser)

    # set up the NeoPixels to match the # of lasers fired
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    for pixel_number in range(0, 5):
        pixels[pixel_number] = (0, 10, 0)
    pixels.show()

    # create frogs
    frogs = []
    for frog_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_frog = stage.Sprite(image_bank_2, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
        frogs.append(a_single_frog)

    # current number of frogs that should be moving down screen, start with just 1
    frog_counter = 1

    # add text at top of screen for score
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    tank = stage.Sprite(image_bank_2, 4, 75, 60)
    sprites.append(tank) # insert at the top of sprite list

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(0, 0)
            background.tile(x_location, y_location, tile_picked)


    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = left_frogs + right_frogs + top_frogs \
                  + bottom_frogs + sprites + lasers + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_X != 0:  # A button
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # update game logic

        # if right D-Pad is pressed

        if keys & ugame.K_RIGHT != 0:
            # if tank moves off right screen, move it back
            if tank.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                tank.x = constants.SCREEN_X - constants.SPRITE_SIZE
            # else move tank right
            else:
                tank.move(tank.x + constants.BALL_SPEED, tank.y)
                tank.set_frame(frame=None,rotation=1)
                tank_direction = "right"

        # if left D-Pad is pressed
        if keys & ugame.K_LEFT != 0:
            # if tank moves off left screen, move it back
            if tank.x < 0:
                tank.x = 0
            # else move tank left
            else:
                tank.move(tank.x - constants.BALL_SPEED, tank.y)
                tank.set_frame(frame=None,rotation=3)
                tank_direction = "left"

        if keys & ugame.K_UP != 0:
            # if tank moves off up screen, move it back
            if tank.y > constants.SCREEN_Y - constants.SPRITE_SIZE:
                tank.y = constants.SCREEN_Y - constants.SPRITE_SIZE
            # else move tank up
            else:
                tank.move(tank.x, tank.y - 1)
                tank.set_frame(frame=None,rotation=0)
                tank_direction = "up"

        # if left D-Pad is pressed
        if keys & ugame.K_DOWN != 0:
            # if tank moves off down screen, move it back
            if tank.y < 0:
                tank.y = 0
            # else move tank down
            else:
                tank.move(tank.x, tank.y + 1)
                tank.set_frame(frame=None,rotation=2)
                tank_direction = "down"


        # if A Button (fire) is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # fire a laser, if we have enough power (meaning we have not used up all the lasers)
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(tank.x, tank.y)
                    lasers_direction[laser_number] = tank_direction
                    sound.stop()
                    sound.play(pew_sound)
                    break

        # each frame move the lasers, that have been fired, up

        # first make all the neopixels yellow, then make them green if it is moving up
        lasers_moving_counter = -1
        for pixel_number in range(0, 5):
            pixels[pixel_number] = (0, 10, 0)

        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0 :
                laser_move_direction = None
                if lasers_direction[laser_number] == "down":
                    lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y + constants.ATTACK_SPEED)
                elif lasers_direction[laser_number] == "up":
                    lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.ATTACK_SPEED)
                elif lasers_direction[laser_number] == "left":
                    lasers[laser_number].move(lasers[laser_number].x - constants.ATTACK_SPEED, lasers[laser_number].y)
                elif lasers_direction[laser_number] == "right":
                    lasers[laser_number].move(lasers[laser_number].x + constants.ATTACK_SPEED, lasers[laser_number].y)


                lasers_moving_counter = lasers_moving_counter + 1
                pixels[lasers_moving_counter] = (10, 10 - (2 * lasers_moving_counter + 2), 0)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                if lasers[laser_number].y > 128:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                if lasers[laser_number].x > 160:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                if lasers[laser_number].y < 1:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        if lasers_moving_counter == 4:
            for pixel_number in range(0, 5):
                pixels[pixel_number] = (10, 0, 0)
        pixels.show()


        # each frame move the frogs down the screen
        for left_frog_number in range(len(left_frogs)):
            if left_frogs[left_frog_number].x < constants.OFF_RIGHT_SCREEN:
                left_frogs[left_frog_number].move(
                left_frogs[left_frog_number].x + ALIEN_SPEED,
                left_frogs[left_frog_number].y)
                if left_frogs[left_frog_number].x > constants.SCREEN_X:
                    left_frogs[left_frog_number].move(constants.OFF_SCREEN_X,
                                                              constants.OFF_SCREEN_Y)
                    reset_left_frog()

        # Scroll asteroids from top of screen
        for top_frog_number in range(len(top_frogs)):
            if top_frogs[top_frog_number].y < constants.OFF_BOTTOM_SCREEN:
                top_frogs[top_frog_number].move(
                top_frogs[top_frog_number].x,
                top_frogs[top_frog_number].y + ALIEN_SPEED)
                if top_frogs[top_frog_number].y > constants.SCREEN_Y:
                    top_frogs[top_frog_number].move(constants.OFF_SCREEN_X,
                                                            constants.OFF_SCREEN_Y)
                    reset_top_frog()

        # Scroll asteroids from right of screen left
        for right_frog_number in range(len(right_frogs)):
            if right_frogs[right_frog_number].x > constants.OFF_LEFT_SCREEN:
                right_frogs[right_frog_number].move(
                right_frogs[right_frog_number].x - ALIEN_SPEED,
                right_frogs[right_frog_number].y)
                if right_frogs[right_frog_number].x < 0 - constants.SPRITE_SIZE:
                    right_frogs[right_frog_number].move(constants.OFF_SCREEN_X,
                                                                constants.OFF_SCREEN_Y)
                    reset_right_frog()

        # Scroll asteroids from bottom of screen
        for down_frog_number in range(len(bottom_frogs)):
            if bottom_frogs[down_frog_number].y > constants.OFF_TOP_SCREEN:
                bottom_frogs[down_frog_number].move(
                bottom_frogs[down_frog_number].x,
                bottom_frogs[down_frog_number].y - ALIEN_SPEED)
                if bottom_frogs[down_frog_number].y < 0 - constants.SPRITE_SIZE:
                    bottom_frogs[down_frog_number].move(constants.OFF_SCREEN_X,
                                                                constants.OFF_SCREEN_Y)
                    reset_bottom_frog()

        # each frame check if any of the lasers are touching any of the frogs
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for frog_number in range(len(left_frogs)):
                    if left_frogs[frog_number].x > 0:
                        if stage.collide(left_frogs[frog_number].x + 1,
                                         left_frogs[frog_number].y + 1,
                                         left_frogs[frog_number].x + 15,
                                         left_frogs[frog_number].y + 15,
                                         lasers[laser_number].x + 3,
                                         lasers[laser_number].y + 3,
                                         lasers[laser_number].x + 13,
                                         lasers[laser_number].y + 13):
                            left_frogs[frog_number].move(constants.OFF_SCREEN_X,
                                                                 constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            # sound.play(impact_sound)
                            score = score + 1
                            reset_left_frog()
                            frog_counter = frog_counter + 1

        # This detects if any lasers hit asteroids heading down
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for frog_number in range(len(top_frogs)):
                    if top_frogs[frog_number].x > 0:
                        if stage.collide(top_frogs[frog_number].x + 1,
                                         top_frogs[frog_number].y + 1,
                                         top_frogs[frog_number].x + 15,
                                         top_frogs[frog_number].y + 15,
                                         lasers[laser_number].x + 3,
                                         lasers[laser_number].y + 3,
                                         lasers[laser_number].x + 13,
                                         lasers[laser_number].y + 13):
                            top_frogs[frog_number].move(constants.OFF_SCREEN_X,
                                                                constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            # sound.play(impact_sound)
                            score = score + 1
                            if score % 10 == 0:
                                ALIEN_SPEED = ALIEN_SPEED + 0.5
                            reset_top_frog()
                            frog_counter = frog_counter + 1

        # This detects if any lasers hit asteroids heading left
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for frog_number in range(len(right_frogs)):
                    if right_frogs[frog_number].x > 0:
                        if stage.collide(right_frogs[frog_number].x + 1,
                                         right_frogs[frog_number].y + 1,
                                         right_frogs[frog_number].x + 15,
                                         right_frogs[frog_number].y + 15,
                                         lasers[laser_number].x + 3,
                                         lasers[laser_number].y + 3,
                                         lasers[laser_number].x + 13,
                                         lasers[laser_number].y + 13):
                            right_frogs[frog_number].move(constants.OFF_SCREEN_X,
                                                                  constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            # sound.play(impact_sound)
                            score = score + 1
                            reset_right_frog()
                            frog_counter = frog_counter + 1

        # This detects if any lasers hit asteroids heading up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for frog_number in range(len(bottom_frogs)):
                    if bottom_frogs[frog_number].x > 0:
                        if stage.collide(bottom_frogs[frog_number].x + 1,
                                         bottom_frogs[frog_number].y + 1,
                                         bottom_frogs[frog_number].x + 15,
                                         bottom_frogs[frog_number].y + 15,
                                         lasers[laser_number].x + 3,
                                         lasers[laser_number].y + 3,
                                         lasers[laser_number].x + 13,
                                         lasers[laser_number].y + 13):
                            bottom_frogs[frog_number].move(constants.OFF_SCREEN_X,
                                                                   constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            # sound.play(impact_sound)
                            score = score + 1
                            reset_bottom_frog()
                            frog_counter = frog_counter + 1

        # This detects a collision between the tank and asteroids going right
        for frog_number in range(len(left_frogs)):
            if left_frogs[frog_number].x > 0:
                if stage.collide(left_frogs[frog_number].x + 1,
                                 left_frogs[frog_number].y + 1,
                                 left_frogs[frog_number].x + 15,
                                 left_frogs[frog_number].y + 15,
                                 tank.x + 3, tank.y + 3, tank.x + 12, tank.y + 12):
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(4.0)
                    sound.stop()
                    game_over_scene(score)

        # This detects a collision between the tank and asteroids going down
        for frog_number in range(len(top_frogs)):
            if top_frogs[frog_number].x > 0:
                if stage.collide(top_frogs[frog_number].x + 1,
                                 top_frogs[frog_number].y + 1,
                                 top_frogs[frog_number].x + 15,
                                 top_frogs[frog_number].y + 15,
                                 tank.x + 3, tank.y + 3, tank.x + 12, tank.y + 12):
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(4.0)
                    sound.stop()
                    game_over_scene(score)

        # This detects a collision between the tank and asteroids going left
        for frog_number in range(len(right_frogs)):
            if right_frogs[frog_number].x > 0:
                if stage.collide(right_frogs[frog_number].x + 1,
                                 right_frogs[frog_number].y + 1,
                                 right_frogs[frog_number].x + 15,
                                 right_frogs[frog_number].y + 15,
                                 tank.x + 3, tank.y + 3, tank.x + 12, tank.y + 12):
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(4.0)
                    sound.stop()
                    game_over_scene(score)

    # This detects a collision between the tank and asteroids going up
        for frog_number in range(len(bottom_frogs)):
            if bottom_frogs[frog_number].x > 0:
                if stage.collide(bottom_frogs[frog_number].x + 1,
                                 bottom_frogs[frog_number].y + 1,
                                 bottom_frogs[frog_number].x + 15,
                                 bottom_frogs[frog_number].y + 15,
                                 tank.x + 3, tank.y + 3, tank.x + 12, tank.y + 12):
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(4.0)
                    sound.stop()
                    game_over_scene(score)

        game.render_sprites(left_frogs + right_frogs + top_frogs +
                            bottom_frogs + sprites + lasers)
        game.tick()


def game_over_scene(final_score):
    # this function is the game over scene
    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text0 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text0.move(22, 20)
    text0.text("Final Score: {:0>2d}".format(final_score))
    text.append(text0)

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(43, 60)
    text1.text("GAME OVER")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(32, 110)
    text2.text("PRESS SELECT")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_SELECT != 0:  # Start button
            keys = 0
            menu_scene()
            #break

        # redraw sprite list

if __name__ == "__main__":
    blank_white_reset_scene()
