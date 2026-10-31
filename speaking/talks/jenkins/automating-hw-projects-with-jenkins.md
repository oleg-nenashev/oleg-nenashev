---
title: "Automating Hardware/Embedded Projects with Jenkins"
description: "Using Jenkins for CI and delivery in open-source hardware and FPGA projects."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - embedded
  - hardware
  - ci-cd
author: oleg_nenashev
speakerdeckId: a7bb233dfd784919bc8c6369201dc5d0
youtubeId: D9Wxvex8o4E
youtube: https://www.youtube.com/watch?v=D9Wxvex8o4E
speakerdeck: https://speakerdeck.com/onenashev/orconf2016-automating-hw-projects-with-jenkins
references:
  - name: "Video"
    url: "https://www.youtube.com/watch?v=D9Wxvex8o4E"
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/orconf2016-automating-hw-projects-with-jenkins"
  - name: "Embedded Testing Conference 2015 materials"
    url: "https://www.embedded-testing.de/archiv/vortragsunterlagen-2015.html"
  - name: "Jenkins blog post on pipelines for hardware"
    url: "https://www.jenkins.io/blog/2016/04/07/pipeline-for-runs-on-hardware/"
presented:
  - event: "ORCONF"
    year: 2016
  - event: "Embedded Testing Conference"
    year: 2015
    location: "Munich"
---

Jenkins is one of the leading open-source automation servers. It’s a framework, which can be adjusted to a particular area with help of its flexibility and plugin system. Many open-source hardware and embedded projects build their Continuous Integration and Delivery flows with Jenkins, because there is not so many tools in the area.

In the talk I would like to cover common use-cases of Jenkins in hardware projects like integration with EDA tools and hardware peripherals like FPGAs and reporting of build, test and coverage reports. After that I’ll share one of two case studies about integration of Jenkins into hardware projects. If I achieve something presentable with the ongoing project by the conference, one of the case studies will be about FuseSoC integration with Jenkins.
