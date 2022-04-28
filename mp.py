from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QHBoxLayout,QVBoxLayout,QStyle,QSlider,QFileDialog
import sys
from PyQt5.QtGui import QIcon,QPalette
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget




class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("picture/play.png"))
        self.setWindowTitle("PyMPlayer")
        self.setGeometry(200, 100, 900, 600)
        pal=self.palette()
        pal.setColor(QPalette.Window,Qt.gray)
        self.setPalette(pal)
        self.create_player()



    def create_player(self):
        self.mediaPlayer=QMediaPlayer(None,QMediaPlayer.VideoSurface)
        videowidget=QVideoWidget()

        self.openbtn=QPushButton('Open Video')
        self.openbtn.clicked.connect(self.open_file)


        self.playbtn=QPushButton()
        self.playbtn.setEnabled(False)
        self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playbtn.clicked.connect(self.play_video)

        self.slider=QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)



        
        hbox=QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)

        hbox.addWidget(self.openbtn)
        hbox.addWidget(self.playbtn)
        hbox.addWidget(self.slider)

        vbox=QVBoxLayout()
        vbox.addWidget(videowidget)

        vbox.addLayout(hbox)

        self.mediaPlayer.setVideoOutput(videowidget)

        self.setLayout(vbox)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)


    def open_file(self):
        filename, _=QFileDialog.getOpenFileName(self,"Open Video File")
        if filename !='':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile((filename))))
            self.playbtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state()==QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediastate_changed(self,state):
        if self.mediaPlayer.state()==QMediaPlayer.PlayingState:
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self,position):
        self.slider.setValue(position)

    def duration_changed(self,duration):
        self.slider.setRange(0,duration)

    def set_position(self,position):
        self.mediaPlayer.setPosition(position)





    
app=QApplication(sys.argv)
pncr=Pencere()
pncr.show()
sys.exit(app.exec_())
