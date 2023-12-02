---
title: Keithley 1950 option
date: 2023-12-02
categories:
  - hardware
tags:
  - keithley195a
numberifyHeadings: false
summary: |
  <img src="https://i.imgur.com/0c3jkUk.png" />
  <p>
    Replacement DC/AC Amps and AC TRMS Volts option for Keithley
    Instruments 195A Digital Multimeter.
  </p>
---

Keithley Instruments 195A Digital Multimeter is a 5½ digit resolution 200 000
count instrument that was manufactured in the 80's, possibly early 90's. It was
available in two configurations: base model that only had DC Volts and Ohms
measurements and model with 1950 option, which added DC/AC Amps and AC TRMS
Volts measurements.

Keithley DMM line has long replaced 195/196/199 series with newer models but
these still show up on Ebay and other outlets and they offer great performance
for reasonable prices. Unfortunately most of the 195A models available online
are the ones without 1950 Option.

This project aims to recreate the 1950 Option PCB and circuitry using modern
components.

In the process some upgrades and some compromises were made. For example this
version of 1950 option board is based on AD8436 TRMS chip that along with newer
opamps provides higher bandwidth and better overall specs than much older AD536
of the original. On the other hand cheaper shunt resistors are used (because
of their availability) with worse drift and tempco characteristics.

{{% alert warning %}}
**High voltage** operation using the new board is **NOT** recommended or
tested.
{{% /alert %}}

---

### Links

[Hardware (KiCad files and gerbers)](https://github.com/openscopeproject/Keithley1950)

[Bill of materials](https://openscopeproject.org/InteractiveHtmlBomDemo/html/Keithley1950.html)

## Pictures

![img](https://i.imgur.com/aX9WxCY.png?width=300px "schematic")

![img](https://i.imgur.com/0c3jkUk.png?width=300px "3D render")

![img](https://i.imgur.com/UacUyqy.jpg?width=300px "End result installed in the meter")

![img](https://i.imgur.com/7FVghgY.jpg?width=300px "Original board next to new version")

![img](https://i.imgur.com/l0e0v63.jpg?width=300px "Genuine Bodge™ on the rev A board")
