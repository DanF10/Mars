import viz
import vizshape
import vizcam
import vizact
import vizconnect
import viztask
import math

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
    #tracker = vizconnect.getRawTool('dtrack_flystick')
    #tracker = viz.add('dtrack_flystick')?
    BUTTON_LEFT = 4
    BUTTON_LEFTMID = 3
    BUTTON_RIGHT = 1
    BUTTON_TRIGGER = 0
else:
    viz.go()

mapPicture = viz.addTexture('Edited map.jpg')
star = viz.addChild('glowingstar.glb')
blueStar = viz.addChild('bluestar.glb')

cam = vizcam.PanoramaNavigate(sensitivity=1.5)
view = viz.MainView

fadeout = vizact.fadeTo(0,time=0.25)
fadein = vizact.fadeTo(1, begin=0, time=0.25)

starout = vizact.fadeTo(0,time=1)
starin = vizact.fadeTo(1,begin=0,time=1)

#r = 12
forwardArrowEuler = [[28,0,60],[0,0,-60],[0,0,-60],[0,0,-60]]
forwardArrowPosition = [[-10.6,-10,5.6],[12,-10,0],[12,-10,0],[12,-10,0]]

backArrowEuler = [[28,0,-60],[180,0,-60],[180,0,-60],[180,0,-60]]
backArrowPosition = [[10.6,-10,-5.6],[-12,-10,0],[-12,-10,0],[-12,-10,0]]

backArrow = vizshape.addCylinder(height=3.5,radius=0.75,color=[1,0,0])
backArrow.setEuler(backArrowEuler[0])
backArrow.setPosition(backArrowPosition[0])
backArrowhead = vizshape.addCone(height=1.5,radius=1.5,parent=backArrow,color=[1,0,0])
backArrowhead.setPosition([0,2.7,0])
backArrow.visible(viz.OFF)
backArrowhead.visible(viz.OFF)

forwardArrow = vizshape.addCylinder(height=3.5,radius=0.75,color=[1,0,0])
forwardArrow.setEuler(forwardArrowEuler[0])
forwardArrow.setPosition(forwardArrowPosition[0])
forwardArrowhead = vizshape.addCone(height=1.5,radius=1.5,parent=forwardArrow,color=[1,0,0])
forwardArrowhead.setPosition([0,2.7,0])
forwardArrow.collideSphere(radius=3)

bigMap = vizshape.addPlane(size=[16,9])
bigMap.disable(viz.CULL_FACE)
bigMap.disable(viz.LIGHTING)
bigMap.texture(mapPicture)
bigMap.visible(viz.OFF)

minimap = vizshape.addPlane(size=[8,8], parent=forwardArrow)
minimap.setEuler([-90,220,0])
minimap.setPosition([-8,3,0])
minimap.texture(mapPicture)
minimap.disable(viz.CULL_FACE)
minimap.disable(viz.LIGHTING)
minimap.visible(viz.OFF)

background = vizshape.addPlane(size=[8.1,8.1], parent=minimap, color=(255,255,0))
background.disable(viz.CULL_FACE)
background.disable(viz.LIGHTING)
background.visible(viz.OFF)

star.setParent(minimap)
star.setScale(0.15,0.15,0.15)
star.setPosition([1,0,3.75])

blueStar.setParent(minimap)
blueStar.setScale(0.15,0.15,0.15)
blueStar.setPosition([1.3,0,3.7])

station001 = viz.addTexture('4k/4k_Station001-shift-rev.tif')
station117 = viz.addTexture('4k/4k_Station117-shift-rev.jpg')
station330 = viz.addTexture('4k/4k_Station330-shift-rev.jpg')
station337 = viz.addTexture('4k/4k_Station337-shift-rev.tif',flags=viz.LOAD_ASYNC)
station350 = viz.addTexture('4k/4k_Station350-shift-rev.tif',flags=viz.LOAD_ASYNC)

sphere001 = vizshape.addSphere(radius=128, slices=256)
sphere001.setPosition([0,0,0])
sphere001.setEuler([180,0,0])
sphere001.texture(station001)
sphere001.disable(viz.CULL_FACE) 
sphere001.disable(viz.LIGHTING)
sphere001.enable(viz.BLEND)
sphere001.disable(viz.INTERSECT_INFO_OBJECT)

sphere117 = vizshape.addSphere(radius=129, slices=256)
sphere117.setPosition([0,0,0])
sphere117.setEuler([180,0,0])
sphere117.texture(station117)
sphere117.disable(viz.CULL_FACE) 
sphere117.disable(viz.LIGHTING)
sphere117.visible(viz.OFF)
sphere117.enable(viz.BLEND)

sphere330 = vizshape.addSphere(radius=130, slices=256)
sphere330.setPosition([0,0,0])
sphere330.setEuler([180,0,0])
sphere330.texture(station330)
sphere330.disable(viz.CULL_FACE) 
sphere330.disable(viz.LIGHTING)
sphere330.visible(viz.OFF)
sphere330.enable(viz.BLEND)

sphere337 = vizshape.addSphere(radius=131, slices=256)
sphere337.setPosition([0,0,0])
sphere337.setEuler([180,0,0])
sphere337.texture(station337)
sphere337.disable(viz.CULL_FACE) 
sphere337.disable(viz.LIGHTING)
sphere337.visible(viz.OFF)
sphere337.enable(viz.BLEND)

sphere350 = vizshape.addSphere(radius=132, slices=256)
sphere350.setPosition([0,0,0])
sphere350.setEuler([180,0,0])
sphere350.texture(station350)
sphere350.disable(viz.CULL_FACE) 
sphere350.disable(viz.LIGHTING)
sphere350.visible(viz.OFF)
sphere350.enable(viz.BLEND)

arrayPos = 0
spheres = []
spheres.append(sphere001)
spheres.append(sphere117)
spheres.append(sphere330)
spheres.append(sphere337)
spheres.append(sphere350)

starPos = []
starPos.append([1,0,3.75])
starPos.append([1.3,0,3.7])
starPos.append([1.1,0,3.55])
starPos.append([1.05,0,3.5])
starPos.append([.95,0,3.4]) 

mapSelect = False

def onMouseMove(e):
    xMapPos = 12*math.sin(viz.radians(int(view.getEuler()[0])))*math.sin(viz.radians(90-int(view.getEuler()[1])))
    yMapPos = -12*math.cos(viz.radians(90-int(view.getEuler()[1])))
    zMapPos = 12*math.cos(viz.radians(int(view.getEuler()[0])))*math.sin(viz.radians(90-int(view.getEuler()[1])))
    bigMap.setPosition([xMapPos,yMapPos,zMapPos])
    bigMap.setEuler([view.getEuler()[0],-90+view.getEuler()[1],0])
    
    if IsThisVillanovaCAVE():
        xRot,yRot,zRot = vizconnect.getTracker("dtrack_flystick").getEuler()
        xPos,yPos,zPos = vizconnect.getTracker("dtrack_flystick").getPosition()
        trackerX = 20*math.sin(viz.radians(int(xRot)))*math.sin(viz.radians(90-int(yRot)))
        trackerY = -20*math.cos(viz.radians(90-int(yRot)))
        trackerZ = 20*math.cos(viz.radians(int(xRot)))*math.sin(viz.radians(90-int(yRot)))
        info = viz.intersect([xPos,yPos,zPos],[trackerX,trackerY,trackerZ])
        view.setPosition([xPos,yPos,0])
        hoverObject = info.object
    else:
        hoverObject = forwardArrow
    #4,5,9 
    if (hoverObject == backArrow or hoverObject == backArrowhead or hoverObject == minimap):
        backArrow.color(0,1,0)
        backArrowhead.color(0,1,0)
        minimap.setParent(backArrow)
        minimap.setPosition([-8,3,0])
        minimap.setEuler([90,220,0])
        minimap.visible(viz.ON)
        blueStar.setPosition(starPos[arrayPos-1])
    #6,7,9
    elif (hoverObject == forwardArrow or hoverObject == forwardArrowhead or hoverObject == minimap):
        forwardArrow.color(0,1,0)
        forwardArrowhead.color(0,1,0)
        minimap.setParent(forwardArrow)
        if (forwardArrow.getPosition()[0] < 0):
            minimap.setPosition([8,3,0])
            minimap.setEuler([-90,220,0])
        else:
            minimap.setPosition([-8,3,0])
            minimap.setEuler([90,220,0])
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

def forwardButtonTransition(destination):
    global arrayPos
    spheres[destination].alpha(1)
    spheres[destination].visible(viz.ON)
    yield viztask.addAction(spheres[arrayPos], fadeout)
    spheres[arrayPos].visible(viz.OFF)
    arrayPos = destination
    star.setPosition(starPos[destination])
    if arrayPos < len(spheres) - 1:
        forwardArrow.setEuler(forwardArrowEuler[destination])
        forwardArrow.setPosition(forwardArrowPosition[destination])
        blueStar.setPosition(starPos[destination+1])
    backArrow.setEuler(backArrowEuler[destination-1])
    backArrow.setPosition(backArrowPosition[destination-1])
    
    if arrayPos == 0:
        backArrow.visible(viz.OFF)
        backArrowhead.visible(viz.OFF)
        forwardArrow.visible(viz.ON)
        forwardArrowhead.visible(viz.ON)
    elif arrayPos == len(spheres) - 1:
        forwardArrow.visible(viz.OFF)
        forwardArrowhead.visible(viz.OFF)
        backArrow.visible(viz.ON)
        backArrowhead.visible(viz.ON)
    else:
        backArrow.visible(viz.ON)
        backArrowhead.visible(viz.ON)
        forwardArrow.visible(viz.ON)
        forwardArrowhead.visible(viz.ON)

def backButtonTransition(destination):
    global arrayPos
    spheres[destination].alpha(0)
    spheres[destination].visible(viz.ON)
    yield viztask.addAction(spheres[destination], fadein)
    spheres[arrayPos].visible(viz.OFF)
    arrayPos = destination
    star.setPosition(starPos[arrayPos])
    if arrayPos > 0:
        backArrow.setEuler(backArrowEuler[destination-1])
        backArrow.setPosition(backArrowPosition[destination-1])
        blueStar.setPosition(starPos[destination-1])
    forwardArrow.setEuler(forwardArrowEuler[destination])
    forwardArrow.setPosition(forwardArrowPosition[destination])
    
    if arrayPos == 0:
        backArrow.visible(viz.OFF)
        backArrowhead.visible(viz.OFF)
        forwardArrow.visible(viz.ON)
        forwardArrowhead.visible(viz.ON)
    elif arrayPos == len(spheres) - 1:
        forwardArrow.visible(viz.OFF)
        forwardArrowhead.visible(viz.OFF)
        backArrow.visible(viz.ON)
        backArrowhead.visible(viz.ON)
    else:
        backArrow.visible(viz.ON)
        backArrowhead.visible(viz.ON)
        forwardArrow.visible(viz.ON)
        forwardArrowhead.visible(viz.ON)
    
def mouseClick():
    global arrayPos
    currObject = viz.pick()
    if ((currObject == backArrow or currObject == backArrowhead) and arrayPos > 0):
        viztask.schedule(backButtonTransition(arrayPos-1))
    elif ((currObject == forwardArrow or currObject == forwardArrowhead) and arrayPos < len(spheres) - 1):
        viztask.schedule(forwardButtonTransition(arrayPos+1))
        
vizact.onmousedown(viz.MOUSEBUTTON_LEFT, mouseClick)

wasPressed = False
counter = 0
lastObj = viz.pick()
def onKeyDown(key):
    global arrayPos, wasPressed, counter
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
        elif arrayPos == len(spheres) - 1:
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
    #FIX BUG WHERE BLUE STAR DISAPPEARS AT END OF ARRAY??
    if key == viz.KEY_RIGHT and bigMap.getVisible() and counter + arrayPos + 1 < len(spheres):
        if counter == -1 and counter + arrayPos + 2 < len(spheres):
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
    elif key == viz.KEY_RETURN and bigMap.getVisible() and counter + arrayPos != arrayPos:
        star.setParent(minimap)
        blueStar.setParent(minimap)
        if counter + arrayPos > arrayPos:
            viztask.schedule(forwardButtonTransition(arrayPos+counter))
        else:
            viztask.schedule(backButtonTransition(arrayPos+counter))
        bigMap.visible(viz.OFF)
    wasPressed = False
    
viz.callback(viz.KEYDOWN_EVENT, onKeyDown)

mapSelect = False
arrowSelect = True
hasRun = False
bigMapRun = False

def onButtonDown(e):
    global mapSelect, arrowSelect, hasRun, counter, bigMapRun
    if IsThisVillanovaCAVE():
        '''
        if rawInput['flystick'].isButtonDown(BUTTON_RIGHT) or rawInput['flystick'].isButtonDown(BUTTON_LEFT):
            if minimap.getVisible() and mapSelect:
                mapSelect = False
                arrowSelect = True
                hasRun = True
                minimap.visible(viz.OFF)
                background.visible(viz.OFF)
            elif minimap.getVisible() and not mapSelect and not hasRun:
                mapSelect = True
                arrowSelect = False
                background.visible(viz.ON)
            hasRun = False
        '''
        if rawInput['flystick'].isButtonDown(BUTTON_TRIGGER):
            xRot,yRot,zRot = vizconnect.getTracker("dtrack_flystick").getEuler()
            xPos,yPos,zPos = vizconnect.getTracker("dtrack_flystick").getPosition()
            trackerX = 20*math.sin(viz.radians(int(xRot)))*math.sin(viz.radians(90-int(yRot)))
            trackerY = -20*math.cos(viz.radians(90-int(yRot)))
            trackerZ = 20*math.cos(viz.radians(int(xRot)))*math.sin(viz.radians(90-int(yRot)))
            info = viz.intersect([xPos,yPos,zPos],[trackerX,trackerY,trackerZ])
            hoverObject = info.object
            #back arrow
            if (hoverObject == backArrow or hoverObject == backArrowhead) and arrayPos > 0 and not mapSelect:
                viztask.schedule(backButtonTransition(arrayPos-1))
            elif (hoverObject == forwardArrow or hoverObject == forwardArrowhead) and arrayPos < len(spheres) - 1 and not mapSelect:
                viztask.schedule(forwardButtonTransition(arrayPos+1))
        elif (mapSelect and rawInput['flystick'].isButtonDown(BUTTON_TRIGGER)) or rawInput['flystick'].isButtonDown(BUTTON_LEFTMID):
            bigMapRun = True
            mapSelect = False
            background.visible(viz.OFF)
            minimap.visible(viz.OFF)
            if not bigMap.getVisible():
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
            else:
                bigMap.visible(viz.OFF)
                if arrayPos == 0:
                    forwardArrow.visible(viz.ON)
                    forwardArrowhead.visible(viz.ON)
                elif arrayPos == len(spheres) - 1:
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
        '''
        elif rawInput['flystick'].isButtonDown(BUTTON_LEFTMID) and bigMap.getVisible() and not bigMapRun:
            bigMap.visible(viz.OFF)
            if arrayPos == 0:
                forwardArrow.visible(viz.ON)
                forwardArrowhead.visible(viz.ON)
            elif arrayPos == len(spheres) - 1:
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
        '''
        if rawInput['flystick'].isButtonDown(BUTTON_RIGHT) and bigMap.getVisible() and counter + arrayPos + 1 < len(spheres):
            if counter == -1 and counter + arrayPos + 2 < len(spheres):
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
            if counter + arrayPos > arrayPos:
                viztask.schedule(forwardButtonTransition(arrayPos+counter))
            else:
                viztask.schedule(backButtonTransition(arrayPos+counter))
            bigMap.visible(viz.OFF)
        bigMapRun = False

if IsThisVillanovaCAVE():
    viz.callback(viz.SENSOR_DOWN_EVENT, onButtonDown)
    

##CAVE INTEGRATION
#def isButtonDown_Trigger():
#    if IsThisVillanovaCAVE():
#        return rawInput['flystick'].isButtonDown(BUTTON_TRIGGER)
#viz.callback(viz.SENSOR_DOWN_EVENT, isButtonDown_Trigger)