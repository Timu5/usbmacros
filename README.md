# USBMacros

Simple tool to map second usb keyboard keys to some key combinations, useful everywhere you may need some extra buttons e.g. flight simulators.

This tool exist as I couldn't find any tools that would work propertly with DCS.


## How it works

It's directly communicating with usb keyboard by bypassing system HID keyboard driver with libusb(WinUSB to be specific). 

New inputs are send throught SendInput API.

## How to use

Install WinUSB driver using zadig for specific keyboard, after that keyboard will no longer be detected as input device. 

Install dependencies: 
```sh
pip install pyusb libusb pydirectinput
```

Modify config.py to match your needs, especialy mappings(see hid2tex.py for possible keys).

Run as administrator:
```
python usbmapper.py
```
