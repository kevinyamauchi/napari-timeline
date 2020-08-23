import sys
import numpy as np

from vispy import scene, plot

from qtpy.QtCore import Qt, QSize
from qtpy import QtWidgets

from napari.layers import Shapes
from napari._vispy.vispy_shapes_layer import VispyShapesLayer

from timeline._vispy.plot_widget import PlotWidget


class QtPlotWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.canvas = scene.SceneCanvas(bgcolor='k', keys=None, vsync=True)
        self.canvas.native.setMinimumSize(QSize(300, 100))
        self.canvas.connect(self.on_mouse_press)
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().addWidget(self.canvas.native)

        self.plot = self.canvas.central_widget.add_widget(
            PlotWidget(fg_color='w', lock_axis=1)
        )

        #self.plot.histogram(np.random.randn(10000), bins=100, color='b')
        # the histogram is just an example, but the axes alone are sufficient:
        self.plot._configure_2d()

        shapes_coords = 10 * np.random.random((1000, 4, 2))

        self.shapes = Shapes(shapes_coords, edge_color=[0, 0, 0, 0])
        self.shapes.selected_data = []
        self.shapes_view = VispyShapesLayer(self.shapes)
        self.plot.view.add(self.shapes_view.node)

    def on_mouse_press(self, event):
        print(event)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700, 500)
        dock_widget = QtWidgets.QDockWidget(self)
        self.plot = QtPlotWidget()
        dock_widget.setWidget(self.plot)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock_widget)


if __name__ == '__main__':

    appQt = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    appQt.exec_()