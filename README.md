# USBMacros

Simple tool to map second usb keyboard keys to some key combinations, useful everywhere you may need some extra buttons e.g. flight simulators.

This tool exist as I couldn't find any tools that would work propertly with DCS.


## How it works

It's directly communicating with usb keyboard by bypassing system HID keyboard driver with libusb(WinUSB to be specific). 

New inputs are send throught SendInput API.

## Limitations

Currently only one keyboard is supported.

## How to use

Install WinUSB driver using [zadig](https://zadig.akeo.ie/) for specific keyboard, after that keyboard will no longer be detected as input device. 

Download latest release from [releases](https://github.com/Timu5/usbmacros/releases).

Modify config.yaml to match your needs, especialy keyboard vendor id, product id and mappings.

Run `usbmacro.exe`


## How to run from source

Install dependencies: 
```sh
pip install pyusb libusb pydirectinput
```

Run as administrator:
```sh
python usbmapper.py
```


