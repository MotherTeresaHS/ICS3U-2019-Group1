.. _splash_scene:

Splash Scene
============

For our splash screens, we have to have two of them: MT Game Studios and our company studios. For a splash screen to work all we had to do was take a 160x128 picture and create our design, then we cut it up into 16x16 pictures and put it in a image bank. Once it's in an image bank we put together like a puzzle on the pybadge, like so:

Here is the MT Game Studio splash screen:

.. figure:: https://raw.githubusercontent.com/Patrick-Gemmell/ICS3U-2019-Group1/master/docs/menu/images/mt_game_studio.bmp
    :height: 256 px
    :align: center
    :alt: Image Bank for MT Game Studios Splash Screen

.. code-block:: python
	:linenos:
    
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

And here is the PP Company splash screen:

.. figure:: https://raw.githubusercontent.com/Patrick-Gemmell/ICS3U-2019-Group1/master/docs/menu/images/menu3.bmp
    :height: 256 px
    :align: center
    :alt: Image Bank for PP Company
    
.. code-block:: python
	:linenos:
    
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









   

