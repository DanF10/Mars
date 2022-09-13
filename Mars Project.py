import viz
import vizshape
import vizcam
import vizact
import vizconnect
import viztask
import math

#Point class to define vectors
class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self,P):
        return Point(self.x - P.x, self.y - P.y, self.z - P.z)

#Vector class for CAVE math
class Vector:
 
    # Initialize 3D Coordinates of the Vector
    def __init__(self,p1,p2):
        self.p1 = Point(p1.x,p1.y,p1.z)
        self.p2 = Point(p2.x,p2.y,p2.z)
 
    def magnitude(self):
        return math.sqrt((self.p1-self.p2).x ** 2 + (self.p1-self.p2).y ** 2 + (self.p1-self.p2).z ** 2)
    
    #dot product
    def __xor__(self, V):
        return (self.p1 - self.p2).x * (V.p1 - V.p2).x + (self.p1 - self.p2).y * (V.p1 - V.p2).y + (self.p1-self.p2).z * (V.p1 - V.p2).z

#Station class for each different place on Mars
class Station:
    def __init__(self,sphere,texture,forwardPos,forwardEuler,backPos,backEuler):
        self.texture = texture
        #Location/Euler for arrow(s) at each station
        self.forwardPos = forwardPos
        self.forwardEuler = forwardEuler
        self.backPos = backPos
        self.backEuler = backEuler
        self.sphere = sphere
        #Set settings for sphere objects & texture with panorama
        sphere.setPosition([0,0,0])
        sphere.texture(texture)
        sphere.disable(viz.CULL_FACE) 
        sphere.disable(viz.LIGHTING)
        sphere.enable(viz.BLEND)

#Initial vizard setup
viz.setMultiSample(4)
viz.fov(60)

def IsThisVillanovaCAVE():
    cave_host_names = ["exx-PC","render-PC"]
    import socket
    if socket.gethostname() in cave_host_names:
        return True
    else:
        return False

if IsThisVillanovaCAVE():
    CONFIG_FILE = "vizconnect_config_CaveFloor+ART_headnode.py"
    vizconnect.go(CONFIG_FILE)
    rawInput = vizconnect.getConfiguration().getRawDict("input")
    vizconnect.getAvatar().getAttachmentPoint("l_hand").getNode3d().remove()
    vizconnect.getAvatar().getAttachmentPoint("r_hand").getNode3d().remove()
    BUTTON_LEFT = 4
    BUTTON_LEFTMID = 3
    BUTTON_RIGHTMID = 2
    BUTTON_RIGHT = 1
    BUTTON_TRIGGER = 0
else:
    viz.go()

mapPicture = viz.addTexture('Edited map.jpg')
star = viz.addChild('glowingstar.glb')
blueStar = viz.addChild('bluestar.glb')
instructions = viz.addText3D('',pos=[-15,2,20])

if IsThisVillanovaCAVE():
    instructions.message('Hello and welcome to a short tour of Mars. Use the joystick to\npan around, and use trigger while looking at an ' +
    'arrow to travel\nto the next station. You can enlarge the map by pressing the\nleft middle button while looking at the minimap, and use the\nleft and right buttons ' +
    'to change your destination station. Enjoy!\nPress the right middle button to continue.')
else:
    instructions.message('Hello and welcome to a short tour of Mars. Use the mouse while\nholding down left click to pan around, and use left click while\nlooking at an ' +
    'arrow to travel to the next station. You can enlarge\nthe map by pressing m while looking at the minimap, and use\nthe left and right arrows ' +
    'to change your destination station. Enjoy!\nPress enter to continue.')
instructions.color(viz.BLACK)

cam = vizcam.PanoramaNavigate(sensitivity=1.5)
view = viz.MainView
if IsThisVillanovaCAVE():
    xPos,yPos,zPos = vizconnect.getTracker("dtrack_flystick").getPosition()
    flystickP = Point(xPos,yPos,zPos)

fadeout = vizact.fadeTo(0,time=0.25)
fadein = vizact.fadeTo(1, begin=0, time=0.25)

starout = vizact.fadeTo(0,time=1)
starin = vizact.fadeTo(1,begin=0,time=1)

bigMap = vizshape.addPlane(size=[16,9])
bigMap.disable(viz.CULL_FACE)
bigMap.disable(viz.LIGHTING)
bigMap.texture(mapPicture)
bigMap.visible(viz.OFF)

texture001 = viz.addTexture('4k/4k_Station001-shift-rev.tif')
texture117 = viz.addTexture('4k/4k_Station117-shift-rev.jpg')
texture193 = viz.addTexture('4k/4k_Station193-shift-rev.jpg')
texture197 = viz.addTexture('4k/4k_Station197-shift-rev.jpg', flags=viz.LOAD_ASYNC)
texture275 = viz.addTexture('4k/4k_Station275-shift-rev.jpg',flags=viz.LOAD_ASYNC)
texture330 = viz.addTexture('4k/4k_Station330-shift-rev.jpg',flags=viz.LOAD_ASYNC)
texture337 = viz.addTexture('4k/4k_Station337-shift-rev.tif',flags=viz.LOAD_ASYNC)
texture350 = viz.addTexture('4k/4k_Station350-shift-rev.tif',flags=viz.LOAD_ASYNC)

sphere001 = vizshape.addSphere(radius=128, slices=256)
station001 = Station(sphere001,texture001,[-10.6,-10,5.6],[28,0,60],None,None)
station001.sphere.setEuler([180,0,0])

sphere117 = vizshape.addSphere(radius=129, slices=256)
station117 = Station(sphere117,texture117,[-4.6,-10,-11.1],[-72,0,60],[10.6,-10,-5.6],[28,0,-60])
station117.sphere.visible(viz.OFF)

sphere193 = vizshape.addSphere(radius=130, slices=256)
station193 = Station(sphere193,texture193,[10.99,-10,4.8],[-208,0,60],[4.6,-10,11.1],[-72,0,-60])
station193.sphere.visible(viz.OFF)
station193.sphere.setEuler([180,0,0])

sphere197 = vizshape.addSphere(radius=131, slices=256)
station197 = Station(sphere197,texture197,[7.6,-10,9.3],[130,0,60],[-10.99,-10,4.8],[-155,0,-60])
station197.sphere.visible(viz.OFF)
station197.sphere.setEuler([180,0,0])

sphere275 = vizshape.addSphere(radius=132, slices=256)
station275 = Station(sphere275,texture275,[6.7,-10,10],[130,0,60],[10.99,-10,-4.8],[-155,0,60])
station275.sphere.visible(viz.OFF)
station275.sphere.setEuler([180,0,0])

sphere330 = vizshape.addSphere(radius=133, slices=256)
station330 = Station(sphere330,texture330,[12,-10,0],[0,0,-60],[-6.7,-10,-10],[-56,0,60])
station330.sphere.setEuler([180,0,0])
station330.sphere.visible(viz.OFF)

sphere337 = vizshape.addSphere(radius=134, slices=256)
station337 = Station(sphere337,texture337,[12,-10,0],[0,0,-60],[-12,-10,0],[180,0,-60])
station337.sphere.setEuler([180,0,0])
station337.sphere.visible(viz.OFF)

sphere350 = vizshape.addSphere(radius=135, slices=256)
station350 = Station(sphere350,texture350,None,None,[-12,-10,0],[180,0,-60])
station350.sphere.setEuler([180,0,0])
station350.sphere.visible(viz.OFF)

arrayPos = 0
stations = [station001,station117,station193,station197,station275,station330,station337,station350]

backArrow = vizshape.addCylinder(height=3.5,radius=0.75,color=[1,0,0])
backArrow.setEuler(stations[1].backEuler)
backArrow.setPosition(stations[1].backPos)
backArrowhead = vizshape.addCone(height=1.5,radius=1.5,parent=backArrow,color=[1,0,0])
backArrowhead.setPosition([0,2.7,0])
backArrow.visible(viz.OFF)
backArrowhead.visible(viz.OFF)
if IsThisVillanovaCAVE():
    bArrowP1 = Point(stations[1].backPos[0],stations[1].backPos[1],stations[1].backPos[2])
    backVec = Vector(bArrowP1,flystickP)

forwardArrow = vizshape.addCylinder(height=3.5,radius=0.75,color=[1,0,0])
forwardArrow.setEuler(stations[0].forwardEuler)
forwardArrow.setPosition(stations[0].forwardPos)
forwardArrowhead = vizshape.addCone(height=1.5,radius=1.5,parent=forwardArrow,color=[1,0,0])
forwardArrowhead.setPosition([0,2.7,0])
if IsThisVillanovaCAVE():
    fArrowP1 = Point(stations[0].forwardPos[0],stations[0].forwardPos[1],stations[0].forwardPos[2])
    forwardVec = Vector(fArrowP1,flystickP)

minimap = vizshape.addPlane(size=[8,8], parent=forwardArrow)
minimap.setEuler([-90,220,0])
minimap.setPosition([-8,3,0])
minimap.texture(mapPicture)
minimap.disable(viz.CULL_FACE)
minimap.disable(viz.LIGHTING)
minimap.visible(viz.OFF)


starPos = [[1,0,3.75],[1.35,0,3.65],[1.35,0,3.77],[1.32,0,3.72],[1.22,0,3.62],[1.1,0,3.55],[1.05,0,3.5],[.95,0,3.4]]
star.setParent(minimap)
star.setScale(0.15,0.15,0.15)
star.setPosition(starPos[0])

blueStar.setParent(minimap)
blueStar.setScale(0.15,0.15,0.15)
blueStar.setPosition(starPos[1])

def onMouseMove(e):
    #print(view.getEuler())
    #Compute bigMap position and euler
    xMapPos = 12*math.sin(viz.radians(int(view.getEuler()[0])))*math.sin(viz.radians(90-int(view.getEuler()[1])))
    yMapPos = -12*math.cos(viz.radians(90-int(view.getEuler()[1])))
    zMapPos = 12*math.cos(viz.radians(int(view.getEuler()[0])))*math.sin(viz.radians(90-int(view.getEuler()[1])))
    bigMap.setPosition([xMapPos,yMapPos,zMapPos])
    bigMap.setEuler([view.getEuler()[0],-90+view.getEuler()[1],0])
        
    if IsThisVillanovaCAVE():
        #vector math
        xRot,yRot,zRot = vizconnect.getTracker("dtrack_flystick").getEuler()
        xPos,yPos,zPos = vizconnect.getTracker("dtrack_flystick").getPosition()
        pX = 20*math.sin(viz.radians(int(xRot)))*math.sin(viz.radians(90-int(yRot)))
        pY = -20*math.cos(viz.radians(90-int(yRot)))
        pZ = 20*math.cos(viz.radians(int(xRot)))*math.sin(viz.radians(90-int(yRot)))
        flystickP = Point(xPos,yPos,zPos)
        flystickP2 = Point(pX,pY,pZ)
        viewVec = Vector(flystickP,flystickP2)
        fArrowP1 = Point(stations[arrayPos].forwardPos[0],stations[arrayPos].forwardPos[1],stations[arrayPos].forwardPos[2])
        #vector between forward arrow and view position
        forwardVec = Vector(fArrowP1,flystickP)
        bArrowP1 = Point(stations[arrayPos].backPos[0],stations[arrayPos].backPos[1],stations[arrayPos].backPos[2])
        backVec = Vector(bArrowP1,flystickP)
        forwardDotProduct = (viewVec ^ forwardVec)/(viewVec.magnitude() * forwardVec.magnitude())
        backDotProduct = (viewVec ^ backVec)/(viewVec.magnitude() * backVec.magnitude())

        if abs(forwardDotProduct) >= .95 and abs(forwardDotProduct) <= 1 and forwardArrow.getVisible():
            hoverObject = forwardArrow
        elif abs(backDotProduct) >= .95 and abs(backDotProduct) <= 1 and backArrow.getVisible():
            hoverObject = backArrow
        else:
            hoverObject = None
    else:
        hoverObject = viz.pick()
    
    #Check if user is hovering either arrow
    if (hoverObject == backArrow or hoverObject == backArrowhead):
        backArrow.color(0,1,0)
        backArrowhead.color(0,1,0)
        minimap.setParent(backArrow)
        if (backArrow.getEuler()[2] < 0):
            minimap.setPosition([-8,3,0])
            minimap.setEuler([90,220,0])
        else:
            minimap.setPosition([8,3,0])
            minimap.setEuler([-90,220,0])
        minimap.visible(viz.ON)
        blueStar.setPosition(starPos[arrayPos-1])
    elif (hoverObject == forwardArrow or hoverObject == forwardArrowhead):
        forwardArrow.color(0,1,0)
        forwardArrowhead.color(0,1,0)
        minimap.setParent(forwardArrow)
        if (forwardArrow.getEuler()[2] < 0):
            minimap.setPosition([-8,3,0])
            minimap.setEuler([90,220,0])
        else:
            minimap.setPosition([8,3,0])
            minimap.setEuler([-90,220,0])
        minimap.visible(viz.ON)
        blueStar.setPosition(starPos[arrayPos+1])
    
    else:
        backArrow.color(1,0,0)
        backArrowhead.color(1,0,0)
        forwardArrow.color(1,0,0)
        forwardArrowhead.color(1,0,0)
        minimap.visible(viz.OFF)

if IsThisVillanovaCAVE():
    viz.callback(viz.UPDATE_EVENT, onMouseMove)
else:
    viz.callback(viz.MOUSE_MOVE_EVENT, onMouseMove)

def transitionStations(destination):
    global arrayPos
    if arrayPos < destination:
        stations[destination].sphere.alpha(1)
        stations[destination].sphere.visible(viz.ON)
        yield viztask.addAction(stations[arrayPos].sphere, fadeout)
        stations[arrayPos].sphere.visible(viz.OFF)
    else:
        stations[destination].sphere.alpha(0)
        stations[destination].sphere.visible(viz.ON)
        yield viztask.addAction(stations[destination].sphere, fadein)
        stations[arrayPos].sphere.visible(viz.OFF)
    arrayPos = destination
    star.setPosition(starPos[destination])
    if stations[arrayPos].forwardPos != None:
        forwardArrow.setEuler(stations[destination].forwardEuler)
        forwardArrow.setPosition(stations[destination].forwardPos)
        blueStar.setPosition(starPos[destination+1])
        forwardArrow.visible(viz.ON)
        forwardArrowhead.visible(viz.ON)
    else:
        forwardArrow.visible(viz.OFF)
        forwardArrowhead.visible(viz.OFF)
    if stations[arrayPos].backPos != None:
        backArrow.setEuler(stations[destination].backEuler)
        backArrow.setPosition(stations[destination].backPos)
        backArrow.visible(viz.ON)
        backArrowhead.visible(viz.ON)
    else:
        backArrow.visible(viz.OFF)
        backArrowhead.visible(viz.OFF)
    
def mouseClick():
    global arrayPos
    currObject = viz.pick()
    if ((currObject == backArrow or currObject == backArrowhead) and arrayPos > 0):
        viztask.schedule(transitionStations(arrayPos-1))
    elif ((currObject == forwardArrow or currObject == forwardArrowhead) and arrayPos < len(stations) - 1):
        viztask.schedule(transitionStations(arrayPos+1))
        
vizact.onmousedown(viz.MOUSEBUTTON_LEFT, mouseClick)

counter = 0

def onKeyDown(key):
    global arrayPos, counter
    wasPressed = False
    if key == 'm' and minimap.getVisible():
        lastObj = viz.pick()
        wasPressed = True
        minimap.visible(viz.OFF)
        bigMap.visible(viz.ON)
        if backArrow.getVisible():
            backArrow.visible(viz.OFF)
            backArrowhead.visible(viz.OFF)
        if forwardArrow.getVisible():
            forwardArrow.visible(viz.OFF)
            forwardArrowhead.visible(viz.OFF)
        star.setParent(bigMap)
        blueStar.setParent(bigMap)
        star.setPosition([starPos[arrayPos][0]/4*8,0,starPos[arrayPos][2]/4*4.5])
        if lastObj == forwardArrow or lastObj == forwardArrowhead:
            counter=1
            blueStar.setPosition([starPos[arrayPos+1][0]/4*8,0,starPos[arrayPos+1][2]/4*4.5])
        else:
            counter=-1
            blueStar.setPosition([starPos[arrayPos-1][0]/4*8,0,starPos[arrayPos-1][2]/4*4.5])
    if key == 'm' and not minimap.getVisible() and not wasPressed and bigMap.getVisible():
        bigMap.visible(viz.OFF)
        if arrayPos == 0:
            forwardArrow.visible(viz.ON)
            forwardArrowhead.visible(viz.ON)
        elif arrayPos == len(stations) - 1:
            backArrow.visible(viz.ON)
            backArrowhead.visible(viz.ON)
        else:
            backArrow.visible(viz.ON)
            backArrowhead.visible(viz.ON)
            forwardArrow.visible(viz.ON)
            forwardArrowhead.visible(viz.ON)
        star.setParent(minimap)
        star.setPosition(starPos[arrayPos])
        blueStar.setParent(minimap)
    if key == viz.KEY_RIGHT and bigMap.getVisible() and counter + arrayPos + 1 < len(stations):
        if counter == -1 and counter + arrayPos + 2 < len(stations):
            counter = counter + 2
        else:
            counter = counter + 1
        blueStar.setPosition([starPos[arrayPos+counter][0]/4*8,0,starPos[arrayPos+counter][2]/4*4.5])
    elif key == viz.KEY_LEFT and bigMap.getVisible() and counter + arrayPos - 1 >= 0:
        if counter == 1 and counter + arrayPos - 2 >= 0:
            counter = counter -2
        else:
            counter = counter - 1
        blueStar.setPosition([starPos[arrayPos+counter][0]/4*8,0,starPos[arrayPos+counter][2]/4*4.5])
    elif key == viz.KEY_RETURN:
        if bigMap.getVisible() and counter + arrayPos != arrayPos:
            star.setParent(minimap)
            blueStar.setParent(minimap)
            viztask.schedule(transitionStations(arrayPos+counter))
            bigMap.visible(viz.OFF)
        elif instructions.getVisible():
            instructions.visible(viz.OFF)
    wasPressed = False
    
viz.callback(viz.KEYDOWN_EVENT, onKeyDown)

def onButtonDown(e):
    global counter
    hasRun = False
    bigMapRun = False
    if IsThisVillanovaCAVE():
        if rawInput['flystick'].isButtonDown(BUTTON_TRIGGER):
            #vector math
            xRot,yRot,zRot = vizconnect.getTracker("dtrack_flystick").getEuler()
            xPos,yPos,zPos = vizconnect.getTracker("dtrack_flystick").getPosition()
            pX = 20*math.sin(viz.radians(int(xRot)))*math.sin(viz.radians(90-int(yRot)))
            pY = -20*math.cos(viz.radians(90-int(yRot)))
            pZ = 20*math.cos(viz.radians(int(xRot)))*math.sin(viz.radians(90-int(yRot)))
            flystickP = Point(xPos,yPos,zPos)
            flystickP2 = Point(pX,pY,pZ)
            viewVec = Vector(flystickP,flystickP2)
            fArrowP1 = Point(stations[arrayPos].forwardPos[0],stations[arrayPos].forwardPos[1],stations[arrayPos].forwardPos[2])
            #vector between forward arrow and view position
            forwardVec = Vector(fArrowP1,flystickP)
            bArrowP1 = Point(stations[arrayPos].backPos[0],stations[arrayPos].backPos[1],stations[arrayPos].backPos[2])
            backVec = Vector(bArrowP1,flystickP)
            forwardDotProduct = (viewVec ^ forwardVec)/(viewVec.magnitude() * forwardVec.magnitude())
            backDotProduct = (viewVec ^ backVec)/(viewVec.magnitude() * backVec.magnitude())

            if abs(forwardDotProduct) >= .95 and abs(forwardDotProduct) <= 1 and forwardArrow.getVisible():
                hoverObject = forwardArrow
            elif abs(backDotProduct) >= .95 and abs(backDotProduct) <= 1 and backArrow.getVisible():
                hoverObject = backArrow
            else:
                hoverObject = None

            if (hoverObject == backArrow or hoverObject == backArrowhead) and arrayPos > 0 and not mapSelect:
                viztask.schedule(transitionStations(arrayPos-1))
            elif (hoverObject == forwardArrow or hoverObject == forwardArrowhead) and arrayPos < len(stations) - 1 and not mapSelect:
                viztask.schedule(transitionStations(arrayPos+1))
            elif mapSelect:
                bigMapRun = True
                mapSelect = False
                background.visible(viz.OFF)
                minimap.visible(viz.OFF)
                bigMap.visible(viz.ON)
                if backArrow.getVisible():
                    backArrow.visible(viz.OFF)
                    backArrowhead.visible(viz.OFF)
                if forwardArrow.getVisible():
                    forwardArrow.visible(viz.OFF)
                    forwardArrowhead.visible(viz.OFF)
                star.setParent(bigMap)
                blueStar.setParent(bigMap)
                star.setPosition([starPos[arrayPos][0]/4*8,0,starPos[arrayPos][2]/4*4.5])
                if minimap.getParents()[0] == forwardArrow:
                    counter=1
                    blueStar.setPosition([starPos[arrayPos+1][0]/4*8,0,starPos[arrayPos+1][2]/4*4.5])
                else:
                    counter=-1
                    blueStar.setPosition([starPos[arrayPos-1][0]/4*8,0,starPos[arrayPos-1][2]/4*4.5])
        elif rawInput['flystick'].isButtonDown(BUTTON_LEFTMID) and bigMap.getVisible():
            bigMap.visible(viz.OFF)
            if arrayPos == 0:
                forwardArrow.visible(viz.ON)
                forwardArrowhead.visible(viz.ON)
            elif arrayPos == len(stations) - 1:
                backArrow.visible(viz.ON)
                backArrowhead.visible(viz.ON)
            else:
                backArrow.visible(viz.ON)
                backArrowhead.visible(viz.ON)
                forwardArrow.visible(viz.ON)
                forwardArrowhead.visible(viz.ON)
            star.setParent(minimap)
            star.setPosition(starPos[arrayPos])
            blueStar.setParent(minimap)
        if rawInput['flystick'].isButtonDown(BUTTON_RIGHTMID) and instructions.getVisible():
            instructions.visible(viz.OFF)
        if rawInput['flystick'].isButtonDown(BUTTON_RIGHT) and bigMap.getVisible() and counter + arrayPos + 1 < len(stations):
            if counter == -1 and counter + arrayPos + 2 < len(stations):
                counter = counter + 2
            else:
                counter = counter + 1
            blueStar.setPosition([starPos[arrayPos+counter][0]/4*8,0,starPos[arrayPos+counter][2]/4*4.5])
        elif rawInput['flystick'].isButtonDown(BUTTON_LEFT) and bigMap.getVisible() and counter + arrayPos - 1 >= 0:
            if counter == 1 and counter + arrayPos - 2 >= 0:
                counter = counter -2
            else:
                counter = counter - 1
            blueStar.setPosition([starPos[arrayPos+counter][0]/4*8,0,starPos[arrayPos+counter][2]/4*4.5])
        elif rawInput['flystick'].isButtonDown(BUTTON_TRIGGER) and not bigMapRun and bigMap.getVisible() and counter + arrayPos != arrayPos:
            star.setParent(minimap)
            blueStar.setParent(minimap)
            viztask.schedule(transitionStations(arrayPos+counter))
            bigMap.visible(viz.OFF)
        bigMapRun = False

if IsThisVillanovaCAVE():
    viz.callback(viz.SENSOR_DOWN_EVENT, onButtonDown)