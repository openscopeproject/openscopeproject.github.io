---
title: TransformIt
date: 2023-12-01
categories:
  - software
tags:
  - kicad
  - plugin
  - python
  - GUI
numberifyHeadings: false
---

![](/img/transformit/logo.png)

KiCad plugin to resize, scale and mirror graphics, tracks, zones, footprints
and other items in the PCB editor.

Inspired by free transform tool in graphics editors.

<!--more-->

Important notes:

* Mirror does not change layers, it transforms in place
* When a singular footprint is selected it's items are scaled so the footprint itself will become larger/smaller
* When more than one item is selected footprints are not changed or rescaled, only repositioned/rotated
* Pads are not rescaled, only repositioned/rotated
* Rotation center is geometrical center of combined bounding box of all selected items

Recommended way to get this plugin is to install it from KiCad's plugin manager.


### Links

Source: https://github.com/openscopeproject/TransformIt
