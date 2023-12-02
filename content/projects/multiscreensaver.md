---
title: MultiScreenSaver
date: 2023-11-28
categories:
  - software
tags:
  - GUI
  - wxWidgets
  - c++
numberifyHeadings: false
---

![](/img/multiscreensaver/logo.png)

A simple photo slideshow screensaver that is optimized to correctly work with multiple screens
with different orientations. It uses GPU rendering through direct2d with smooth scaling and
blend image transition.

<!--more-->

Portrait and landscape photo directories are configurable separately and will be displayed on
corresponding monitors in a random order.

Simple keyboard actions like pause slideshow, next/previous image are also supported.

### Links

Source: https://github.com/openscopeproject/MultiScreenSaver

Downloads: https://github.com/openscopeproject/MultiScreenSaver/releases

### Installation
Extract screensaver into a suitable location and right click → install.

To uninstall simply delete the file. If you want to delete the settings too then open regedit and delete this path: HKEY_CURRENT_USER\SOFTWARE\OpenScopeProject\MultiScreenSaver.

### Configuration
Right click → configure or go to screensaver settings in windows control panel.

![](/img/multiscreensaver/config.png)
