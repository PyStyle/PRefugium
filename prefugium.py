# This is the code for OS P/Refugium a Meta-Interface by Kyan Pur-Djandaghi.
# Computer.wav and Wavin.wav written by Kyan Pur-Djandaghi
#
# Excerpts of these external works have been used:
#
# camera.py Copyright (C) 2013 Riverbank Computing Limited.
# Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
#
# ui_camery.py, ui_imagesettings.py, ui_videosettings.py
# by: PyQt5 UI code generator 5.0-snapshot-478d7f271b71
#


from PyQt5.QtWidgets import *
from PyQt5.QtCore import (Qt, QByteArray, qFuzzyCompare, QTimer, QUrl)
from PyQt5.QtGui import QIcon, QPen, QBrush, QColor, QKeySequence, QPalette, QPixmap
from PyQt5.QtWidgets import (QWidget, QProgressBar, qApp,
    QPushButton, QApplication)
from PyQt5.QtMultimedia import (QAudioEncoderSettings, QCamera, QSound,
    QCameraImageCapture, QImageEncoderSettings, QMediaMetaData,
    QMediaRecorder, QMultimedia, QVideoEncoderSettings)
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QDialog,
    QMainWindow, QMessageBox)

from ui_camera import Ui_Camera
from ui_imagesettings import Ui_ImageSettingsUi
from ui_videosettings import Ui_VideoSettingsUi
import sys
import os
import time
from random import randint

class MyWin(QWidget):
    width = 992
    height = 600
    count = 0

    def __init__(self):
        super(MyWin, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.buttons = []

        self.scrollText = QTextEdit()
        self.viewterms = QPushButton("View the Terms and Conditions")
        self.viewterms.clicked.connect(self.loadTerms)

        vbox = QVBoxLayout()
        vbox.addWidget(self.scrollText)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.viewterms, alignment=Qt.AlignLeft)
        vbox.addLayout(self.buttonLayout)
        self.setLayout(vbox)

        self.setGeometry(0,0, self.width, self.height)
        self.setWindowTitle('Welcome to OS Prefugium')
        self.show()

    def loadTerms(self):

        fp = open("terms_apply.html", 'r')
        filetext = fp.read()
        self.scrollText.setHtml(filetext)
        fp.close()

        self.viewterms.setVisible(False)
        accept = QPushButton("Accept Digital Rights")
        accept.clicked.connect(self.acceptPush)
        deny = QPushButton("Deny Digital Rights")
        deny.clicked.connect(self.denyPush)
        digital = QPushButton("View Digital Rights")
        digital.clicked.connect(self.digitalPush)
        self.buttonLayout.addWidget(accept, alignment=Qt.AlignLeft)
        self.buttonLayout.addWidget(deny, alignment=Qt.AlignLeft)
        self.buttonLayout.addWidget(digital, alignment=Qt.AlignLeft)
        self.buttonLayout.addStretch(1)
        self.setWindowTitle("Welcome to OS Prefugium")

    def scatter(self):
        for but in self.buttons:
            but.move(randint(50, self.width - 100), randint(50, self.height - 50))

    def acceptPush(self):
        if self.count > 3:
            self.win = MyWin4()
            self.hide()
        else:
            self.count=self.count +1

        for i in range(42):
            newbut = QPushButton(self)
            newbut.setText("OBEY!")
            newbut.clicked.connect(self.acceptPush)
            newbut.setVisible(True)
            self.buttons.append(newbut)
        self.scatter()

    def denyPush(self):
        self.win = MyWin2()
        self.hide()

    def digitalPush(self):
        fp = open("charter.html", 'r')
        filetext = fp.read()
        self.scrollText.setHtml(filetext)
        fp.close()

class MyWin2(QWidget):

    width = 992
    height = 600


    def __init__(self):
        super(MyWin2, self).__init__()
        self.initGUI()

    def initGUI(self):

        self.imageView = QLabel(self)
        self.pixmap = QPixmap(os.getcwd() + '/images/home_install.png')
        self.imageView.setPixmap(self.pixmap)
        self.btnContinue = QPushButton("Continue")
        self.btnContinue.clicked.connect(self.Prefugia)
        self.btnCancel = QPushButton("Cancel")
        self.btnCancel.clicked.connect(self.close)


        vbox = QVBoxLayout()
        vbox.addWidget(self.imageView)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.btnCancel, alignment=Qt.AlignLeft)
        self.buttonLayout.addWidget(self.btnContinue, alignment=Qt.AlignLeft)
        vbox.addLayout(self.buttonLayout)
        self.setLayout(vbox)
        self.buttonLayout.addStretch(1)

        self.setGeometry(0,0, self.width, self.height)
        self.setWindowTitle('You are one step from OS Prefugium')
        self.show()

    def close(self):
        sys.exit()

    def Prefugia(self):
        self.win = Progress()
        self.hide()

class Progress(QProgressDialog):
    def __init__(self):
        QProgressDialog.__init__(self)
        self.setWindowTitle("Install OS Prefugium")
        self.setLabelText("Retrieving Fingerprint Data")
        self.canceled.connect(self.close)
        self.setRange(0, 100)
        self.show()

        for count in range(self.minimum(), self.maximum() + 1):
            self.setValue(count)
            qApp.processEvents()
            time.sleep(0.05)

        self.Prefugia()

    def Prefugia(self):
        self.win = MyWin3()
        self.hide()

    def close(self):
        sys.exit()


class MyWin3(QWidget):

    width = 992
    height = 600

    def __init__(self):
        super(MyWin3, self).__init__()
        self.initGUI()

    def initGUI(self):

        self.imageView = QLabel(self)
        self.pixmap = QPixmap(os.getcwd() + '/images/home.png')
        self.imageView.setPixmap(self.pixmap)
        self.sound = QSound("sounds/Wavvin.wav")
        self.sound.play()

        self.setGeometry(0,0, self.width, self.height)
        self.setWindowTitle('Welcome to your personal Prefugium')
        self.show()

    def close(self):
        sys.exit()

class MyWin4(QWidget):

    width = 992
    height = 600

    def __init__(self):
        super(MyWin4, self).__init__()
        self.initGUI()

    def initGUI(self):

        self.imageView = QLabel(self)
        self.pixmap = QPixmap(os.getcwd() + '/images/home_glitch_0.png')
        self.imageView.setPixmap(self.pixmap)
        self.sound = QSound("sounds/Computer.wav")
        self.sound.play()
        camera.show()

        self.setGeometry(0,0, self.width, self.height)
        self.setWindowTitle('Welcome back to Reality')
        self.show()

    def close(self):
        sys.exit()

class Camera(QMainWindow):

    def __init__(self, parent=None):
        super(Camera, self).__init__(parent)

        self.ui = Ui_Camera()
        self.camera = None
        self.imageCapture = None
        self.mediaRecorder = None
        self.isCapturingImage = False
        self.applicationExiting = False

        self.imageSettings = QImageEncoderSettings()
        self.audioSettings = QAudioEncoderSettings()
        self.videoSettings = QVideoEncoderSettings()
        self.videoContainerFormat = ''
        self.setWindowTitle('IACS is watching you')
        self.ui.setupUi(self)

        cameraDevice = QByteArray()

        videoDevicesGroup = QActionGroup(self)
        videoDevicesGroup.setExclusive(True)

        for deviceName in QCamera.availableDevices():
            description = QCamera.deviceDescription(deviceName)
            videoDeviceAction = QAction(description, videoDevicesGroup)
            videoDeviceAction.setCheckable(True)
            videoDeviceAction.setData(deviceName)

            if cameraDevice.isEmpty():
                cameraDevice = deviceName
                videoDeviceAction.setChecked(True)

            self.ui.menuDevices.addAction(videoDeviceAction)

        videoDevicesGroup.triggered.connect(self.updateCameraDevice)
        self.ui.captureWidget.currentChanged.connect(self.updateCaptureMode)

        self.ui.lockButton.hide()

        self.setCamera(cameraDevice)

    def setCamera(self, cameraDevice):
        if cameraDevice.isEmpty():
            self.camera = QCamera()
        else:
            self.camera = QCamera(cameraDevice)

        self.camera.stateChanged.connect(self.updateCameraState)
        self.camera.error.connect(self.displayCameraError)

        self.mediaRecorder = QMediaRecorder(self.camera)
        self.mediaRecorder.stateChanged.connect(self.updateRecorderState)

        self.imageCapture = QCameraImageCapture(self.camera)

        self.mediaRecorder.durationChanged.connect(self.updateRecordTime)
        self.mediaRecorder.error.connect(self.displayRecorderError)

        self.mediaRecorder.setMetaData(QMediaMetaData.Title, "IACS WATCHES U")

        self.ui.exposureCompensation.valueChanged.connect(
                self.setExposureCompensation)

        self.camera.setViewfinder(self.ui.viewfinder)

        self.updateCameraState(self.camera.state())
        self.updateLockStatus(self.camera.lockStatus(), QCamera.UserRequest)
        self.updateRecorderState(self.mediaRecorder.state())

        self.imageCapture.readyForCaptureChanged.connect(self.readyForCapture)
        self.imageCapture.imageCaptured.connect(self.processCapturedImage)
        self.imageCapture.imageSaved.connect(self.imageSaved)

        self.camera.lockStatusChanged.connect(self.updateLockStatus)

        self.ui.captureWidget.setTabEnabled(0,
                self.camera.isCaptureModeSupported(QCamera.CaptureStillImage))
        self.ui.captureWidget.setTabEnabled(1,
                self.camera.isCaptureModeSupported(QCamera.CaptureVideo))

        self.updateCaptureMode()
        self.camera.start()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        if event.key() == Qt.Key_CameraFocus:
            self.displayViewfinder()
            self.camera.searchAndLock()
            event.accept()
        elif event.key() == Qt.Key_Camera:
            if self.camera.captureMode() == QCamera.CaptureStillImage:
                self.takeImage()
            elif self.mediaRecorder.state() == QMediaRecorder.RecordingState:
                self.stop()
            else:
                self.record()

            event.accept()
        else:
            super(Camera, self).keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return

        if event.key() == Qt.Key_CameraFocus:
            self.camera.unlock()
        else:
            super(Camera, self).keyReleaseEvent(event)

    def updateRecordTime(self):
        msg = "Recorded %d sec" % self.mediaRecorder.duration() // 1000
        self.ui.statusbar.showMessage(msg)

    def processCapturedImage(self, requestId, img):
        scaledImage = img.scaled(self.ui.viewfinder.size(), Qt.KeepAspectRatio,
                Qt.SmoothTransformation)

        self.ui.lastImagePreviewLabel.setPixmap(QPixmap.fromImage(scaledImage))

        self.displayCapturedImage()
        QTimer.singleShot(4000, self.displayViewfinder)

    def configureCaptureSettings(self):
        if self.camera.captureMode() == QCamera.CaptureStillImage:
            self.configureImageSettings()
        elif self.camera.captureMode() == QCamera.CaptureVideo:
            self.configureVideoSettings()

    def configureVideoSettings(self):
        settingsDialog = VideoSettings(self.mediaRecorder)

        settingsDialog.setAudioSettings(self.audioSettings)
        settingsDialog.setVideoSettings(self.videoSettings)
        settingsDialog.setFormat(self.videoContainerFormat)

        if settingsDialog.exec_():
            self.audioSettings = settingsDialog.audioSettings()
            self.videoSettings = settingsDialog.videoSettings()
            self.videoContainerFormat = settingsDialog.format()

            self.mediaRecorder.setEncodingSettings(self.audioSettings,
                    self.videoSettings, self.videoContainerFormat)

    def configureImageSettings(self):
        settingsDialog = ImageSettings(self.imageCapture)

        settingsDialog.setImageSettings(self.imageSettings)

        if settingsDialog.exec_():
            self.imageSettings = settingsDialog.imageSettings()
            self.imageCapture.setEncodingSettings(self.imageSettings)

    def record(self):
        self.mediaRecorder.record()
        self.updateRecordTime()

    def pause(self):
        self.mediaRecorder.pause()

    def stop(self):
        self.mediaRecorder.stop()

    def setMuted(self, muted):
        self.mediaRecorder.setMuted(muted)

    def toggleLock(self):
        if self.camera.lockStatus() in (QCamera.Searching, QCamera.Locked):
            self.camera.unlock()
        elif self.camera.lockStatus() == QCamera.Unlocked:
            self.camera.searchAndLock()

    def updateLockStatus(self, status, reason):
        indicationColor = Qt.black

        if status == QCamera.Searching:
            self.ui.statusbar.showMessage("Focusing...")
            self.ui.lockButton.setText("Focusing...")
            indicationColor = Qt.yellow
        elif status == QCamera.Locked:
            self.ui.lockButton.setText("Unlock")
            self.ui.statusbar.showMessage("Focused", 2000)
            indicationColor = Qt.darkGreen
        elif status == QCamera.Unlocked:
            self.ui.lockButton.setText("Focus")

            if reason == QCamera.LockFailed:
                self.ui.statusbar.showMessage("Focus Failed", 2000)
                indicationColor = Qt.red

        palette = self.ui.lockButton.palette()
        palette.setColor(QPalette.ButtonText, indicationColor)
        self.ui.lockButton.setPalette(palette)

    def takeImage(self):
        self.isCapturingImage = True
        self.imageCapture.capture()

    def startCamera(self):
        self.camera.start()

    def stopCamera(self):
        self.camera.stop()

    def updateCaptureMode(self):
        tabIndex = self.ui.captureWidget.currentIndex()
        captureMode = QCamera.CaptureStillImage if tabIndex == 0 else QCamera.CaptureVideo

        if self.camera.isCaptureModeSupported(captureMode):
            self.camera.setCaptureMode(captureMode)

    def updateCameraState(self, state):
        if state == QCamera.ActiveState:
            self.ui.actionStartCamera.setEnabled(False)
            self.ui.actionStopCamera.setEnabled(True)
            self.ui.captureWidget.setEnabled(True)
            self.ui.actionSettings.setEnabled(True)
        elif state in (QCamera.UnloadedState, QCamera.LoadedState):
            self.ui.actionStartCamera.setEnabled(True)
            self.ui.actionStopCamera.setEnabled(False)
            self.ui.captureWidget.setEnabled(False)
            self.ui.actionSettings.setEnabled(False)

    def updateRecorderState(self, state):
        if state == QMediaRecorder.StoppedState:
            self.ui.recordButton.setEnabled(True)
            self.ui.pauseButton.setEnabled(True)
            self.ui.stopButton.setEnabled(False)
        elif state == QMediaRecorder.PausedState:
            self.ui.recordButton.setEnabled(True)
            self.ui.pauseButton.setEnabled(False)
            self.ui.stopButton.setEnabled(True)
        elif state == QMediaRecorder.RecordingState:
            self.ui.recordButton.setEnabled(False)
            self.ui.pauseButton.setEnabled(True)
            self.ui.stopButton.setEnabled(True)

    def setExposureCompensation(self, index):
        self.camera.exposure().setExposureCompensation(index * 0.5)

    def displayRecorderError(self):
        QMessageBox.warning(self, "Capture error",
                self.mediaRecorder.errorString())

    def displayCameraError(self):
        QMessageBox.warning(self, "Camera error", self.camera.errorString())

    def updateCameraDevice(self, action):
        self.setCamera(action.data())

    def displayViewfinder(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def displayCapturedImage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def readyForCapture(self, ready):
        self.ui.takeImageButton.setEnabled(ready)

    def imageSaved(self, id, fileName):
        self.isCapturingImage = False

        if self.applicationExiting:
            self.close()

    def closeEvent(self, event):
        if self.isCapturingImage:
            self.setEnabled(False)
            self.applicationExiting = True
            event.ignore()
        else:
            event.accept()


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    win = MyWin()
    camera = Camera()
    sys.exit(app.exec_())
