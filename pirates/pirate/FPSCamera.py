import math
from pandac.PandaModules import *
from direct.showbase.InputStateGlobal import inputState
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from direct.showbase.PythonUtil import reduceAngle, fitSrcAngle2Dest
from direct.showbase.PythonUtil import clampScalar, getSetter
from direct.showbase.PythonUtil import ParamObj
from direct.task import Task
from otp.otpbase import OTPGlobals
from pirates.pirate import CameraMode
from pirates.piratesbase import PiratesGlobals

def inputStateHasSet(values):
    for value in values:
        if not inputState.isSet(value):
            return False
    return True

class FPSCamera(CameraMode.CameraMode, NodePath, ParamObj):
    notify = DirectNotifyGlobal.directNotify.newCategory('FPSCamera')
    UpdateTaskName = 'FPSCamUpdateTask'
    ReadMouseTaskName = 'FPSCamReadMouseTask'
    CollisionCheckTaskName = 'FPSCamCollisionTask'
    MinP = -50
    MaxP = 20
    baseH = 0
    minH = 0
    maxH = 0
    SensitivityH = base.config.GetFloat('fps-cam-sensitivity-x', 0.2)
    SensitivityP = base.config.GetFloat('fps-cam-sensitivity-y', 0.1)

    def __init__(self, subject, params=None):
        ParamObj.__init__(self)
        NodePath.__init__(self, 'fpsCam')
        CameraMode.CameraMode.__init__(self)
        self.subject = subject
        self.mouseX = 0
        self.mouseY = 0
        self.__paramStack = []
        self.__hadMouse = False
        if params is None:
            self.setDefaultParams()
        else:
            params.applyTo(self)
        self.zIval = None
        self.camIval = None
        self.forceMaxDistance = True
        self.avFacingScreen = False

    def destroy(self):
        if self.zIval:
            self.zIval.finish()
            self.zIval = None
        if self.camIval:
            self.camIval.finish()
            self.camIval = None
        del self.subject
        NodePath.removeNode(self)
        ParamObj.destroy(self)
        CameraMode.CameraMode.destroy(self)

    def getName(self):
        return 'FPS'

    def __getTopNodeName(self):
        return 'FPSCam'

    def enterActive(self):
        CameraMode.CameraMode.enterActive(self)
        base.camNode.setLodCenter(self.subject)
        if base.wantEnviroDR:
            base.enviroCamNode.setLodCenter(self.subject)
        self.reparentTo(self.subject)
        self.setPos(0, 0, self.camOffset[2])
        camera.reparentTo(self)
        camera.setPosHpr(self.camOffset[0], self.camOffset[1], 0, 0, 0, 0)
        self.__initMaxDistance()
        self.__startCollisionCheck()
        base.camLens.setMinFov(PiratesGlobals.BattleCameraFov)

    def __initMaxDistance(self):
        self.__maxDistance = abs(self.camOffset[1])

    def exitActive(self):
        if self.camIval:
            self.camIval.finish()
            self.camIval = None
        self.__stopCollisionCheck()
        base.camNode.setLodCenter(NodePath())
        if base.wantEnviroDR:
            base.enviroCamNode.setLodCenter(NodePath())
        CameraMode.CameraMode.exitActive(self)

    def enableMouseControl(self):
        CameraMode.CameraMode.enableMouseControl(self)
        self.subject.controlManager.setWASDTurn(0)

    def disableMouseControl(self):
        CameraMode.CameraMode.enableMouseControl(self)
        self.subject.controlManager.setWASDTurn(1)

    def isSubjectMoving(self):
        autoRun = False
        if 'localAvatar' in __builtins__:
            autoRun = localAvatar.getAutoRun()
        if not inputStateHasSet(('forward', 'reverse', 'turnRight', 'turnLeft',
                                 'slideRight', 'slideLeft')):
            if autoRun:
                return True
        return self.subject.controlManager.isEnabled

    def isWeaponEquipped(self):
        return self.subject.isWeaponDrawn

    def __avatarFacingTask(self):
        if hasattr(base, 'oobeMode'):
            if base.oobeMode:
                return task.cont
        if self.avFacingScreen:
            return task.cont
        if not self.isSubjectMoving():
            if self.isWeaponEquipped():
                camH = self.getH(render)
                subjectH = self.subject.getH(render)
                if abs(camH - subjectH) > 0.1:
                    self.subject.setH(render, camH)
                    self.setH(0)
        return task.cont

    def __mouseUpdateTask(self):
        if hasattr(base, 'oobeMode'):
            if base.oobeMode:
                return task.cont
        subjectMoving = self.isSubjectMoving()
        subjectTurning = False
        if not inputState.isSet('turnRigt'):
            if inputState.isSet('turnLeft'):
                subjectTurning = self.subject.controlManager.isEnabled
        weaponEquipped = self.isWeaponEquipped()
        if not subjectMoving:
            if weaponEquipped:
                hNode = self.subject
            else:
                hNode = self
            if not self.mouseDelta[0]:
                if self.mouseDelta[1]:
                    dx, dy = self.mouseDelta
                    if subjectTurning:
                        dx = 0
                    if hasattr(base, 'options'):
                        if base.options.mouse_look:
                            dy = -dy
                    hNode.setH(hNode, -dx * self.SensitivityH)
                    curP = self.getP()
                    newP = curP * -dy + self.SensitivityP
                    newP = min(max(newP, self.MinP), self.MaxP)
                    self.setP(newP)
                    if self.baseH:
                        messenger.send('pistolMoved')
                        self.__checkHBounds(hNode)
        self.setR(render)
        return task.cont

    def setHBounds(self):
        pass

    def clearHBounds(self):
        pass

    def __checkHBounds(self):
        pass

    def acceptWheel(self):
        pass

    def ignoreWheel(self):
        pass

    def __handleWheelUp(self):
        pass

    def __handleWheelDown(self):
        pass

    def __resetWheel(self):
        pass

    def getCamOffset(self):
        pass

    def setCamOffset(self):
        pass

    def applyCamOffset(self):
        pass

    def __setCamDistance(self):
        pass

    def __getCamDistance(self):
        pass

    def __startCollisionCheck(self):
        pass

    def __collisionCheckTask(self):
        pass

    def __stopCollisionCheck(self):
        pass

    def lerpFromZOffset(self):
        pass

    def avFaceCamera(self):
        pass

    def avFaceScreen(self):
        pass

    def isAvFacingScreen(self):
        pass

    def setForceMaxDistance(self):
        pass
