#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class radar_lite_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "radar_lite_test")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.frequency = frequency = 800000000
        self.bandwidth = bandwidth = 100000
        self.TargetVelocity = TargetVelocity = 1
        self.LowPassFilter = LowPassFilter = (1,0)

        ##################################################
        # Blocks
        ##################################################
        # Create the options list
        self._frequency_options = [800000000, 1200000000, 1800000000]
        # Create the labels list
        self._frequency_labels = ['800MHz', '1200MHz', '1800MHz']
        # Create the combo box
        # Create the radio buttons
        self._frequency_group_box = Qt.QGroupBox("'frequency'" + ": ")
        self._frequency_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._frequency_button_group = variable_chooser_button_group()
        self._frequency_group_box.setLayout(self._frequency_box)
        for i, _label in enumerate(self._frequency_labels):
            radio_button = Qt.QRadioButton(_label)
            self._frequency_box.addWidget(radio_button)
            self._frequency_button_group.addButton(radio_button, i)
        self._frequency_callback = lambda i: Qt.QMetaObject.invokeMethod(self._frequency_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._frequency_options.index(i)))
        self._frequency_callback(self.frequency)
        self._frequency_button_group.buttonClicked[int].connect(
            lambda i: self.set_frequency(self._frequency_options[i]))
        self.top_layout.addWidget(self._frequency_group_box)
        # Create the options list
        self._bandwidth_options = [100000, 200000, 500000]
        # Create the labels list
        self._bandwidth_labels = ['100KHz', '200KHz', '500KHz']
        # Create the combo box
        # Create the radio buttons
        self._bandwidth_group_box = Qt.QGroupBox("'bandwidth'" + ": ")
        self._bandwidth_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._bandwidth_button_group = variable_chooser_button_group()
        self._bandwidth_group_box.setLayout(self._bandwidth_box)
        for i, _label in enumerate(self._bandwidth_labels):
            radio_button = Qt.QRadioButton(_label)
            self._bandwidth_box.addWidget(radio_button)
            self._bandwidth_button_group.addButton(radio_button, i)
        self._bandwidth_callback = lambda i: Qt.QMetaObject.invokeMethod(self._bandwidth_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._bandwidth_options.index(i)))
        self._bandwidth_callback(self.bandwidth)
        self._bandwidth_button_group.buttonClicked[int].connect(
            lambda i: self.set_bandwidth(self._bandwidth_options[i]))
        self.top_layout.addWidget(self._bandwidth_group_box)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            bandwidth, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                bandwidth,
                bandwidth/10,
                bandwidth/10,
                window.WIN_HAMMING,
                6.76))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, bandwidth,True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(bandwidth, analog.GR_COS_WAVE, frequency, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)
        # Create the options list
        self._TargetVelocity_options = [1, 2, 3]
        # Create the labels list
        self._TargetVelocity_labels = ['Velocity 1', 'Velocity 2', 'Velocity 3']
        # Create the combo box
        # Create the radio buttons
        self._TargetVelocity_group_box = Qt.QGroupBox("'TargetVelocity'" + ": ")
        self._TargetVelocity_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._TargetVelocity_button_group = variable_chooser_button_group()
        self._TargetVelocity_group_box.setLayout(self._TargetVelocity_box)
        for i, _label in enumerate(self._TargetVelocity_labels):
            radio_button = Qt.QRadioButton(_label)
            self._TargetVelocity_box.addWidget(radio_button)
            self._TargetVelocity_button_group.addButton(radio_button, i)
        self._TargetVelocity_callback = lambda i: Qt.QMetaObject.invokeMethod(self._TargetVelocity_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._TargetVelocity_options.index(i)))
        self._TargetVelocity_callback(self.TargetVelocity)
        self._TargetVelocity_button_group.buttonClicked[int].connect(
            lambda i: self.set_TargetVelocity(self._TargetVelocity_options[i]))
        self.top_layout.addWidget(self._TargetVelocity_group_box)
        # Create the options list
        self._LowPassFilter_options = [(1, 0), (0, 1)]
        # Create the labels list
        self._LowPassFilter_labels = ['Yes', 'No']
        # Create the combo box
        # Create the radio buttons
        self._LowPassFilter_group_box = Qt.QGroupBox("'LowPassFilter'" + ": ")
        self._LowPassFilter_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._LowPassFilter_button_group = variable_chooser_button_group()
        self._LowPassFilter_group_box.setLayout(self._LowPassFilter_box)
        for i, _label in enumerate(self._LowPassFilter_labels):
            radio_button = Qt.QRadioButton(_label)
            self._LowPassFilter_box.addWidget(radio_button)
            self._LowPassFilter_button_group.addButton(radio_button, i)
        self._LowPassFilter_callback = lambda i: Qt.QMetaObject.invokeMethod(self._LowPassFilter_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._LowPassFilter_options.index(i)))
        self._LowPassFilter_callback(self.LowPassFilter)
        self._LowPassFilter_button_group.buttonClicked[int].connect(
            lambda i: self.set_LowPassFilter(self._LowPassFilter_options[i]))
        self.top_layout.addWidget(self._LowPassFilter_group_box)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "radar_lite_test")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self._frequency_callback(self.frequency)
        self.analog_sig_source_x_0.set_frequency(self.frequency)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self._bandwidth_callback(self.bandwidth)
        self.analog_sig_source_x_0.set_sampling_freq(self.bandwidth)
        self.blocks_throttle_0.set_sample_rate(self.bandwidth)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.bandwidth, self.bandwidth/10, self.bandwidth/10, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.bandwidth)

    def get_TargetVelocity(self):
        return self.TargetVelocity

    def set_TargetVelocity(self, TargetVelocity):
        self.TargetVelocity = TargetVelocity
        self._TargetVelocity_callback(self.TargetVelocity)

    def get_LowPassFilter(self):
        return self.LowPassFilter

    def set_LowPassFilter(self, LowPassFilter):
        self.LowPassFilter = LowPassFilter
        self._LowPassFilter_callback(self.LowPassFilter)




def main(top_block_cls=radar_lite_test, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
