---
title: "Docker and Jenkins [as Code]"
description: "Hands-on Jenkins configuration management with Docker, Kubernetes, Configuration as Code, and Groovy hooks."
layout: talk
template: talk.html
category: workshops
type: workshop
headerImage: false
tag:
  - jenkins
  - docker
  - kubernetes
  - configuration-as-code
  - ci-cd
author: oleg_nenashev
github: https://github.com/oleg-nenashev/demo-jenkins-config-as-code
speakerdeckId: 61615b9107bb4d94afbbbc10a45ab030
speakerdeck: https://speakerdeck.com/onenashev/docker-and-jenkins-as-code
references:
  - name: "Docker and Jenkins [as Code] talk slides"
    url: "https://speakerdeck.com/onenashev/docker-and-jenkins-as-code"
  - name: "Jenkins Configuration as Code demo"
    url: "https://github.com/oleg-nenashev/demo-jenkins-config-as-code"
---

How can you make a Jenkins installation reproducible, portable, and easier to maintain?
In this hands-on workshop, we manage Jenkins configuration as code and run Jenkins
with Docker and Kubernetes. We explore controller and agent images, build a custom
Jenkins image, and manage its plugins and configuration alongside the code.

Participants use Jenkins Configuration as Code (JCasC) to define settings in YAML
and Groovy hooks to customize initialization where needed. We discuss how the two
approaches work together, how to handle configuration changes, and how container
images and Kubernetes agents fit into a repeatable Jenkins setup.

The workshop can be adapted to a duration of **2 to 8 hours**, from an introduction
to a deeper, hands-on exploration.

## Workshop chapters

1. **Jenkins configuration as code:** Explore the components of a Jenkins
   installation and the benefits of storing configuration alongside code.
2. **Jenkins with Docker:** Run controller and agent images, build a custom
   Jenkins image, and manage its plugins.
3. **Jenkins Configuration as Code:** Define and apply Jenkins settings with
   JCasC and YAML, and manage configuration changes.
4. **Groovy hooks:** Customize Jenkins initialization with Groovy and combine
   hooks with JCasC where additional flexibility is needed.
5. **Jenkins on Kubernetes:** Explore containerized Jenkins deployments and
   Kubernetes agents as part of a repeatable setup.

The depth and hands-on exercises in each chapter can be adapted to the available time.
