from PySide import QtGui, QtCore

from lu.innocence.userinterface.component.scene.abstract_layer import AbstractLayer


class SceneBackgroundWhiteLayer(AbstractLayer):
    def __init__(self, unit_width, unit_height, unit_size, parent=None):
        super(SceneBackgroundWhiteLayer, self).__init__(unit_width,
                                                        unit_height,
                                                        unit_size,
                                                        parent)

    def paint(self, painter, option, widget):
        rect = self.boundingRect()
        painter.fillRect(rect, QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0)))
        outer_bounding = QtCore.QRectF(rect.x() - 1, rect.y() - 1, rect.width() + 2, rect.height() + 2)
        painter.drawRect(outer_bounding)
