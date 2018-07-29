from random import randint

from hypar import glTF

from aecSpace.aecPoint import aecPoint
from aecSpace.aecShaper import aecShaper
from aecSpace.aecSpace import aecSpace
from aecSpace.aecSpacer import aecSpacer

shaper = aecShaper()

model = glTF()
colorAqua = model.add_material(0.3, 0.72, 0.392, 0.5, 0.8, "Aqua")
colorBlue = model.add_material(0.0, 0.631, 0.945, 0.5, 0.8, "Blue")
colorGreen = model.add_material(0.486, 0.733, 0.0, 0.5, 0.8, "Green")
colorPurple = model.add_material(0.75, 0.07, 1.0, 0.5, 0.8, "Purple")
colorWhite = model.add_material(1.0, 1.0, 1.0, 1.0, 0.8, "White")
colorYellow = model.add_material(1.0, 0.733, 0.0, 0.2, 0.8, "Yellow")

def placeBath(space: aecSpace, rotation: float = 0):
    origin = space.origin_floor
    center = space.center_floor
    
    point = aecPoint(origin.x, origin.y + 2750)
    bath = aecSpace()
    bath.boundary = shaper.makeBox(point, 4130, 1380)
    bath.height = 2749
    bath.level = origin.z
    bath.rotate(rotation, center)
    mesh = bath.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorBlue)
    
    point = aecPoint(point.x, point.y + 390)
    tank = aecSpace()
    tank.boundary = shaper.makeBox(point, 200, 600)
    tank.height = 330
    tank.level = origin.z + 400
    tank.rotate(rotation, center)
    mesh = tank.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)

    point = aecPoint(point.x + 400, point.y + 300)
    bowl = aecSpace()
    bowl.boundary = shaper.makeCylinder(point, 270)
    bowl.height = 410
    bowl.level = origin.z
    bowl.rotate(rotation, center)
    mesh = bowl.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)   
       
    point = aecPoint(origin.x + 3650, origin.y + 2750)
    vanity = aecSpace()
    vanity.boundary = shaper.makeBox(point, 480, 1380)  
    vanity.height = 780
    vanity.level = origin.z
    vanity.rotate(rotation, center)    
    mesh = vanity.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)   

def placeBathFixtures(space: aecSpace, rotation: float = 0):
    origin = space.origin_floor 
    mesh = space.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorBlue)    
      
    point = aecPoint(origin.x + 1, origin.y + 3129)
    tub = aecSpace()
    tub.boundary = shaper.makeBox(point, 2000, 1000)
    tub.height = 450
    tub.level = origin.z
    tub.rotate(rotation, space.center_floor)
    mesh = tub.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)   
    
    point = aecPoint(origin.x + 1, origin.y + 150)
    tank = aecSpace()
    tank.boundary = shaper.makeBox(point, 200, 600)
    tank.height = 330
    tank.level = origin.z + 400
    tank.rotate(rotation, space.center_floor)
    mesh = tank.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)    
        
    point = aecPoint(point.x + 400, point.y + 300)
    bowl = aecSpace()
    bowl.boundary = shaper.makeCylinder(point, 270)
    bowl.height = 410
    bowl.level = origin.z
    bowl.rotate(rotation, space.center_floor)    
    mesh = bowl.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)    
    
    point = aecPoint(origin.x + 1, origin.y + 1000)
    vanity = aecSpace()
    vanity.boundary = shaper.makeBox(point, 480, 1500) 
    vanity.height = 780
    vanity.level = origin.z
    vanity.rotate(rotation, space.center_floor)
    mesh = vanity.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)       
    
    mirror = aecSpace()
    mirror.boundary = shaper.makeBox(point, 10, 1500)
    mirror.height = 1500
    mirror.level = point.z + 1000
    mirror.rotate(rotation, space.center_floor)    
    mesh = mirror.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite) 

def placeBed(space: aecSpace, rotation: float = 0, bedBath = 0):
    origin = space.origin_floor
    center = space.center_floor
    if bedBath == 1: 
        placeBath(space, rotation)
        space.boundary = shaper.makeBox(space.origin_floor, 4130, 2750)
        space.rotate(rotation, center)
    mesh = space.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorGreen)
    
    point = aecPoint(origin.x + 1500, origin.y + 1)
    bed = aecSpace()
    bed.boundary = shaper.makeBox(point, 1500, 2000)
    bed.height = 600
    bed.rotate(rotation, center)
    mesh = bed.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)    
    
    point = aecPoint(origin.x + 1600, origin.y + 20)
    pillows = aecSpace()
    pillows.boundary = shaper.makeBox(point, 1300, 400)
    pillows.height = 150
    pillows.level = origin.z + 600
    pillows.rotate(rotation, center)    
    mesh = pillows.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)

def placeCloset(space: aecSpace, rotation: float = 0):
    origin = space.origin_floor
    point = aecPoint(origin.x + 1, origin.y + 1)
    closet = aecSpace()
    closet.boundary = shaper.makeBox(point, 700, 2750)
    closet.height = 2749
    closet.rotate(rotation, space.center_floor)
    mesh = closet.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorYellow)

def placeFurniture(space: aecSpace, rotation: float = 0):
    origin = space.origin_floor
    mesh = space.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorAqua)
    
    point = aecPoint(origin.x + 1032.5, origin.y)
    couchSeat = aecSpace()
    couchSeat.boundary = shaper.makeBox(point, 2000, 800)
    couchSeat.height = 370
    couchSeat.rotate(rotation, space.center_floor)    
    mesh = couchSeat.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)

    couchBack = aecSpace()
    couchBack.boundary = shaper.makeBox(point, 2000, 200)
    couchBack.height = 330
    couchBack.level = origin.z + 380
    couchBack.rotate(rotation, space.center_floor)    
    mesh = couchBack.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)        
    
    point = aecPoint(point.x + 300, point.y + 1200)
    table = aecSpace()
    table.boundary = shaper.makeBox(point, 1400, 600)
    table.height = 370
    table.rotate(rotation, space.center_floor)    
    mesh = table.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)

def placeKitchen(space: aecSpace, rotation: float = 0):
    origin = space.origin_floor
    mesh = space.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorPurple)
    
    point = aecPoint(origin.x + 1, origin.y + 1)
    kitchen = aecSpace()
    kitchen.boundary = shaper.makeL(origin = point, 
                                    xSize = 3097.5, 
                                    ySize = 3097.5, 
                                    xWidth = 750, 
                                    yDepth = 750)
    kitchen.height = 1000
    kitchen.rotate(rotation, space.center_floor)
    mesh = kitchen.mesh_graphic
    model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorWhite)


def modularHousing(xUnits: int = 1, bedBath = 0):
    module = 4130    
    space = aecSpace()
    spacer = aecSpacer()
    space.boundary = shaper.makeBox(aecPoint(), module, module)
    space.height = 2750
    rooms = \
    [
         "Bath", 
         "Bed", 
         "Hall",      
         "Kitchen",
         "Living"
    ]
    rotations = [0, 90, 180, 270]
    spaces = spacer.row(space, xUnits)
    spaces += [space]
    extSpaces = []
    for unit in spaces:
        yUnits = randint(0, 3)
        if yUnits > 0: extSpaces += spacer.row(space = unit, copies = yUnits, xAxis = False)
    spaces += extSpaces
    for unit in spaces:
        room = rooms[randint(0, len(rooms) - 1)]
        rotation = rotations[randint(0, 3)]
        if room == "Living":
            placeFurniture(unit, rotation)
            rooms.remove("Living")
        if room == "Bath":
            placeBathFixtures(unit, rotation)
            rooms.remove("Bath")
        if room == "Kitchen":
            placeKitchen(unit, rotation)
            rooms.remove("Kitchen")
        if room == "Bed":
            placeBed(unit, rotation, bedBath)
        if room == "Hall": 
            mesh = unit.mesh_graphic
            model.add_triangle_mesh(mesh.vertices, mesh.normals, mesh.indices, colorYellow)            
            rooms.remove("Hall")
    modules = len(spaces)
    return {"model": model.save_base64(), 'computed':{'Total modules':modules}}   
#    model.save_glb('model.glb')
#
#modularHousing(xUnits = randint(1, 4), 
#               bedBath = randint(0, 1)) 

