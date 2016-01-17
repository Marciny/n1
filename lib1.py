import math, random, pyglet, resources, physicalobject, settings

half_width = settings.screen_width / 2
half_height = settings.screen_height / 2


def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt( (point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

def asteroids(num_asteroids, player_position, batch = None):
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, settings.map_width)
            asteroid_y = random.randint(0, settings.map_height) 
            new_asteroid = physicalobject.PhysicalObject( img=resources.ast_img(), x=asteroid_x, y=asteroid_y, batch=batch)
            new_asteroid.rotation = random.randint(0, 360)
            new_asteroid.velocity_x = random.randrange(-40,41)
            new_asteroid.velocity_y = random.randrange(-40,41)
            new_asteroid.rotation_velocity = random.randint(-20,21) / 10
            asteroids.append(new_asteroid)
    return asteroids

##def planetize(n)

def accurate_distance(point_1=(0, 0), point_2=(0, 0)):
    vx = point_1[0] - point_2[0]
    vy = point_1[1] - point_2[1]
    if abs(vx) > settings.map_width /2:
        if vx >= 0:          
            vx = -settings.map_width + vx
        else :
            vx = settings.map_width + vx
    if abs(vy) > settings.map_height/2:
        if vy >= 0:          
            vy = -settings.map_width + vy
        else :
            vy = settings.map_width + vy
    dist = math.sqrt(vx **2 + vy ** 2)
    return [dist, vx, vy]



## przekopiowane z pygameu
class MyCamera(object):
    def __init__(self, camera_func):
        self.camera_func = camera_func
        self.offset = [0, 0]
        self.paralax = 0.2
        
    def posupd (self, pos):
        posx = pos[0] + self.offset[0]
        posy = pos[1] + self.offset[1]
        return posx, posy

    def paralaxedupd  (self, pos):
        posx = pos[0] + self.offset[0] * self.paralax
        posy = pos[1] + self.offset[1] * self.paralax
        return posx, posy

    def update(self, offpos):
        self.offset =  self.camera_func(self.offset, offpos)

    def center(self, offset):           # późniejsze camera.update(mousepos) kontroluje, czy ekran nie będzie pokazywał obszaru poza mapą
        l, t =  round(half_width - offset[0]), round(half_height - offset[1])
        self.offset = [l,t]


def simple_camera(current_offset, offpos):
    new_offset =[-offpos[0] + half_width,
                  -offpos[1] + half_height]
    return new_offset
    
    


