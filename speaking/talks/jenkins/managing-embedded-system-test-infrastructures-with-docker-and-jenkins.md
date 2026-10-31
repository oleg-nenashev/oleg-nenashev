---
title: "Managing Embedded System test infrastructures with Docker and Jenkins"
description: "When and how to use Docker and Jenkins in embedded and hardware-in-the-loop testing."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - embedded
  - docker
  - jenkins
  - testing
  - hardware
author: oleg_nenashev
speakerdeckId: 69a185bdb1f946428b08b1510bb01bb0
speakerdeck: https://speakerdeck.com/onenashev/managing-embedded-system-test-infrastructures-with-docker-and-jenkins
references:
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/managing-embedded-system-test-infrastructures-with-docker-and-jenkins"
presented:
  - event: "Embedded Conference Scandinavia"
    year: 2017
  - event: "CloudBees Automotive Day"
    year: 2018
---

Virtualization and Containerization are one of the hottest areas in the test automation of software systems. 

Such approaches simplify management of test environments, reduce costs and improve reproducibility of tests. 

Docker is one of the popular container platforms in the area.

Are such approaches applicable to the Embedded Systems area? 

Container technologies have limitations, especially when it comes to tests involving hardware-in-the-loop (HWIL) in the loop or drivers. 

In test automation flows it is important to know Docker limitations to properly combine it with other approaches.

This talk focuses on Docker usage specifics in simulation-based and HWIL test automation with Docker and automation servers like Jenkins. 

The talk includes overview of Docker advantages and disadvantages, and provides examples from real-world projects. 

Main takeaways from the talk are the recommendations when and how to use Docker in Embedded Systems testing. 

And how to migrate the automation flows to such new approaches.
