import yaml

USB_TIMEOUT = 5  # Timeout in MS

def load_config(filename):
    with open(filename, "r") as content:
        config = yaml.safe_load(content)

        devices = []
        for device_id in config['devices']:
            device = config['devices'][device_id]
            devices.append(Device(device_id, device['name'], device['vid'], device['pid'], device['mappings']))

        return Config(config.get("key_stroke_delay", None) or 0.1, devices)

class Device:
    def __init__(self, id, name, vid, pid, mappings):
        self.id = id
        self.name = name
        self.vid = vid
        self.pid = pid
        self.mappings = mappings

class Config:
    def __init__(self, key_stroke_delay, devices):
        self.key_stroke_delay = key_stroke_delay
        self.devices = devices
