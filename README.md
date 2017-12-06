# AutoTouchpad
Automatically turn off tap to click while typing on Ubuntu. Ctrl, Shift and Alt keys are excluded but their combinations are not, i.e. Alt + Tab still disable touchpad for 1 second. 

The program use `xinput` to listen for keystrokes and disable the touchpad for 1 second after a normal key is pressed.
You need to run `xinput list` to determine the id of your keyboard and replace the 17 in command `xinput test 17` with the id you found.

Example output of `xinput list` is
```
xinput list
⎡ Virtual core pointer                      id=2    [master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer                id=4    [slave  pointer  (2)]
⎜   ↳ Microsoft Microsoft® Nano Transceiver v1.0    id=11   [slave  pointer  (2)]
⎜   ↳ Microsoft Microsoft® Nano Transceiver v1.0    id=12   [slave  pointer  (2)]
⎜   ↳ DLL082A:01 06CB:76AF Touchpad             id=14   [slave  pointer  (2)]
⎜   ↳ SynPS/2 Synaptics TouchPad                id=18   [slave  pointer  (2)]
⎣ Virtual core keyboard                     id=3    [master keyboard (2)]
    ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
    ↳ Power Button                              id=6    [slave  keyboard (3)]
    ↳ Video Bus                                 id=7    [slave  keyboard (3)]
    ↳ Power Button                              id=8    [slave  keyboard (3)]
    ↳ Sleep Button                              id=9    [slave  keyboard (3)]
    ↳ Microsoft Microsoft® Nano Transceiver v1.0    id=10   [slave  keyboard (3)]
    ↳ Integrated_Webcam_HD                      id=13   [slave  keyboard (3)]
    ↳ Intel Virtual Button driver               id=15   [slave  keyboard (3)]
    ↳ Intel HID events                          id=16   [slave  keyboard (3)]
    **↳ AT Translated Set 2 keyboard                id=17   [slave  keyboard (3)]**
    ↳ Dell WMI hotkeys                          id=19   [slave  keyboard (3)]
    ↳ Microsoft Microsoft® Nano Transceiver v1.0    id=20   [slave  keyboard (3)]
```
