def mdt_devices_detect():
    from veryeasymdt import mdtListDevices
    print("Detecting mdt devices")
    print(mdtListDevices())
    print()


def visa_devices_detect():
    import pyvisa
    print("Detecting visa devices")
    visa_rm = pyvisa.ResourceManager()
    for visa_addr in visa_rm.list_resources():
        inst = visa_rm.open_resource(visa_addr)
        print(visa_addr, inst.query("*IDN?"))
        print()


def holoeye_slm_detect():
    from holoeye import slmdisplaysdk
    print("Detecting Holoeye SLM devices (Detection window will pop up)")
    slm = slmdisplaysdk.SLMDisplay()
    print()


if __name__ == '__main__':
    mdt_devices_detect()
    visa_devices_detect()
    holoeye_slm_detect()
