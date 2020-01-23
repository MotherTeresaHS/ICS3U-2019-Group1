.. _space_ship:

Tank
==========

In this project we used a series of 16 pixels by 16 pixels picture to act as our characters, enemies and such. All we did was make a 16x256 file and inserted the  sprites along the picture and then uploaded to the pybadge.

.. figure:: https://raw.githubusercontent.com/Patrick-Gemmell/ICS3U-2019-Group1/master/docs/image_bank/sprites.bmp
    :height: 256 px
    :align: center
    :alt: Image Bank for Shooter Shootout

Next we continued to use the sprite and find a way to move it around, and this was how we did it.

.. code-block:: python
	:linenos:
        
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
	
Next we had to update the direction of the ship which goes with the directins the lasers are shooting, we did so by assigning a direction with a variable to change direction of ship by rotating and shooting direction.

.. code-block:: python
	:linenos:
	
	
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
X
