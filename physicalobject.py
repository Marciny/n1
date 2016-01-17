import pyglet, settings, lib1, math, resources
class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y, self.rotation_velocity = 0.0, 0.0, 0.0
        self.new_objects = []
        self.dead = False
        self.max_velocity = 300
        self.min_velocity =  - 300
    def update(self, dt, camera):

        self.velocity_x= min(self.velocity_x, self.max_velocity)
        self.velocity_x= max(self.velocity_x, self.min_velocity)
        self.velocity_y= min(self.velocity_y, self.max_velocity)
        self.velocity_y= max(self.velocity_y, self.min_velocity)
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.x, self.y = camera.posupd(self.position)
        self.rotation += self.rotation_velocity

        self.check_bounds()
    def check_bounds(self):
        min_x = -self.image.width/2         # -, ponieważ z min mamy do czynienia ciągle (dół ekranu to min), a z maxem nie (góra ekranu << max)
        min_y = -self.image.height/2
        max_x = settings.map_width - self.image.width/2
        max_y = settings.map_height - self.image.height/2
##        min_x = 0
##        min_y = 0
##        max_x = settings.map_width 
##        max_y = settings.map_height 
        if self.x < min_x:
            self.x += settings.map_width
        elif self.x > max_x:
            self.x -= settings.map_width
        if self.y < min_y:
            self.y += settings.map_height
        elif self.y > max_y:
            self.y -= settings.map_height
    def collides_with(self, other_object):
        collision_distance = self.image.width/4 + other_object.image.width/4
        actual_distance = lib1.distance( self.position, other_object.position)
        return (actual_distance <= collision_distance)
    def handle_collision_with(self, other_object):
        self.dead = True

class Planet(PhysicalObject):
    def __init__ (self, gravity = 15000, *args, **kwargs):
        super(Planet, self).__init__(*args, **kwargs)
        self.gravity = gravity
        self.denominator = 1
        self.pulling_distance = math.sqrt(self.gravity  * self.denominator ** 2)* 10
        self.dead = False
        self.container.append(self)

    def pull(self, other_object):
        actual_distance, vx, vy = lib1.accurate_distance( self.position, other_object.position) # tu do zmiany kwestia grawitacji ponad podziałami
        if actual_distance > 50:
        #if actual_distance < self.pulling_distance and actual_distance > 100:
            pulling_force = self.gravity / (actual_distance / self.denominator) ** 2
            force_x = pulling_force*vx/actual_distance
            force_y = pulling_force*vy/actual_distance
            force_x = min(200, force_x)
            force_y = min(200, force_y)
            other_object.velocity_x += force_x
            other_object.velocity_y += force_y

class Bullet(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__( resources.bullet_image, *args, **kwargs)
        pyglet.clock.schedule_once(self.die, 0.6)
        self.max_velocity = 5000
        self.min_velocity = -5000
    def die(self, dt):
        self.dead = True


##            other_object.velocity_x = other_object.velocity_x + force_x
##            other_object.velocity_y = other_object.velocity_y + force_y

            
        
        
