from PySide import QtCore
from PySide import QtGui

from lu.innocence.userinterface.component.scene.MouseCursorLayer import MouseCursorLayer
from lu.innocence.userinterface.component.scene.Scene import Scene
from lu.innocence.userinterface.component.scene.SceneBackgroundWhiteLayer import SceneBackgroundWhiteLayer
from lu.innocence.userinterface.component.scene.TileLayer import TileLayer
from lu.innocence.userinterface.component.scene.Tileset import Tileset


class SceneCanvas(QtGui.QGraphicsView):

    def __init__(self, parent=0):
        super(SceneCanvas, self).__init__(parent)
        self.setMouseTracking(True)
        self.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.zoom_value = 250
        self.current_scene = None

    def leaveEvent(self, event):
        if self.current_scene is not None:
            self.current_scene.mouseLeaveEvent()

    def enterEvent(self, event):
        if self.current_scene is not None:
            self.current_scene.mouseEnterEvent()

    def wheelEvent(self, event):
        if QtGui.QApplication.keyboardModifiers() & QtCore.Qt.ControlModifier:
            if event.delta() > 0:
                self.zoom_value += 6
                if 500 < self.zoom_value:
                    self.zoom_value = 500
                else:
                    if 0 < self.zoom_value:
                        self.zoom_value = 0
            self.setup_matrix()
        else:
            super(SceneCanvas, self).wheelEvent(event)

    def scrollContentsBy(self, dx, dy):

        super(SceneCanvas, self).scrollContentsBy(dx, dy)
        if self.current_scene is not None:
            scale = pow(2, (self.zoom_value - 250) / 50)
            if scale < 0.2:
                scale = 0.2

            t_x = self.horizontalScrollBar().value()
            t_y = self.verticalScrollBar().value()

            self.current_scene.changeViewport(QtCore.QPointF(t_x, t_y), scale)
            self.current_scene.update(t_x, t_y, self.width() / scale, self.height() / scale)

    def setup_matrix(self):

        if self.current_scene is not None:
            scale = pow(2, (self.zoom_value - 250) / 50)
            if scale < 0.2:
                scale = 0.2

            t_x = self.horizontalScrollBar().value()
            t_y = self.verticalScrollBar().value()
            self.current_scene.changeViewport(QtCore.QPointF(t_x, t_y), scale)

            matrix = QtGui.QMatrix()
            matrix.scale(scale, scale)
            self.setMatrix(matrix)

    def init(self):

        mapWidth = 250
        mapHeight = 250
        tileDim = 32

        self.current_scene = Scene(self)

        background = SceneBackgroundWhiteLayer(mapWidth, mapHeight, tileDim)
        tileLayer = TileLayer(mapWidth, mapHeight, tileDim)
        tileLayer2 = TileLayer(mapWidth, mapHeight, tileDim)
        tileLayer3 = TileLayer(mapWidth, mapHeight, tileDim)
        tileLayer4 = TileLayer(mapWidth, mapHeight, tileDim)
        mouseCursor = MouseCursorLayer(mapWidth, mapHeight, tileDim)

        self.current_scene.addLayer(background)
        self.current_scene.addLayer(tileLayer)
        self.current_scene.addLayer(tileLayer2)
        self.current_scene.addLayer(tileLayer3)
        self.current_scene.addLayer(tileLayer4)
        self.current_scene.addLayer(mouseCursor)

        # Dummy
        desert_tileset = Tileset("desert.png", 32)

        tileLayer.addTileset(desert_tileset)
        tileLayer2.addTileset(desert_tileset)
        tileLayer3.addTileset(desert_tileset)
        tileLayer4.addTileset(desert_tileset)
        mouseCursor.setCurrentTileset(desert_tileset)

        t_x = 0
        t_y = 0

        for i in range(0, mapWidth):
            t_x = 0 if t_x == 7 else t_x + 1
            for j in range(0, mapHeight):
                t_y = 0 if t_y == 14 else t_y + 1

                # tileLayer->addTileAt(i,j,0,1,0)
                # Worst Case
                tileLayer.addTileAt(i, j, 0, t_x, t_y)
                tileLayer2.addTileAt(i, j, 0, t_x, t_y)
                tileLayer3.addTileAt(i, j, 0, t_x, t_y)
                tileLayer4.addTileAt(i, j, 0, t_x, t_y)
        # Dummy end
        self.setScene(self.current_scene)
        self.setSceneRect(0, 0, tileDim * mapWidth, tileDim * mapHeight)
        self.centerOn(0, 0)
