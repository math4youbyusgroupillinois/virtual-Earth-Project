from omega import *
from cyclops import *
# from omegaToolKit import *


# mm = None

# mm = MenuManager.createAndInitialize()

# keyboardMenu = mm.getMainMenu().addButton('keyboard', 'setKeyboardVisibility()')

# recentlyVisitedmenu = mm.getMainMenu().addSubMenu("Recently Found")

# savedcityMenu = mm.getMainMenu().addSubMenu("Saved Places")

# resetCamMenu = mm.getMainMenu().addButton("Reset Camera", "resetCamera()")

# def resetCamera():
# 	pass

# def setKeyboardVisibility():
# 	global mm

# 	mm.getMainMenu().hide()

# ---------------------------------------------------------------------------

uim = UiModule.createAndInitialize()
uiRoot = uim.getUi()

# containerRect = Container.create(ContainerLayout.LayoutHorizontal,uiRoot)
# containerRect.setAutosize(True)

# imgPinContainer = Container.create(ContainerLayout.LayoutHorizontal,containerRect)
# imgPinContainer.setAutosize(False)
# imgPinContainer.setWidth(300)
# imgPinContainer.setHeight(400)

# imgPin = Image.create(imgPinContainer)
# imgPin.setData(loadImage("YAGE/EARTHold/data/textures/pin.png"))
# imgPin.setCenter(imgPinContainer.getCenter())


# backspaceKey = Container.create(ContainerLayout.LayoutVertical,containerRect)
# backspaceKey.setAutosize(False)
# backspaceKey.setWidth(400)
# backspaceKey.setHeight(400)
# backspaceKey.setHorizontalAlign(HAlign.AlignLeft)
# backspaceKey.setStyleValue('border', '1 #ffffff')

# imgContainer = Container.create(ContainerLayout.LayoutVertical, containerRect)
# imgContainer.setAutosize(False)
# imgContainer.setWidth(300)
# imgContainer.setHeight(300)
# imgContainer.setStyleValue('border', '1 #ffffff')

# img = Image.create(imgContainer)
# img.setData(loadImage("YAGE/EARTHold/data/textures/delete-icon-white.png"))
# img.setCenter(imgContainer.getCenter())

# Btn = Label.create(backspaceKey)
# Btn.setText(' ')
# Btn.setFont('YAGE/EARTHold/data/fonts/Arial.ttf ' + '36')

# backspaceBtn = Label.create(backspaceKey)
# backspaceBtn.setText('Chicago')
# backspaceBtn.setColor(Color('#C56B3A'))
# backspaceBtn.setFont('YAGE/EARTHold/data/fonts/Arial.ttf ' + '36')

# backspaceLbl = Label.create(backspaceKey)
# backspaceLbl.setText('United States')
# backspaceLbl.setColor(Color('#C56B3A'))
# backspaceLbl.setFont('YAGE/EARTHold/data/fonts/Arial.ttf ' + '36')

# lbl = Label.create(backspaceKey)
# lbl.setText('38.3456456, -73.5456789')
# lbl.setColor(Color('#C56B3A'))
# lbl.setFont('YAGE/EARTHold/data/fonts/Arial.ttf ' + '28')


hud = Container.create(ContainerLayout.LayoutVertical, uim.getUi())
hud.setStyle('fill: #00000080')
l1 = Label.create(hud)
l2 = Label.create(hud)
l3 = Label.create(hud)

l1.setFont('fonts/arial.ttf 20')
l1.setText("Heads up display test")

l2.setFont('fonts/arial.ttf 14')
l2.setText("Camera position:")

l3.setFont('fonts/arial.ttf 14')

# enable 3d mode for the hud container and attach it to the camera.
c3d = hud.get3dSettings()
c3d.enable3d = True
c3d.position = Vector3(0, 2.5, -2.5)
# Rotate the hud a little. Note that rotation needs to be specified 
# as a vector.
c3d.normal = quaternionFromEulerDeg(0,-30,0) * Vector3(0,0,1)
# Scale is the conversion factor between pixels and meters
c3d.scale = 0.004
c3d.node = getDefaultCamera()

print hud.getWidth()
print hud.getHeight()


def onUpdate(frame, time, dt):
    l3.setText(str(getDefaultCamera().getPosition()))
setUpdateFunction(onUpdate)




