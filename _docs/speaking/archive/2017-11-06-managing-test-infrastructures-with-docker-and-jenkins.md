---
title: "Managing Embedded Systems test infrastructures with Docker and Jenkins"
layout: talk
category: talks
headerImage: false
date: 2017-11-06
lastPresented:
    title: Embedded Conference Scandinavia 2017
    url: http://www.embeddedconference.se/app/attendee/default.asp?PageId=57726&MenuItemId=54357&parent=54348&ProjectId=9774
tag:
- jenkins
- docker
author: oleg_nenashev
slideSource: external
slidesUrl: https://pages.cloudbees.com/ECS2017/Oleg_Nenashev
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
