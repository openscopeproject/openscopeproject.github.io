---
title: InteractiveHtmlBom
date: 2023-11-25
categories:
  - software
tags:
  - kicad
  - plugin
  - python
  - GUI
  - CLI
menu:
  main:
    identifier: ibom
    weight: 1
    params:
      # icon: '<i class="fas fa-fw fa-blog"></i>'
      description: InteractiveHtmlBom
summary: |
  <img src="/img/ibom/logo.png" />
  <p>Python app for generating interactive Bill of Materials (BOM) for electronics PCBs.</p>
  <p>
    Designed as a helper for manual assembly this tool allows you to search components,
    quickly find their placement on the PCB, mark your progress as you solder components.
    It can also highlight nets for troubleshooting and tracing where the signals go.</p>
  <p>
    Initially written as a KiCad plugin it currently also supports Eagle, Fusion360,
    Allegro PCB Designer and EasyEDA.
  </p>
---

InteractiveHtmlBom (ibom for short) is a BOM tool for various electronics CAD packages designed
to make manual assembly easier. It also serves as an excellent troubleshooting and documentation aid.

Initially written as KiCad plugin it currently also supports Eagle, Fusion360,
Allegro PCB Designer and EasyEDA.

This tool generates a convenient Bill of Materials (BOM) listing with the ability to visually
correlate and easily search for components and their placements on the PCB. It is particularly
useful when hand-soldering a prototype, as it allows users to quickly find locations of
components groups on the board. It is also possible to reverse lookup the component group
by clicking on a footprint on the board drawing.

There is an option to include tracks/zones data as well as netlist information allowing dynamic
highlight of nets on the board. This feature is particularly useful for troubleshooting the prototype.

Generated html page is fully self contained, doesn't need internet connection to work and can
be packaged with documentation of your project or hosted anywhere on the web.

**Links**

Source: https://github.com/openscopeproject/InteractiveHtmlBom

Demos: https://openscopeproject.org/InteractiveHtmlBomDemo/

Wiki with installation instructions and other useful info:

https://github.com/openscopeproject/InteractiveHtmlBom/wiki

**Gif demo**

This is from a pre-release version. Much more functionality was added since, check the demos link above.

![demo](https://openscopeproject.org/InteractiveHtmlBomDemo/gif/capture.gif)