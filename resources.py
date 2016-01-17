import pyglet, random
pyglet.resource.path = ['data']
pyglet.resource.reindex()

def centered_img(img):
    img.anchor_x, img.anchor_y = round(img.width/2), round(img.height/2)
    return img

def ast_img():
    return random.choice((ast1_img, ast2_img, ast3_img, ast4_img))

bg_image = pyglet.resource.image('space20001600.jpg')
##bg_image = pyglet.resource.image('space.jpg')
statek_image = pyglet.resource.image('statekCtr.png')
##statek_image.scale = 32/50
##statek_image.width, statek_image.height = 32,32
statek_image= centered_img(statek_image)
engine_image = pyglet.resource.image('engine.png')
engine_image.anchor_x, engine_image.anchor_y = 15, 20

ast1_img = centered_img(pyglet.resource.image('ast1.png'))
ast2_img = centered_img(pyglet.resource.image('ast2.png'))
ast3_img = centered_img(pyglet.resource.image('ast3.png'))
ast4_img = centered_img(pyglet.resource.image('ast4.png'))

planet1_img = centered_img(pyglet.resource.image('qlkaTr.png'))
planet2_img = centered_img(pyglet.resource.image('greenplanet2.png'))
planet3_img = centered_img(pyglet.resource.image('bigplanet.png'))
planet4_img = centered_img(pyglet.resource.image('bigplanet2.png'))

bullet_image =  centered_img(pyglet.resource.image('bullet.png'))

    



