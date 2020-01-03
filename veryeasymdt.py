from ctypes import *
from os import getcwd

# region import dll functions

mdtLib = cdll.LoadLibrary(getcwd() + "\\MDT_COMMAND_LIB_x64.dll")
cmdOpen = mdtLib.Open
cmdOpen.restype = c_int
cmdOpen.argtypes = [c_char_p, c_int, c_int]

cmdIsOpen = mdtLib.IsOpen
cmdOpen.restype = c_int
cmdOpen.argtypes = [c_char_p]

cmdList = mdtLib.List
cmdList.argtypes = [c_char_p]
cmdList.restype = c_int

cmdGetId = mdtLib.GetId
cmdGetId.restype = c_int
cmdGetId.argtypes = [c_int, c_char_p]

cmdGetLimtVoltage = mdtLib.GetLimitVoltage
cmdGetLimtVoltage.restype = c_int
cmdGetLimtVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetAllVoltage = mdtLib.SetAllVoltage
cmdSetAllVoltage.restype = c_int
cmdSetAllVoltage.argtypes = [c_int, c_double]

cmdGetMasterScanEnable = mdtLib.GetMasterScanEnable
cmdGetMasterScanEnable.restype = c_int
cmdGetMasterScanEnable.argtypes = [c_int, POINTER(c_int)]

cmdSetMasterScanEnable = mdtLib.SetMasterScanEnable
cmdSetMasterScanEnable.restype = c_int
cmdSetMasterScanEnable.argtypes = [c_int, c_int]

cmdGetMasterScanVoltage = mdtLib.GetMasterScanVoltage
cmdGetMasterScanVoltage.restype = c_int
cmdGetMasterScanVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetMasterScanVoltage = mdtLib.SetMasterScanVoltage
cmdSetMasterScanVoltage.restype = c_int
cmdSetMasterScanVoltage.argtypes = [c_int, c_double]

cmdGetXAxisVoltage = mdtLib.GetXAxisVoltage
cmdGetXAxisVoltage.restype = c_int
cmdGetXAxisVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetXAxisVoltage = mdtLib.SetXAxisVoltage
cmdSetXAxisVoltage.restype = c_int
cmdSetXAxisVoltage.argtypes = [c_int, c_double]

cmdGetYAxisVoltage = mdtLib.GetYAxisVoltage
cmdGetYAxisVoltage.restype = c_int
cmdGetYAxisVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetYAxisVoltage = mdtLib.SetYAxisVoltage
cmdSetYAxisVoltage.restype = c_int
cmdSetYAxisVoltage.argtypes = [c_int, c_double]

cmdGetZAxisVoltage = mdtLib.GetZAxisVoltage
cmdGetZAxisVoltage.restype = c_int
cmdGetZAxisVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetZAxisVoltage = mdtLib.SetZAxisVoltage
cmdSetZAxisVoltage.restype = c_int
cmdSetZAxisVoltage.argtypes = [c_int, c_double]

cmdGetXAxisMinVoltage = mdtLib.GetXAxisMinVoltage
cmdGetXAxisMinVoltage.restype = c_int
cmdGetXAxisMinVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetXAxisMinVoltage = mdtLib.SetXAxisMinVoltage
cmdSetXAxisMinVoltage.restype = c_int
cmdSetXAxisMinVoltage.argtypes = [c_int, c_double]

cmdGetYAxisMinVoltage = mdtLib.GetYAxisMinVoltage
cmdGetYAxisMinVoltage.restype = c_int
cmdGetYAxisMinVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetYAxisMinVoltage = mdtLib.SetYAxisMinVoltage
cmdSetYAxisMinVoltage.restype = c_int
cmdSetYAxisMinVoltage.argtypes = [c_int, c_double]

cmdGetZAxisMinVoltage = mdtLib.GetZAxisMinVoltage
cmdGetZAxisMinVoltage.restype = c_int
cmdGetZAxisMinVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetZAxisMinVoltage = mdtLib.SetZAxisMinVoltage
cmdSetZAxisMinVoltage.restype = c_int
cmdSetZAxisMinVoltage.argtypes = [c_int, c_double]

cmdGetXAxisMaxVoltage = mdtLib.GetXAxisMaxVoltage
cmdGetXAxisMaxVoltage.restype = c_int
cmdGetXAxisMaxVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetXAxisMaxVoltage = mdtLib.SetXAxisMaxVoltage
cmdSetXAxisMaxVoltage.restype = c_int
cmdSetXAxisMaxVoltage.argtypes = [c_int, c_double]

cmdGetYAxisMaxVoltage = mdtLib.GetYAxisMaxVoltage
cmdGetYAxisMaxVoltage.restype = c_int
cmdGetYAxisMaxVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetYAxisMaxVoltage = mdtLib.SetYAxisMaxVoltage
cmdSetYAxisMaxVoltage.restype = c_int
cmdSetYAxisMaxVoltage.argtypes = [c_int, c_double]

cmdGetZAxisMaxVoltage = mdtLib.GetZAxisMaxVoltage
cmdGetZAxisMaxVoltage.restype = c_int
cmdGetZAxisMaxVoltage.argtypes = [c_int, POINTER(c_double)]

cmdSetZAxisMaxVoltage = mdtLib.SetZAxisMaxVoltage
cmdSetZAxisMaxVoltage.restype = c_int
cmdSetZAxisMaxVoltage.argtypes = [c_int, c_double]

cmdGetVoltageAdjustmentResolution = mdtLib.GetVoltageAdjustmentResolution
cmdGetVoltageAdjustmentResolution.restype = c_int
cmdGetVoltageAdjustmentResolution.argtypes = [c_int, POINTER(c_int)]

cmdSetVoltageAdjustmentResolution = mdtLib.SetVoltageAdjustmentResolution
cmdSetVoltageAdjustmentResolution.restype = c_int
cmdSetVoltageAdjustmentResolution.argtypes = [c_int, c_int]

cmdGetXYZAxisVoltage = mdtLib.GetXYZAxisVoltage
cmdGetXYZAxisVoltage.restype = c_int
cmdGetXYZAxisVoltage.argtypes = [c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

cmdSetXYZAxisVoltage = mdtLib.SetXYZAxisVoltage
cmdSetXYZAxisVoltage.restype = c_int
cmdSetXYZAxisVoltage.argtypes = [c_int, c_double, c_double, c_double]


# region command for MDT694B(X-AXIS) and MDT693B(X-AXIS, Y-AXIS, Z-AXIS)
def mdtListDevices():
    """ List all connected MDT devices
    Returns:
       The mdt device list, each deice item is [serialNumber, mdtType]
    """
    str = create_string_buffer(1024, '\0')
    result = cmdList(str)
    devicesStr = str.raw.decode("utf-8").rstrip('\x00').split(',')
    length = len(devicesStr)
    i = 0
    devices = []
    devInfo = ["", ""]
    MDTTypeList = ["MDT693B", "MDT694B"]
    while (i < length):
        str = devicesStr[i]
        if (i % 2 == 0):
            if str != '':
                devInfo[0] = str
            else:
                i += 1
        else:
            isFind = False
            for mt in MDTTypeList:
                if (str.find(mt) >= 0):
                    str = mt
                    isFind = True
                    break
            if (isFind):
                devInfo[1] = str
                devices.append(devInfo.copy())
        i += 1
    return devices


def mdtOpen(serialNo, nBaud, timeout):
    """ Open MDT device
    Args:
        serialNo: serial number of MDT device
        nBaud: bit per second of port
        timeout: set timeout value in (s)
    Returns:
        non-negative number: hdl number returned Successful; negative number: failed.
    """
    return cmdOpen(serialNo.encode('utf-8'), nBaud, timeout)


def mdtIsOpen(serialNo):
    """ Check opened status of MDT device
    Args:
        serialNo: serial number of MDT device
    Returns:
        0: MDT device is not opened; 1: MDT device is opened.
    """
    return cmdIsOpen(serialNo.encode('utf-8'))


def mdtGetId(hdl, id):
    """ Get the product header and firmware version
    Args:
        hdl: the handle of opened MDT device
        id: the output id string
    Returns:
        0: Success; negative number: failed.
    """
    idStr = create_string_buffer(1024, '\0')
    ret = cmdGetId(hdl, idStr)
    id.append(idStr.raw.decode("utf-8").rstrip('\x00'))
    return ret


def mdtGetLimtVoltage(hdl, voltage):
    """ Get output voltage limit setting.
    Args:
        hdl: the handle of opened MDT device
        voltage: the output voltage
    Returns:
        0: Success; negative number: failed.
    """
    vol = c_double(0)
    ret = cmdGetLimtVoltage(hdl, vol)
    voltage[0] = vol.value
    return ret


def mdtCommonFunc(serialNumber):
    hdl = mdtOpen(serialNumber, 115200, 3)
    # or check by "mdtIsOpen(devs[0])"
    if (hdl < 0):
        print("Connect ", serialNumber, "fail")
        return -1
    else:
        print("Connect ", serialNumber, "successful")

    result = mdtIsOpen(serialNumber)
    print("mdtIsOpen ", result)

    id = []
    result = mdtGetId(hdl, id)
    if (result < 0):
        print("mdtGetId fail ", result)
    else:
        print(id)

    limitVoltage = [0]
    result = mdtGetLimtVoltage(hdl, limitVoltage)
    if (result < 0):
        print("mdtGetLimtVoltage fail ", result)
    else:
        print("mdtGetLimtVoltage ", limitVoltage)
    return hdl, id, limitVoltage


class MDT:
    def __init__(self, serial):
        self.serial = serial
        self.hdl, self.id, self.limt_voltage = mdtCommonFunc(serial)

    def Close(self):
        """ Close opened MDT device

        Returns:
            0: Success; negative number: failed.
        """
        ret = mdtLib.Close(self.hdl)
        if ret < 0:
            print("mdtClose fail ", ret)
        return None

    def GetXAxisVoltage(self):
        """ Get the X axis output voltage.
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetXAxisVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetXAxisVoltage fail ", ret)
        return vol.value

    def SetXAxisVoltage(self, voltage):
        """ Set the output voltage for the X axis.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetXAxisVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetXAxisVoltage fail ", ret)
        return None

    def GetXAxisMinVoltage(self):
        """ Get the minimum output voltage limit for X axis.
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetXAxisMinVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetXAxisMinVoltage fail ", ret)
        return vol.value

    def SetXAxisMinVoltage(self, voltage):
        """ Set the minimum output voltage limit for X axis.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetXAxisMinVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetXAxisMinVoltage fail ", ret)
        return None

    def GetXAxisMaxVoltage(self):
        """ Get the maximum output voltage limit for X axis.
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetXAxisMaxVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetXAxisMaxVoltage fail ", ret)
        return vol.value

    def SetXAxisMaxVoltage(self, voltage):
        """ Set the maximum output voltage limit for X axis.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetXAxisMaxVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetXAxisMaxVoltage fail ", ret)
        return None

    def GetVoltageAdjustmentResolution(self):
        """ Get the current step resolution.
        Returns:
            0: Success; negative number: failed.
        """
        sa = c_int(0)
        ret = cmdGetVoltageAdjustmentResolution(self.hdl, sa)
        if ret < 0:
            print("mdtGetVoltageAdjustmentResolution fail ", ret)
        return sa.value

    def SetVoltageAdjustmentResolution(self, step):
        """ Set the step resolution when using up/down arrow keys.
        Args:
            step: target step range:(1 ~ 1000)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetVoltageAdjustmentResolution(self.hdl, step)
        if ret < 0:
            print("mdtSetVoltageAdjustmentResolution fail ", ret)
        return None

    # region only for MDT693B(X-AXIS, Y-AXIS, Z-AXIS)
    def GetYAxisVoltage(self):
        """ Get the Y axis output voltage.
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetYAxisVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetYAxisVoltage fail ", ret)
        return vol.value

    def SetYAxisVoltage(self, voltage):
        """ Set the output voltage for the Y axis.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetYAxisVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetYAxisVoltage fail ", ret)
        return None

    def GetYAxisMinVoltage(self):
        """ Get the minimum output voltage limit for Y axis.
        Args:
            hdl: the handle of opened MDT device
            voltage: the output voltage
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetYAxisMinVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetYAxisMinVoltage fail ", ret)
        return vol.value

    def SetYAxisMinVoltage(self, voltage):
        """ Set the minimum output voltage limit for Y axis.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetYAxisMinVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetYAxisMinVoltage fail ", ret)
        return None

    def GetYAxisMaxVoltage(self):
        """ Get the maximum output voltage limit for Y axis.
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetYAxisMaxVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetYAxisMaxVoltage fail ", ret)
        return vol.value

    def SetYAxisMaxVoltage(self, voltage):
        """ Set the maximum output voltage limit for Y axis.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetYAxisMaxVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetYAxisMaxVoltage fail ", ret)
        return None

    def GetZAxisVoltage(self):
        """ Get the Z axis output voltage.
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetZAxisVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetZAxisVoltage fail ", ret)
        return vol.value

    def SetZAxisVoltage(self, voltage):
        """ Set the output voltage for the Z axis.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetZAxisVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetZAxisVoltage fail ", ret)
        return None

    def GetZAxisMinVoltage(self):
        """ Get the minimum output voltage limit for Z axis.
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetZAxisMinVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetZAxisMinVoltage fail ", ret)
        return vol.value

    def SetZAxisMinVoltage(self, voltage):
        """ Set the minimum output voltage limit for Z axis.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetZAxisMinVoltage(hdl, voltage)
        if ret < 0:
            print("mdtSetZAxisMinVoltage fail ", ret)
        return

    def GetZAxisMaxVoltage(self):
        """ Get the maximum output voltage limit for Z axis.
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetZAxisMaxVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetZAxisMaxVoltage fail ", ret)
        return vol.value

    def SetZAxisMaxVoltage(self, voltage):
        """ Set the maximum output voltage limit for Z axis.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetZAxisMaxVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetZAxisMaxVoltage fail ", ret)
        return None

    def GetXYZAxisVoltage(self):
        """ Get the x,y,z axis output voltages.
        Args:
            xyzVoltage: the output x,y,z axis voltage
        Returns:
            0: Success; negative number: failed.
        """
        volX = c_double(0)
        volY = c_double(0)
        volZ = c_double(0)
        ret = cmdGetXYZAxisVoltage(self.hdl, volX, volY, volZ)
        if ret < 0:
            print("mdtGetXYZAxisVoltage fail ", ret)
        return volX.value, volY.value, volZ.value

    def SetXYZAxisVoltage(self, xVoltage, yVoltage, zVoltage):
        """ Set the x,y,z axis output voltages.
        Args:
            hdl: the handle of opened MDT device
            xVoltage: the x axis input voltage range:(0 ~ limit voltage)
            yVoltage: the y axis input voltage range:(0 ~ limit voltage)
            zVoltage: the z axis input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetXYZAxisVoltage(self.hdl, xVoltage, yVoltage, zVoltage)
        if ret < 0:
            print("mdtSetXYZAxisVoltage fail ", ret)
        return None

    def SetAllVoltage(self, voltage):
        """ Set all outputs to desired voltage.
        Args:
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetAllVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetAllVoltage fail ", ret)
        return None

    def GetMasterScanEnable(self):
        """ Get the state of the Master Scan enable.
        Returns:
            0: Success; negative number: failed.
        """
        sa = c_int(0)
        ret = cmdGetMasterScanEnable(self.hdl, sa)
        if ret < 0:
            print("mdtGetMasterScanEnable fail ", ret)
        return sa.value

    def SetMasterScanEnable(self, state):
        """ Set Master Scan mode.
        Args:
            state: current master scan state.(1-enable,0-disable)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetMasterScanEnable(self.hdl, state)
        if ret < 0:
            print("mdtSetMasterScanEnable fail ", ret)
        return None

    def GetMasterScanVoltage(self):
        """ Get the master scan voltage.
        Args:
            voltage: the output voltage
        Returns:
            0: Success; negative number: failed.
        """
        vol = c_double(0)
        ret = cmdGetMasterScanVoltage(self.hdl, vol)
        if ret < 0:
            print("mdtGetMasterScanVoltage fail ", ret)
        return vol.value

    def SetMasterScanVoltage(self, voltage):
        """ Set a master scan voltage that adds to the x, y, and z axis voltages.
        Args:
            hdl: the handle of opened MDT device
            voltage: the input voltage range:(0 ~ limit voltage)
        Returns:
            0: Success; negative number: failed.
        """
        ret = cmdSetMasterScanVoltage(self.hdl, voltage)
        if ret < 0:
            print("mdtSetMasterScanVoltage fail ", ret)
        return None

    def SetVoltage(self, axis, voltage):
        if (axis == 'x') or (axis == 'X'):
            self.SetXAxisVoltage(voltage)
        elif (axis == 'y') or (axis == 'Y'):
            self.SetYAxisVoltage(voltage)
        elif (axis == 'z') or (axis == 'Z'):
            self.SetZAxisVoltage(voltage)
        else:
            raise ValueError('Parameter axis should be "x", "y", or "z", either in lowercase or uppercase.')
