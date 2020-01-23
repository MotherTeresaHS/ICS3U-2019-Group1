.. _start_scene:

Start Scene
===========
For the start scene there are two parts, the picture and the button loop. The picture is just like the splash screens in which we put sprites together on a screen. And for the loop all we did was a while True loop and put it so that when they press start it detects and goes to game scene.

.. figure:: https://raw.githubusercontent.com/Patrick-Gemmell/ICS3U-2019-Group1/master/docs/menu/images/menu2.bmp
    :height: 256 px
    :align: center
    :alt: Image Bank for Main Menu
    
    
And this is the code we used:
    
.. code-block:: python
	:linenos:
  
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
    



