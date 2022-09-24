import usb.core
import usb.util
import time
import pydirectinput
import hid2text
from config import *


class USBMapper:

    def __init__(self):
        self.key_down = []

    def on_key_down(self, keys):
        for key in keys:
            key_name = hid2text.hid_code_to_string(key)
            if key != 0 and key not in self.key_down and key_name in mapping:
                self.key_down.append(key)
                target = mapping[key_name]
                print(f'keydown {key_name} into  {target}')
                for subkey in target:
                    pydirectinput.keyDown(subkey)
                    time.sleep(KEY_STROKE_DELAY)

    def on_key_up(self, keys):
        to_remove = self.key_down.copy()
        for key in keys:
            if key != 0 and key in to_remove:
                to_remove.remove(key)

        for key in to_remove:
            key_name = hid2text.hid_code_to_string(key)
            self.key_down.remove(key)
            target = mapping[key_name].copy()
            print(f'keyup {key_name} into {target}')
            target.reverse()
            for subkey in target:
                pydirectinput.keyUp(subkey)
                time.sleep(KEY_STROKE_DELAY)

    def init(self):
        self.dev = usb.core.find(
            idVendor=USB_VENDOR_ID, idProduct=USB_PRODUCT_ID)
        self.endpoint = self.dev[0][(0, 0)][0]

    def loop(self):
        while True:
            control = None

            try:
                control = self.dev.read(self.endpoint.bEndpointAddress,
                                        self.endpoint.wMaxPacketSize, USB_TIMEOUT)
            except:
                pass

            if control != None:
                mods = control[0]
                keys = control[2:]
                all_keys = hid2text.mods_to_keys(mods) + list(keys)
                self.on_key_down(all_keys)
                self.on_key_up(all_keys)

            time.sleep(0.01)

if __name__ == "__main__":
    mapper = USBMapper()
    mapper.init()
    mapper.loop()