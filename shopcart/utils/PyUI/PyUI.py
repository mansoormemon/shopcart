import os
import importlib.resources

from PyQt6.QtCore import QDir, Qt
from PyQt6.QtWidgets import (
    QWidgetAction,
    QApplication,
    QCheckBox,
    QComboBox,
    QGraphicsDropShadowEffect,
    QLabel,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QTextEdit,
    QWidget
)


###############################
# Application
###############################

class Application(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pkg_root = os.path.dirname(os.path.abspath(__file__))
        QDir.addSearchPath('resources', f'{pkg_root}/res')

        with importlib.resources.open_text(f'{__package__}.res.stylesheets', "default.qss") as stylesheet_file:
            stylesheet = stylesheet_file.read()

        self.setStyleSheet(stylesheet)


###############################
# Push Buttons
###############################

class PushButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setCursor(Qt.CursorShape.PointingHandCursor)


class PrimaryButton(PushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SecondaryButton(PushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SuccessButton(PushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WarningButton(PushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ErrorButton(PushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


###############################
# Check Box
###############################

class CheckBox(QCheckBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setCursor(Qt.CursorShape.PointingHandCursor)


###############################
# Radio Button
###############################

class RadioButton(QRadioButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setCursor(Qt.CursorShape.PointingHandCursor)


###############################
# Combo Box
###############################

class ComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.view().window().setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint)
        self.view().window().setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.view().window().setStyleSheet(
            ''' 
                QComboBox QFrame {
                    background-color: transparent;
                    padding: 7.5px;
                }
                
                QComboBox QAbstractItemView { 
                    background-color: #ffffff;
                }
            '''
        )
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(0, 0)
        effect.setBlurRadius(6)
        effect.setColor(Qt.GlobalColor.gray)
        self.view().window().setGraphicsEffect(effect)


###############################
# Labels
###############################

class SuccessLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WarningLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ErrorLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


###############################
# Paragraph
###############################

class Paragraph(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setReadOnly(True)
        self.setAlignment(Qt.AlignmentFlag.AlignJustify)


###############################
# Progress Bar
###############################

class ProgressBar(QProgressBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setTextVisible(False)


###############################
# Card
###############################

class Card(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
