import usb.core
import usb.util
import time
import pydirectinput
import hid2text
import config


class USBMapper:

    def __init__(self, config):
        self.key_down = []
        self.config = config

    def on_key_down(self, keys, device):
        for key in keys:
            key_name = hid2text.hid_code_to_string(key)
            if key != 0 and key not in self.key_down and key_name in device.mappings:
                self.key_down.append(key)
                target = device.mappings[key_name]
                print(f'keydown {key_name} into {target}')
                for subkey in target:
                    pydirectinput.keyDown(subkey)
                    time.sleep(self.config.key_stroke_delay)

    def on_key_up(self, keys, device):
        to_remove = self.key_down.copy()
        for key in keys:
            if key != 0 and key in to_remove:
                to_remove.remove(key)

        for key in to_remove:
            key_name = hid2text.hid_code_to_string(key)
            self.key_down.remove(key)
            target = device.mappings[key_name].copy()
            print(f'keyup {key_name} into {target}')
            target.reverse()
            for subkey in target:
                pydirectinput.keyUp(subkey)
                time.sleep(self.config.key_stroke_delay)

    def init(self, device):
        self.dev = usb.core.find(
            idVendor=int(device.vid, base=16), idProduct=int(device.pid, base=16))
        self.endpoint = self.dev[0][(0, 0)][0]

    def loop(self, device):
        while True:
            control = None

            try:
                control = self.dev.read(self.endpoint.bEndpointAddress,
                                        self.endpoint.wMaxPacketSize, config.USB_TIMEOUT)
            except usb.core.USBTimeoutError:
                pass

            if control != None:
                mods = control[0]
                keys = control[2:]
                all_keys = hid2text.mods_to_keys(mods) + list(keys)
                self.on_key_down(all_keys, device)
                self.on_key_up(all_keys, device)

            time.sleep(0.01)

if __name__ == "__main__":
    _config = config.load_config("config.yaml")
    mapper = USBMapper(_config)
    mapper.init(_config.devices[0])
    mapper.loop(_config.devices[0])