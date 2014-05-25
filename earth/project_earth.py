from omega import *
from cyclops import *

from orbitNavigation import *
from coordinateConvertor import *
from caveutil import *
from Location import *
from CoordinateCalculator import CoordinateCalculator
from coordinateSystemNode import *

import csv

#global declarations
scene = None
light1 = None
earthHybridModel = None
earthHybrid = None

earthHybridModelwithoutElevation = None
earthHybridwithoutElevation = None

earthRoadModel = None
earthRoad = None

earthRoadModelwithoutElevation = None
earthRoadwithoutElevation = None

earthAerialModel = None
earthAerial = None

earthAerialModelwithoutElevation = None
earthAerialwithoutElevation = None

atmoHybrid = None
atmoAerial = None
sky = None
cam = None
orientOriginal = None
orbit_cam = None
mm = None
uim = None
uiRoot = None
searchText = None
laser = None

keyboardWindow = None
dragWidget = None
keyboardWidget = None
textWidget = None
textBox = None
listBox = None
keysWidget = None
textLabel = None
backspaceKey = None
backspaceBtn = None
commaKey = None
commaBtn = None
fullstopkey = None
fullstopBtn = None
quoteKey = None
quoteBtn = None
spaceKey = None
spaceKeyBtn = None
sizeUpContainer = None
sizeUpLbl = None
sizeDownContainer = None
sizeDownLbl = None
closeBtnContainer = None
closeLbl = None
infoContainer = None
infoCityLbl	= None
infoCountryLbl = None
clearKey = None
clearKeyBtn = None
textBoxContainer = None

goBtnContainer = None
goLbl = None

countryNameLbl =None
countryNameContainer =None

wand_pos = None
wand_orient = None

keysContainer = []
keys = []
keysBtn = []

boolKeyboard = False
isMoreCity = False
keyboardWindowx = 0
keyboardWindowy = 0
keyboardContainerwidth = 0
keyboardContainerheight = 0
fontsize = 0


searchText = ''
searchCityInfo = ''
searchCountryInfo = ''
enabledisableStr = 'Enable Keyboard'
alphabets = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
cityDict = {}
autoCompleteOptions = []
autoCompleteList = []
autoCompleteDict = {}
listCount = 0
searchTextPrevLen = 0
searchTextCurrLen = 0
dragWidgetPressed = False
keyboard_XstartOffset = 0
keyboard_YstartOffset = 0
elevationMenu = None
elevationmenuStr = 'Disable Elevation'
isElevationVisible = True

cityListContainer = []
cityListLbl = []
countryKeyList = []
currentCountryIndex = 0
citystartIdx = 0
cityendIdx = 0
currentCityBucket = 0
cityTotalBucket = 0
max_no_pinnedCity = 8
max_no_recentCity = 8
boolCitySelected = False

providerCounter = 0

pinnedLocationList = []
recentLocationList = []

pinnedContainerwidth = 1366
pinnedContainerheight = (768 / 2) - 10

recentContainerWidth = 1366
recentContainerHeight = (768 / 2) - 10

recentlyVisitedContainer = []
recentlyVisitedInfoContainer = []
recentlyVisitedInfoLocalityLbl = []
recentlyVisitedInfoCountryLbl = []
recentlyVisitedInfoLatLonLbl = []
pinnedCityContainer = []
pinnedCityPinContainer = []
pinnedCityInfoContainer = []
pinnedCityInfoLocalityLbl = []
pinnedCityInfoCountryLbl = []
pinnedCityInfoLatLonLbl = []

pinnedCityDelContainer = []
recentlyVisitedDelContainer = []
pinnedParentContainer = None
recentlyVisitedParentContainer = None
skyradius = None


def main():
	initScene()
	initMenu()
	initCaveKeyboard()
	loadStars()
	readCitycsv()
	createCityContainers()
	loadLaserPointer()
	testDataSphere()

	setUpdateFunction(onUpdate)
	setEventFunction(handleEvent)

def initScene():
	global scene
	global light1
	global earthHybridModel
	global earthAerialModel
	global earthRoadModel
	global earthHybrid
	global earthAerial
	global earthRoad
	global earthAerialwithoutElevation
	global earthHybridwithoutElevation
	global earthAerialModelwithoutElevation
	global earthHybridModelwithoutElevation
	global earthRoadwithoutElevation
	global earthRoadModelwithoutElevation
	global atmoHybrid
	global atmoAerial
	global sky
	global cam
	global orientOriginal
	global orbit_cam
	global keyboardContainerwidth
	global keyboardContainerheight
	global keyboardWindowx
	global keyboardWindowy
	global fontsize
	global dist
	global skyradius

	scene = getSceneManager()
	scene.setBackgroundColor(Color(0, 0, 0, 1))

	light1 = Light.create()
	light1.setLightType(LightType.Directional)
	light1.setLightDirection(Vector3(-1.0, -1.0, -1.0))
	light1.setColor(Color(0.7, 0.7, 0.7, 1.0))
	light1.setAmbient(Color(0.5, 0.5, 0.5, 1.0))
	light1.setEnabled(True)

	earthHybridModel = ModelInfo()
	earthHybridModel.name = "earthHybrid"
	earthHybridModel.path = "bing.earth"
	scene.loadModel(earthHybridModel)
	earthHybrid = StaticObject.create("earthHybrid")
	earthHybrid.setScale(Vector3(1.0, 1.0, 1.0))
	earthHybrid.setEffect("colored -v emissive -g 1.0 -s 40")
	earthHybrid.getMaterial().setDoubleFace(1)
	earthHybrid.getMaterial().setProgram("textured")
	earthHybrid.setPosition(Vector3(0.0,0.0,0.0))

	print 'Loaded Bing Hybrid Model.............................ok'

	earthAerialModel = ModelInfo()
	earthAerialModel.name = "earthAerial"
	earthAerialModel.path = "bingaerial.earth"
	scene.loadModel(earthAerialModel)
	earthAerial = StaticObject.create("earthAerial")
	earthAerial.setScale(Vector3(1.0, 1.0, 1.0))
	earthAerial.setEffect("colored -v emissive -g 1.0 -s 40")
	earthAerial.getMaterial().setDoubleFace(1)
	earthAerial.getMaterial().setProgram("textured")
	earthAerial.setPosition(Vector3(0.0,0.0,0.0))
	earthAerial.setVisible(False)

	print 'Loaded Bing Aerial Model ............................ok'

	earthRoadModel = ModelInfo()
	earthRoadModel.name = "earthRoad"
	earthRoadModel.path = "bingroad.earth"
	scene.loadModel(earthRoadModel)
	earthRoad = StaticObject.create("earthRoad")
	earthRoad.setScale(Vector3(1.0, 1.0, 1.0))
	earthRoad.setEffect("colored -v emissive -g 1.0 -s 40")
	earthRoad.getMaterial().setDoubleFace(1)
	earthRoad.getMaterial().setProgram("textured")
	earthRoad.setPosition(Vector3(0.0,0.0,0.0))
	earthRoad.setVisible(False)

	print 'Loaded Bing Road Model ...............................ok'

	earthHybridModelwithoutElevation = ModelInfo()
	earthHybridModelwithoutElevation.name = "earthHybridwithoutElevation"
	earthHybridModelwithoutElevation.path = "bingnoelevation.earth"
	scene.loadModel(earthHybridModelwithoutElevation)
	earthHybridwithoutElevation = StaticObject.create("earthHybridwithoutElevation")
	earthHybridwithoutElevation.setScale(Vector3(1.0, 1.0, 1.0))
	earthHybridwithoutElevation.setEffect("colored -v emissive -g 1.0 -s 40")
	earthHybridwithoutElevation.getMaterial().setDoubleFace(1)
	earthHybridwithoutElevation.getMaterial().setProgram("textured")
	earthHybridwithoutElevation.setPosition(Vector3(0.0,0.0,0.0))
	earthHybridwithoutElevation.setVisible(False)

	print 'Loaded Bing Hybrid Model Without Elevation.............................ok'

	earthAerialModelwithoutElevation = ModelInfo()
	earthAerialModelwithoutElevation.name = "earthAerialwithoutElevation"
	earthAerialModelwithoutElevation.path = "bingaerialnoelevation.earth"
	scene.loadModel(earthAerialModelwithoutElevation)
	earthAerialwithoutElevation = StaticObject.create("earthAerialwithoutElevation")
	earthAerialwithoutElevation.setScale(Vector3(1.0, 1.0, 1.0))
	earthAerialwithoutElevation.setEffect("colored -v emissive -g 1.0 -s 40")
	earthAerialwithoutElevation.getMaterial().setDoubleFace(1)
	earthAerialwithoutElevation.getMaterial().setProgram("textured")
	earthAerialwithoutElevation.setPosition(Vector3(0.0,0.0,0.0))
	earthAerialwithoutElevation.setVisible(False)

	print 'Loaded Bing Aerial Model Without Elevation............................ok'

	earthRoadModelwithoutElevation = ModelInfo()
	earthRoadModelwithoutElevation.name = "earthRoadwithoutElevation"
	earthRoadModelwithoutElevation.path = "bingroadnoelevation.earth"
	scene.loadModel(earthRoadModelwithoutElevation)
	earthRoadwithoutElevation = StaticObject.create("earthRoadwithoutElevation")
	earthRoadwithoutElevation.setScale(Vector3(1.0, 1.0, 1.0))
	earthRoadwithoutElevation.setEffect("colored -v emissive -g 1.0 -s 40")
	earthRoadwithoutElevation.getMaterial().setDoubleFace(1)
	earthRoadwithoutElevation.getMaterial().setProgram("textured")
	earthRoadwithoutElevation.setPosition(Vector3(0.0,0.0,0.0))
	earthRoadwithoutElevation.setVisible(False)

	print 'Loaded Bing Road Model Without Elevation...............................ok'

	atmoHybrid = SphereShape.create(6378100 + 80000, 5)
	earthHybrid.addChild(atmoHybrid)
	atmoHybrid.setEffect('./atmosphere -e #9090f030 -a -t')

	atmoAerial = SphereShape.create(6378100 + 80000, 5)
	earthAerial.addChild(atmoAerial)
	atmoAerial.setEffect('./atmosphere -e #9090f030 -a -t')

	# Load the sky sphere
	sky=caveutil.loadObject(getSceneManager(), "sky", "data/textures/sky.fbx", False, False, True, False, True)
	sky.setScale(Vector3(1.0,1.0,1.0))
	# sky.setScale(Vector3(2000.0,2000.0,2000.0))
	sky.getMaterial().setDoubleFace(True)
	sky.getMaterial().setProgram("textured emissive")
	sky.setVisible(False)
	earthHybrid.addChild(sky)
	skyradius = sky.getBoundRadius()
	skyradius = float(skyradius)

	setNearFarZ(1, 100000000)

	queueCommand(':depthpart on 1000')

	cam = getDefaultCamera()
	cam.setControllerEnabled(False)
	cam.setPosition(Vector3(195825.80, -7498234.13, 7039488.51))
	cam.pitch(radians(30))
	orientOriginal = cam.getOrientation()

	# interpol_cam = InterpolActor(cam)
	# interpol_cam.setTransitionType(InterpolActor.SMOOTH)	# Use SMOOTH ease-in/ease-out interpolation rather than LINEAR
	# interpol_cam.setDuration(7)							# Set interpolation duration to 3 seconds
	# interpol_cam.setOperation(InterpolActor.POSITION | InterpolActor.ORIENT)	# Interpolate both position and orientation
	
	orbit_cam = orbitNavigation(cam)
	orbit_cam.setTranslationSpeed(100.0)
	orbit_cam.setRotationSpeed(10.0)

	keyboardContainerwidth = 4268
	keyboardContainerheight = 1920
	keyboardWindowx = 1366 * 12
	keyboardWindowy = 384
	fontsize = 56



def initMenu():
	global mm
	global uim
	global uiRoot
	global enabledisableStr
	global keyboardMenu
	global elevationMenu
	global elevationmenuStr

	i = 0
	menuBtn = []
	menuOption = None
	city = None
	country = None
	
	mm = MenuManager.createAndInitialize()
	uim = UiModule.createAndInitialize()


	wf = uim.getWidgetFactory()
	uiRoot = uim.getUi()

	keyboardMenu = mm.getMainMenu().addButton(str(enabledisableStr), 'setKeyboardVisibility()')

	topPlacesmenu = mm.getMainMenu().addSubMenu("My Places")
	with open("data/menucities.csv","rU") as data:
		rows = csv.reader(data)
		for row in rows:
			if str(row[0]):
				city = str(row[0]).strip()
			else:
				city = ''
			if str(row[1]):
				country = str(row[1]).strip()
			else:
				country = ''

			menuBtn.append(topPlacesmenu.addButton(city.title(),"selectedCity('" + str(city) + "')"))
			# menuBtn[i].getButton().setCheckable(True)
			# menuBtn[i].getButton().setRadio(True)
			# menuBtn[i].getButton().setChecked(False)
			i = i + 1

	# chicagoBtn = recentlyVisitedmenu.addButton("Chicago, US","selectedCity(\"chicago\")")
	# chicagoBtn.getButton().setCheckable(True)
	# chicagoBtn.getButton().setRadio(True)
	# chicagoBtn.getButton().setChecked(False)
	# chennaiBtn = recentlyVisitedmenu.addButton("Chennai, IN","selectedCity(\"chennai\")")
	# chennaiBtn.getButton().setCheckable(True)
	# chennaiBtn.getButton().setRadio(True)
	# chennaiBtn.getButton().setChecked(False)
	# tokyoBtn = recentlyVisitedmenu.addButton("Tokyo, JPN","selectedCity(\"tokyo\")")
	# tokyoBtn.getButton().setCheckable(True)
	# tokyoBtn.getButton().setRadio(True)
	# tokyoBtn.getButton().setChecked(False)
	# parisBtn = recentlyVisitedmenu.addButton("Paris, FR", "selectedCity(\"paris\")")
	# parisBtn.getButton().setCheckable(True)
	# parisBtn.getButton().setRadio(True)
	# parisBtn.getButton().setChecked(False)

	elevationMenu = mm.getMainMenu().addButton(str(elevationmenuStr), 'setElevationVisibility()')

	resetCamMenu = mm.getMainMenu().addButton("Reset Camera", "resetCamera()")

def selectedCity(locString):
	global cam
	lat = None
	lon = None
	locality = None
	district = None
	country = None
	qold = None
	qnew = None
	oldPos = None
	cityInfoList = []

	a = getLocationbyQuery(locString)
	cityInfoList = a[0]
	lat = str(cityInfoList[0])
	lon = str(cityInfoList[1])
	locality = cityInfoList[4].strip()
	district = cityInfoList[2].strip()
	country = cityInfoList[3].strip()

	broadcastCommand("onmenuCitySelected('" + lat + '/' + lon + '/' + locality + '/' + district + '/' + country + "')")

def onmenuCitySelected(inputList):
	global cam
	lat = None
	lon = None
	locality = None
	district = None
	country = None
	qold = None
	qnew = None
	oldPos = None

	inputList = inputList.split('/')
	lat,lon,locality,district,country = inputList

	lat = float(lat)
	lon = float(lon)
	locality = locality.strip()
	district = district.strip()
	country = country.strip()

	targetPos = geodetic2ecef(lat, lon, 300)
	lookatPoint = geodetic2ecef(lat, lon, 0)
			
	# get the old position and orientation
	qold = cam.getOrientation()
	oldPos = cam.getPosition()
			
	# set the new position and look at the City. Get the new orientation
	cam.setPosition(Vector3(float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
	cam.lookAt(Vector3(float(lookatPoint[0]), float(lookatPoint[1]), float(lookatPoint[2])), Vector3(0.0, 1.0, 0.0))
	# qnew = cam.getOrientation()

	# Restore the old camera position and orientation
	# cam.setPosition(Vector3(float(oldPos[0]), float(oldPos[1]), float(oldPos[2])))
	# cam.setOrientation(qold)

	# cam.setPosition(Vector3( float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
	# cam.setOrientation(qnew)

def initCaveKeyboard():
	global uiRoot
	global keyboardWindow
	global keyboardWindowx
	global keyboardWindowy
	global keyboardContainerwidth
	global keyboardContainerheight
	global fontsize

	global dragWidget
	global keyboardWidget
	global textWidget
	global textBox
	global listBox
	global keysWidget
	global textLabel
	global keysContainer
	global keys
	global backspaceKey
	global backspaceBtn
	global commaKey
	global commaBtn
	global fullstopkey
	global fullstopBtn
	global quoteKey
	global quoteBtn
	global spaceKey
	global spaceKeyBtn
	global sizeUpContainer
	global sizeUpLbl
	global sizeDownContainer
	global sizeDownLbl
	global closeBtnContainer
	global closeLbl
	global keysBtn
	global clearKey
	global clearKeyBtn
	global textBoxContainer
	global goBtnContainer
	global goLbl
	
	global infoContainer
	global infoCityLbl
	global infoCountryLbl
	global searchCityInfo
	global searchCountryInfo
	global countryNameContainer
	global countryNameLbl
	global cityListContainer
	global cityListLbl

	keyboardWindow = Container.create(ContainerLayout.LayoutVertical, uiRoot)
	keyboardWindow.setAutosize(False)
	keyboardWindow.setWidth(keyboardContainerwidth + int(keyboardContainerheight / 13))
	keyboardWindow.setHeight(keyboardContainerheight + int(keyboardContainerheight / 10) + int(keyboardContainerheight / 5))
	keyboardWindow.setStyleValue('fill','#C0C0C0')
	keyboardWindow.setStyleValue('border', '2 #ffffff')
	keyboardWindow.setPosition(Vector2(keyboardWindowx, keyboardWindowy))
	keyboardWindow.setDraggable(True)
	keyboardWindow.setVisible(False)

	dragWidget = Container.create(ContainerLayout.LayoutHorizontal, keyboardWindow)
	dragWidget.setAutosize(False)
	dragWidget.setWidth(keyboardWindow.getWidth())
	dragWidget.setHeight(int(keyboardContainerheight / 5))
	dragWidget.setStyleValue('border','2 #ffffff')
	dragWidget.setHorizontalAlign(HAlign.AlignRight)
	dragWidget.setPadding(int(keyboardContainerheight / 250))
	dragWidget.setPinned(True)

	keyboardWidget = Container.create(ContainerLayout.LayoutHorizontal, keyboardWindow)
	keyboardWidget.setAutosize(False)
	keyboardWidget.setWidth(keyboardContainerwidth)
	keyboardWidget.setHeight(keyboardContainerheight)
	keyboardWidget.setStyleValue('fill','#C0C0C0')
	keyboardWidget.setStyleValue('border', '2 #ffffff')

	# text widget 
	textWidget = Container.create(ContainerLayout.LayoutVertical, keyboardWidget)
	textWidget.setAutosize(False)
	textWidget.setWidth(int(keyboardWidget.getWidth() / 4))
	textWidget.setHeight(keyboardWidget.getHeight())
	textWidget.setVerticalAlign(VAlign.AlignTop)
	textWidget.setStyleValue('border', '2 #ffffff')
	textWidget.setPadding(8)
	# textWidget.setClippingEnabled(True)

	textBoxContainer = Container.create(ContainerLayout.LayoutHorizontal, textWidget)
	textBoxContainer.setAutosize(True)
	textBoxContainer.setPadding(5)

	textBox = Container.create(ContainerLayout.LayoutHorizontal, textBoxContainer)
	textBox.setAutosize(False)
	textBox.setWidth(int((textWidget.getWidth() * 4.5) / 6))
	textBox.setHeight(int((textWidget.getHeight() * 12) / 132))
	textBox.setClippingEnabled(True)
	textBox.setVerticalAlign(VAlign.AlignMiddle)
	textBox.setHorizontalAlign(HAlign.AlignLeft)
	textBox.setStyleValue('fill', '#ffffff')

	textLabel = Label.create(textBox)
	textLabel.setText(searchText)
	textLabel.setColor(Color('black'))
	textLabel.setFont('data/fonts/Arial.ttf ' + str(fontsize))

	goBtnContainer = Container.create(ContainerLayout.LayoutVertical, textBoxContainer)
	goBtnContainer.setAutosize(False)
	goBtnContainer.setWidth(int(textWidget.getWidth() / 6))
	goBtnContainer.setHeight(int((textWidget.getHeight() * 12) / 132))
	goBtnContainer.setMargin(int(goBtnContainer.getHeight() / 3))
	goBtnContainer.setStyleValue('fill', '#6f7376')
	goBtnContainer.setStyleValue('border', '2 #000000')
	goBtnContainer.setVisible(True)

	goLbl = Button.create(goBtnContainer)
	goLbl.setText('Go')
	goLbl.getLabel().setColor(Color('white'))
	goLbl.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	cursorLbl = Label.create(textBox)
	cursorLbl.setAutosize(False)
	cursorLbl.setText(' ')
	cursorLbl.setWidth(8)
	cursorLbl.setHeight(70)
	cursorLbl.setStyleValue('fill', '#000000')

	listBox = Container.create(ContainerLayout.LayoutVertical, textWidget)
	listBox.setAutosize(False)
	listBox.setWidth(int((textWidget.getWidth() * 5.5) / 6))
	listBox.setHeight(int((textWidget.getHeight() * 96) / 132))
	listBox.setStyleValue('border', '2 #ffffff')
	listBox.setPadding(2)
	listBox.setVisible(False)
	listBox.setClippingEnabled(True)

	countryNameContainer = Container.create(ContainerLayout.LayoutVertical, listBox)
	countryNameContainer.setAutosize(False)
	countryNameContainer.setWidth(int((textWidget.getWidth() * 5.5) / 6))
	countryNameContainer.setHeight(int((textWidget.getHeight() * 12) / 132))
	countryNameContainer.setMargin(int(countryNameContainer.getHeight() / 4))
	countryNameContainer.setStyleValue('fill', '#778899')

	# alter currentCountryIndex in ButtonRight,ButtonLeft event
	countryNameLbl = Label.create(countryNameContainer)
	countryNameLbl.setText('')
	countryNameLbl.setColor(Color('white'))
	countryNameLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize))

	i = 0
	for i in range(7):
		cityListContainer.append(Container.create(ContainerLayout.LayoutVertical, listBox))
		cityListContainer[i].setAutosize(False)
		cityListContainer[i].setWidth(int((textWidget.getWidth() * 5.5) / 6))
		cityListContainer[i].setHeight(int((textWidget.getHeight() * 12) / 132))
		cityListContainer[i].setMargin(int((cityListContainer[i].getHeight()) / 4))
		cityListContainer[i].setStyleValue('fill', '#ffffff')

		cityListLbl.append(Label.create(cityListContainer[i]))
		cityListLbl[i].setText('')
		cityListLbl[i].setColor(Color('black'))
		cityListLbl[i].setFont('data/fonts/Arial.ttf ' + str(fontsize))

	infoContainer = Container.create(ContainerLayout.LayoutVertical, textWidget)
	infoContainer.setAutosize(False)
	infoContainer.setWidth(int((textWidget.getWidth() * 5.5) / 6))
	infoContainer.setHeight(int((textWidget.getHeight() * 18) / 132))
	infoContainer.setMargin(int(infoContainer.getHeight() / 4))
	infoContainer.setStyleValue('border', '2 #ffffff')
	# infoContainer.setVisible(False)
	infoContainer.setClippingEnabled(True)
	infoContainer.setPadding(15)
	
	infoCityLbl = Label.create(infoContainer)
	infoCityLbl.setText(searchCityInfo)
	infoCityLbl.setColor(Color('black'))
	infoCityLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 3 / 4))

	infoCountryLbl = Label.create(infoContainer)
	infoCountryLbl.setText(searchCountryInfo)
	infoCountryLbl.setColor(Color('black'))
	infoCountryLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 3 / 4))

	# Keys Widget
	keysWidget = Container.create(ContainerLayout.LayoutVertical, keyboardWidget)
	keysWidget.setAutosize(False)
	keysWidget.setWidth(int((keyboardWidget.getWidth() * 3) / 4))
	keysWidget.setHeight(keyboardWidget.getHeight())
	keysWidget.setStyleValue('border', '2 #cccccc')
	keysWidget.setMargin(int(keysWidget.getHeight() / 20))
	keysWidget.setPadding(int(keysWidget.getHeight() / 20))

	# Container Holding keys. 3 rows
	i = 0
	j = 0
	for i in range(4):
		keysContainer.append(Container.create(ContainerLayout.LayoutHorizontal, keysWidget))
		keysContainer[i].setWidth(int((keysWidget.getWidth() * 5) / 6))
		keysContainer[i].setHeight(int((keysWidget.getHeight() * 2) / 9))
		keysContainer[i].setPadding(int(keysWidget.getWidth() / 70))

	for j in range(26):
		if(j <= 9):
			keys.append(Container.create(ContainerLayout.LayoutVertical, keysContainer[0]))
			keys[j].setAutosize(False)
			keys[j].setWidth(int(keysContainer[2].getWidth() / 12))
			keys[j].setHeight(int(keysContainer[2].getWidth() / 12))
			keys[j].setStyleValue('fill','#363636')
			keys[j].setStyleValue('border', '2 #ffffff')
			keys[j].setMargin(int(keys[j].getWidth() / 2))

			keysBtn.append(Button.create(keys[j]))
			keysBtn[j].setText(alphabets[j])
			keysBtn[j].getLabel().setColor(Color('white'))
			keysBtn[j].getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

		elif(j >= 10 and j <= 18):
			keys.append(Container.create(ContainerLayout.LayoutVertical, keysContainer[1]))
			keys[j].setAutosize(False)
			keys[j].setWidth(int(keysContainer[2].getWidth() / 12))
			keys[j].setHeight(int(keysContainer[2].getWidth() / 12))
			keys[j].setStyleValue('fill','#363636')
			keys[j].setStyleValue('border', '2 #ffffff')
			keys[j].setMargin(int(keys[j].getWidth() / 2))

			keysBtn.append(Button.create(keys[j]))
			keysBtn[j].setText(alphabets[j])
			keysBtn[j].getLabel().setColor(Color('white'))
			keysBtn[j].getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

		elif(j >= 19 and j <= 25):
			keys.append(Container.create(ContainerLayout.LayoutVertical, keysContainer[2]))
			keys[j].setAutosize(False)
			keys[j].setWidth(int(keysContainer[2].getWidth() / 12))
			keys[j].setHeight(int(keysContainer[2].getWidth() / 12))
			keys[j].setStyleValue('fill','#363636')
			keys[j].setStyleValue('border', '2 #ffffff')
			keys[j].setMargin(int(keys[j].getWidth() / 2))

			keysBtn.append(Button.create(keys[j]))
			keysBtn[j].setText(alphabets[j])
			keysBtn[j].getLabel().setColor(Color('white'))
			keysBtn[j].getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))
		
	# Back Space Key
	backspaceKey = Container.create(ContainerLayout.LayoutVertical,keysContainer[0])
	backspaceKey.setAutosize(False)
	backspaceKey.setWidth(int(keysContainer[2].getWidth() * 2 / 12))
	backspaceKey.setHeight(int(keysContainer[2].getWidth() / 12))
	backspaceKey.setStyleValue('fill','#363636')
	backspaceKey.setStyleValue('border', '2 #ffffff')
	backspaceKey.setMargin(int(backspaceKey.getHeight() / 2))

	backspaceBtn = Button.create(backspaceKey)
	backspaceBtn.setText('delete')
	backspaceBtn.getLabel().setColor(Color('white'))
	backspaceBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# quote key
	quoteKey = Container.create(ContainerLayout.LayoutVertical, keysContainer[1])
	quoteKey.setAutosize(False)
	quoteKey.setWidth(int(keysContainer[1].getWidth() / 12))
	quoteKey.setHeight(int(keysContainer[1].getWidth() / 12))
	quoteKey.setStyleValue('fill','#363636')
	quoteKey.setStyleValue('border', '2 #ffffff')
	quoteKey.setHorizontalAlign(HAlign.AlignCenter)

	quoteBtn = Button.create(quoteKey)
	quoteBtn.setText("'")
	quoteBtn.getLabel().setColor(Color('white'))
	quoteBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# comma Key
	commaKey = Container.create(ContainerLayout.LayoutVertical, keysContainer[2])
	commaKey.setAutosize(False)
	commaKey.setWidth(int(keysContainer[1].getWidth() / 12))
	commaKey.setHeight(int(keysContainer[1].getWidth() / 12))
	commaKey.setStyleValue('fill','#363636')
	commaKey.setStyleValue('border', '2 #ffffff')
	commaKey.setMargin(int(commaKey.getWidth() / 2))

	commaBtn = Button.create(commaKey)
	commaBtn.setText(',')
	commaBtn.getLabel().setColor(Color('white'))
	commaBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# full stop key
	fullstopkey = Container.create(ContainerLayout.LayoutVertical, keysContainer[2])
	fullstopkey.setAutosize(False)
	fullstopkey.setWidth(int(keysContainer[2].getWidth() / 12))
	fullstopkey.setHeight(int(keysContainer[2].getWidth() / 12))
	fullstopkey.setStyleValue('fill','#363636')
	fullstopkey.setStyleValue('border', '2 #ffffff')
	fullstopkey.setMargin(int(fullstopkey.getWidth() / 2 ))

	fullstopBtn = Button.create(fullstopkey)
	fullstopBtn.setText('.')
	fullstopBtn.getLabel().setColor(Color('white'))
	fullstopBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# space key
	spaceKey = Container.create(ContainerLayout.LayoutVertical, keysContainer[3])
	spaceKey.setAutosize(False)
	spaceKey.setWidth(int((keysContainer[2].getWidth() * 6) / 12))
	spaceKey.setHeight(int(keysContainer[2].getWidth() / 12))
	spaceKey.setStyleValue('fill','#363636')
	spaceKey.setStyleValue('border', '2 #ffffff')

	spaceKeyBtn = Button.create(spaceKey)
	spaceKeyBtn.setText('')
	spaceKeyBtn.getLabel().setColor(Color('white'))
	spaceKeyBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	#clear key
	clearKey = Container.create(ContainerLayout.LayoutVertical, keysContainer[3])
	clearKey.setAutosize(False)
	clearKey.setWidth(int((keysContainer[2].getWidth() * 2) / 12))
	clearKey.setHeight(int(keysContainer[2].getWidth() / 12))
	clearKey.setStyleValue('fill','#363636')
	clearKey.setStyleValue('border', '2 #ffffff')
	clearKey.setMargin(int(clearKey.getHeight() / 2))

	clearKeyBtn = Button.create(clearKey)
	clearKeyBtn.setText('clear')
	clearKeyBtn.getLabel().setColor(Color('white'))
	clearKeyBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# # # # # # # # # # # # # # #
	sizeDownContainer = Container.create(ContainerLayout.LayoutVertical, dragWidget)
	sizeDownContainer.setAutosize(False)
	sizeDownContainer.setWidth(int(keysContainer[2].getWidth() / 12))
	sizeDownContainer.setHeight(int(keysContainer[2].getWidth() / 12))
	sizeDownContainer.setStyleValue('fill','#363636')
	sizeDownContainer.setStyleValue('border', '2 #ffffff')
	sizeDownContainer.setMargin(int(keys[j].getWidth() / 2))

	sizeDownLbl = Label.create(sizeDownContainer)
	sizeDownLbl.setText('-')
	sizeDownLbl.setColor(Color('white'))
	sizeDownLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 3))

	sizeUpContainer = Container.create(ContainerLayout.LayoutVertical, dragWidget)
	sizeUpContainer.setAutosize(False)
	sizeUpContainer.setWidth(int(keysContainer[2].getWidth() / 12))
	sizeUpContainer.setHeight(int(keysContainer[2].getWidth() / 12))
	sizeUpContainer.setStyleValue('fill','#363636')
	sizeUpContainer.setStyleValue('border', '2 #ffffff')
	sizeUpContainer.setMargin(int(keys[j].getWidth() / 3))

	sizeUpLbl = Label.create(sizeUpContainer)
	sizeUpLbl.setText('+')
	sizeUpLbl.setColor(Color('white'))
	sizeUpLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 2))

	closeBtnContainer = Container.create(ContainerLayout.LayoutVertical, dragWidget)
	closeBtnContainer.setAutosize(False)
	closeBtnContainer.setWidth(int(keysContainer[2].getWidth() / 12))
	closeBtnContainer.setHeight(int(keysContainer[2].getWidth() / 12))
	closeBtnContainer.setStyleValue('fill','#363636')
	closeBtnContainer.setStyleValue('border', '2 #ffffff')
	closeBtnContainer.setMargin(int(closeBtnContainer.getWidth() / 4))

	closeLbl = Label.create(closeBtnContainer)
	closeLbl.setText('X')
	closeLbl.setColor(Color('white'))
	closeLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 2))
	
def setKeyboardVisibility():
	global boolKeyboard
	global keyboardWindow
	global enabledisableStr
	global keyboardMenu
	global mm

	boolKeyboard = not boolKeyboard
	# print showKeyboard
	if (boolKeyboard):
		keyboardWindow.setVisible(True)
		enabledisableStr = 'Disable Keyboard'
	else:
		keyboardWindow.setVisible(False)
		enabledisableStr = 'Enable Keyboard'
	keyboardMenu.getButton().setText(enabledisableStr)
	mm.getMainMenu().hide()

def setElevationVisibility():
	global isElevationVisible
	global elevationMenu
	global elevationmenuStr
	global mm 

	isElevationVisible = not isElevationVisible

	if isElevationVisible:
		elevationmenuStr = 'Disable Elevation'
	else:
		elevationmenuStr = 'Enable Elevation'
	elevationMenu.getButton().setText(elevationmenuStr)

	mm.getMainMenu().hide()
	changeProvider()

def sizeUpScript():
	global keyboardWindow
	global dragWidget
	global keyboardWidget
	global textWidget
	global textBox
	global listBox
	global keysWidget
	global textLabel
	global keysContainer
	global keys
	global backspaceKey
	global backspaceBtn
	global commaKey
	global commaBtn
	global fullstopkey
	global fullstopBtn
	global quoteKey
	global quoteBtn
	global spaceKey
	global spaceKeyBtn
	global sizeUpContainer
	global sizeUpLbl
	global sizeDownContainer
	global sizeDownLbl
	global closeBtnContainer
	global closeLbl
	global keysBtn
	global clearKey
	global clearKeyBtn

	global goBtnContainer
	global goLbl

	global keyboardContainerwidth
	global keyboardContainerheight
	global fontsize
	global keyboardWindowx
	global keyboardWindowy
	global infoContainer
	global infoCityLbl
	global infoCountryLbl
	global searchCityInfo
	global searchCountryInfo
	global countryNameContainer
	global countryNameLbl
	global cityListContainer
	global cityListLbl

	keyboardPosVal = []

	if (keyboardContainerwidth + int(853.75) <= 5122):
		keyboardContainerwidth += int(853.75)
	if (keyboardContainerheight + int(384) <= 2304):
		keyboardContainerheight += int(384)

	keyboardPosVal = keyboardWindow.getPosition()
	keyboardWindowx = keyboardPosVal[0]
	keyboardWindowy = keyboardPosVal[1]

	fontsize = int(keyboardContainerheight / 27)
	if (keyboardWindowx + (keyboardContainerwidth + int(keyboardContainerheight / 13)) > 1366 * 18):
		keyboardWindowx = 1366 * 18 - (keyboardContainerwidth + int(keyboardContainerheight / 13))

	if (keyboardWindowy + (keyboardContainerheight + int(keyboardContainerheight / 10) + int(keyboardContainerheight / 5)) > 768 * 4):
		keyboardWindowy = 768 * 4 - (keyboardContainerheight + int(keyboardContainerheight / 10) + int(keyboardContainerheight / 5))

	keyboardWindow.setWidth(keyboardContainerwidth + int(keyboardContainerheight / 13))
	keyboardWindow.setHeight(keyboardContainerheight + int(keyboardContainerheight / 10) + int(keyboardContainerheight / 5))
	keyboardWindow.setPosition(Vector2(keyboardWindowx,keyboardWindowy))

	dragWidget.setWidth(keyboardWindow.getWidth())
	dragWidget.setHeight(int(keyboardContainerheight / 5))
	dragWidget.setPadding(int(keyboardContainerheight / 250))

	keyboardWidget.setWidth(keyboardContainerwidth)
	keyboardWidget.setHeight(keyboardContainerheight)

	textWidget.setWidth(int(keyboardWidget.getWidth() / 4))
	textWidget.setHeight(keyboardWidget.getHeight())

	textBox.setWidth(int((textWidget.getWidth() * 5) / 6))
	textBox.setHeight(int((textWidget.getHeight() * 12) / 132))

	textLabel.setFont('data/fonts/Arial.ttf ' + str(fontsize))

	goBtnContainer.setWidth(int(textWidget.getWidth() / 6))
	goBtnContainer.setHeight(int((textWidget.getHeight() * 12) / 132))
	goBtnContainer.setMargin(int(goBtnContainer.getHeight() / 3))

	goLbl.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	listBox.setWidth(int((textWidget.getWidth() * 5) / 6))
	listBox.setHeight(int((textWidget.getHeight() * 96) / 132))

	for i in range(7):
		cityListContainer[i].setWidth(int((textWidget.getWidth() * 5.5) / 6))
		cityListContainer[i].setHeight(int((textWidget.getHeight() * 12) / 132))

		cityListLbl[i].setFont('data/fonts/Arial.ttf ' + str(fontsize))


	infoContainer.setWidth(int((textWidget.getWidth() * 5.5) / 6))
	infoContainer.setHeight(int((textWidget.getHeight() * 12) / 132))
	
	infoCityLbl.setText(searchCityInfo)
	infoCityLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 3 / 4))

	infoCountryLbl.setText(searchCountryInfo)
	infoCountryLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 3 / 4))

	countryNameContainer.setWidth(int((textWidget.getWidth() * 5.5) / 6))
	countryNameContainer.setHeight(int((textWidget.getHeight() * 12) / 132))
	
	countryNameLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize))

	keysWidget.setWidth(int((keyboardWidget.getWidth() * 3) / 4))
	keysWidget.setHeight(keyboardWidget.getHeight())
	keysWidget.setMargin(int(keysWidget.getHeight() / 20))
	keysWidget.setPadding(int(keysWidget.getHeight() / 20))

	i = 0
	j = 0
	for i in range(4):
		keysContainer[i].setWidth(int((keysWidget.getWidth() * 5) / 6))
		keysContainer[i].setHeight(int((keysWidget.getHeight() * 2) / 9))
		keysContainer[i].setPadding(int(keysWidget.getWidth() / 70))

	for j in range(26):
		if(j <= 9):
			keys[j].setWidth(int(keysContainer[2].getWidth() / 12))
			keys[j].setHeight(int(keysContainer[2].getWidth() / 12))
			keys[j].setMargin(int(keys[j].getWidth() / 2))

			keysBtn[j].getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

		elif(j >= 10 and j <= 18):
			keys[j].setWidth(int(keysContainer[2].getWidth() / 12))
			keys[j].setHeight(int(keysContainer[2].getWidth() / 12))
			keys[j].setMargin(int(keys[j].getWidth() / 2))

			keysBtn[j].getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

		elif(j >= 19 and j <= 25):
			keys[j].setWidth(int(keysContainer[2].getWidth() / 12))
			keys[j].setHeight(int(keysContainer[2].getWidth() / 12))
			keys[j].setMargin(int(keys[j].getWidth() / 2))

			keysBtn[j].getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	backspaceKey.setWidth(int(keysContainer[2].getWidth() * 2 / 12))
	backspaceKey.setHeight(int(keysContainer[2].getWidth() / 12))
	backspaceKey.setMargin(int(backspaceKey.getHeight() / 2))

	backspaceBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	quoteKey.setWidth(int(keysContainer[1].getWidth() / 12))
	quoteKey.setHeight(int(keysContainer[1].getWidth() / 12))
	quoteKey.setHorizontalAlign(HAlign.AlignCenter)

	quoteBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# comma Key
	commaKey.setWidth(int(keysContainer[1].getWidth() / 12))
	commaKey.setHeight(int(keysContainer[1].getWidth() / 12))
	commaKey.setMargin(int(commaKey.getWidth() / 2))

	commaBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# full stop key
	fullstopkey.setWidth(int(keysContainer[2].getWidth() / 12))
	fullstopkey.setHeight(int(keysContainer[2].getWidth() / 12))
	fullstopkey.setMargin(int(fullstopkey.getWidth() / 2 ))

	fullstopBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# space key
	spaceKey.setWidth(int((keysContainer[2].getWidth() * 6) / 12))
	spaceKey.setHeight(int(keysContainer[2].getWidth() / 12))

	clearKey.setWidth(int((keysContainer[2].getWidth() * 2) / 12))
	clearKey.setHeight(int(keysContainer[2].getWidth() / 12))

	clearKeyBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	sizeDownContainer.setWidth(int(keysContainer[2].getWidth() / 12))
	sizeDownContainer.setHeight(int(keysContainer[2].getWidth() / 12))
	sizeDownContainer.setMargin(int(keys[j].getWidth() / 2))

	sizeDownLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 3))

	sizeUpContainer.setWidth(int(keysContainer[2].getWidth() / 12))
	sizeUpContainer.setHeight(int(keysContainer[2].getWidth() / 12))
	sizeUpContainer.setMargin(int(keys[j].getWidth() / 3))

	sizeUpLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 2))

	closeBtnContainer.setWidth(int(keysContainer[2].getWidth() / 12))
	closeBtnContainer.setHeight(int(keysContainer[2].getWidth() / 12))
	closeBtnContainer.setMargin(int(closeBtnContainer.getWidth() / 4))

	closeLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 2))

def sizeDownScript():
	global keyboardWindow
	global dragWidget
	global keyboardWidget
	global textWidget
	global textBox
	global listBox
	global keysWidget
	global textLabel
	global keysContainer
	global keys
	global backspaceKey
	global backspaceBtn
	global commaKey
	global commaBtn
	global fullstopkey
	global fullstopBtn
	global quoteKey
	global quoteBtn
	global spaceKey
	global spaceKeyBtn
	global sizeUpContainer
	global sizeUpLbl
	global sizeDownContainer
	global sizeDownLbl
	global closeBtnContainer
	global closeLbl
	global keysBtn
	global clearKey
	global clearKeyBtn
	global goBtnContainer
	global goLbl

	global keyboardContainerwidth
	global keyboardContainerheight
	global fontsize
	global keyboardWindowx
	global keyboardWindowy
	global searchCityInfo
	global searchCountryInfo
	global infoContainer
	global infoCityLbl
	global infoCountryLbl
	global countryNameLbl
	global countryNameContainer
	global cityListContainer
	global cityListLbl

	if ((keyboardContainerwidth - int(853.75) >= 3415)):
		keyboardContainerwidth -= int(853.75)
	if ((keyboardContainerheight - 384) >= 1536):
		keyboardContainerheight -= int(384)
	
	fontsize = int(keyboardContainerheight / 27)
	if (keyboardWindowx + (keyboardContainerwidth + int(keyboardContainerheight / 13)) > 1366 * 18):
		keyboardWindowx = 1366 * 18 - (keyboardContainerwidth + int(keyboardContainerheight / 13))

	if (keyboardWindowy + (keyboardContainerheight + int(keyboardContainerheight / 10) + int(keyboardContainerheight / 5)) > 768 * 4):
		keyboardWindowy = 768 * 4 - (keyboardContainerheight + int(keyboardContainerheight / 10) + int(keyboardContainerheight / 5))

	keyboardWindow.setWidth(keyboardContainerwidth + int(keyboardContainerheight / 13))
	keyboardWindow.setHeight(keyboardContainerheight + int(keyboardContainerheight / 10) + int(keyboardContainerheight / 5))
	keyboardWindow.setPosition(Vector2(keyboardWindowx,keyboardWindowy))

	dragWidget.setWidth(keyboardWindow.getWidth())
	dragWidget.setHeight(int(keyboardContainerheight / 5))
	dragWidget.setPadding(int(keyboardContainerheight / 250))

	keyboardWidget.setWidth(keyboardContainerwidth)
	keyboardWidget.setHeight(keyboardContainerheight)

	textWidget.setWidth(int(keyboardWidget.getWidth() / 4))
	textWidget.setHeight(keyboardWidget.getHeight())

	textBox.setWidth(int((textWidget.getWidth() * 5) / 6))
	textBox.setHeight(int((textWidget.getHeight() * 12) / 132))

	textLabel.setFont('data/fonts/Arial.ttf ' + str(fontsize))

	goBtnContainer.setWidth(int(textWidget.getWidth() / 6))
	goBtnContainer.setHeight(int((textWidget.getHeight() * 12) / 132))
	goBtnContainer.setMargin(int(goBtnContainer.getHeight() / 3))

	goLbl.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	listBox.setWidth(int((textWidget.getWidth() * 5) / 6))
	listBox.setHeight(int((textWidget.getHeight() * 96) / 132))

	for i in range(7):
		cityListContainer[i].setWidth(int((textWidget.getWidth() * 5.5) / 6))
		cityListContainer[i].setHeight(int((textWidget.getHeight() * 12) / 132))

		cityListLbl[i].setFont('data/fonts/Arial.ttf ' + str(fontsize))

	infoContainer.setWidth(int((textWidget.getWidth() * 5.5) / 6))
	infoContainer.setHeight(int((textWidget.getHeight() * 12) / 132))
	
	infoCityLbl.setText(searchCityInfo)
	infoCityLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 3 / 4))

	infoCountryLbl.setText(searchCountryInfo)
	infoCountryLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 3 / 4))

	countryNameContainer.setWidth(int((textWidget.getWidth() * 5.5) / 6))
	countryNameContainer.setHeight(int((textWidget.getHeight() * 12) / 132))
	
	countryNameLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize))

	keysWidget.setWidth(int((keyboardWidget.getWidth() * 3) / 4))
	keysWidget.setHeight(keyboardWidget.getHeight())
	keysWidget.setMargin(int(keysWidget.getHeight() / 20))
	keysWidget.setPadding(int(keysWidget.getHeight() / 20))

	i = 0
	j = 0
	for i in range(4):
		keysContainer[i].setWidth(int((keysWidget.getWidth() * 5) / 6))
		keysContainer[i].setHeight(int((keysWidget.getHeight() * 2) / 9))
		keysContainer[i].setPadding(int(keysWidget.getWidth() / 70))

	for j in range(26):
		if(j <= 9):
			keys[j].setWidth(int(keysContainer[2].getWidth() / 12))
			keys[j].setHeight(int(keysContainer[2].getWidth() / 12))
			keys[j].setMargin(int(keys[j].getWidth() / 2))

			keysBtn[j].getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

		elif(j >= 10 and j <= 18):
			keys[j].setWidth(int(keysContainer[2].getWidth() / 12))
			keys[j].setHeight(int(keysContainer[2].getWidth() / 12))
			keys[j].setMargin(int(keys[j].getWidth() / 2))

			keysBtn[j].getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

		elif(j >= 19 and j <= 25):
			keys[j].setWidth(int(keysContainer[2].getWidth() / 12))
			keys[j].setHeight(int(keysContainer[2].getWidth() / 12))
			keys[j].setMargin(int(keys[j].getWidth() / 2))

			keysBtn[j].getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	backspaceKey.setWidth(int(keysContainer[2].getWidth() * 2 / 12))
	backspaceKey.setHeight(int(keysContainer[2].getWidth() / 12))
	backspaceKey.setMargin(int(backspaceKey.getHeight() / 2))

	backspaceBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	quoteKey.setWidth(int(keysContainer[1].getWidth() / 12))
	quoteKey.setHeight(int(keysContainer[1].getWidth() / 12))
	quoteKey.setHorizontalAlign(HAlign.AlignCenter)

	quoteBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# comma Key
	commaKey.setWidth(int(keysContainer[1].getWidth() / 12))
	commaKey.setHeight(int(keysContainer[1].getWidth() / 12))
	commaKey.setMargin(int(commaKey.getWidth() / 2))

	commaBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# full stop key
	fullstopkey.setWidth(int(keysContainer[2].getWidth() / 12))
	fullstopkey.setHeight(int(keysContainer[2].getWidth() / 12))
	fullstopkey.setMargin(int(fullstopkey.getWidth() / 2 ))

	fullstopBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	# space key
	spaceKey.setWidth(int((keysContainer[2].getWidth() * 6) / 12))
	spaceKey.setHeight(int(keysContainer[2].getWidth() / 12))

	clearKey.setWidth(int((keysContainer[2].getWidth() * 2) / 12))
	clearKey.setHeight(int(keysContainer[2].getWidth() / 12))

	clearKeyBtn.getLabel().setFont('data/fonts/Arial.ttf ' + str(fontsize))

	sizeDownContainer.setWidth(int(keysContainer[2].getWidth() / 12))
	sizeDownContainer.setHeight(int(keysContainer[2].getWidth() / 12))
	sizeDownContainer.setMargin(int(keys[j].getWidth() / 2))

	sizeDownLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 3))

	sizeUpContainer.setWidth(int(keysContainer[2].getWidth() / 12))
	sizeUpContainer.setHeight(int(keysContainer[2].getWidth() / 12))
	sizeUpContainer.setMargin(int(keys[j].getWidth() / 3))

	sizeUpLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 2))

	closeBtnContainer.setWidth(int(keysContainer[2].getWidth() / 12))
	closeBtnContainer.setHeight(int(keysContainer[2].getWidth() / 12))
	closeBtnContainer.setMargin(int(closeBtnContainer.getWidth() / 4))

	closeLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize * 2))

def startkeyboardMovement():
	global dragWidgetPressed
	global keyboard_XstartOffset
	global keyboard_YstartOffset
	laserPos = []
	

	dragWidgetPressed = True

	keyboardPosition = keyboardWindow.getPosition()
	laserPos = laser.getCenter()

	keyboard_XstartOffset = laserPos[0] - keyboardPosition[0]
	keyboard_YstartOffset = laserPos[1] - keyboardPosition[1]

	# hitPos = laser.getCenter()
	# keyboardPosition = keyboardWindow.getPosition()
	# keyboardWindowx = keyboardPosition[0]
	# keyboardWindowy = keyboardPosition[1]

	# keyboard_XstartOffset = hitPos[0] - keyboardWindowx
	# keyboard_YstartOffset = hitPos[1] - keyboardWindowy
	# keyboard_XendOffset = keyboardContainerwidth + int(keyboardContainerheight / 13) - hitPos[0]
	# keyboard_YendOffset = keyboardContainerheight + int(keyboardContainerheight / 10) + int(keyboardContainerheight / 5) - hitPos[1]



def stopKeyboardMovement():
	global dragWidgetPressed

	dragWidgetPressed = False

def updateKeyboardMovement():
	global dragWidgetPressed
	global laser
	global keyboardWindow
	global keyboard_XstartOffset
	global keyboard_YstartOffset

	laserPos = []

	laserPos = laser.getCenter()

	if dragWidgetPressed:
		keyboardWindow.setPosition(Vector2(laserPos[0] - keyboard_XstartOffset,laserPos[1] - keyboard_YstartOffset))

def readCitycsv():
	global cityDict
	global autoCompleteOptions

	tempItem = []
	countrydata = {}
	key = None
	count = 0

	with open("data/countryCode.csv", "rU") as data:
		rows = csv.reader(data)
		for row in rows:
			countryName = str(row[0]).lower()
			countryCode = str(row[1]).lower()

			if(countrydata):
				if countryCode in countrydata:
					print countryCode + ' already there'
				else:
					countrydata[countryCode] = countryName
			else:
				countrydata[countryCode] = countryName

	with open("data/worldcitiespop.csv", "rU") as data:
		rows = csv.reader(data)
		for row in rows:
			country = str(row[0]).lower()
			city = str(row[2]).lower()
			state = str(row[3]).lower()
			lat = str(row[5])
			lon = str(row[6])
			population = str(row[4]).strip()

			if not population:
				population = 0
			else:
				population = int(population)

			if population > 50000:
				if country in countrydata:
					countryFull = countrydata[country]
					key = city.strip() +', ' + countryFull.strip()
					autoCompleteOptions.append(key)
					tempItem =[city, state, country, countryFull, population, lat, lon]
					count += 1

				if (cityDict):
					if key in cityDict:
						# print key + 'already exists'
						pass
					else:
						cityDict[key] = tempItem
				else:
					cityDict[key] = tempItem

	print str(count) + ' records of cities'

def processautoComplete(searchTxt):
	global listCount
	global autoCompleteList
	global searchTextPrevLen
	global searchTextCurrLen
	global autoCompleteDict
	global currentCountryIndex

	searchTxt = searchTxt.lower()
	searchTxt = searchTxt.strip()

	# --------------------
	# print elements starting with searchText
	# call this module everytime the length of i/p string changes
	if not searchTxt:
		autoCompleteList = []
	else:
		if ((searchTextPrevLen == 0 and searchTextCurrLen == 1) or (searchTextPrevLen > searchTextCurrLen)):
			for i in range(len(autoCompleteOptions)):
				if autoCompleteOptions[i].startswith(searchTxt):
					autoCompleteList.append(autoCompleteOptions[i])
					currentCountryIndex = 0
		else:
			for i in range(len(autoCompleteList)):
				if autoCompleteList[i].startswith(searchTxt):
					autoCompleteList.append(autoCompleteList[i])
					currentCountryIndex = 0


	autoCompleteList = autoCompleteList[listCount:]

	listCount = len(autoCompleteList)
	autoCompleteDict = {}

	if listCount > 0 :
		for i in range(listCount):
			keyCol = autoCompleteList[i].split(',')

			keyCol[1] = keyCol[1].strip()

			# print keyCol[1] + ' ' + autoCompleteList[i]

			if autoCompleteDict:
				if keyCol[1] in autoCompleteDict:
					tempList = autoCompleteDict[keyCol[1]]
					tempList.append(autoCompleteList[i])
					autoCompleteDict[keyCol[1]] = tempList
				else:
					tempList = []
					tempList.append(autoCompleteList[i])
					autoCompleteDict[keyCol[1]] = tempList
			else:
				tempList = []
				tempList.append(autoCompleteList[i])
				autoCompleteDict[keyCol[1]] = tempList
	else:
		autoCompleteDict = {}

	# countryKeyList = autoCompleteDict.keys()
	# print '------------------------------------------------------'
	# print countryKeyList
	# print currentCountryIndex
	# print '------------------------------------------------------'
	

def updateAutocompleteContainers():
	global countryNameLbl
	global countryKeyList
	global currentCountryIndex
	global currentCityBucket
	global fontsize
	global isMoreCity
	global autoCompleteDict
	global infoLbl
	global searchInfo
	global cityListContainer
	global cityListLbl
	global citystartIdx
	global cityendIdx
	global cityTotalBucket

	cityList = []

	if autoCompleteDict:
		listBox.setVisible(True)
		countryKeyList = autoCompleteDict.keys()
		cityList = autoCompleteDict[countryKeyList[currentCountryIndex]]

		# if len(cityList) > 7:
		# 	isMoreCity = True
		# 	print isMoreCity
		# else:
		# 	isMoreCity = False
		# 	print isMoreCity
		
		countryNameLbl.setText(countryKeyList[currentCountryIndex].title())
		countryNameLbl.setFont('data/fonts/Arial.ttf ' + str(fontsize))

		cityTotalBucket = len(cityList) / 7 
		
		# handle more than 7 cities
		if currentCityBucket <= cityTotalBucket:
			citystartIdx = currentCityBucket * 7

		if currentCityBucket + 1 <= cityTotalBucket:
			cityendIdx = ((currentCityBucket + 1) * 7)
		else:
			cityendIdx = len(cityList)

		# print '---------------------update Container -------------------------'
		# print 'cityTotalBucket = ' + str(cityTotalBucket) + ', ' + 'currentCityBucket = ' + str(currentCityBucket)
		# print 'citystartIdx = ' +str(citystartIdx) + ', ' + 'cityendIdx = ' + str(cityendIdx)
		# print cityList
		# print '---------------------------------------------------------------'

			
		for cityIdx in range(citystartIdx,cityendIdx):
			cityListContainer[cityIdx % 7].setVisible(True)
			cityListLbl[cityIdx % 7].setText(cityList[cityIdx].title())

		if ((currentCityBucket == cityTotalBucket) and (cityendIdx < ((currentCityBucket + 1) * 7))):
			for cityIdx in range(cityendIdx, ((currentCityBucket + 1) * 7)):
				cityListLbl[cityIdx % 7].setText('')
				cityListContainer[cityIdx % 7].setVisible(False)
		
		if cityTotalBucket > 0:
			searchCityInfo = str(citystartIdx) + ' - ' + str(cityendIdx) + ' / ' + str(len(cityList))+ ' ' + 'Cities'
			searchCountryInfo = str(currentCountryIndex + 1) + ' / ' + str(len(countryKeyList)) + ' Countries'
		else:
			searchCityInfo = str(len(cityList))+ ' ' + 'Cities'
			searchCountryInfo = str(currentCountryIndex + 1) + ' / ' + str(len(countryKeyList)) + ' Countries'

		infoCityLbl.setText(searchCityInfo)
		infoCountryLbl.setText(searchCountryInfo)
	else:
		searchCountryInfo = ''
		searchCityInfo = 'No Results'
		infoCityLbl.setText(searchCityInfo)
		infoCountryLbl.setText(searchCountryInfo)
		listBox.setVisible(False)



def goToSelectedCity(passedCity):
	global cityDict
	global recentLocationList
	global boolCitySelected
	global cam
	global max_no_recentCity
	global recentlyVisitedParentContainer

	cityInfoList = []
	responseDict = {}
	lat = None
	lon = None
	country = None
	district = None
	locality = None
	address = None

	targetPos = None
	lookatPoint = None
	qold = None
	oldPos = None
	qnew = None

	geodeticlist = []
	latstart = None
	longistart = None
	passedCity = passedCity.lower()
	key = 0

	if boolCitySelected:
		if passedCity in cityDict.keys():
			cityInfoList = cityDict[passedCity]

			lat = cityInfoList[5]
			lon = cityInfoList[6]
			locality = cityInfoList[0]
			district = cityInfoList[1]
			country = cityInfoList[3]

			targetPos = geodetic2ecef(lat, lon, 300)
			lookatPoint = geodetic2ecef(lat, lon, 0)
			
			# get the old position and orientation
			qold = cam.getOrientation()
			oldPos = cam.getPosition()
			
			# set the new position and look at the City. Get the new orientation
			cam.setPosition(Vector3(float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
			cam.lookAt(Vector3(float(lookatPoint[0]), float(lookatPoint[1]), float(lookatPoint[2])), Vector3(0.0, 1.0, 0.0))
			qnew = cam.getOrientation()

			# Restore the old camera position and orientation
			cam.setPosition(Vector3(float(oldPos[0]), float(oldPos[1]), float(oldPos[2])))
			cam.setOrientation(qold)

			#Use oldPos to get (latstart, longistart) and function arguments to get target (latend,longiend)
			geodeticlist = ecef2geodetic(float(oldPos[0]),float(oldPos[1]),float(oldPos[2]))
			latstart = float(geodeticlist[0])
			longistart = float(geodeticlist[1])

			cityInfoList = [lat, lon, district, country,locality, address, targetPos, qnew, lookatPoint]
			cam.setPosition(Vector3( float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
			cam.setOrientation(qnew)

		else:
			responseDict = getLocationbyQuery(passedCity)
			if responseDict:
				if key in responseDict.keys():
					cityInfoList = responseDict[key]
					lat,lon,district,country,locality,address = cityInfoList
					lat = float(lat)
					lon = float(lon)
					district = district.strip()
					country = country.strip()
					locality = locality.strip()
					address = address.strip()

					#convert lat-lon-alt to cartesian using coordinate Convertor 
					targetPos = geodetic2ecef(lat, lon, 300)
					lookatPoint = geodetic2ecef(lat, lon, 0)

					# get the old position and orientation
					qold = cam.getOrientation()
					oldPos = cam.getPosition()
					# set the new position and look at the City. Get the new orientation
					cam.setPosition(Vector3(float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
					cam.lookAt(Vector3(float(lookatPoint[0]), float(lookatPoint[1]), float(lookatPoint[2])), Vector3(0.0, 1.0, 0.0))
					qnew = cam.getOrientation()
					# Restore the old camera position and orientation
					cam.setPosition(Vector3(float(oldPos[0]), float(oldPos[1]), float(oldPos[2])))
					cam.setOrientation(qold)

					#Use oldPos to get (latstart, longistart) and function arguments to get target (latend,longiend)
					geodeticlist = ecef2geodetic(float(oldPos[0]),float(oldPos[1]),float(oldPos[2]))
					latstart = float(geodeticlist[0])
					longistart = float(geodeticlist[1])

					cityInfoList = [lat, lon, district, country,locality, address, targetPos, qnew, lookatPoint]
					cam.setPosition(Vector3( float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
					cam.setOrientation(qnew)

	else:
		responseDict = getLocationbyQuery(passedCity)
		if responseDict:
			if key in responseDict.keys():
				cityInfoList = responseDict[key]
				lat,lon,district,country,locality,address = cityInfoList
				lat = float(lat)
				lon = float(lon)
				district = district.strip()
				country = country.strip()
				locality = locality.strip()
				address = address.strip()

				#convert lat-lon-alt to cartesian using coordinate Convertor 
				targetPos = geodetic2ecef(lat, lon, 300)
				lookatPoint = geodetic2ecef(lat, lon, 0)

				# get the old position and orientation
				qold = cam.getOrientation()
				oldPos = cam.getPosition()
				# set the new position and look at the City. Get the new orientation
				cam.setPosition(Vector3(float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
				cam.lookAt(Vector3(float(lookatPoint[0]), float(lookatPoint[1]), float(lookatPoint[2])), Vector3(0.0, 1.0, 0.0))
				qnew = cam.getOrientation()
				# Restore the old camera position and orientation
				cam.setPosition(Vector3(float(oldPos[0]), float(oldPos[1]), float(oldPos[2])))
				cam.setOrientation(qold)

				#Use oldPos to get (latstart, longistart) and function arguments to get target (latend,longiend)
				geodeticlist = ecef2geodetic(float(oldPos[0]),float(oldPos[1]),float(oldPos[2]))
				latstart = float(geodeticlist[0])
				longistart = float(geodeticlist[1])

				cityInfoList = [lat, lon, district, country,locality, address, targetPos, qnew, lookatPoint]

				cam.setPosition(Vector3( float(targetPos[0]), float(targetPos[1]), float(targetPos[2])))
				cam.setOrientation(qnew)

	if recentLocationList:
		if len(recentLocationList) < max_no_recentCity:
			recentlyVisitedParentContainer.setStyleValue('border', '0')
			recentLocationList.append(cityInfoList)
			# print '--------------------recentlyVisited city--------------------'
			# print recentLocationList
		else:
			recentlyVisitedParentContainer.setStyleValue('border', '4 #FF4500')
			# print 'delete one of the cities'
	else:
		recentLocationList.append(cityInfoList)

	updateRecentlyVisitedContainers()

	boolCitySelected = False

def resetCamera():
	global cam
	global orientOriginal

	cam.setPosition(Vector3(195825.80, -7498234.13, 7039488.51))
	cam.setOrientation(orientOriginal)

def loadLaserPointer():
	global uim
	global laser
	
	laser = Image.create(uim.getUi())
	laser.setData(loadImage("data/textures/laser_dot.png"))
	laser.setCenter(Vector2(100, 100))
	laser.setVisible(False)

def setPin(isHit, hitPosition):
	global cam
	global pinnedLocationList
	global max_no_pinnedCity
	global pinnedParentContainer
	
	dummyDist = None
	dummyDist = math.sqrt((float(hitPosition[0]) * float(hitPosition[0])) + (float(hitPosition[1]) * float(hitPosition[1])) + (float(hitPosition[2]) * float(hitPosition[2])))
	print str(dummyDist) + ' m'
	# camDistance = camDistCalc(cam)
	# print camDistance


	pinCount = 0
	pointInfoList = {}
	tempList = []
	tempPinnedList = []
	qold = None

	hitPositionLocal = cam.convertWorldToLocalPosition(hitPosition)
	linesegmentLocal = hitPositionLocal + Vector3(0.0,50.0,0.0)
	linesegmentWorld = cam.convertLocalToWorldPosition(linesegmentLocal)
	
	if isHit:
		print 'Set Pin Module len(pinnedList) = ' + str(len(pinnedLocationList)) + ' max_no_pinnedCity ='+str(max_no_pinnedCity)
		if (len(pinnedLocationList) < max_no_pinnedCity):
			pinnedParentContainer.setStyleValue('border', '0')
			sphere = SphereShape.create(18, 5)
			sphere.setPosition(linesegmentWorld)
			sphere.setEffect("colored -d red")

			lines = LineSet.create()
			linesegment = lines.addLine()
			linesegment.setStart(hitPosition)
			linesegment.setEnd(linesegmentWorld)
			linesegment.setThickness(4)
			lines.getMaterial().setColor(Color('#A0A0A0'), Color('#A0A0A0'))

			latlong = ecef2geodetic(float(hitPosition[0]),float(hitPosition[1]),float(hitPosition[2]))
			print 'latlong ' + str(latlong[0]) + ' ' + str(latlong[1]) + ' ' + str(latlong[2]) + ' m'
			print '-------------------------------convertXYZtolatlonalt----------------------------'
			# samplelatlongalt = convertXYZtolatlonalt(float(hitPosition[0]),float(hitPosition[1]),float(hitPosition[2]))
			# print 'samplelatlongalt ' + str(samplelatlongalt[0]) + ' ' + str(samplelatlongalt[1]) + ' ' + str(samplelatlongalt[2]) + ' m'
			# print str(samplelatlongalt[2]) + ' m'
			lookfromPoint = geodetic2ecef(latlong[0], latlong[1], latlong[2] + 100)


			pointInfoList = getLocationbyPoint(latlong[0], latlong[1])

			qold = cam.getOrientation()
			oldPos = cam.getPosition()

			linesegmentLocal = linesegmentLocal + Vector3(0.0,150.0,0.0)
			pos = cam.convertLocalToWorldPosition(linesegmentLocal)
			cam.setPosition(pos)
			cam.lookAt(linesegmentWorld, Vector3(0.0,1.0,0.0))
			Qnew = cam.getOrientation()


			cam.setPosition(oldPos)
			cam.setOrientation(qold)


			if pointInfoList:
				tempList = pointInfoList[0]
				lati,longi,adminDistrict,country,locality, address = tempList
				tempPinnedList = [lati,longi,adminDistrict,country,locality, address, pos, Qnew]
				pinnedLocationList.append(tempPinnedList)
				print '----------------pinnedLocationList------------------'
				print pinnedLocationList
				print 'count after inserting = ' + str(len(pinnedLocationList))
			else:
				tempList = [latlong[0], latlong[1], '', '', '', '', pos, Qnew]
				pinnedLocationList.append(tempList)
				print '-------------pinnedLocationList adding my own list------------'
				print pinnedLocationList
				print 'count after inserting my own value = ' + str(len(pinnedLocationList))

		else:
			pinnedParentContainer.setStyleValue('border', '4 #FF4500')
			print 'reached Max Pin Limit'

	updatePinnedContainers()

def goToCity(pinList, index):
	global pinnedLocationList
	global cam

	pos = None
	qnew = None

	tempCityList = pinList[index]

	pos = tempCityList[6]
	qnew = tempCityList[7]

	cam.setPosition(Vector3(float(pos[0]), float(pos[1]), float(pos[2])))
	cam.setOrientation(qnew)

def onUpdate(frame, t, dt):
	global orbit_cam
	global wand_pos
	global wand_orient
	global cam
	global sky

	global dragWidgetPressed
	global boolKeyboard

	orbit_cam.updateNavigation(wand_pos,wand_orient,dt)
	
	camDistance = camDistCalc(cam)

	if camDistance < 8000:
		sky.setVisible(True)
	else:
		sky.setVisible(False)
	
	if (camDistance < 0.0 or camDistance < 100.0):
		# print camDistance
		orbit_cam.setTranslationSpeed(850.0)
	else:
		orbit_cam.setTranslationSpeed(camDistance + math.sqrt(camDistance) + 850.0)

	if boolKeyboard:
		if dragWidgetPressed:
			updateKeyboardMovement()

def handleEvent():
	global scene
	global mm
	global orbit_cam
	global wand_pos
	global wand_orient
	global uiRoot
	global earthHybrid
	global earthAerial
	global earthRoad

	global boolKeyboard
	global keyboardWindow
	global keyboardWindowx
	global keyboardWindowy
	global enabledisableStr
	global keyboardMenu
	global keys
	global searchText
	global textLabel
	global backspaceKey
	global commaKey
	global fullstopkey
	global spaceKey
	global quoteKey
	global cursorLbl
	global listBox
	global keyboardWidget
	global textWidget
	global textBox
	global fontsize
	global infoContainer
	global goBtnContainer

	global clearKey

	global closeBtnContainer
	global sizeUpContainer
	global sizeDownContainer

	global autoCompleteList
	global autoCompleteDict
	global searchTextCurrLen
	global searchTextPrevLen
	global dragWidgetPressed

	global laser
	global countryKeyList
	global currentCountryIndex
	global cityTotalBucket
	global currentCityBucket
	global cityListContainer
	global boolCitySelected

	global recentLocationList
	global pinnedLocationList
	global pinnedParentContainer
	global pinnedCityContainer
	global pinnedCityInfoContainer
	global pinnedCityDelContainer
	global recentlyVisitedParentContainer
	global recentlyVisitedContainer
	global recentlyVisitedInfoContainer
	global recentlyVisitedDelContainer

	global providerCounter
	global isElevationVisible
	global earthHybridwithoutElevation
	global earthAerialwithoutElevation
	global earthRoadwithoutElevation

	keyboardPos = []
	tempList = []
	dummyList = []
	chosenCityIdx = 0
	selectedAutoCompletedCity = ''
	i = 0
	boolprocessautoComplete = True
	keyboardPos = keyboardWindow.getPosition()

	e = getEvent()

	if e.getServiceType() == ServiceType.Pointer:
		if uiRoot.isEventInside(e):
			pos = e.getPosition()
			laser.setCenter(Vector2(pos[0], pos[1]))
			e.setProcessed()

	if e.getServiceType() == ServiceType.Wand:
		if e.isButtonDown(EventFlags.Button7):
			orbit_cam.startNavigation(wand_pos, wand_orient)
			e.setProcessed()
		if e.isButtonUp(EventFlags.Button7):
			orbit_cam.stopNavigation()
			e.setProcessed()
		
		if (boolKeyboard):
			if e.isButtonDown(EventFlags.Button2):
				hitPos = laser.getCenter()
				keyboardWindow.setPosition(Vector2(keyboardPos[0], keyboardPos[1]))
				for i in range(26):
					if (keys[i].hitTest(Vector2(hitPos[0],hitPos[1]))):
						keys[i].setStyleValue('border', '2 #363636')
						textBox.setStyleValue('border', '1 #ffffff')
						searchText += alphabets[i]
						textLabel.setText(searchText)
				if (backspaceKey.hitTest(Vector2(hitPos[0], hitPos[1]))):
					backspaceKey.setStyleValue('border', '2 #363636')
					searchText = searchText[:-1]
					textLabel.setText(searchText)
				elif (commaKey.hitTest(Vector2(hitPos[0], hitPos[1]))):
					commaKey.setStyleValue('border', '2 #363636')
					searchText += ","
					textLabel.setText(searchText)
				elif (quoteKey.hitTest(Vector2(hitPos[0], hitPos[1]))):
					quoteKey.setStyleValue('border', '2 #363636')
					searchText += "'"
					textLabel.setText(searchText)
				elif (spaceKey.hitTest(Vector2(hitPos[0], hitPos[1]))):
					spaceKey.setStyleValue('border', '2 #363636')
					searchText += ' '
					textLabel.setText(searchText)
				elif (fullstopkey.hitTest(Vector2(hitPos[0], hitPos[1]))):
					fullstopkey.setStyleValue('border', '2 #363636')
					searchText += '.'
					textLabel.setText(searchText)
				elif (closeBtnContainer.hitTest(Vector2(hitPos[0], hitPos[1]))):
					keyboardWindow.setVisible(False)
					searchText = ''
					boolKeyboard = not boolKeyboard
					enabledisableStr = 'Enable Keyboard'
					textLabel.setText(searchText)
					keyboardMenu.getButton().setText(enabledisableStr)
				elif (sizeUpContainer.hitTest(Vector2(hitPos[0], hitPos[1]))):
					sizeUpContainer.setStyleValue('border', '2 #363636')
					sizeUpScript()
				elif (sizeDownContainer.hitTest(Vector2(hitPos[0], hitPos[1]))):
					sizeDownContainer.setStyleValue('border', '2 #363636')
					sizeDownScript()
				elif (dragWidget.hitTest(Vector2(hitPos[0], hitPos[1]))):
					startkeyboardMovement()
					dragWidget.setStyleValue('fill', '#787878')
				elif (clearKey.hitTest(Vector2(hitPos[0], hitPos[1]))):
					clearKey.setStyleValue('border', '2 #363636')
					searchText = ''
					textLabel.setText(searchText)
				else:
					pass

				if searchText.strip():
					if (goBtnContainer.hitTest(Vector2(hitPos[0], hitPos[1]))):
						goToSelectedCity(searchText)
				else:
					if (goBtnContainer.hitTest(Vector2(hitPos[0], hitPos[1]))):
						textBox.setStyleValue('border', '3 #ff0000')

				if (listBox.isVisible()):
					j = 0
					for j in range(7):
						if (cityListContainer[j].isVisible()):
							if(cityListContainer[j].hitTest(Vector2(hitPos[0], hitPos[1]))):
								chosenCityIdx = currentCityBucket * 7 + j
								tempCityList = autoCompleteDict[countryKeyList[currentCountryIndex]]
								selectedAutoCompletedCity = tempCityList[chosenCityIdx]
								searchText = selectedAutoCompletedCity
								textLabel.setText(searchText.title())
								boolCitySelected = True
								boolprocessautoComplete = False

				if not searchText:
					listBox.setVisible(False)
					infoContainer.setVisible(False)
				else:
					listBox.setVisible(True)
					infoContainer.setVisible(True)
					searchTextCurrLen = len(searchText)
					if boolprocessautoComplete:
						processautoComplete(searchText)
						updateAutocompleteContainers()
					else:
						pass


				searchTextPrevLen = len(searchText)
				e.setProcessed()

			if e.isButtonUp(EventFlags.Button2):
				for i in range(26):
						keys[i].setStyleValue('border', '2 #ffffff')
				backspaceKey.setStyleValue('border', '2 #ffffff')
				commaKey.setStyleValue('border', '2 #ffffff')
				quoteKey.setStyleValue('border', '2 #ffffff')
				spaceKey.setStyleValue('border', '2 #ffffff')
				fullstopkey.setStyleValue('border', '2 #ffffff')
				sizeUpContainer.setStyleValue('border', '2 #ffffff')
				sizeDownContainer.setStyleValue('border', '2 #ffffff')
				clearKey.setStyleValue('border', '2 #ffffff')

				if dragWidgetPressed:
					stopKeyboardMovement()
					dragWidget.setStyleValue('fill', '#C0C0C0')

				e.setProcessed()

			if e.isButtonDown(EventFlags.ButtonRight):
				if autoCompleteDict:
					tempKeyCount = len(autoCompleteDict) - 1
					if tempKeyCount == currentCountryIndex:
						currentCountryIndex = 0
					else:
						currentCountryIndex += 1
					
					currentCityBucket = 0
					updateAutocompleteContainers()
					
				e.setProcessed()

			if e.isButtonDown(EventFlags.ButtonLeft):
				if autoCompleteDict:
					tempKeyCount = len(autoCompleteDict) - 1
					if currentCountryIndex == 0:
						currentCountryIndex = tempKeyCount
					else:
						currentCountryIndex -= 1

					currentCityBucket = 0
					updateAutocompleteContainers()
					
				e.setProcessed()

			if e.isButtonDown(EventFlags.ButtonDown):
				if autoCompleteDict:
					if currentCityBucket == cityTotalBucket:
						currentCityBucket = cityTotalBucket
					else:
						currentCityBucket += 1
					# print 'Button Down Pressed. CityCurrentBucket = ' + str(currentCityBucket)
					updateAutocompleteContainers()
				e.setProcessed()

			if e.isButtonDown(EventFlags.ButtonUp):
				if autoCompleteDict:
					if currentCityBucket == 0:
						currentCityBucket = 0
					else:
						currentCityBucket -= 1
					# print 'Button up Pressed. CityCurrentBucket = ' + str(currentCityBucket)
					updateAutocompleteContainers()
				e.setProcessed()

			# if e.isButtonDown(EventFlags.Button3):
			# 	hitPos = laser.getCenter()
			# 	if (listBox.isVisible()):
			# 		j = 0
			# 		for j in range(7):
			# 			if (cityListContainer[j].isVisible()):
			# 				if(cityListContainer[j].hitTest(Vector2(hitPos[0], hitPos[1]))):
			# 					chosenCityIdx = currentCityBucket * 7 + j
			# 					tempCityList = autoCompleteDict[countryKeyList[currentCountryIndex]]
			# 					selectedAutoCompletedCity = tempCityList[chosenCityIdx]
			# 					searchText = selectedAutoCompletedCity
			# 					textLabel.setText(searchText.title())
			# 					boolCitySelected = True

			# 	e.setProcessed()
		else:
			if e.isButtonDown(EventFlags.ButtonRight):
				if (providerCounter < 2):
					providerCounter += 1
				elif (providerCounter == 2):
					providerCounter = 0
				changeProvider()

			if e.isButtonDown(EventFlags.ButtonLeft):
				if (providerCounter > 0):
					providerCounter -= 1
				elif (providerCounter == 0):
					providerCounter = 2
				changeProvider()


		if e.isButtonDown(EventFlags.Button5):
			r = getRayFromEvent(e)
			if isElevationVisible:
				if (providerCounter % 3 == 0):
					hitData = hitNode(earthHybrid, r[1], r[2])
					print 'Target - hit Hybrid mode...........................' + str(hitData[0])
					setPin(hitData[0], hitData[1])
				elif (providerCounter % 3 == 1):
					hitData = hitNode(earthAerial, r[1], r[2])
					print 'Target - hit Aerial Mode...........................' + str(hitData[0])
					setPin(hitData[0], hitData[1])
				elif (providerCounter % 3 == 2):
					hitData = hitNode(earthRoad, r[1], r[2])
					print 'Target - hit Road Mode...........................' + str(hitData[0])
					setPin(hitData[0], hitData[1])
			else:
				if (providerCounter % 3 == 0):
					hitData = hitNode(earthHybridwithoutElevation, r[1], r[2])
					print 'Target - hit Hybrid mode...........................' + str(hitData[0])
					setPin(hitData[0], hitData[1])
				elif (providerCounter % 3 == 1):
					hitData = hitNode(earthAerialwithoutElevation, r[1], r[2])
					print 'Target - hit Aerial Mode...........................' + str(hitData[0])
					setPin(hitData[0], hitData[1])
				elif (providerCounter % 3 == 2):
					hitData = hitNode(earthRoadwithoutElevation, r[1], r[2])
					print 'Target - hit Road Mode...........................' + str(hitData[0])
					setPin(hitData[0], hitData[1])
			e.setProcessed()

		if pinnedParentContainer.isVisible() or recentlyVisitedParentContainer.isVisible():
			if e.isButtonDown(EventFlags.Button3):
				hitPos = laser.getCenter()
				for i in range(len(pinnedLocationList)):
					if pinnedCityContainer[i].isVisible():
						if pinnedCityDelContainer[i].hitTest(Vector2(hitPos[0], hitPos[1])):
							dummyList = deleteElementFromList(pinnedLocationList, i)
							print '----pinned list after deleting element--------' + str(i)
							print dummyList
							updatePinnedContainers()

						if pinnedCityInfoContainer[i].hitTest(Vector2(hitPos[0], hitPos[1])):
							goToCity(pinnedLocationList, i)

				for j in range(len(recentLocationList)):
					if recentlyVisitedContainer[j].isVisible():
						# print 'Recently Visited Delete Button Visible'
						if recentlyVisitedDelContainer[j].hitTest(Vector2(hitPos[0], hitPos[1])):
							# print 'Recently Visited delete Button hit ' + str(j)
							dummyList = deleteElementFromList(recentLocationList, j)
							# print '---------recent list after deleting element------' + str(j)
							# print dummyList
							updateRecentlyVisitedContainers()

						if recentlyVisitedInfoContainer[j].hitTest(Vector2(hitPos[0], hitPos[1])):
							goToCity(recentLocationList, j)


		# if e.isButtonDown(EventFlags.ButtonRight):
		# 	if (providerCounter < 2):
		# 		providerCounter += 1
		# 	elif (providerCounter == 2):
		# 		providerCounter = 0
		# 	changeProvider()
		# 	e.setProcessed()

		# if e.isButtonDown(EventFlags.ButtonLeft):
		# 	if (providerCounter > 0):
		# 		providerCounter -= 1
		# 	elif (providerCounter == 0):
		# 		providerCounter = 2
		# 	changeProvider()
		# 	e.setProcessed()

	if e.getServiceType() == ServiceType.Mocap:
		if e.getSourceId() == 1:
			wand_pos = e.getPosition()
			wand_orient = e.getOrientation()

			# 2d laser pointer
			keyboardXstart = keyboardPos[0] 
			keyboardYstart = keyboardPos[1]
			keyboardXend = keyboardPos[0] + keyboardContainerwidth
			keyboardYend = keyboardPos[1] + keyboardContainerheight

			screenPosition = CoordinateCalculator()
			refVec = Vector3(0.0,0.0,-1.0)
			v = wand_orient * refVec
			screenPosition.set_position(wand_pos.x, wand_pos.y, wand_pos.z)
			screenPosition.set_orientation(v.x, v.y, v.z)
			screenPosition.calculate()
			screenX = screenPosition.get_x()
			screenY = screenPosition.get_y()
			pixelX = int(screenX * 24588)
			pixelY = int(screenY *  3072)
			laser.setCenter(Vector2(pixelX, pixelY))

			if not laser.isVisible():
				laser.setVisible(True)
			# if (((screenX >= 0.0 and screenX <= 0.333333) or (screenX > 0.666666 and screenX <= 1.0)) and screenY >= 0.0 and screenY <= 1.0) or (screenX > 0.444444 and screenX <= 0.555555 and screenY >= 0.875 and screenY <= 1.0):
			# if (boolKeyboard):
			# 	if not laser.isVisible():
			# 		laser.setVisible(True)
			# 		# scene.hideWand(0)
			# else:
			# 	if (pinnedParentContainer.isVisible() and ((screenX >= 0.0 and screenX <= 0.05555) and (screenY >= 0.0 and screenY <= 1.0))):
			# 		if not laser.isVisible():
			# 			laser.setVisible(True)
			# 	elif (recentlyVisitedParentContainer.isVisible() and ((screenX >= 0.9444 and screenX <= 1.0) and (screenY > 0.0 and screenY <= 1.0))):
			# 		if not laser.isVisible():
			# 			laser.setVisible(True)
			# 	else:
			# 		if laser.isVisible():
			# 			laser.setVisible(False)
		

def camDistCalc(camera):
	d = []
	d0 = None
	d1 = None
	d2 = None
	d = camera.getPosition()
	d0 = float(d[0])
	d1 = float(d[1])
	d2 = float(d[2])
	camDist = math.sqrt(d0*d0 + d1*d1 + d2*d2) - 6378100.0
	
	return camDist

def createCityContainers():
	global pinnedParentContainer
	global recentlyVisitedParentContainer

	global pinnedCityContainer
	global pinnedContainerheight
	global pinnedContainerwidth
	global pinnedCityPinContainer
	global pinnedCityInfoContainer
	global pinnedCityInfoLocalityLbl
	global pinnedCityInfoCountryLbl
	global pinnedCityInfoLatLonLbl
	global pinnedCityDelContainer

	global recentlyVisitedContainer
	global recentContainerWidth
	global recentContainerHeight
	global recentlyVisitedInfoContainer
	global recentlyVisitedInfoLocalityLbl
	global recentlyVisitedInfoCountryLbl
	global recentlyVisitedInfoLatLonLbl
	global recentlyVisitedDelContainer
	
	global uiRoot
	global max_no_pinnedCity
	global max_no_recentCity
	global fontsize

	i = 0
	j = 0

	pinImg = None
	pindelImg = None
	recentdelImg = None

	pinnedParentContainer = Container.create(ContainerLayout.LayoutVertical, uiRoot)
	pinnedParentContainer.setAutosize(True)
	pinnedParentContainer.setPosition(Vector2(0.0,0.0))

	recentlyVisitedParentContainer = Container.create(ContainerLayout.LayoutVertical, uiRoot)
	recentlyVisitedParentContainer.setAutosize(True)
	recentlyVisitedParentContainer.setPosition(Vector2(1366 * 17, 0.0))

	for i in range(max_no_pinnedCity):
		pinnedCityContainer.append(Container.create(ContainerLayout.LayoutHorizontal, pinnedParentContainer))
		pinnedCityContainer[i].setAutosize(False)
		pinnedCityContainer[i].setWidth(int(pinnedContainerwidth))
		pinnedCityContainer[i].setHeight(int(pinnedContainerheight))
		pinnedCityContainer[i].setVerticalAlign(VAlign.AlignMiddle)
		pinnedCityContainer[i].setStyleValue('border' , '2 #ffffff')
		pinnedCityContainer[i].setStyleValue('fill', '#181818')
		pinnedCityContainer[i].setVisible(False)

		pinnedCityPinContainer.append(Container.create(ContainerLayout.LayoutVertical, pinnedCityContainer[i]))
		pinnedCityPinContainer[i].setAutosize(False)
		pinnedCityPinContainer[i].setWidth(int(pinnedContainerwidth / 5))
		pinnedCityPinContainer[i].setHeight(int(pinnedContainerheight))

		pinImg = Image.create(pinnedCityPinContainer[i])
		pinImg.setData(loadImage("data/textures/pin.png"))
		pinImg.setCenter(pinnedCityPinContainer[i].getCenter())

		pinnedCityInfoContainer.append(Container.create(ContainerLayout.LayoutVertical, pinnedCityContainer[i]))
		pinnedCityInfoContainer[i].setAutosize(False)
		pinnedCityInfoContainer[i].setWidth(int(pinnedContainerwidth * 3 / 5))
		pinnedCityInfoContainer[i].setHeight(int(pinnedContainerheight))
		pinnedCityInfoContainer[i].setHorizontalAlign(HAlign.AlignLeft)
		pinnedCityInfoContainer[i].setClippingEnabled(True)
		pinnedCityInfoContainer[i].setPadding(40)

		pinnedCityInfoLocalityLbl.append(Label.create(pinnedCityInfoContainer[i]))
		pinnedCityInfoLocalityLbl[i].setText('')
		pinnedCityInfoLocalityLbl[i].setColor(Color('#C56B3A'))
		pinnedCityInfoLocalityLbl[i].setFont('data/fonts/Arial.ttf ' + str(fontsize))

		pinnedCityInfoCountryLbl.append(Label.create(pinnedCityInfoContainer[i]))
		pinnedCityInfoCountryLbl[i].setText('')
		pinnedCityInfoCountryLbl[i].setColor(Color('#C56B3A'))
		pinnedCityInfoCountryLbl[i].setFont('data/fonts/Arial.ttf ' + str(fontsize))

		pinnedCityInfoLatLonLbl.append(Label.create(pinnedCityInfoContainer[i]))
		pinnedCityInfoLatLonLbl[i].setText('')
		pinnedCityInfoLatLonLbl[i].setColor(Color('#1E90FF'))
		pinnedCityInfoLatLonLbl[i].setFont('data/fonts/Arial.ttf ' + str(int(fontsize * 3 / 4)))

		pinnedCityDelContainer.append(Container.create(ContainerLayout.LayoutVertical, pinnedCityContainer[i]))
		pinnedCityDelContainer[i].setAutosize(False)
		pinnedCityDelContainer[i].setWidth(int(pinnedContainerwidth / 5))
		pinnedCityDelContainer[i].setHeight(int(pinnedContainerheight * 4 / 5))
		# pinnedCityDelContainer[i].setStyleValue('border', '1 #ffffff')

		pindelImg = Image.create(pinnedCityDelContainer[i])
		pindelImg.setData(loadImage("data/textures/delete-icon-white.png"))
		pindelImg.setCenter(pinnedCityDelContainer[i].getCenter())
				
	for j in range(max_no_recentCity):
		recentlyVisitedContainer.append(Container.create(ContainerLayout.LayoutHorizontal, recentlyVisitedParentContainer))
		recentlyVisitedContainer[j].setAutosize(False)
		recentlyVisitedContainer[j].setWidth(int(recentContainerWidth))
		recentlyVisitedContainer[j].setHeight(int(recentContainerHeight))
		recentlyVisitedContainer[j].setVerticalAlign(VAlign.AlignMiddle)
		recentlyVisitedContainer[j].setStyleValue('border', '2 #ffffff')
		recentlyVisitedContainer[j].setStyleValue('fill', '#181818')
		recentlyVisitedContainer[j].setVisible(False)

		recentlyVisitedInfoContainer.append(Container.create(ContainerLayout.LayoutVertical, recentlyVisitedContainer[j]))
		recentlyVisitedInfoContainer[j].setAutosize(False)
		recentlyVisitedInfoContainer[j].setWidth(int(pinnedContainerwidth * 4 / 5))
		recentlyVisitedInfoContainer[j].setHeight(int(pinnedContainerheight))
		recentlyVisitedInfoContainer[j].setHorizontalAlign(HAlign.AlignLeft)
		recentlyVisitedInfoContainer[j].setClippingEnabled(True)
		recentlyVisitedInfoContainer[j].setPadding(40)

		recentlyVisitedInfoLocalityLbl.append(Label.create(recentlyVisitedInfoContainer[j]))
		recentlyVisitedInfoLocalityLbl[j].setText('')
		recentlyVisitedInfoLocalityLbl[j].setColor(Color('#C56B3A'))
		recentlyVisitedInfoLocalityLbl[j].setFont('data/fonts/Arial.ttf ' + str(fontsize))

		recentlyVisitedInfoCountryLbl.append(Label.create(recentlyVisitedInfoContainer[j]))
		recentlyVisitedInfoCountryLbl[j].setText('')
		recentlyVisitedInfoCountryLbl[j].setColor(Color('#C56B3A'))
		recentlyVisitedInfoCountryLbl[j].setFont('data/fonts/Arial.ttf ' + str(fontsize))

		recentlyVisitedInfoLatLonLbl.append(Label.create(recentlyVisitedInfoContainer[j]))
		recentlyVisitedInfoLatLonLbl[j].setText('')
		recentlyVisitedInfoLatLonLbl[j].setColor(Color('#1E90FF'))
		recentlyVisitedInfoLatLonLbl[j].setFont('data/fonts/Arial.ttf ' + str(int(fontsize * 3 / 4)))

		recentlyVisitedDelContainer.append(Container.create(ContainerLayout.LayoutVertical, recentlyVisitedContainer[j]))
		recentlyVisitedDelContainer[j].setAutosize(False)
		recentlyVisitedDelContainer[j].setWidth(int(pinnedContainerwidth / 5))
		recentlyVisitedDelContainer[j].setHeight(int(pinnedContainerheight * 4 / 5))
		# recentlyVisitedDelContainer[j].setStyleValue('border', '1 #ffffff')
		
		recentdelImg = Image.create(recentlyVisitedDelContainer[j])
		recentdelImg.setData(loadImage("data/textures/delete-icon-white.png"))
		recentdelImg.setCenter(recentlyVisitedDelContainer[j].getCenter())

	pinnedParentContainer.setVisible(False)
	recentlyVisitedParentContainer.setVisible(False)



def updatePinnedContainers():
	global pinnedParentContainer
	global pinnedCityContainer
	global pinnedCityInfoLocalityLbl
	global pinnedCityInfoCountryLbl
	global pinnedCityInfoLatLonLbl
	global max_no_pinnedCity
	global pinnedLocationList

	idx = 0
	i = 0
	j = 0
	temp = []

	print '-----------------------Update Pinned Containers -----------------------------'
	print len(pinnedLocationList)
	if len(pinnedLocationList) > 0:
		pinnedParentContainer.setVisible(True)
		pinnedParentContainer.setPosition(Vector2(0.0,0.0))
		for idx in range(len(pinnedLocationList)):
			pinnedCityContainer[idx].setVisible(True)
			temp = pinnedLocationList[idx]
			print 'temp ............'
			print temp[4] + ' , ' + temp[2] + ' , ' + temp[3]
			print str(len(temp[4])) + ' , ' + str(len(temp[2])) + ' , ' + str(len(temp[3]))
			# tempPinnedList = [lati,longi,adminDistrict,countryRegion,locality, address, cam.getPosition(), Qnew]

			# pinnedCityInfoLocalityLbl[idx].setText(temp[4])
			# pinnedCityInfoCountryLbl[idx].setText(temp[3])
			# pinnedCityInfoLatLonLbl[idx].setText(str(temp[0])+ ', ' + str(temp[1]))
			broadcastCommand("onupdatePinnedContainers('" + str(temp[0]) + '/' + str(temp[1]) + '/' + temp[2] + '/' + temp[3] + '/' + temp[4] + '/' + str(idx) + "')")
			
			# if str(temp[4]):
			# 	pinnedCityInfoLocalityLbl[idx].setText(str(temp[4]))
			# else:
			# 	if str(temp[2]):
			# 		pinnedCityInfoLocalityLbl[idx].setText(str(temp[2]))
			# 	else:
			# 		if str(temp[5]):
			# 			pinnedCityInfoLocalityLbl[idx].setText(str(temp[5]))
			# 		else:
			# 			pinnedCityInfoLocalityLbl[idx].setText('')

			# if str(temp[3]):
			# 	pinnedCityInfoCountryLbl[idx].setText(str(temp[3]))
			# else:
			# 	pinnedCityInfoCountryLbl[idx].setText('')

			# if str(temp[0]) or str(temp[1]):
			# 	print str(temp[0])+ ', ' + str(temp[1])
			# 	pinnedCityInfoLatLonLbl[idx].setText(str(temp[0])+ ', ' + str(temp[1]))
			# else:
			# 	pinnedCityInfoLatLonLbl[idx].setText('')
		# broadcastCommand("labelLoader('"+str(temp[0]) + '/' + str(temp[1])+ '/' +str(temp[2])+ '/' +str(temp[3]) +'/'+str(temp[4]) "')")


		if len(pinnedLocationList) < max_no_pinnedCity:
			for i in range(len(pinnedLocationList),max_no_pinnedCity):
				pinnedCityInfoLocalityLbl[i].setText('')
				pinnedCityInfoCountryLbl[i].setText('')
				pinnedCityInfoLatLonLbl[i].setText('')
				pinnedCityContainer[i].setVisible(False)
	else:
		for j in range(len(pinnedLocationList),max_no_pinnedCity):
			pinnedCityInfoLocalityLbl[j].setText('')
			pinnedCityInfoCountryLbl[j].setText('')
			pinnedCityInfoLatLonLbl[j].setText('')
			pinnedCityContainer[j].setVisible(False)
		pinnedParentContainer.setVisible(False)


def onupdatePinnedContainers(containerInfo):
	global pinnedCityInfoLocalityLbl
	global pinnedCityInfoCountryLbl
	global pinnedCityInfoLatLonLbl


	containerInfo = containerInfo.split('/')
	lat,lon,state,country,locality,index = containerInfo

	index = int(index)

	pinnedCityInfoLocalityLbl[index].setText(locality)
	pinnedCityInfoCountryLbl[index].setText(country)
	pinnedCityInfoLatLonLbl[index].setText(lat + ' , ' + lon)

def updateRecentlyVisitedContainers():
	global recentlyVisitedParentContainer
	global recentLocationList
	global recentlyVisitedContainer
	global recentlyVisitedInfoLocalityLbl
	global recentlyVisitedInfoCountryLbl
	global recentlyVisitedInfoLatLonLbl
	global max_no_recentCity

	idx = 0
	i = 0
	j = 0
	recentCities = []


	if len(recentLocationList) > 0:
		recentlyVisitedParentContainer.setVisible(True)
		for idx in range(len(recentLocationList)):
			recentlyVisitedContainer[idx].setVisible(True)
			recentCities = recentLocationList[idx]
			# cityInfoList = [lat, lon, district, country,locality, address, targetPos, lookatPoint, qnew]			# cityInfoList = [locality, district, country, address, qnew, oldPos, targetPos, lookatPoint]
			if recentCities[4]:
				recentlyVisitedInfoLocalityLbl[idx].setText(recentCities[4].title())
			else:
				if recentCities[2]:
					recentlyVisitedInfoLocalityLbl[idx].setText(recentCities[2].title())
				else:
					recentlyVisitedInfoLocalityLbl[idx].setText(recentCities[5].title())
			if recentCities[3]:
				recentlyVisitedInfoCountryLbl[idx].setText(recentCities[3].title())
			else:
				recentlyVisitedInfoCountryLbl[idx].setText('')

			if recentCities[0] or recentCities[1]:
				recentlyVisitedInfoLatLonLbl[idx].setText(str(recentCities[0])+ ', ' + str(recentCities[1]))
			else:
				recentlyVisitedInfoLatLonLbl[idx].setText('')

		if len(recentLocationList) < max_no_recentCity:
			for i in range(len(recentLocationList),max_no_recentCity):
				recentlyVisitedInfoLocalityLbl[i].setText('')
				recentlyVisitedInfoCountryLbl[i].setText('')
				recentlyVisitedInfoLatLonLbl[i].setText('')
				recentlyVisitedContainer[i].setVisible(False)
	else:
		for j in range(len(recentLocationList),max_no_recentCity):
			recentlyVisitedInfoLocalityLbl[j].setText('')
			recentlyVisitedInfoCountryLbl[j].setText('')
			recentlyVisitedInfoLatLonLbl[j].setText('')
			recentlyVisitedContainer[j].setVisible(False)
		recentlyVisitedParentContainer.setVisible(False)

def deleteElementFromList(tempList, idx):
	i = 0

	for i in range(idx, len(tempList) - 1):
		tempList[i] = tempList[i + 1]

	del(tempList[len(tempList) - 1])

	return tempList

def changeProvider():
	global earthHybrid
	global earthAerial
	global earthRoad
	global providerCounter

	global earthAerialwithoutElevation
	global earthHybridwithoutElevation
	global earthRoadwithoutElevation
	global isElevationVisible

	if isElevationVisible:
		if (providerCounter % 3 == 0):
			earthHybrid.setVisible(True)
			earthRoad.setVisible(False)
			earthAerial.setVisible(False)
			earthRoadwithoutElevation.setVisible(False)
			earthHybridwithoutElevation.setVisible(False)
			earthAerialwithoutElevation.setVisible(False)
		elif (providerCounter % 3 == 1):
			earthHybrid.setVisible(False)
			earthAerial.setVisible(True)
			earthRoad.setVisible(False)
			earthRoadwithoutElevation.setVisible(False)
			earthHybridwithoutElevation.setVisible(False)
			earthAerialwithoutElevation.setVisible(False)
		elif (providerCounter % 3 == 2):
			earthHybrid.setVisible(False)
			earthAerial.setVisible(False)
			earthRoad.setVisible(True)
			earthRoadwithoutElevation.setVisible(False)
			earthHybridwithoutElevation.setVisible(False)
			earthAerialwithoutElevation.setVisible(False)

	else:
		if (providerCounter % 3 == 0):
			earthHybrid.setVisible(False)
			earthRoad.setVisible(False)
			earthAerial.setVisible(False)
			earthRoadwithoutElevation.setVisible(False)
			earthHybridwithoutElevation.setVisible(True)
			earthAerialwithoutElevation.setVisible(False)
		elif (providerCounter % 3 == 1):
			earthHybrid.setVisible(False)
			earthAerial.setVisible(False)
			earthRoad.setVisible(False)
			earthRoadwithoutElevation.setVisible(False)
			earthHybridwithoutElevation.setVisible(False)
			earthAerialwithoutElevation.setVisible(True)
		elif (providerCounter % 3 == 2):
			earthHybrid.setVisible(False)
			earthAerial.setVisible(False)
			earthRoad.setVisible(False)
			earthRoadwithoutElevation.setVisible(True)
			earthHybridwithoutElevation.setVisible(False)
			earthAerialwithoutElevation.setVisible(False)
		
def loadStars():
# cant use skybox here because sters need to rotate with the earth
#skybox = Skybox()
#skybox.loadCubeMap("stars2", "png")
#earth.setSkyBox(skybox)

	global earthAerial
	global earthHybrid

	starMag = float(0)
	starX = float(0)
	starY = float(0)
	starZ = float(0)

	stars = SceneNode.create("stars")
	stars.setVisible(False)

        # for now lets start with 4000 stars in the data file

	with open("data/hyparcusxyz_small.csv","rU") as data:
		rows = csv.reader(data)
		for row in rows:
			starMag = float(row[0])
			starX = float(row[1])
			starY = float(row[2])
			starZ = float(row[3])

			# convert x, y, z stars so all stars at distance 100000 away in sphere
			distance = sqrt(starX * starX + starY * starY + starZ * starZ)
			starX = starX / distance * 100000
			starY = starY / distance * 100000
			starZ = starZ / distance * 100000

			# print starMag, starX, starY, starZ

	                # convert star magnitude to object size
			refinedScale = (25 - (starMag + 1.5)) * 3
			if refinedScale < 1:
				refinedScale = 1

			#SphereShape* model = new SphereShape(scene, 0.5f);
			model = SphereShape.create(1, 1)
			model.setEffect("colored -d white -e white");
			model.setPosition(Vector3(starX, starY, starZ))
                        #model.setScale(Vector3(100, 100, 100))
			model.setScale(Vector3(refinedScale, refinedScale, refinedScale))
	       		stars.addChild(model)


	               # should replace the sphere with a shader
                       #model = StaticObject.create("defaultSphere")
                       #model.setScale(Vector3(100, 100, 100))
                       #model.setPosition(Vector3(starX, starY, starZ))
                       #model.setEffect('colored -d white -e white')
                       #stars.addChild(model)

	stars.setScale(Vector3(10000, 10000, 10000))
	earthHybrid.addChild(stars)
	earthAerial.addChild(stars)
	stars.setVisible(True)



# ---------------------------------------------Enter Your Code here---------------------------------------------------

divvyDict = {}

def testDataSphere():
	# global box
	# cartesianList = []
	# # test data  176 m is the elevation of chicago
	# cartesianList = convertlatlonalttoXYZ(41.867172995, -87.625955007, 180.0)

	# print str(cartesianList[0]) + ' ' + str(cartesianList[1]) + ' ' + str(cartesianList[2])
	# box = BoxShape.create(4.0,4.0,4.0)
	# box.setPosition(Vector3(float(cartesianList[0]), float(cartesianList[1]), float(cartesianList[2])))
	# box.setEffect("colored -d #028900")
	# box.getMaterial().setAlpha(0.9)
	loadDivvyData()
	global divvyDict
	keys = []
	valueList = []
	singlevalueList = []
	box = []

	cartesianList = []
	chicagoElevation = 176
	heightDifference = 4.0
	height = 0
	pitchangle = 0
	i = 0
	j = 0
	k = 0
	_totalDocks = 0
	_docksinService = 0
	_docksOutofService = 0
	count = 0
	latitude = None
	longitude = None

	keys = divvyDict.keys()
	for i in range(len(keys)):
		if i == 0 :
			continue
		else:
			if i in divvyDict:
				valueList = divvyDict[i]
				for j in range(len(valueList)):
					singlevalueList = valueList[j]
					height = chicagoElevation
					# [ID, total docks, docks in service, status, lat, lon]
					_totalDocks = int(singlevalueList[1])
					_docksinService = int(singlevalueList[2])
					_docksOutofService = _totalDocks - _docksinService
					latitude = float(singlevalueList[4])
					longitude = float(singlevalueList[5])
					pitchangle = 180.0 - latitude				
					for k in range(_totalDocks):
						height += heightDifference
						cartesianList = convertlatlonalttoXYZ(latitude, longitude, height)
						box.append(BoxShape.create(4.0,4.0,4.0))
						box[count].setPosition(Vector3(float(cartesianList[0]), float(cartesianList[1]), float(cartesianList[2])))
						if k < _docksinService:
							box[count].box.setEffect("colored -d #028900")
						else:
							box[count].box.setEffect("colored -d #7F0104")
						box[count].getMaterial().setAlpha(0.9)
						box[count].pitch(pitchangle)
						count += 1


def loadDivvyData():
	retrievedList = []
	tempList = []
	key = None
	i = 0
	firstLine = True

	with open("Divvy_Bicycle_Stations.csv","rU") as data:
		rows = csv.reader(data)
		for row in rows:
			if firstLine:
				firstLine = False
				continue
			if (str(row[0]) and str(row[3]) and str(row[4]) and str(row[5]) and str(row[6]) and str(row[7])):
				i += 1
				if str(row[5]).lower() == 'in service':
					key = 1
				else:
					key = 0
				tempList = [str(row[0]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7])]
				# tempList = [ID, total docks, docks in service, status, lat, lon]
				if key in divvyDict.keys():
					retrievedList = divvyDict[key]
					retrievedList.append(tempList)
					divvyDict[key] = retrievedList
					retrievedList = []
				else:
					retrievedList.append(tempList)
					divvyDict[key] = retrievedList
					retrievedList = []

	print str(i) + ' line of data in Divvy csv.............................Loaded'



if __name__ == "__main__":
	main()
