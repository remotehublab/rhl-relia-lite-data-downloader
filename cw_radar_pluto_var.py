#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Cw Radar Pluto Var
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
from gnuradio import iio



from gnuradio import qtgui

class cw_radar_pluto_var(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Cw Radar Pluto Var", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Cw Radar Pluto Var")
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

        self.settings = Qt.QSettings("GNU Radio", "cw_radar_pluto_var")

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
        self.samp_rate = samp_rate = 600000
        self.my_path = my_path = "/home/rhlab/Downloads/files/"
        self.freq_op = freq_op = 1600000000
        self.fan_vel = fan_vel = 3
        self.filename_tx = filename_tx = str(my_path)+"tx-freq-"+str(int(freq_op/1000000))+"-velocity-"+str(fan_vel)+"-bw-"+str(int(samp_rate/1000))
        self.filename_lpf_y = filename_lpf_y = str(my_path)+"rx-freq-"+str(int(freq_op/1000000))+"-velocity-"+str(fan_vel)+"-bw-"+str(int(samp_rate/1000))+"-lpf-y"
        self.filename_lpf_n = filename_lpf_n = str(my_path)+"rx-freq-"+str(int(freq_op/1000000))+"-velocity-"+str(fan_vel)+"-bw-"+str(int(samp_rate/1000))+"-lpf-n"
        self.dec = dec = 1024*4
        self.addr = addr = "192.168.2.1"

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_2_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate/dec, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_2_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_2_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_2_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_2_0.enable_grid(False)
        self.qtgui_freq_sink_x_2_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_2_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_2_0.set_fft_window_normalized(False)



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
                self.qtgui_freq_sink_x_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_2_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_2_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_2_0_win)
        self.qtgui_freq_sink_x_2 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate/dec, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_2.set_update_time(0.10)
        self.qtgui_freq_sink_x_2.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_2.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2.enable_autoscale(True)
        self.qtgui_freq_sink_x_2.enable_grid(False)
        self.qtgui_freq_sink_x_2.set_fft_average(1.0)
        self.qtgui_freq_sink_x_2.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2.enable_control_panel(False)
        self.qtgui_freq_sink_x_2.set_fft_window_normalized(False)



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
                self.qtgui_freq_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_2_win = sip.wrapinstance(self.qtgui_freq_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_2_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            dec,
            firdes.low_pass(
                1,
                samp_rate,
                80,
                100,
                window.WIN_HAMMING,
                6.76))
        self.iio_pluto_source_0 = iio.fmcomms2_source_fc32(addr if addr else iio.get_pluto_uri(), [True, True], 32768)
        self.iio_pluto_source_0.set_len_tag_key('packet_len')
        self.iio_pluto_source_0.set_frequency(freq_op)
        self.iio_pluto_source_0.set_samplerate(samp_rate)
        self.iio_pluto_source_0.set_gain_mode(0, 'slow_attack')
        self.iio_pluto_source_0.set_gain(0, 64)
        self.iio_pluto_source_0.set_quadrature(True)
        self.iio_pluto_source_0.set_rfdc(True)
        self.iio_pluto_source_0.set_bbdc(True)
        self.iio_pluto_source_0.set_filter_params('Auto', '', 0, 0)
        self.iio_pluto_sink_0 = iio.fmcomms2_sink_fc32(addr if addr else iio.get_pluto_uri(), [True, True], 32768, False)
        self.iio_pluto_sink_0.set_len_tag_key('')
        self.iio_pluto_sink_0.set_bandwidth(1000000)
        self.iio_pluto_sink_0.set_frequency(freq_op)
        self.iio_pluto_sink_0.set_samplerate(samp_rate)
        self.iio_pluto_sink_0.set_attenuation(0, 0)
        self.iio_pluto_sink_0.set_filter_params('Auto', '', 0, 0)
        # Create the options list
        self._fan_vel_options = [1, 2, 3]
        # Create the labels list
        self._fan_vel_labels = ['Vel 1', 'Vel 2', 'Vel 3']
        # Create the combo box
        self._fan_vel_tool_bar = Qt.QToolBar(self)
        self._fan_vel_tool_bar.addWidget(Qt.QLabel("velocity of fan" + ": "))
        self._fan_vel_combo_box = Qt.QComboBox()
        self._fan_vel_tool_bar.addWidget(self._fan_vel_combo_box)
        for _label in self._fan_vel_labels: self._fan_vel_combo_box.addItem(_label)
        self._fan_vel_callback = lambda i: Qt.QMetaObject.invokeMethod(self._fan_vel_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._fan_vel_options.index(i)))
        self._fan_vel_callback(self.fan_vel)
        self._fan_vel_combo_box.currentIndexChanged.connect(
            lambda i: self.set_fan_vel(self._fan_vel_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._fan_vel_tool_bar)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, str(filename_tx), False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, str(filename_lpf_n), False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, str(filename_lpf_y), False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0, 0)
        self.analog_agc_xx_0_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0_0.set_max_gain(65536)
        self.analog_agc_xx_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.analog_agc_xx_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.iio_pluto_sink_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.qtgui_freq_sink_x_2_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.analog_agc_xx_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_2, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "cw_radar_pluto_var")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_filename_lpf_n(str(self.my_path)+"rx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000))+"-lpf-n")
        self.set_filename_lpf_y(str(self.my_path)+"rx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000))+"-lpf-y")
        self.set_filename_tx(str(self.my_path)+"tx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000)))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.iio_pluto_sink_0.set_samplerate(self.samp_rate)
        self.iio_pluto_source_0.set_samplerate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 80, 100, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_2.set_frequency_range(0, self.samp_rate/self.dec)
        self.qtgui_freq_sink_x_2_0.set_frequency_range(0, self.samp_rate/self.dec)

    def get_my_path(self):
        return self.my_path

    def set_my_path(self, my_path):
        self.my_path = my_path
        self.set_filename_lpf_n(str(self.my_path)+"rx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000))+"-lpf-n")
        self.set_filename_lpf_y(str(self.my_path)+"rx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000))+"-lpf-y")
        self.set_filename_tx(str(self.my_path)+"tx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000)))

    def get_freq_op(self):
        return self.freq_op

    def set_freq_op(self, freq_op):
        self.freq_op = freq_op
        self.set_filename_lpf_n(str(self.my_path)+"rx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000))+"-lpf-n")
        self.set_filename_lpf_y(str(self.my_path)+"rx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000))+"-lpf-y")
        self.set_filename_tx(str(self.my_path)+"tx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000)))
        self.iio_pluto_sink_0.set_frequency(self.freq_op)
        self.iio_pluto_source_0.set_frequency(self.freq_op)

    def get_fan_vel(self):
        return self.fan_vel

    def set_fan_vel(self, fan_vel):
        self.fan_vel = fan_vel
        self._fan_vel_callback(self.fan_vel)
        self.set_filename_lpf_n(str(self.my_path)+"rx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000))+"-lpf-n")
        self.set_filename_lpf_y(str(self.my_path)+"rx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000))+"-lpf-y")
        self.set_filename_tx(str(self.my_path)+"tx-freq-"+str(int(self.freq_op/1000000))+"-velocity-"+str(self.fan_vel)+"-bw-"+str(int(self.samp_rate/1000)))

    def get_filename_tx(self):
        return self.filename_tx

    def set_filename_tx(self, filename_tx):
        self.filename_tx = filename_tx
        self.blocks_file_sink_0_0_0.open(str(self.filename_tx))

    def get_filename_lpf_y(self):
        return self.filename_lpf_y

    def set_filename_lpf_y(self, filename_lpf_y):
        self.filename_lpf_y = filename_lpf_y
        self.blocks_file_sink_0.open(str(self.filename_lpf_y))

    def get_filename_lpf_n(self):
        return self.filename_lpf_n

    def set_filename_lpf_n(self, filename_lpf_n):
        self.filename_lpf_n = filename_lpf_n
        self.blocks_file_sink_0_0.open(str(self.filename_lpf_n))

    def get_dec(self):
        return self.dec

    def set_dec(self, dec):
        self.dec = dec
        self.qtgui_freq_sink_x_2.set_frequency_range(0, self.samp_rate/self.dec)
        self.qtgui_freq_sink_x_2_0.set_frequency_range(0, self.samp_rate/self.dec)

    def get_addr(self):
        return self.addr

    def set_addr(self, addr):
        self.addr = addr




def main(top_block_cls=cw_radar_pluto_var, options=None):

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
