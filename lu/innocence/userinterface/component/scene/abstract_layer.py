from PySide import QtGui, QtCore


class AbstractLayer(QtGui.QGraphicsItem):

    def __init__(self, unit_width, unit_height, unit_size, parent=None):
        super(AbstractLayer, self).__init__(parent)
        self.unit_width = unit_width
        self.unit_height = unit_height
        self.unit_size = unit_size
        self.setFlag(QtGui.QGraphicsItem.ItemClipsChildrenToShape)
        self.zoom_value = 1
        self.startPosition = QtCore.QRectF()

    def setUnitSize(self, unitSize):
        self.unit_size = unitSize

    def setUnitDimension(self, unit_width, unit_height):
        self.unit_width = unit_width
        self.unit_height = unit_height

    def boundingRect(self):
        return QtCore.QRectF(0, 0,
                             self.unit_width * self.unit_size,
                             self.unit_height * self.unit_size)

    def setZoom(self, zoom):
        if zoom < 0.2:
            zoom = 0.2
        self.zoom_value = zoom

    def setRenderingStartPosition(self, startPos):
        self.startPosition.setX(startPos.x())
        self.startPosition.setY(startPos.y())

    def mouseMoveEvent(self, event):
        super(AbstractLayer, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(AbstractLayer, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        super(AbstractLayer, self).mouseRelease(event)
