[![Build Status](https://travis-ci.org/gheja/gbdk.svg?branch=master)](https://travis-ci.org/gheja/gbdk)

GBDK - for AWS Cloud9
=====================

"The GameBoy Developer's Kit (GBDK), is a set of tools that enable to
develop programs for the Nintendo GameBoy system, either in C or in
assembly. GBDK includes a set of libraries for the most common
requirements and generates image files for use with a real GameBoy or
with an emulator.

From http://gbdk.sourceforge.net

Quick summary
=============

The version is specifically designed to run on AWS Cloud9 instance as your developement platform.

Build
=====

Start an AWS Cloud9 instance.

Under "Platform" ensure you select "Ubuntu Server 18.04 LTS"

Load dependancies: 
```
sudo apt-get -y install make gcc g++ bison flex
```

Download the repo: 
```
wget --no-check-certificate --content-disposition https://github.com/MotherTeresaHS/gbdk/archive/master.zip
```

Unzip the file (and rename the folder to gbdk): 
```
unzip gbdk-master.zip && mv gbdk-master gbdk && rm gbdk-master.zip
```

Change director into new folder: 
```
cd gdbk
```

Run MakeFile: 
```
make
```

Then install binaries: 
```
sudo make install
```

Run new builds of a GameBoy *.gb ROM
====================================

To build a new game, go to the ./game folder
In here is a game.c file, that is the "Hello, World!" program for the GameBoy.

Run the following command:
```
/opt/gbdk/bin/lcc -o game.gb game.c
```
then copy game.gb over to ./web/rom directory to see it run in simulator

OR you could run this and it will build your ROM and place it right in the ROMs folder
```
/opt/gbdk/bin/lcc -o ../web/rom/game.gb game.c
```

Open up ./web/index.html
The best way to see your game in the online simulator is to open up the index.html file in the Cloud9 IDE.
Then go to menu "Preview" and "Preview File index.html"
A small window will appear on the right with the simulator running.
Here are the keyboard shortcuts for the buttons on the GameBoy:
* Up - Up Arrow / W
* Down - Down Arrow / S
* Left - Left Arrow / A
* Right - Right Arrow / D
* A - Alt / Z / J
* B - Ctrl / K / X
* Start - Enter
* Select - Shift

If you would like virtual GameBoy buttons:
* move the cursor over to the arrow in the corner where a tool tip will say "Pop Out into a new window"
* select this and a full screen version of the website will appear
* in Chrome go to "View, Developer, Developer Tools"
* Select the "Toggle Device" tool button (looks like a mobile phone infront of a desktop monitor)
* Then reload the page and virtual buttons will appear at the bottom

Making Sprite Data
==================

Install this tool, to make sprite tiles from PNG files

[https://www.npmjs.com/package/ggbgfx-cli](https://www.npmjs.com/package/ggbgfx-cli)

Run: 
```
npm install -g ggbgfx-cli
```

Make your own 8x8 Tile
======================
You can use the web page provided in Tile_generator, created by Sean Kelly [https://www.spkelly.net/tilegen/](https://www.spkelly.net/tilegen/)

Gameboy Tile Data Generator (gbtdg)
===================================
For converting PNG files into tiles and maps for backgrounds
[https://github.com/MotherTeresaHS/gbtdg](https://github.com/MotherTeresaHS/gbtdg)  
Preview [here](https://gameboy.s3-us-west-2.amazonaws.com/gbtdg/index.html)
