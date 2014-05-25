from omega import *
from cyclops import *
from skybox import *
from orbitNavigation import *

global scaleFact
scaleFact = 1000

scene = getSceneManager()

# set the background to black
scene.setBackgroundColor(Color(0, 0, 0, 1))

# Create a directional light                                                                                    
light1 = Light.create()
light1.setLightType(LightType.Directional)
light1.setLightDirection(Vector3(-1.0, -1.0, -1.0))
light1.setColor(Color(0.7, 0.7, 0.7, 1.0))
light1.setAmbient(Color(0.5, 0.5, 0.5, 1.0))
light1.setEnabled(True)

# Load a static model
torusModel = ModelInfo()
torusModel.name = "torus"
torusModel.path = "mapquestaerial.earth"
scene.loadModel(torusModel)

# Create a scene object using the loaded model
torus = StaticObject.create("torus")
torus.setEffect("colored -v emissive -g 1.0 -s 40")
setNearFarZ(1 , 20 * torus.getBoundRadius())

queueCommand(':autonearfar on')
# queueCommand(':depthpart on -5056752.5')

cam = getDefaultCamera()
cam.setControllerEnabled(False)
cam.setPosition(Vector3(313173.30 , -4469345.79 , 6357944.23 ))
orbit_cam = orbitNavigation(cam)
orbit_cam.setTranslationSpeed(10.0)
orbit_cam.setRotationSpeed(35.0)

zoomCam = zoomNav(cam)
zoomCam.setTranslationSpeed(100.0)
wand_pos = None
wand_orient = None

# Setting the camera by hand. Should find a better way
# and give the user a better way to fly around the planet

# planet is centered at 0,0,0 with radius of 6356752.5 - earth is 6371 km
# so this is in cm?
# cam.setPosition(Vector3(313173.30 , -4467345.79 , 657944.23 ))


# cam.roll(6.24159)


# cam.roll(120.00)
# cam.pitch(60.00)

# set a fast speed for travel by default
# cam.getController().setSpeed(30000)

#call skybox setup
setupSkyboxSwitcher()
# since the scale here is pretty large stereo doesnt help much
# so lets start with it turned off
toggleStereo()

# button handling Scripts
def handleEvent():
	global orbit_cam
	global wand_pos
	global wand_orient

	e = getEvent()

	if e.getServiceType() == ServiceType.Wand:
		if(e.isButtonDown(EventFlags.Button7)):
			orbit_cam.startNavigation(wand_pos, wand_orient)
		if(e.isButtonUp(EventFlags.Button7)):
			orbit_cam.stopNavigation()
		if(e.isButtonDown(EventFlags.Button5)):
			while True:
				zoomCam.focusOn(torus)
				zoomCam.startNavigation(wand_pos,wand_orient)
				if(e.isButtonUp(EventFlags.Button5)):
					break
		if(e.isButtonUp(EventFlags.Button5)):
			zoomCam.stopNavigation()
	if e.getServiceType() == ServiceType.Mocap:
		if(e.getSourceId() == 1):
			wand_pos = e.getPosition()
			wand_orient = e.getOrientation()




# it would be better to set the speed based on the height over the surface
# to move slower as you get closer

d0 = 0
d1 = 0
d2 = 0
r = 0

# set flight speed based on altitude

def onUpdate(frame, t, dt):
	global orbit_cam
	global wand_pos
	global wand_orient
        
	orbit_cam.updateNavigation(wand_pos, wand_orient, dt)

	# hittingFloat = getHittingDist()
    # setCamSpeed(hittingDist)
	# d = cam.getPosition()
	# d0 = float(d[0])
	# d1 = float(d[1])
	# d2 = float(d[2])
	# r = math.sqrt(d0*d0 + d1*d1 + d2*d2) - torus.getBoundRadius() # altitude in cm
	# cam.getController().setSpeed(0.25 * r)


# def setCamSpeed(hittingDist):
# 	d = cam.getPosition()
# 	d0 = float(d[0])
# 	d1 = float(d[1])
# 	d2 = float(d[2])
# 	r = math.sqrt(d0*d0 + d1*d1 + d2*d2) - torus.getBoundRadius() # altitude in cm
# 	cam.getController().setSpeed(0.25 * r)

def getHittingDist():
	q = cam.getOrientation()
	dirVec = q * Vector3(0.0, 0.0, -1.0)
	pos = cam.getPosition()
	posX = float(pos[0])
	posY = float(pos[1])
	posZ = float(pos[2])
	camStopTuple = hitNode(torus,pos,dirVec)
	return camStopTuple[0]
	# if camStopTuple[0]:
	# 	hitVector = camStopTuple[1]
	# 	hitX = float(hitVector[0])
	# 	hitY = float(hitVector[1])
	# 	hitZ = float(hitVector[2])
	# 	hittingDist = math.sqrt((posX - hitX)*(posX - hitX) + (posY - hitY)*(posY - hitY) + (posZ - hitZ)*(posz - hitZ))
	# 	return hittingDist
	# return 0.0

setUpdateFunction(onUpdate)
setEventFunction(handleEvent)

