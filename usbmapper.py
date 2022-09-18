import usb.core
import usb.util
import time
import pydirectinput
import hid2text
from config import *

key_down = []


def mods_to_keys(mods):
    result = []
    for i in range(8):
        if (mods & (1 << i)) > 0:
            result.append(224 + i)
    return result


def on_key_down(keys):
    for key in keys:
        key_name = hid2text.hid_code_to_string(key)
        if key != 0 and key not in key_down and key_name in mapping:
            key_down.append(key)
            target = mapping[key_name]
            print(f'keydown {key_name} into  {target}')
            for subkey in target:
                pydirectinput.keyDown(subkey)
                time.sleep(KEY_STROKE_DELAY)


def on_key_up(keys):
    to_remove = key_down.copy()
    for key in keys:
        if key != 0 and key in to_remove:
            to_remove.remove(key)

    for key in to_remove:
        key_name = hid2text.hid_code_to_string(key)
        key_down.remove(key)
        target = mapping[key_name].copy()
        print(f'keyup {key_name} into {target}')
        target.reverse()
        for subkey in target:
            pydirectinput.keyUp(subkey)
            time.sleep(KEY_STROKE_DELAY)


dev = usb.core.find(idVendor=USB_VENDOR_ID, idProduct=USB_PRODUCT_ID)
endpoint = dev[0][(0, 0)][0]

while True:
    control = None

    try:
        control = dev.read(endpoint.bEndpointAddress,
                           endpoint.wMaxPacketSize, USB_TIMEOUT)
    except:
        pass

    if control != None:
        mods = control[0]
        keys = control[2:]
        all_keys = mods_to_keys(mods) + list(keys)
        on_key_down(all_keys)
        on_key_up(all_keys)

    time.sleep(0.01)
