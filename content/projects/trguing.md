---
title: TrguiNG
date: 2023-11-28
categories:
  - software
tags:
  - transmission
  - GUI
  - torrents
  - rust
  - typescript
  - tauri
post:
  params:
    numberifyHeadings: false
menu:
  main:
    identifier: trguing
    weight: 1
    params:
      # icon: '<i class="fas fa-fw fa-blog"></i>'
      description: 'TrguiNG'
summary: |
  <img src="/img/trguing/screenshots/1.png" />
  <p>Multiplatform remote GUI for transmission torrent daemon.</p>
  <p>Written in Rust and Typescript/React using Tauri framework and Mantine UI library.</p>
---

TrguiNG is a multiplatform remote GUI for [transmission](https://transmissionbt.com) torrent daemon
written in Rust and Typescript/React using Tauri framework and Mantine UI library.

You can use this program in 2 ways: as a native Windows/Linux/Mac app and as a web gui served by transmission itself by setting `$TRANSMISSION_WEB_HOME` environment variable to point to TrguiNG web assets.

**Features**

* Multi tabbed interface for concurrent server connections (native app only)
* Torrent creation with fast multi threaded hashing (native app only)
* Powerful torrent filtering options
* Efficient network usage
* Configurable path mappings to directly access torrent files if their location is mounted locally (native app only)
* Latest transmission features support: labels, bandwidth groups, sequential download
* Dark/light/custom theme support

**Links**

Source code:
https://github.com/openscopeproject/TrguiNG

Downloads for windows/mac/debian/web:
https://github.com/openscopeproject/TrguiNG/releases

Flathub:
https://flathub.org/apps/org.openscopeproject.TrguiNG

Arch AUR:
https://aur.archlinux.org/packages/trgui-ng

**Screenshots**

![Main window](/img/trguing/screenshots/1.png "Main window")
![Adding a torrent](/img/trguing/screenshots/2.png "Adding a torrent")
![Dark theme, peers tab](/img/trguing/screenshots/3.png "Dark theme, peers tab")
![Creating new torrent](/img/trguing/screenshots/4.png "Creating new torrent")
![Torrent properties](/img/trguing/screenshots/5.png "Torrent properties")
![Server settings](/img/trguing/screenshots/6.png "Server settings")
