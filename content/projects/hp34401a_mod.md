---
title: HP 34401a OLED display mod
date: 2023-12-02
categories:
  - hardware
tags:
  - display mod
  - 34401a
  - c++
numberifyHeadings: false
summary: |
  <img src="https://i.imgur.com/FP5pQ6R.jpg" />
  <p>OLED display replacement for HP's legendary 34401a 6½ digit multimeter.</p>
---

Many of the old meters in 34401a series are still in great working condition,
however their aging VFD displays are failing in various ways. Low contrast,
leaking current in segment drivers, shattered glass are frequent cause of
these excellent devices being written off.

While replacement VFDs are still sold on some markets, they are not cheap and
getting them intact in mail is a lottery. Also replacing the VFD itself does not
always resolve the issue since in some cases it's the driver IC that is at fault.

On older issue 34401a meters (fw version 06-04-01 and prior) have a custom HP
designed micro controller with integrated high voltage VFD driver which is not
obtainable, unless bought as a whole front panel assembly, which again is not cheap.

This mod sniffs on the SPI bus of the front panel and draws the display data
on a modern OLED display. It is a direct replacement for the hard to source
original VFD displays.

### Links

[Hardware (KiCad files and gerbers)](https://github.com/openscopeproject/HP34401a-OLED-HW)

[Bill of materials](https://openscopeproject.org/InteractiveHtmlBomDemo/hp34401a_oled/ibom.html)

[Firmware (c++, built with platformio)](https://github.com/openscopeproject/HP34401a-OLED-FW)

[Prebuilt firmware blobs](https://github.com/openscopeproject/HP34401a-OLED-FW/releases)

[EEVBlog thread with history of the project](https://www.eevblog.com/forum/repair/hp-34401a-dmm-with-leaking-segments/)


### Pictures

![proof of concept](https://i.imgur.com/AId0xw1.jpg?width=300px "proof of concept")

![first prototype](https://i.imgur.com/bZpQViy.jpg?width=300px "first prototype")

![final product](https://i.imgur.com/FP5pQ6R.jpg?width=300px "final product")

### Schematic and PCB
![schematic](https://github.com/openscopeproject/HP34401a-OLED-HW/raw/master/schematic.png?width=300px)

![pcb render](https://github.com/openscopeproject/HP34401a-OLED-HW/raw/master/render.png?width=300px)
