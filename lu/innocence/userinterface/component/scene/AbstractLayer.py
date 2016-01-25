from PySide import QtGui, QtCore


class AbstractLayer(QtGui.QGraphicsItem):

    def __init__(self, unit_width, unit_height, unit_size, parent):
        super(AbstractLayer, self).__init__(parent)
        self.unit_width = unit_width
        self.unit_height = unit_height
        self.unit_size = unit_size
        self.setFlag(QtGui.QGraphicsItem.ItemClipsChildrenToShape)

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
            self.zoom = 0.2
            m_zoom = zoom

    def setRenderingStartPosition(self, startPos):
        self.startPosition.setX(startPos.x())
        self.startPosition.setY(startPos.y())

    def mouseMoveEvent(self, event):
        super(QtGui.QGraphicsItem, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        super(QtGui.QGraphicsItem, self).mousePressEvent(event)

    def mouseReleaseEvent(self,event):
        super(QtGui.QGraphicsItem, self).mouseRelease(event)
