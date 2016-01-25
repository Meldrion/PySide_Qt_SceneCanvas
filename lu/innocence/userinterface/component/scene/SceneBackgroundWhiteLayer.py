from PySide import QtGui

from lu.innocence.userinterface.component.scene.AbstractLayer import AbstractLayer


class SceneBackgroundWhiteLayer(AbstractLayer):

    def __init__(self, unit_width, unit_height, unit_size, parent=0):
        super(SceneBackgroundWhiteLayer, self).__init__(unit_width,
                                                        unit_height,
                                                        unit_size,
                                                        parent)

    def paint(self, painter, option, widget):
        rect = self.boundingRect()
        painter.fillRect(rect, QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0)))
        self.outerBounding(rect.x() - 1, rect.y() - 1,
                           rect.width() + 2, rect.height() + 2)
        painter.drawRect(self.outerBounding)
