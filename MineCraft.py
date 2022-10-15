from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            scale = 150,
            texture = "sky_sunset",
            double_sided = True
        )

class hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            scale = (0.2,0.3),
            color = color.red,
            rotation = Vec3(150, -10,0),
            position = Vec2(0.4,-0.4)
        )

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            model = 'cube',
            color = color.white,
            texture = "grass",
            position = position,
            origin_y = 0.5)


    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position=self.position+ mouse.normal)
            if key == "right mouse down":
                destroy(self)
for z in range(20):
    for x in range(20):
        voxel = Voxel((x,0,z))



player = FirstPersonController()
sky = Sky()
handd = hand()


app.run()