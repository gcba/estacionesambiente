#!/usr/bin/env python
from conf import config
from Tkinter import *
import ScrolledText as tkst

# !/usr/bin/python
from Tkinter import *
import time
import datetime
from conf import config


stationName = "La Boca"



qSensors = 1


class gui(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.buttons = []
        self.sLabels = []
        self.protocol("WM_DELETE_WINDOW", self.iconify)
        self.bind('<Escape>', lambda e: self.goodByeL())
        self.create()

    def create(self):
        self.geometry('400x%d' % ((len(config.sensors_st)*25)+82))
        self.columnconfigure(0, weight=1, minsize=200)
        self.resizable(width=FALSE, height=FALSE)
        self.grid()

        i = 1
        t = Label(self, text="Available Sensors in: %s" % config.EPAStationName, anchor="w", fg="black")

        t.grid(column=0, row=0, sticky="EW")
        for key, value in config.sensors_st.iteritems():
            bgColor = "white" if value == config.sensor_online else "red"
            bst = "Runnig..." if value == config.sensor_online else "Calibration"
            self.sLabels.append(
                Label(self, text='Sensor: %s | Status: %s' % (key, bst), bg="%s" % bgColor, fg="black", anchor="w",
                      width=50))
            self.sLabels[i - 1].grid(column=0, row=i, padx=(2, 2), sticky='EW')
            self.buttons.append(Button(self, text="%s" % bst, fg="black", width=10,
                                       command=lambda i=i, key=key: self.OnButtonClick(i, key)))
            self.buttons[i - 1].grid(column=3, row=i, padx=(2, 2), sticky="EW")
            i += 1
        self.console = tkst.ScrolledText(self, wrap='word', height=5, width=50, bg='black', fg='green')
        self.console.grid(column=None, row=i, sticky=EW, rowspan=2, columnspan=2, padx=(5, 5), pady=(5, 5))
        self.console.config(state=DISABLED)
        gb = Button(self, text="EXIT!", fg="black", command=self.goodByeL)
        gb.grid(column=3, row=i, padx=(2,2), pady=(5,5), sticky=W+E+N+S)

    def OnButtonClick(self, bId, sensor):
        i = int(bId)
        config.sensors_st[sensor] = config.sensor_online if config.sensors_st[sensor] == config.sensor_offline else config.sensor_offline
        bgColor = "white" if config.sensors_st[sensor] == config.sensor_online else "red"
        bst = "Runnig..." if config.sensors_st[sensor] == config.sensor_online else "Calibration"
        self.buttons[i - 1] = Button(self, text="%s" % bst, fg="black", width=10,
                                     command=lambda i=i, sensor=sensor: self.OnButtonClick(i, sensor))
        self.buttons[i - 1].grid(column=3, row=i, padx=(2, 2), sticky='EW')
        self.sLabels[i - 1] = Label(self, text='Sensor: %s | Status: %s' % (sensor, bst), bg=bgColor, fg="black",
                                    anchor="w", width=50)
        self.sLabels[i - 1].grid(column=0, row=i, padx=(2, 2), sticky='EW')
        msg = "[%s] SENSOR: %s id:%d change to: %s \n" % (
            datetime.datetime.fromtimestamp(time.time()).strftime('%Y/%m/%d %H:%M:%S'), sensor, (i), bst)
        self.console.config(state=NORMAL)
        self.console.insert(INSERT, msg)
        config.log.add("INFO: Sensor \"%s\"[%d] change status to: \"%s\"" % (sensor, i, bst) )
        self.console.config(state=DISABLED)

    def goodByeL(self):
        self.destroy()

