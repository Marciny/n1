import pyglet, resources, settings, physicalobject, player
from pyglet.gl import *
from lib1 import *



def main():
    
    def update(dt):

        to_add = []
        
        if not statek.dead:
            camera.update(statek.position)
        for planet in planets:
            for obj in game_objects:
                planet.pull(obj)
                    
        for obj in all_objects:
            obj.update(dt, camera)
            to_add.extend(obj.new_objects)
            obj.new_objects = []
##            if obj.dead:
##                all_objects.remove(obj)

            if obj.__class__.__name__ == 'Bullet' :
                for ast in asteroids_cont:
                    if obj.collides_with(ast):
                        obj.handle_collision_with(ast)
                        ast.handle_collision_with(obj)
##                        all_objects.remove(obj)
                        all_objects.remove(ast)
                        non_player_objects.remove(ast)
                        ast.delete()
##                        asteroids_cont.remove(ast)

            if obj.dead:
                all_objects.remove(obj)
                
            
        all_objects.extend(to_add)
            
        for obj in non_player_objects:
            if not statek.dead and not obj.dead:
                if statek.collides_with(obj):
                    statek.handle_collision_with(obj)
                    statek.delete()             
                    game_objects.remove(statek)
                    all_objects.remove(statek)
                    camera.offset = [0,0]

            

        for obj in bg_sprites:
            obj.set_position(camera.paralaxedupd(obj.position)[0],
                             camera.paralaxedupd(obj.position)[1]) # brzytko wygląda
            if obj.position[0] >  bg_sprite1.width :
                obj.set_position(obj.position[0] - 2 * bg_sprite1.width, obj.position[1])
            if obj.position[0] < -(2 * bg_sprite1.width - window.width):
                obj.set_position(obj.position[0] + 2 * bg_sprite1.width, obj.position[1])
            if obj.position[1] > bg_sprite1.height:
                obj.set_position(obj.position[0] ,obj.position[1] - 2 * bg_sprite1.height)
            if obj.position[1] < -(2 * bg_sprite1.height - window.height):
                obj.set_position(obj.position[0] ,obj.position[1] + 2 * bg_sprite1.height)
            

            
     

    window = pyglet.window.Window(settings.screen_width, settings.screen_height)#fullscreen="true")#1100,700)#)
##    image = pyglet.image.load('space.jpg')
    main_batch = pyglet.graphics.Batch()
    planet_batch = pyglet.graphics.Batch()
    background = pyglet.graphics.Batch()
    planets = []
    
##    physicalobject.Planet.batch = planet_batch
    physicalobject.Planet.container = planets
    planet1 = physicalobject.Planet(img = resources.planet1_img, x = 650, y = 150, batch = planet_batch )
    planet2 = physicalobject.Planet(img = resources.planet1_img, x = 175, y = 600, batch = planet_batch )
    planet3 = physicalobject.Planet(img = resources.planet2_img, x = 700, y = 500, batch = planet_batch, gravity = 7500 )
    planet4 = physicalobject.Planet(img = resources.planet3_img, x = 200, y = 200, batch = planet_batch, gravity = 30000 )
    planet5 = physicalobject.Planet(img = resources.planet2_img, x = 1600, y = 1600, batch = planet_batch, gravity = 7500 )
    planet6 = physicalobject.Planet(img = resources.planet3_img, x = 1000, y = 1300, batch = planet_batch, gravity = 30000 )
    planet7 = physicalobject.Planet(img = resources.planet2_img, x = 1300, y = 1300, batch = planet_batch, gravity = 7500 )
    planet8 = physicalobject.Planet(img = resources.planet2_img, x = 700, y = 1300, batch = planet_batch, gravity = 7500 )
    planet9 = physicalobject.Planet(img = resources.planet4_img, x = 1400, y = 600, batch = planet_batch, gravity = 60000 )
    planet10 = physicalobject.Planet(img = resources.planet2_img, x = 2200, y = 1400, batch = planet_batch, gravity = 7500 )
    planet11 = physicalobject.Planet(img = resources.planet1_img, x = 1950, y = 1100, batch = planet_batch )
    planet12 = physicalobject.Planet(img = resources.planet1_img, x = 1900, y = 100, batch = planet_batch )
    planet13 = physicalobject.Planet(img = resources.planet3_img, x = 100, y = 1300, batch = planet_batch,  gravity = 30000 )
##    planets = [planet1] + [planet2] + [planet3] + [planet4] + [planet5] + [planet6] + [planet7] + [planet8] + [planet9]+ [planet10]
    coords = [window.width / 2, window.height / 2]
    statek = player.Player(x=coords[0], y=coords[1], batch=main_batch)

    window.push_handlers(statek)
    window.push_handlers(statek.key_handler)

    bg_sprite1 = pyglet.sprite.Sprite(img = resources.bg_image, x=0, y=0, batch = background)
    bg_sprite2 = pyglet.sprite.Sprite(img = resources.bg_image, x=0, y=-bg_sprite1.height, batch = background)
    bg_sprite3 = pyglet.sprite.Sprite(img = resources.bg_image, x=-bg_sprite1.width, y=0, batch = background)
    bg_sprite4 = pyglet.sprite.Sprite(img = resources.bg_image, x=-bg_sprite1.width, y=-bg_sprite1.height, batch = background)
    bg_sprites = [bg_sprite1] + [bg_sprite2]+ [bg_sprite3]+ [bg_sprite4]
    asteroids_cont = asteroids(50, coords, main_batch)
    non_player_objects = asteroids_cont #+ planets
    game_objects = [statek] + asteroids_cont
    all_objects = [statek] + asteroids_cont + planets
    camera = MyCamera(simple_camera)
    
    
    @window.event
    def on_draw():
        window.clear()
        background.draw()
##        resources.bg_image.blit(0, 0)
        planet_batch.draw()
        main_batch.draw()
                    

    pyglet.clock.schedule_interval(update, 1/120.0) 
    pyglet.app.run()


if __name__ == '__main__':
    main()
