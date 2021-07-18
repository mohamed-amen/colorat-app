from clipboard import copy
from colour import Color
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                             QLineEdit, QPushButton, QSizePolicy, QSlider,
                             QSpacerItem, QVBoxLayout, QHBoxLayout, QWidget,
                             QStackedWidget, QRadioButton, QComboBox)

from PyQt5.QtGui import QCursor, QIcon



class RGBPage(QWidget):


    def __init__(self):
        QWidget.__init__(self)

        self.Widgets()
        self.value_changed()


    def Widgets(self):

        self.mainframe = QFrame()

        #-----------------------------------------------#

        self.red_label = QLabel('red')
        self.red_slider = QSlider(Qt.Horizontal)
        self.red_value = QLabel()

        #-----------------------------------------------#

        self.green_label = QLabel('green')
        self.green_slider = QSlider(Qt.Horizontal)
        self.green_value = QLabel()

        #-----------------------------------------------#

        self.blue_label = QLabel('blue')
        self.blue_slider = QSlider(Qt.Horizontal)
        self.blue_value = QLabel()

        #-----------------------------------------------#

        self.line_edit = QLineEdit()

        #-----------------------------------------------#

        self.controls_frame = QFrame()

        #-----------------------------------------------#

        self.copy_button = QPushButton('copy color')

        #-----------------------------------------------#

        self.get_data = QPushButton('Inherit color')

        #-----------------------------------------------#

        self.spacer = QSpacerItem(0, 0, vPolicy = QSizePolicy.Expanding)

        #-----------------------------------------------#

        self.mainframe_vlayout = QVBoxLayout(self.mainframe)

        #-----------------------------------------------#

        self.controls_grid = QGridLayout(self.controls_frame)

        #-----------------------------------------------#

        self.main_layout = QVBoxLayout(self)

        #-----------------------------------------------#

        self.top_frame = QFrame()

        #-----------------------------------------------#

        self.top_frame_layout = QHBoxLayout(self.top_frame)

        #-----------------------------------------------#

        self.rgb_radio = QRadioButton('RGB')
        self.rgba_radio = QRadioButton('RGBA')

        #-----------------------------------------------#

        self.Style()


    def Style(self):


        self.red_label.setAlignment(Qt.AlignCenter)

        self.red_slider.setMinimum(0)
        self.red_slider.setMaximum(255)
        self.red_slider.setValue(255)
        self.red_slider.valueChanged.connect(self.value_changed)
        self.red_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.red_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.green_label.setAlignment(Qt.AlignCenter)

        self.green_slider.setMinimum(0)
        self.green_slider.setMaximum(255)
        self.green_slider.setValue(255)
        self.green_slider.valueChanged.connect(self.value_changed)
        self.green_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.green_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.blue_label.setAlignment(Qt.AlignCenter)

        self.blue_slider.setMinimum(0)
        self.blue_slider.setMaximum(255)
        self.blue_slider.setValue(255)
        self.blue_slider.valueChanged.connect(self.value_changed)
        self.blue_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.blue_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.setReadOnly(True)

        #-----------------------------------------------#

        self.controls_frame.setMinimumSize(0, 150)

        #-----------------------------------------------#

        self.copy_button.clicked.connect(self.copy)
        self.copy_button.setCursor(QCursor(Qt.PointingHandCursor))

        #-----------------------------------------------#

        self.rgba_radio.setLayoutDirection(Qt.RightToLeft)
        self.rgba_radio.setCursor(QCursor(Qt.PointingHandCursor))
        self.rgba_radio.clicked.connect(lambda: [MainRGB.__init__.stacked.setCurrentIndex(1), self.rgb_radio.setChecked(True)])

        #-----------------------------------------------#

        self.rgb_radio.setChecked(True)
        self.rgb_radio.setCursor(QCursor(Qt.PointingHandCursor))
        self.rgb_radio.clicked.connect(lambda: MainRGB.__init__.stacked.setCurrentIndex(0))

        #-----------------------------------------------#

        self.top_frame_layout.addWidget(self.rgba_radio)
        self.top_frame_layout.addWidget(self.line_edit)
        self.top_frame_layout.addWidget(self.rgb_radio)

        #-----------------------------------------------#

        self.get_data.clicked.connect(self.change_value)
        self.get_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.get_data.setToolTip('press to inherit the color from the previous page')

        #-----------------------------------------------#

        self.mainframe_vlayout.addWidget(self.top_frame)
        self.mainframe_vlayout.addWidget(self.copy_button, alignment=Qt.AlignCenter)
        self.mainframe_vlayout.addWidget(self.get_data, alignment=Qt.AlignCenter)
        self.mainframe_vlayout.addItem(self.spacer)
        self.mainframe_vlayout.addWidget(self.controls_frame)

        #-----------------------------------------------#

        self.controls_grid.addWidget(self.red_label, 0, 0)
        self.controls_grid.addWidget(self.red_slider, 0, 1)
        self.controls_grid.addWidget(self.red_value, 0, 2)

        self.controls_grid.addWidget(self.green_label, 1, 0)
        self.controls_grid.addWidget(self.green_slider, 1, 1)
        self.controls_grid.addWidget(self.green_value, 1, 2)

        self.controls_grid.addWidget(self.blue_label, 2, 0)
        self.controls_grid.addWidget(self.blue_slider, 2, 1)
        self.controls_grid.addWidget(self.blue_value, 2, 2)

        #-----------------------------------------------#
        self.main_layout.addWidget(self.mainframe)


    def change_value(self):

        self.data_path = (u"c:/colorat/data.txt")

        self.data = open(self.data_path, 'r')

        Data_var = self.data.readlines()

        self.red_slider.setValue(int(Data_var[0]))
        self.green_slider.setValue(int(Data_var[1]))
        self.blue_slider.setValue(int(Data_var[2]))

        self.data.close()


    def value_changed(self):

        self.data_path = (u"c:/colorat/data.txt")

        self.data = open(self.data_path, 'w')
        self.data.write(f'{self.red_slider.value()}\n{self.green_slider.value()}\n{self.blue_slider.value()}\n' )
        self.data.close()


        rsv = self.red_slider.value()                      # rsv = red slider value
        gsv = self.green_slider.value()                    # gsv = green slider value
        bsv = self.blue_slider.value()                     # bsv = blue slider value


        n = 0                                # n = number

        icl = [0, 0, 0]                      # icl = inverted color list
        cl = [rsv, gsv, bsv]                 # cl = color list

        for ic in cl:                        # ic = inverted color
            if ic > 127.5:
                fsm = abs(127.5 - ic) * 2     # fsm = first step more
                ssm = ic - fsm                 # ssm = second step more
                icl[n] = ssm
                n += 1
                if n == 3:
                    n = 0
            else:
                fsl = (127.5 - ic) * 2        # fsl = first step less
                ssl = ic + fsl                # ssl = second step less
                icl[n] = ssl
                n += 1
                if n == 3:
                    n = 0


        ir = icl[0]                           # ir = inverted red
        ig = icl[1]                           # ig = inverted green
        ib = icl[2]                           # ib = inverted blue

        self.setStyleSheet('QLabel{'
                           'font-size:20px;'
                           'background:transparent;'
                           '}'
                           'QWidget{'
                           f'background:rgb({rsv}, {gsv}, {bsv});'
                           '}'
                           'QFrame{ '
                           f'background:rgb({rsv}, {gsv}, {bsv});'
                           '}'
                           'QLineEdit{ '
                           'border:0px;'
                           'font-size:20px;'
                           '}'
                           'QSlider::handle{'
                           'border-radius:4px;'
                           'border:1.2px solid'
                           '}')


        self.red_value.setText(f'{rsv}')
        self.green_value.setText(f'{gsv}')
        self.blue_value.setText(f'{bsv}')

        self.red_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});font-family: Baloo Chettan 2')
        self.green_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.blue_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')

        self.rgb_radio.setStyleSheet(f'font-size: 19px; color: rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.rgba_radio.setStyleSheet(f'font-size: 19px; color: rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')

        self.line_edit.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')

        self.red_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.green_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.blue_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')


        c = Color(rgb=((rsv/255), (gsv/255), (bsv/255)))


        if rsv|gsv|bsv > 127.5:
            self.copy_button.setStyleSheet('QPushButton{'
                                           f'color:rgb({ir}, {ig}, {ib});'
                                           'font-size:20px;'
                                           'border:1.3px solid;'
                                           'padding:5px;'
                                           'padding-top:2px;'
                                           'border-radius:5px;'
                                           'font-family: Baloo Chettan 2'
                                           '}'
                                           'QPushButton:hover{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-15}%)'
                                           '}'
                                           'QPushButton:pressed{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-30}%)'
                                           '}')

            self.get_data.setStyleSheet('QPushButton{'
                                        f'color:rgb({ir}, {ig}, {ib});'
                                        'font-size:20px;'
                                        'border:1.3px solid;'
                                        'padding:5px;'
                                        'padding-top:2px;'
                                        'border-radius:5px;'
                                        'font-family: Baloo Chettan 2'
                                        '}'
                                        'QPushButton:hover{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-15}%)'
                                        '}'
                                        'QPushButton:pressed{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-30}%)'
                                        '}')

        else:
            self.copy_button.setStyleSheet('QPushButton{'
                                           f'color:rgb({ir}, {ig}, {ib});'
                                           'font-size:20px;'
                                           'border:1.3px solid;'
                                           'padding:5px;'
                                           'padding-top:2px;'
                                           'border-radius:5px;'
                                           'font-family: baloo chettan 2'
                                           '}'
                                           'QPushButton:hover{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+15}%)'
                                           '}'
                                           'QPushButton:pressed{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+30}%)'
                                           '}')

            self.get_data.setStyleSheet('QPushButton{'
                                        f'color:rgb({ir}, {ig}, {ib});'
                                        'font-size:20px;'
                                        'border:1.3px solid;'
                                        'padding:5px;'
                                        'padding-top:2px;'
                                        'border-radius:5px;'
                                        'font-family: baloo chettan 2'
                                        '}'
                                        'QPushButton:hover{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+15}%)'
                                        '}'
                                        'QPushButton:pressed{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+30}%)'
                                        '}')


        self.line_edit.setText(f'rgb({rsv}, {gsv}, {bsv})')

        self.red_slider.setStyleSheet('QSlider::handle{background: red}')
        self.green_slider.setStyleSheet('QSlider::handle{background:rgb(0 , 255, 0)}')
        self.blue_slider.setStyleSheet('QSlider::handle{background: blue}')

        self.copy_button.setMaximumSize(16777215, 30)
        self.get_data.setMaximumSize(16777215, 30)


    def copy(self):
        copy(self.line_edit.text())





class RGBAPage(QWidget):


    def __init__(self):
        QWidget.__init__(self)

        self.Widgets()
        self.value_changed()


    def Widgets(self):

        self.mainframe = QFrame()

        #-----------------------------------------------#

        self.red_label = QLabel('red')
        self.red_slider = QSlider(Qt.Horizontal)
        self.red_value = QLabel()

        #-----------------------------------------------#

        self.green_label = QLabel('green')
        self.green_slider = QSlider(Qt.Horizontal)
        self.green_value = QLabel()

        #-----------------------------------------------#

        self.blue_label = QLabel('blue')
        self.blue_slider = QSlider(Qt.Horizontal)
        self.blue_value = QLabel()

        #-----------------------------------------------#

        self.alpha_label = QLabel('alpha')
        self.alpha_slider = QSlider(Qt.Horizontal)
        self.alpha_value = QLabel()

        #-----------------------------------------------#

        self.line_edit = QLineEdit()

        #-----------------------------------------------#

        self.controls_frame = QFrame()

        #-----------------------------------------------#

        self.copy_button = QPushButton('copy color')

        #-----------------------------------------------#

        self.get_data = QPushButton('Inherit color')

        #-----------------------------------------------#

        self.spacer = QSpacerItem(0, 0, vPolicy = QSizePolicy.Expanding)

        #-----------------------------------------------#

        self.mainframe_vlayout = QVBoxLayout(self.mainframe)

        #-----------------------------------------------#

        self.controls_grid = QGridLayout(self.controls_frame)

        #-----------------------------------------------#

        self.main_layout = QVBoxLayout(self)

        #---------------------#-------------------------#

        self.top_frame = QFrame()

        #-----------------------------------------------#

        self.top_frame_layout = QHBoxLayout(self.top_frame)

        #-----------------------------------------------#

        self.rgb_radio = QRadioButton('RGB')
        self.rgba_radio = QRadioButton('RGBA')

        #-----------------------------------------------#

        self.trans_label = QLabel('Transparency is 100%')

        self.label_layout = QVBoxLayout(self.trans_label)

        #---------------------#-------------------------#

        self.Style()


    def Style(self):


        self.red_label.setAlignment(Qt.AlignCenter)

        self.red_slider.setMinimum(0)
        self.red_slider.setMaximum(255)
        self.red_slider.setValue(255)
        self.red_slider.valueChanged.connect(self.value_changed)
        self.red_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.red_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.green_label.setAlignment(Qt.AlignCenter)

        self.green_slider.setMinimum(0)
        self.green_slider.setMaximum(255)
        self.green_slider.setValue(255)
        self.green_slider.valueChanged.connect(self.value_changed)
        self.green_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.green_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.blue_label.setAlignment(Qt.AlignCenter)

        self.blue_slider.setMinimum(0)
        self.blue_slider.setMaximum(255)
        self.blue_slider.setValue(255)
        self.blue_slider.valueChanged.connect(self.value_changed)
        self.blue_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.blue_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.alpha_label.setAlignment(Qt.AlignCenter)

        self.alpha_slider.setMinimum(0)
        self.alpha_slider.setMaximum(100)
        self.alpha_slider.setValue(100)
        self.alpha_slider.valueChanged.connect(self.value_changed)
        self.alpha_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.alpha_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.setReadOnly(True)

        #-----------------------------------------------#

        self.controls_frame.setMinimumSize(350, 150)

        #-----------------------------------------------#

        self.copy_button.clicked.connect(self.copy)
        self.copy_button.setCursor(QCursor(Qt.PointingHandCursor))

        #-----------------------------------------------#

        self.rgba_radio.setLayoutDirection(Qt.RightToLeft)
        self.rgba_radio.setChecked(True)
        self.rgba_radio.setCursor(QCursor(Qt.PointingHandCursor))
        self.rgba_radio.clicked.connect(lambda: MainRGB.__init__.stacked.setCurrentIndex(1))

        #-----------------------------------------------#

        self.rgb_radio.setCursor(QCursor(Qt.PointingHandCursor))
        self.rgb_radio.clicked.connect(lambda: [MainRGB.__init__.stacked.setCurrentIndex(0), self.rgba_radio.setChecked(True)])

        #-----------------------------------------------#

        self.top_frame_layout.addWidget(self.rgba_radio)
        self.top_frame_layout.addWidget(self.line_edit)
        self.top_frame_layout.addWidget(self.rgb_radio)

        #-----------------------------------------------#

        self.url = (u"c:/colorat/background.jpg")

        self.trans_label.setAlignment(Qt.AlignCenter)
        self.trans_label.setStyleSheet('QLabel{'
                                       f'background-image: url({self.url});'
                                       'font-family: Baloo Chettan 2'
                                       '}')

        #-----------------------------------------------#

        self.label_layout.addWidget(self.mainframe)
        self.label_layout.setContentsMargins(0, 0, 0, 0)

        #-----------------------------------------------#

        self.get_data.clicked.connect(self.change_value)
        self.get_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.get_data.setToolTip('press to inherit the color from the previous page')

        #-----------------------------------------------#

        self.mainframe_vlayout.addWidget(self.top_frame)
        self.mainframe_vlayout.addWidget(self.copy_button, alignment=Qt.AlignCenter)
        self.mainframe_vlayout.addWidget(self.get_data, alignment=Qt.AlignCenter)
        self.mainframe_vlayout.addItem(self.spacer)
        self.mainframe_vlayout.addWidget(self.controls_frame)

        #-----------------------------------------------#

        self.controls_grid.addWidget(self.red_label, 0, 0)
        self.controls_grid.addWidget(self.red_slider, 0, 1)
        self.controls_grid.addWidget(self.red_value, 0, 2)

        self.controls_grid.addWidget(self.green_label, 1, 0)
        self.controls_grid.addWidget(self.green_slider, 1, 1)
        self.controls_grid.addWidget(self.green_value, 1, 2)

        self.controls_grid.addWidget(self.blue_label, 2, 0)
        self.controls_grid.addWidget(self.blue_slider, 2, 1)
        self.controls_grid.addWidget(self.blue_value, 2, 2)

        self.controls_grid.addWidget(self.alpha_label, 3, 0)
        self.controls_grid.addWidget(self.alpha_slider, 3, 1)
        self.controls_grid.addWidget(self.alpha_value, 3, 2)

        #-----------------------------------------------#

        self.main_layout.addWidget(self.trans_label)


    def change_value(self):

        self.data_path = (u"c:/colorat/data.txt")

        self.data = open(self.data_path, 'r')

        Data_var = self.data.readlines()

        self.red_slider.setValue(int(Data_var[0]))
        self.green_slider.setValue(int(Data_var[1]))
        self.blue_slider.setValue(int(Data_var[2]))

        self.data.close()


    def value_changed(self):

        self.data_path = (u"c:/colorat/data.txt")

        self.data = open(self.data_path, 'w')
        self.data.write(f'{self.red_slider.value()}\n{self.green_slider.value()}\n{self.blue_slider.value()}\n' )
        self.data.close()

        rsv = self.red_slider.value()                      # rsv = red slider value
        gsv = self.green_slider.value()                    # gsv = green slider value
        bsv = self.blue_slider.value()                     # bsv = blue slider value
        asv = (self.alpha_slider.value()) / 100


        n = 0                                # n = number

        icl = [0, 0, 0]                      # icl = inverted color list
        cl = [rsv, gsv, bsv]                 # cl = color list

        for ic in cl:                        # ic = inverted color
            if ic > 127.5:
                fsm = abs(127.5 - ic) * 2     # fsm = first step more
                ssm = ic - fsm                 # ssm = second step more
                icl[n] = ssm
                n += 1
                if n == 3:
                    n = 0
            else:
                fsl = (127.5 - ic) * 2        # fsl = first step less
                ssl = ic + fsl                # ssl = second step less
                icl[n] = ssl
                n += 1
                if n == 3:
                    n = 0




        trans = self.alpha_slider.value()              # trans = transparent
        it = 0


        if trans > 50:
            fsm = abs(50 - trans) * 2
            ssm = trans - fsm
            it = ssm                              # it = inverted transparent

        else:
            fsl = (50 - trans) * 2
            ssl = trans + fsl
            it = ssl


        self.trans_label.setText(f'Transparency is {it}%')


        ir = icl[0]                           # ir = inverted red
        ig = icl[1]                           # ig = inverted green
        ib = icl[2]                           # ib = inverted blue

        self.setStyleSheet('QLabel{ \n'
                           'font-size:20px;\n'
                           'background:transparent;\n'
                           '}\n'
                           'QWidget{ \n'
                           f'background:rgba({rsv}, {gsv}, {bsv}, {asv});\n'
                           '}\n'
                           'QFrame{ \n'
                           f'background:rgba({rsv}, {gsv}, {bsv}, {asv});\n'
                           '}\n'
                           'QLineEdit{ \n'
                           'border:0px;\n'
                           'font-size:20px;\n'
                           '}\n'
                           'QSlider::handle{\n'
                           'border-radius:4px;\n'
                           'border:1.2px solid;\n'
                           '}')


        self.red_value.setText(f'{rsv}')
        self.green_value.setText(f'{gsv}')
        self.blue_value.setText(f'{bsv}')
        self.alpha_value.setText(f'{asv}')

        self.red_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});background:transparent; font-family: Baloo Chettan 2')
        self.green_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});background:transparent; font-family: Baloo Chettan 2')
        self.blue_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});background:transparent; font-family: Baloo Chettan 2')
        self.alpha_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});background:transparent; font-family: Baloo Chettan 2')

        self.line_edit.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});background:transparent; font-family: Baloo Chettan 2')

        self.red_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});background:transparent; font-family: Baloo Chettan 2')
        self.green_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});background:transparent; font-family: Baloo Chettan 2')
        self.blue_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});background:transparent; font-family: Baloo Chettan 2')
        self.alpha_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib});background:transparent; font-family: Baloo Chettan 2')

        self.rgb_radio.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); background:transparent; font-size:19px; font-family: Baloo Chettan 2')
        self.rgba_radio.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); background:transparent; font-size:19px; font-family: Baloo Chettan 2')


        c = Color(rgb=((rsv/255), (gsv/255), (bsv/255)))


        if rsv|gsv|bsv > 127.5:
            self.copy_button.setStyleSheet('QPushButton{'
                                           f'color:rgb({ir}, {ig}, {ib});'
                                           'font-size:20px;'
                                           'border:1.3px solid;'
                                           'padding:5px;'
                                           'padding-top:2px;'
                                           'border-radius:5px;'
                                           'font-family: Baloo Chettan 2'
                                           '}'
                                           'QPushButton:hover{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-15}%)'
                                           '}'
                                           'QPushButton:pressed{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-30}%)'
                                           '}')

            self.get_data.setStyleSheet('QPushButton{'
                                        f'color:rgb({ir}, {ig}, {ib});'
                                        'font-size:20px;'
                                        'border:1.3px solid;'
                                        'padding:5px;'
                                        'padding-top:2px;'
                                        'border-radius:5px;'
                                        'font-family: Baloo Chettan 2'
                                        '}'
                                        'QPushButton:hover{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-15}%)'
                                        '}'
                                        'QPushButton:pressed{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-30}%)'
                                        '}')

        else:
            self.copy_button.setStyleSheet('QPushButton{'
                                           f'color:rgb({ir}, {ig}, {ib});'
                                           'font-size:20px;'
                                           'border:1.3px solid;'
                                           'padding:5px;'
                                           'padding-top:2px;'
                                           'border-radius:5px;'
                                           'font-family: Baloo Chettan 2'
                                           '}'
                                           'QPushButton:hover{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+15}%)'
                                           '}'
                                           'QPushButton:pressed{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+30}%)'
                                           '}')

            self.get_data.setStyleSheet('QPushButton{'
                                        f'color:rgb({ir}, {ig}, {ib});'
                                        'font-size:20px;'
                                        'border:1.3px solid;'
                                        'padding:5px;'
                                        'padding-top:2px;'
                                        'border-radius:5px;'
                                        'font-family: Baloo Chettan 2'
                                        '}'
                                        'QPushButton:hover{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+15}%)'
                                        '}'
                                        'QPushButton:pressed{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+30}%)'
                                        '}')


        self.line_edit.setText(f'rgba({rsv}, {gsv}, {bsv}, {asv})')

        self.red_slider.setStyleSheet('QSlider::handle{background: red}QSlider{background:transparent}')
        self.green_slider.setStyleSheet('QSlider::handle{background:rgb(0 , 255, 0)}QSlider{background:transparent}')
        self.blue_slider.setStyleSheet('QSlider::handle{background: blue}QSlider{background:transparent}')
        self.alpha_slider.setStyleSheet('QSlider::handle{background: white}QSlider{background:transparent}')

        self.copy_button.setMaximumSize(16777215, 30)
        self.get_data.setMaximumSize(16777215, 30)


    def copy(self):
        copy(self.line_edit.text())





class MainRGB(QWidget):


    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout(self)

        MainRGB.__init__.stacked = QStackedWidget(self)

        MainRGB.__init__.stacked.setStyleSheet('border-radius:10px;')

        MainRGB.__init__.stacked.addWidget(RGBPage())
        MainRGB.__init__.stacked.addWidget(RGBAPage())


        self.layout.addWidget(MainRGB.__init__.stacked)

        self.layout.setContentsMargins(0, 0, 0, 0)






class HSLPage(QWidget):


    def __init__(self):
        QWidget.__init__(self)

        self.Widgets()
        self.value_changed()


    def Widgets(self):

        self.mainframe = QFrame()

        #-----------------------------------------------#

        self.hue_label = QLabel('hue')
        self.hue_slider = QSlider(Qt.Horizontal)
        self.hue_value = QLabel()

        #-----------------------------------------------#

        self.saturation_label = QLabel('saturation')
        self.saturation_slider = QSlider(Qt.Horizontal)
        self.saturation_value = QLabel()

        #-----------------------------------------------#

        self.lightness_label = QLabel('lightness')
        self.lightness_slider = QSlider(Qt.Horizontal)
        self.lightness_value = QLabel()

        #-----------------------------------------------#

        self.line_edit = QLineEdit()

        #-----------------------------------------------#

        self.controls_frame = QFrame()

        #-----------------------------------------------#

        self.copy_button = QPushButton('copy color')

        #-----------------------------------------------#

        self.spacer = QSpacerItem(0, 0, vPolicy = QSizePolicy.Expanding)

        #-----------------------------------------------#

        self.get_data = QPushButton('Inherit color')

        #-----------------------------------------------#

        self.mainframe_vlayout = QVBoxLayout(self.mainframe)

        #-----------------------------------------------#

        self.controls_grid = QGridLayout(self.controls_frame)

        #-----------------------------------------------#

        self.main_layout = QVBoxLayout(self)

        #-----------------------------------------------#

        self.Style()


    def Style(self):


        self.hue_label.setAlignment(Qt.AlignCenter)

        self.hue_slider.setMinimum(0)
        self.hue_slider.setMaximum(359)
        self.hue_slider.setValue(0)
        self.hue_slider.valueChanged.connect(self.value_changed)
        self.hue_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.hue_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.saturation_label.setAlignment(Qt.AlignCenter)

        self.saturation_slider.setMinimum(0)
        self.saturation_slider.setMaximum(100)
        self.saturation_slider.setValue(0)
        self.saturation_slider.valueChanged.connect(self.value_changed)
        self.saturation_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.saturation_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.lightness_label.setAlignment(Qt.AlignCenter)

        self.lightness_slider.setMinimum(0)
        self.lightness_slider.setMaximum(100)
        self.lightness_slider.setValue(100)
        self.lightness_slider.valueChanged.connect(self.value_changed)
        self.lightness_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.lightness_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.setReadOnly(True)

        #-----------------------------------------------#

        self.copy_button.clicked.connect(self.copy)
        self.copy_button.setCursor(QCursor(Qt.PointingHandCursor))

        #-----------------------------------------------#

        self.get_data.clicked.connect(self.change_value)
        self.get_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.get_data.setToolTip('press to inherit the color from the previous page')

        #-----------------------------------------------#

        self.mainframe_vlayout.addWidget(self.line_edit)
        self.mainframe_vlayout.addWidget(self.copy_button, alignment=Qt.AlignCenter)
        self.mainframe_vlayout.addWidget(self.get_data, alignment=Qt.AlignCenter)
        self.mainframe_vlayout.addItem(self.spacer)
        self.mainframe_vlayout.addWidget(self.controls_frame)
        self.mainframe_vlayout.setContentsMargins(9, 18, 9, 9)

        #-----------------------------------------------#

        self.controls_grid.addWidget(self.hue_label, 0, 0)
        self.controls_grid.addWidget(self.hue_slider, 0, 1)
        self.controls_grid.addWidget(self.hue_value, 0, 2)

        self.controls_grid.addWidget(self.saturation_label, 1, 0)
        self.controls_grid.addWidget(self.saturation_slider, 1, 1)
        self.controls_grid.addWidget(self.saturation_value, 1, 2)

        self.controls_grid.addWidget(self.lightness_label, 2, 0)
        self.controls_grid.addWidget(self.lightness_slider, 2, 1)
        self.controls_grid.addWidget(self.lightness_value, 2, 2)

        #-----------------------------------------------#

        self.controls_frame.setMinimumSize(0, 150)

        #-----------------------------------------------#

        self.main_layout.addWidget(self.mainframe)


    def change_value(self):

        self.data_path = (u"c:/colorat/data.txt")

        self.data = open(self.data_path, 'r')

        Data_var = self.data.readlines()

        rgb2hsl = Color(rgb=((int(Data_var[0])/255), (int(Data_var[1])/255), (int(Data_var[2])/255)))

        self.hue_slider.setValue(int(rgb2hsl.hue * 360))
        self.saturation_slider.setValue(int(rgb2hsl.saturation * 100))
        self.lightness_slider.setValue(int(rgb2hsl.luminance * 100))

        self.data.close()


    def value_changed(self):

        hsv = self.hue_slider.value()                        # hsv = hue slider value
        ssv = self.saturation_slider.value()                 # ssv = saturation slider value
        lsv = self.lightness_slider.value()                  # lsv = lightness slider value

        rgb_color = Color(hsl=((hsv/360), (ssv/100), (lsv/100)))

        self.data_path = (u"c:/colorat/data.txt")

        self.data = open(self.data_path, 'w')
        self.data.write(f'{int(rgb_color.red * 255)}\n{int(rgb_color.green * 255)}\n{int(rgb_color.blue * 255)}\n' )
        self.data.close()


        r = rgb_color.red * 255
        g = rgb_color.green * 255
        b = rgb_color.blue * 255


        n = 0                                # n = number

        icl = [0, 0, 0]                      # icl = inverted color list
        cl = [r, g, b]                 # cl = color list

        for ic in cl:                        # ic = inverted color
            if ic > 127.5:
                fsm = abs(127.5 - ic) * 2     # fsm = first step more
                ssm = ic - fsm                 # ssm = second step more
                icl[n] = ssm
                n += 1
                if n == 3:
                    n = 0
            else:
                fsl = (127.5 - ic) * 2        # fsl = first step less
                ssl = ic + fsl                # ssl = second step less
                icl[n] = ssl
                n += 1
                if n == 3:
                    n = 0


        ir = icl[0]                           # ir = inverted red
        ig = icl[1]                           # ig = inverted green
        ib = icl[2]                           # ib = inverted blue

        self.setStyleSheet('QLabel{ \n'
                           'font-size:20px;\n'
                           'background:transparent;\n'
                           '}\n'
                           'QWidget{ \n'
                           f'background:hsl({hsv}, {ssv}%, {lsv}%);\n'
                           '}\n'
                           'QFrame{ \n'
                           f'background:hsl({hsv}, {ssv}%, {lsv}%);\n'
                           '}\n'
                           'QLineEdit{ \n'
                           'border:0px;\n'
                           'font-size:20px;\n'
                           '}\n'
                           'QSlider::handle{\n'
                           'border-radius:4px;\n'
                           'border:1.2px solid;\n'
                           '}')


        self.hue_value.setText(f'{hsv}')
        self.saturation_value.setText(f'{ssv}%')
        self.lightness_value.setText(f'{lsv}%')

        self.hue_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.saturation_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.lightness_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')

        self.line_edit.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')

        self.hue_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.saturation_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.lightness_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')



        if lsv > 50:
            self.copy_button.setStyleSheet('QPushButton{'
                                           f'color:rgb({ir}, {ig}, {ib});'
                                           'font-size:20px;'
                                           'border:1.3px solid;'
                                           'padding:5px;'
                                           'padding-top:2px;'
                                           'border-radius:5px;'
                                           'font-family: Baloo Chettan 2'
                                           '}'
                                           'QPushButton:hover{'
                                           f'background:hsl({hsv}, {ssv}%, {(lsv)-15}%)'
                                           '}'
                                           'QPushButton:pressed{'
                                           f'background:hsl({hsv}, {ssv}%, {(lsv)-30}%)'
                                           '}')

            self.get_data.setStyleSheet('QPushButton{'
                                        f'color:rgb({ir}, {ig}, {ib});'
                                        'font-size:20px;'
                                        'border:1.3px solid;'
                                        'padding:5px;'
                                        'padding-top:2px;'
                                        'border-radius:5px;'
                                        'font-family: Baloo Chettan 2'
                                        '}'
                                        'QPushButton:hover{'
                                        f'background:hsl({hsv}, {ssv}%, {(lsv)-15}%)'
                                        '}'
                                        'QPushButton:pressed{'
                                        f'background:hsl({hsv}, {ssv}%, {(lsv)-30}%)'
                                        '}')

        else:
            self.copy_button.setStyleSheet('QPushButton{'
                                           f'color:rgb({ir}, {ig}, {ib});'
                                           'font-size:20px;'
                                           'border:1.3px solid;'
                                           'padding:5px;'
                                           'padding-top:2px;'
                                           'border-radius:5px;'
                                           'font-family: Baloo Chettan 2'
                                           '}'
                                           'QPushButton:hover{'
                                           f'background:hsl({hsv}, {ssv}%, {(lsv)+15}%)'
                                           '}'
                                           'QPushButton:pressed{'
                                           f'background:hsl({hsv}, {ssv}%, {(lsv)+30}%)'
                                           '}')

            self.get_data.setStyleSheet('QPushButton{'
                                        f'color:rgb({ir}, {ig}, {ib});'
                                        'font-size:20px;'
                                        'border:1.3px solid;'
                                        'padding:5px;'
                                        'padding-top:2px;'
                                        'border-radius:5px;'
                                        'font-family: Baloo Chettan 2'
                                        '}'
                                        'QPushButton:hover{'
                                        f'background:hsl({hsv}, {ssv}%, {(lsv)+15}%)'
                                        '}'
                                        'QPushButton:pressed{'
                                        f'background:hsl({hsv}, {ssv}%, {(lsv)+30}%)'
                                        '}')


        self.line_edit.setText(f'hsl({hsv}, {ssv}%, {lsv}%)')

        self.hue_slider.setStyleSheet('QSlider::handle{background: red}')
        self.saturation_slider.setStyleSheet('QSlider::handle{background:rgb(0 , 255, 0)}')
        self.lightness_slider.setStyleSheet('QSlider::handle{background: blue}')

        self.copy_button.setMaximumSize(16777215, 30)
        self.get_data.setMaximumSize(16777215, 30)


    def copy(self):
        copy(self.line_edit.text())







class HexPage(QWidget):


    def __init__(self):
        QWidget.__init__(self)

        self.Widgets()
        self.value_changed()


    def Widgets(self):

        self.mainframe = QFrame()

        #-----------------------------------------------#

        self.red_label = QLabel('red')
        self.red_slider = QSlider(Qt.Horizontal)
        self.red_value = QLabel()

        #-----------------------------------------------#

        self.green_label = QLabel('green')
        self.green_slider = QSlider(Qt.Horizontal)
        self.green_value = QLabel()

        #-----------------------------------------------#

        self.blue_label = QLabel('blue')
        self.blue_slider = QSlider(Qt.Horizontal)
        self.blue_value = QLabel()

        #-----------------------------------------------#

        self.line_edit = QLineEdit()

        #-----------------------------------------------#

        self.controls_frame = QFrame()

        #-----------------------------------------------#

        self.copy_button = QPushButton('copy color')

        #-----------------------------------------------#

        self.spacer = QSpacerItem(0, 0, vPolicy = QSizePolicy.Expanding)

        #-----------------------------------------------#

        self.get_data = QPushButton('Inherit color')

        #-----------------------------------------------#

        self.mainframe_vlayout = QVBoxLayout(self.mainframe)

        #-----------------------------------------------#

        self.controls_grid = QGridLayout(self.controls_frame)

        #-----------------------------------------------#

        self.main_layout = QVBoxLayout(self)

        #-----------------------------------------------#

        self.Style()


    def Style(self):


        self.red_label.setAlignment(Qt.AlignCenter)

        self.red_slider.setMinimum(0)
        self.red_slider.setMaximum(255)
        self.red_slider.setValue(255)
        self.red_slider.valueChanged.connect(self.value_changed)
        self.red_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.red_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.green_label.setAlignment(Qt.AlignCenter)

        self.green_slider.setMinimum(0)
        self.green_slider.setMaximum(255)
        self.green_slider.setValue(255)
        self.green_slider.valueChanged.connect(self.value_changed)
        self.green_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.green_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.blue_label.setAlignment(Qt.AlignCenter)

        self.blue_slider.setMinimum(0)
        self.blue_slider.setMaximum(255)
        self.blue_slider.setValue(255)
        self.blue_slider.valueChanged.connect(self.value_changed)
        self.blue_slider.setCursor(QCursor(Qt.PointingHandCursor))

        self.blue_value.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------#

        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.setReadOnly(True)

        #-----------------------------------------------#

        self.controls_frame.setMinimumSize(0, 150)

        #-----------------------------------------------#

        self.copy_button.clicked.connect(self.copy)
        self.copy_button.setCursor(QCursor(Qt.PointingHandCursor))

        #-----------------------------------------------#

        self.get_data.clicked.connect(self.change_value)
        self.get_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.get_data.setToolTip('press to inherit the color from the previous page')

        #-----------------------------------------------#

        self.mainframe_vlayout.addWidget(self.line_edit)
        self.mainframe_vlayout.addWidget(self.copy_button, alignment=Qt.AlignCenter)
        self.mainframe_vlayout.addWidget(self.get_data, alignment=Qt.AlignCenter)
        self.mainframe_vlayout.addItem(self.spacer)
        self.mainframe_vlayout.addWidget(self.controls_frame)
        self.mainframe_vlayout.setContentsMargins(9, 18, 9, 9)

        #-----------------------------------------------#

        self.controls_grid.addWidget(self.red_label, 0, 0)
        self.controls_grid.addWidget(self.red_slider, 0, 1)
        self.controls_grid.addWidget(self.red_value, 0, 2)

        self.controls_grid.addWidget(self.green_label, 1, 0)
        self.controls_grid.addWidget(self.green_slider, 1, 1)
        self.controls_grid.addWidget(self.green_value, 1, 2)

        self.controls_grid.addWidget(self.blue_label, 2, 0)
        self.controls_grid.addWidget(self.blue_slider, 2, 1)
        self.controls_grid.addWidget(self.blue_value, 2, 2)

        #-----------------------------------------------#
        self.main_layout.addWidget(self.mainframe)


    def change_value(self):

        self.data_path = (u"c:/colorat/data.txt")

        self.data = open(self.data_path, 'r')

        Data_var = self.data.readlines()

        self.red_slider.setValue(int(Data_var[0]))
        self.green_slider.setValue(int(Data_var[1]))
        self.blue_slider.setValue(int(Data_var[2]))

        self.data.close()


    def value_changed(self):

        self.data_path = (u"c:/colorat/data.txt")

        self.data = open(self.data_path, 'w')
        self.data.write(f'{self.red_slider.value()}\n{self.green_slider.value()}\n{self.blue_slider.value()}\n' )
        self.data.close()


        rsv = self.red_slider.value()                      # rsv = red slider value
        gsv = self.green_slider.value()                    # gsv = green slider value
        bsv = self.blue_slider.value()                     # bsv = blue slider value

        c = Color(rgb=((rsv/255), (gsv/255), (bsv/255)))

        Hex = f'{c.hex_l}'
        hrsv = Hex[1:3]                                   # hrsv = hex red slider value
        hgsv = Hex[3:5]                                   # hgsv = hex green slider value
        hbsv = Hex[5:7]                                   # hbsv = hex blue slider value


        n = 0                                # n = number

        icl = [0, 0, 0]                      # icl = inverted color list
        cl = [rsv, gsv, bsv]                 # cl = color list

        for ic in cl:                        # ic = inverted color
            if ic > 127.5:
                fsm = abs(127.5 - ic) * 2     # fsm = first step more
                ssm = ic - fsm                 # ssm = second step more
                icl[n] = ssm
                n += 1
                if n == 3:
                    n = 0
            else:
                fsl = (127.5 - ic) * 2        # fsl = first step less
                ssl = ic + fsl                # ssl = second step less
                icl[n] = ssl
                n += 1
                if n == 3:
                    n = 0


        ir = icl[0]                           # ir = inverted red
        ig = icl[1]                           # ig = inverted green
        ib = icl[2]                           # ib = inverted blue

        self.setStyleSheet('QLabel{ \n'
                           'font-size:20px;\n'
                           'background:transparent;\n'
                           '}\n'
                           'QWidget{ \n'
                           f'background:rgb({rsv}, {gsv}, {bsv});\n'
                           '}\n'
                           'QFrame{ \n'
                           f'background:rgb({rsv}, {gsv}, {bsv});\n'
                           '}\n'
                           'QLineEdit{ \n'
                           'border:0px;\n'
                           'font-size:20px;\n'
                           '}\n'
                           'QSlider::handle{\n'
                           'border-radius:4px;\n'
                           'border:1.2px solid;\n'
                           '}')


        self.red_value.setText(f'{hrsv}')
        self.green_value.setText(f'{hgsv}')
        self.blue_value.setText(f'{hbsv}')

        self.red_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.green_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.blue_label.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')

        self.line_edit.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')

        self.red_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.green_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')
        self.blue_value.setStyleSheet(f'color:rgb({ir}, {ig}, {ib}); font-family: Baloo Chettan 2')





        if rsv|gsv|bsv > 127.5:
            self.copy_button.setStyleSheet('QPushButton{'
                                           f'color:rgb({ir}, {ig}, {ib});'
                                           'font-size:20px;'
                                           'border:1.3px solid;'
                                           'padding:5px;'
                                           'padding-top:2px;'
                                           'border-radius:5px;'
                                           'font-family: Baloo Chettan 2'
                                           '}'
                                           'QPushButton:hover{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-15}%)'
                                           '}'
                                           'QPushButton:pressed{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-30}%)'
                                           '}')

            self.get_data.setStyleSheet('QPushButton{'
                                        f'color:rgb({ir}, {ig}, {ib});'
                                        'font-size:20px;'
                                        'border:1.3px solid;'
                                        'padding:5px;'
                                        'padding-top:2px;'
                                        'border-radius:5px;'
                                        'font-family: Baloo Chettan 2'
                                        '}'
                                        'QPushButton:hover{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-15}%)'
                                        '}'
                                        'QPushButton:pressed{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)-30}%)'
                                        '}')

        else:
            self.copy_button.setStyleSheet('QPushButton{'
                                           f'color:rgb({ir}, {ig}, {ib});'
                                           'font-size:20px;'
                                           'border:1.3px solid;'
                                           'padding:5px;'
                                           'padding-top:2px;'
                                           'border-radius:5px;'
                                           'font-family: Baloo Chettan 2'
                                           '}'
                                           'QPushButton:hover{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+15}%)'
                                           '}'
                                           'QPushButton:pressed{'
                                           f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+30}%)'
                                           '}')

            self.get_data.setStyleSheet('QPushButton{'
                                        f'color:rgb({ir}, {ig}, {ib});'
                                        'font-size:20px;'
                                        'border:1.3px solid;'
                                        'padding:5px;'
                                        'padding-top:2px;'
                                        'border-radius:5px;'
                                        'font-family: Baloo Chettan 2'
                                        '}'
                                        'QPushButton:hover{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+15}%)'
                                        '}'
                                        'QPushButton:pressed{'
                                        f'background:hsl({c.hue*360}, {c.saturation*100}%, {(c.luminance*100)+30}%)'
                                        '}')



        self.line_edit.setText(f'#{hrsv}{hgsv}{hbsv}')

        self.red_slider.setStyleSheet('QSlider::handle{background: red}')
        self.green_slider.setStyleSheet('QSlider::handle{background:rgb(0 , 255, 0)}')
        self.blue_slider.setStyleSheet('QSlider::handle{background: blue}')

        self.copy_button.setMaximumSize(16777215, 30)
        self.get_data.setMaximumSize(16777215, 30)


    def copy(self):
        copy(self.line_edit.text())







class MainWindow(QWidget):

    def __init__(self):

        QWidget.__init__(self)
        self.resize(500, 500)
        self.setMinimumSize(402, 402)
        self.setWindowIcon(QIcon(u"c:/colorat/colorat logo.ico"))

        layout = QVBoxLayout(self)

        frame = QFrame(self)

        self.frame_layout = QHBoxLayout(frame)
        self.frame_layout.setContentsMargins(10, 10, 10, 0)

        self.rgb = QPushButton('RGB')
        self.Hex = QPushButton('Hex')
        self.hsl = QPushButton('HSL')


        self.rgb.setCheckable(True)
        self.Hex.setCheckable(True)
        self.hsl.setCheckable(True)

        self.rgb.setChecked(True)

        self.frame_layout.addWidget(self.hsl)
        self.frame_layout.addWidget(self.rgb)
        self.frame_layout.addWidget(self.Hex)

        self.rgb.clicked.connect(lambda: [self.stacked.setCurrentIndex(0), self.Hex.setChecked(False), self.hsl.setChecked(False)])
        self.Hex.clicked.connect(lambda: [self.stacked.setCurrentIndex(1), self.rgb.setChecked(False), self.hsl.setChecked(False)])
        self.hsl.clicked.connect(lambda: [self.stacked.setCurrentIndex(2), self.rgb.setChecked(False), self.Hex.setChecked(False)])

        self.buttons_Qss = ('QPushButton{border-radius: 5px; background: hsl(170, 0%, 75%); padding-top:5; padding-bottom:5; font-size:15px}'
                            'QPushButton:hover{background: hsl(170, 0%, 60%)}'
                            'QPushButton:pressed{background: hsl(170, 0%, 50%)}'
                            'QPushButton:checked{background:rgb(255, 114, 0);}')

        self.rgb.setStyleSheet(self.buttons_Qss)
        self.Hex.setStyleSheet(self.buttons_Qss)
        self.hsl.setStyleSheet(self.buttons_Qss)

        self.rgb.setCursor(QCursor(Qt.PointingHandCursor))
        self.Hex.setCursor(QCursor(Qt.PointingHandCursor))
        self.hsl.setCursor(QCursor(Qt.PointingHandCursor))


        self.stacked = QStackedWidget(self)
        self.stacked.setStyleSheet('border-radius:10px;')

        self.stacked.addWidget(MainRGB())
        self.stacked.addWidget(HexPage())
        self.stacked.addWidget(HSLPage())

        self.stacked.setCurrentIndex(0)

        layout.addWidget(frame)
        layout.addWidget(self.stacked)
        layout.setContentsMargins(0, 0, 0, 0)


        self.show()



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()
