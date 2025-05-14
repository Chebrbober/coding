# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audio_playerMLUFvN.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSlider, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 700)
        MainWindow.setMinimumSize(QSize(700, 700))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        MainWindow.setToolTipDuration(1)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.file_act = QAction(MainWindow)
        self.file_act.setObjectName(u"file_act")
        self.file_act.setVisible(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(640, 360))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setWeight(QFont.Black)
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.song_table = QTableWidget(self.centralwidget)
        if (self.song_table.columnCount() < 2):
            self.song_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.song_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.song_table.rowCount() < 15):
            self.song_table.setRowCount(15)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.song_table.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.song_table.setItem(1, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.song_table.setItem(2, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.song_table.setItem(3, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.song_table.setItem(4, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.song_table.setItem(8, 0, __qtablewidgetitem7)
        self.song_table.setObjectName(u"song_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.song_table.sizePolicy().hasHeightForWidth())
        self.song_table.setSizePolicy(sizePolicy1)
        self.song_table.setStyleSheet(u"QTableWidget {\n"
"    border: none;\n"
"    color: white;\n"
"    font-family: \"Montserrat\";\n"
"    gridline-color: #555555;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border-bottom: 1px solid #d0d0d0;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #aaffff;\n"
"    color: black;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    font-family: \"Montserrat\";\n"
"}")

        self.verticalLayout_2.addWidget(self.song_table)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 125))
        self.frame.setStyleSheet(u"background-color: rgb(37, 37, 37);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.prev_track_bt = QToolButton(self.frame)
        self.prev_track_bt.setObjectName(u"prev_track_bt")
        self.prev_track_bt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.prev_track_bt.setStyleSheet(u"QToolButton {\n"
"width: 40px;\n"
"height: 40px;\n"
"border: 7px;\n"
"border-width: 3px;\n"
"border-color: orange;\n"
"border-radius: 21px;\n"
"}\n"
"QToolButton::hover {\n"
"background-color: rgb(60, 60, 60);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/skip_previous_24dp_E8EAED_FILL1_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prev_track_bt.setIcon(icon)
        self.prev_track_bt.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.prev_track_bt)

        self.play_pause_bt = QToolButton(self.frame)
        self.play_pause_bt.setObjectName(u"play_pause_bt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.play_pause_bt.sizePolicy().hasHeightForWidth())
        self.play_pause_bt.setSizePolicy(sizePolicy2)
        self.play_pause_bt.setMinimumSize(QSize(48, 48))
        self.play_pause_bt.setMaximumSize(QSize(16777215, 16777215))
        self.play_pause_bt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.play_pause_bt.setToolTipDuration(-1)
        self.play_pause_bt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.play_pause_bt.setStyleSheet(u"QToolButton {\n"
"border: 1px solid;\n"
"border-radius: 25.4px;\n"
"border-width: 3px;\n"
"border-color: white;\n"
"}\n"
"QToolButton::hover {\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/play_arrow_24dp_E8EAED_FILL1_wght400_GRAD0_opsz24 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/pause_24dp_E8EAED_FILL1_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon1.addFile(u":/icons/pause_24dp_E8EAED_FILL1_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.play_pause_bt.setIcon(icon1)
        self.play_pause_bt.setIconSize(QSize(42, 42))
        self.play_pause_bt.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_3.addWidget(self.play_pause_bt)

        self.next_track_bt = QToolButton(self.frame)
        self.next_track_bt.setObjectName(u"next_track_bt")
        font1 = QFont()
        font1.setBold(False)
        self.next_track_bt.setFont(font1)
        self.next_track_bt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.next_track_bt.setStyleSheet(u"QToolButton {\n"
"width: 40px;\n"
"height: 40px;\n"
"border: 7px;\n"
"border-width: 3px;\n"
"border-color: orange;\n"
"border-radius: 21px;\n"
"}\n"
"QToolButton::hover {\n"
"background-color: rgb(60, 60, 60);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/skip_next_24dp_E8EAED_FILL1_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.next_track_bt.setIcon(icon2)
        self.next_track_bt.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.next_track_bt)

        self.playback_sl = QSlider(self.frame)
        self.playback_sl.setObjectName(u"playback_sl")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.playback_sl.sizePolicy().hasHeightForWidth())
        self.playback_sl.setSizePolicy(sizePolicy3)
        self.playback_sl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.playback_sl.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 1px;\n"
"	border: 1px solid #ffffff;\n"
"	border-radius: 1px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color: rgb(41, 144, 255);\n"
"	width: 10px;\n"
"	margin: -5px -1px;\n"
"	border-radius: 5px ;\n"
"	border: 1px solid rgb(42, 92, 255);\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"	background: #ffffff\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"	background-color: rgb(41, 144, 255);\n"
"}\n"
"")
        self.playback_sl.setOrientation(Qt.Orientation.Horizontal)
        self.playback_sl.setTickPosition(QSlider.TickPosition.NoTicks)
        self.playback_sl.setTickInterval(0)

        self.horizontalLayout_3.addWidget(self.playback_sl)

        self.time_lb = QLabel(self.frame)
        self.time_lb.setObjectName(u"time_lb")
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.time_lb.setFont(font2)
        self.time_lb.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.time_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.time_lb)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.mute_unmute_bt = QToolButton(self.frame)
        self.mute_unmute_bt.setObjectName(u"mute_unmute_bt")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mute_unmute_bt.sizePolicy().hasHeightForWidth())
        self.mute_unmute_bt.setSizePolicy(sizePolicy4)
        self.mute_unmute_bt.setMaximumSize(QSize(45, 45))
        self.mute_unmute_bt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mute_unmute_bt.setStyleSheet(u"QToolButton {\n"
"width: 40px;\n"
"height: 40px;\n"
"border: 7px;\n"
"border-width: 3px;\n"
"border-color: orange;\n"
"border-radius: 21px;\n"
"}\n"
"QToolButton::hover {\n"
"background-color: rgb(60, 60, 60);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/volume_off_24dp_E8EAED_FILL1_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/volume_up_24dp_E8EAED_FILL1_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.mute_unmute_bt.setIcon(icon3)
        self.mute_unmute_bt.setIconSize(QSize(24, 24))
        self.mute_unmute_bt.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.mute_unmute_bt.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.mute_unmute_bt.setAutoRaise(False)
        self.mute_unmute_bt.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout.addWidget(self.mute_unmute_bt)

        self.volume_sl = QSlider(self.frame)
        self.volume_sl.setObjectName(u"volume_sl")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(123)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.volume_sl.sizePolicy().hasHeightForWidth())
        self.volume_sl.setSizePolicy(sizePolicy5)
        self.volume_sl.setMaximumSize(QSize(195, 16777215))
        self.volume_sl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.volume_sl.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.volume_sl.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	height: 1px;\n"
"	border: 1px solid #ffffff;\n"
"	border-radius: 1px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background-color: rgb(41, 144, 255);\n"
"	width: 10px;\n"
"	margin: -5px -1px;\n"
"	border-radius: 5px ;\n"
"	border: 1px solid rgb(42, 92, 255);\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"	background: #ffffff\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"	background-color: rgb(41, 144, 255);\n"
"}\n"
"")
        self.volume_sl.setPageStep(5)
        self.volume_sl.setSliderPosition(0)
        self.volume_sl.setOrientation(Qt.Orientation.Horizontal)
        self.volume_sl.setInvertedAppearance(False)
        self.volume_sl.setInvertedControls(False)
        self.volume_sl.setTickPosition(QSlider.TickPosition.NoTicks)
        self.volume_sl.setTickInterval(0)

        self.horizontalLayout.addWidget(self.volume_sl)

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontal_spacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.Qt.AlignmentFlag.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.meuBar = QMenuBar(MainWindow)
        self.meuBar.setObjectName(u"meuBar")
        self.meuBar.setGeometry(QRect(0, 0, 700, 21))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setBold(False)
        self.meuBar.setFont(font3)
        self.meuBar.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"background-color: rgb(45,45,45)")
        self.menu = QMenu(self.meuBar)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"")
        MainWindow.setMenuBar(self.meuBar)

        self.meuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.file_act)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PlayerForever", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.file_act.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        ___qtablewidgetitem = self.song_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.song_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None));

        __sortingEnabled = self.song_table.isSortingEnabled()
        self.song_table.setSortingEnabled(False)
        self.song_table.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.prev_track_bt.setToolTip(QCoreApplication.translate("MainWindow", u"Previous", None))
#endif // QT_CONFIG(tooltip)
        self.prev_track_bt.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(shortcut)
        self.prev_track_bt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Left", None))
#endif // QT_CONFIG(shortcut)
        self.play_pause_bt.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(shortcut)
        self.play_pause_bt.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.next_track_bt.setToolTip(QCoreApplication.translate("MainWindow", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.next_track_bt.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(shortcut)
        self.next_track_bt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Right", None))
#endif // QT_CONFIG(shortcut)
        self.time_lb.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.mute_unmute_bt.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(shortcut)
        self.mute_unmute_bt.setShortcut(QCoreApplication.translate("MainWindow", u"M", None))
#endif // QT_CONFIG(shortcut)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

