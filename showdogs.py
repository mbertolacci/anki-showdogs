from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from anki.hooks import wrap

import os
import random

mw.showdogs = {}
mw.showdogs['card_count'] = 0
mw.showdogs['interval'] = 9

def showDog():
    mw.showdogs['card_count'] = mw.showdogs['card_count'] + 1
    if mw.showdogs['card_count'] % mw.showdogs['interval'] != 0:
        return

    dialog = QDialog(mw)
    layout = QVBoxLayout(dialog)
    dialog.setLayout(layout)

    dogs_dir = os.path.join(mw.pm.addonFolder(), 'showdogs')

    image_path = random.choice(os.listdir(dogs_dir))
    data = open(os.path.join(dogs_dir, image_path), 'r').read()

    image = QImage()
    image.loadFromData(data)

    label = QLabel()
    label.setPixmap(QPixmap(image))

    layout.addWidget(label)

    dialog.exec_()

mw.reviewer.nextCard = wrap(mw.reviewer.nextCard, showDog)