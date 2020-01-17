#include <gb/gb.h>
#include <stdio.h>
#include "charSprites.c"
#include "background.c"
#include "backgroundTiles.c"
#include "ppSplash.c"
#include "ppSplash1.c"
#include "mtSplashData.c"
#include "mtSplashMap.c"
#include "shooterSplashData.c"
#include "shooterSplashMap.c"
#include "bulletSprite.c"
#include "GameCharacter.c"

struct GameCharacter tank;
struct GameCharacter bullet;
struct GameCharacter frog;
int kills = 1;
UBYTE spritesize = 4;

void performantDelay(UINT8 numloops){
    UINT8 counter;
    for(counter = 0; counter < numloops; counter++){
        wait_vbl_done();
    }
}


UBYTE checkCollisions(struct GameCharacter* one, struct GameCharacter* two){
    return (one->x >= two->x && one->x <= two->x + two->width) && (one->y >= two->y && one->y <= two->y + two->height)
           || (two->x >= one->x && two->x <= one->x + one->width) && (two->y >= one->y && two->y <= one->y + one->height);
}


void moveGameCharacter(struct GameCharacter* character, UINT8 x, UINT8 y){
    move_sprite(character->spritids[0], x, y);

}


void setupBullet(){
    bullet.x = 180;
    bullet.y = 180;
    bullet.width = 8;
    bullet.height = 8;

    set_sprite_tile(0, 0);
    bullet.spritids[0] = 1;

    moveGameCharacter(&bullet, bullet.x, bullet.y);
}


void setupTank(){
    tank.x = 88;
    tank.y = 138;
    tank.width = 8;
    tank.height = 8;

    set_sprite_tile(1, 1);
    tank.spritids[0] = 0;

    moveGameCharacter(&tank, tank.x, tank.y);
}


void setupFrog(){
    frog.x = 88;
    frog.y = 255;
    frog.width = 8;
    frog.height = 8;

    set_sprite_tile(2, 2);
    frog.spritids[0] = 2;

    moveGameCharacter(&frog, frog.x, frog.y);
}


void shoot(){
    kills = 1;
    bullet.y = tank.y;
    bullet.x = tank.x;
    moveGameCharacter(&bullet, bullet.x, bullet.y);
    if(joypad() & J_A){
        NR52_REG = 0x80;
        NR51_REG = 0x11;
        NR50_REG = 0x77;

        NR10_REG = 0x1E;
        NR11_REG = 0x10;
        NR12_REG = 0xF3;
        NR13_REG = 0x00;
        NR14_REG = 0x87;
                 
        while(bullet.x != 0){
            performantDelay(5);
            bullet.y -= 2;
            scroll_sprite(1,0,-2);
            if(bullet.y < -245){
                bullet.y = -246;
                bullet.x = -246;
                moveGameCharacter(&bullet, bullet.x, bullet.y);
                break;
             }
         }
    }
    if(!checkCollisions(&bullet, &frog)){
        bullet.x = 180;
        bullet.y = 180;
        frog.y = -244;
        kills += 1;
    }
}

void main(){

    UINT8 currentspriteindex = 0;

    // these registers must be in this specific order!
    NR52_REG = 0x80; // is 1000 0000 in binary and turns on sound
    NR50_REG = 0x77; // sets the volume for both left and right channel just set to max 0x77
    NR51_REG = 0xFF; // is 1111 1111 in binary, select which chanels we want to use in this case all of them. One bit for the L one bit for the R of all four channels
    set_sprite_data(0, 3, charSprites);

    set_bkg_data(0, 105, mtSplashData);
    set_bkg_tiles(0, 0, 20, 18, mtSplashMap);
    
    SHOW_BKG;
    DISPLAY_ON;

    waitpad(J_START);

    set_bkg_data(0, 126, ppSplash);
    set_bkg_tiles(0, 0, 20, 18, ppSplash1);

    SHOW_BKG;
    DISPLAY_ON;

    waitpad(J_START);

    set_bkg_data(0, 212, shooterSplashData);
    set_bkg_tiles(0, 0, 20, 18, shooterSplashMap);

    SHOW_BKG;
    DISPLAY_ON;

    waitpad(J_START);

    set_bkg_data(0, 7, backgroundTiles);
    set_bkg_tiles(0, 0, 20, 18, background);

    SHOW_SPRITES;
    SHOW_BKG;
    DISPLAY_ON;

    setupTank();
    setupBullet();
    setupFrog();

    while(!checkCollisions(&tank, &frog)){

        performantDelay(5/kills);
        frog.y += 2;
        if(frog.y > 144){
            frog.y = -244;
            frog.x = tank.x;
        }
        moveGameCharacter(&frog, frog.x, frog.y);

        switch(joypad()){
            case J_LEFT:
                tank.x -= 2;
                moveGameCharacter(&tank, tank.x, tank.y);
                break;
            case J_RIGHT: 
                tank.x += 2;
                moveGameCharacter(&tank, tank.x, tank.y);
                break;  
            case J_UP: 
                tank.y -= 2;
                moveGameCharacter(&tank, tank.x, tank.y);
                break; 
            case J_DOWN: 
                tank.y += 2;
                moveGameCharacter(&tank, tank.x, tank.y);
                break;
            case J_A: 
                shoot();
        }
    }
     printf("\n \n \n \n \n \n \n === GAME  OVER ===");
}
