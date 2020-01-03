from veryeasymdt import *
from holoeye import slmdisplaysdk
import pyvisa
import numpy as np
from utils import ascii_list_to_ndarray, extract_effi_ct, extract_ave_effi
import time


class AutoAlignment:
    def __init__(self, mdt_serial0, mdt_serial1, slm_datafiles, ks_mppm_addr, powermeter_ports, **kwargs):
        # connect the Thorlabs piezo controllers
        self.mdt0 = MDT(mdt_serial0)
        self.mdt1 = MDT(mdt_serial1)
        self.mdt0.SetAllVoltage(20)
        self.mdt1.SetAllVoltage(20)
        self.__current_set_voltages = [20] * 6
        self.limit_voltages = self.get_limit_voltages()

        # connect Holoeye SLM
        self.slm = slmdisplaysdk.SLMDisplay()
        self.slm.utilsSLMPreviewShow()
        self.slm_datafiles = slm_datafiles
        self.slm_data_handles = self.slm_preload_data_from_file()
        self.slmErrorCode = slmdisplaysdk.SLMDisplay.ErrorCode
        self.slmShowFlags = slmdisplaysdk.SLMDisplay.ShowFlags

        # connect the Keysight multiport powermeter
        visa_rm = pyvisa.ResourceManager()
        self.ks_mppm = visa_rm.open_resource(ks_mppm_addr)
        self.ks_mppm.query('*IDN?')
        self.ks_mppm.write('*RST')
        self.ks_mppm.query('*TST?')
        self.ports_pyindices = np.array(powermeter_ports) - 1
        self.nport = len(powermeter_ports)

        # other parameters
        self.best_ave_effi = 0
        self.best_voltages = [0] * 6

        time.sleep(1)

    def get_current_set_voltages(self):
        return self.__current_set_voltages

    def slm_preload_data_from_file(self):
        handles = []
        for df in slm_datafiles:
            error, hd = self.slm.loadDataFromFile(df)
            assert error == self.slmErrorCode.NoError, self.slm.errorString(error)
            handles.append(hd)
        return handles

    def get_power(self):
        power_ascii = self.ks_mppm.query('fetch:power:all:csv?')
        power = np.fromstring(power_ascii, count=8, sep=',')
        return power

    def get_transfer_matrix(self):
        tm = np.zeros((self.nport, self.nport))
        for i, handle in self.slm_data_handles:
            self.slm.showDatahandle(handle)
            tm[i, :] = self.get_power()
        return tm

    def step_optimize_xp0(self, step):
        current = self.mdt0.GetXYZAxisVoltage()
        self.mdt0.SetXAxisVoltage(current + step)

    def step_optimize(self, step):

        # to get the current transfer matrix, average efficiency and set voltages
        transfer_matrix = self.get_transfer_matrix()
        ave_effi = extract_ave_effi(transfer_matrix)
        previous_set_voltages = self.__current_set_voltages.copy()
        current_set_voltages = self.__current_set_voltages

        # to move forward and backward along every axis and compare the average efficiency
        operations = [self.mdt0.SetXAxisVoltage,
                      self.mdt0.SetYAxisVoltage,
                      self.mdt0.SetZAxisVoltage,
                      self.mdt1.SetXAxisVoltage,
                      self.mdt1.SetYAxisVoltage,
                      self.mdt1.SetZAxisVoltage]
        dev_ax = [0, 1, 2, 3, 4, 5]
        for op, dev_ax in zip(operations, dev_ax):
            new_voltage_f = current_set_voltages[dev_ax] + step
            op(new_voltage_f)
            new_transfer_matrix_f = self.get_transfer_matrix()
            new_ave_effi_f = extract_ave_effi(new_transfer_matrix_f)

            new_voltage_b = current_set_voltages[dev_ax] - step
            op(new_voltage_b)
            new_transfer_matrix_b = self.get_transfer_matrix()
            new_ave_effi_b = extract_ave_effi(new_transfer_matrix_b)

            effi_argmax = np.argmax([new_ave_effi_f, new_ave_effi_b, ave_effi])
            if effi_argmax == 0:
                current_set_voltages[dev_ax] = new_voltage_f
            elif effi_argmax == 1:
                current_set_voltages[dev_ax] = new_voltage_b
            op(current_set_voltages[dev_ax])

        # to check whether the current efficiency is better than the previous best
        new_transfer_matrix = self.get_transfer_matrix()
        new_ave_effi = extract_ave_effi(new_transfer_matrix)
        if new_ave_effi > self.best_ave_effi:
            self.best_ave_effi = new_ave_effi
            self.best_voltages = self.__current_set_voltages

        if current_set_voltages == previous_set_voltages:
            return False
        else:
            return True

    def get_limit_voltages(self):
        m0 = self.mdt0
        m1 = self.mdt1
        limit_voltages = np.array([[m0.GetXAxisMinVoltage(), m0.GetXAxisMaxVoltage()],
                                   [m0.GetYAxisMinVoltage(), m0.GetYAxisMaxVoltage()],
                                   [m0.GetZAxisMinVoltage(), m0.GetZAxisMaxVoltage()],
                                   [m1.GetXAxisMinVoltage(), m1.GetXAxisMaxVoltage()],
                                   [m1.GetYAxisMinVoltage(), m1.GetYAxisMaxVoltage()],
                                   [m1.GetZAxisMinVoltage(), m1.GetZAxisMaxVoltage()]])
        return limit_voltages

    def update_limit_voltages(self):
        self.limit_voltages = self.get_limit_voltages

    def randomize(self):
        m0 = self.mdt0
        m1 = self.mdt1
        lv = self.limit_voltages

        x0 = np.random.uniform(lv[0, 0], lv[0, 1])
        m0.SetXAxisVoltage(x0)
        y0 = np.random.uniform(lv[1, 0], lv[1, 1])
        m0.SetYAxisVoltage(y0)
        z0 = np.random.uniform(lv[2, 0], lv[2, 1])
        m0.SetYAxisVoltage(z0)
        x1 = np.random.uniform(lv[3, 0], lv[3, 1])
        m1.SetXAxisVoltage(x1)
        y1 = np.random.uniform(lv[4, 0], lv[4, 1])
        m1.SetYAxisVoltage(y1)
        z1 = np.random.uniform(lv[5, 0], lv[5, 1])
        m1.SetYAxisVoltage(z1)

        self.__current_set_voltages = [x0, y0, z0, x1, y1, z1]


if __name__ == '__main__':
    mdt_serial0 = ''
    mdt_serial1 = ''
    ks_mppm_addr = ''
    slm_datafiles = []
    powermeter_ports = [1, 2, 3, 4, 5, 6, 7]
    step = 0.2
    epoch = 5

    aa = AutoAlignment(mdt_serial0, mdt_serial1, slm_datafiles, ks_mppm_addr, powermeter_ports)
    for ep in range(epoch):
        if aa.step_optimize(step):
            aa.randomize()
