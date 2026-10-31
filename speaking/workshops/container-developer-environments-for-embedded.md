---
title: "Container Developer Environments. Virtualizing your IDEs for embedded projects"
description: "Hands-on workshop on building Dev Containers and Cloud Development Environments for a ROS2 robotics project."
layout: talk
template: talk.html
category: workshops
type: workshop
headerImage: false
tag:
  - embedded
  - devcontainers
  - cloud-development-environments
  - testing
author: oleg_nenashev
github: https://github.com/oleg-nenashev/cde-for-embedded-workshop
speakerdeck: https://speakerdeck.com/onenashev/workshop-container-developer-environments-virtualizing-your-ides-for-embedded-projects
references:
  - name: "Workshop repository"
    url: "https://github.com/oleg-nenashev/cde-for-embedded-workshop"
  - name: "Workshop slides"
    url: "https://speakerdeck.com/onenashev/workshop-container-developer-environments-virtualizing-your-ides-for-embedded-projects"
presented: []
---

Embedded development and QA are entering a new era, enabled by Cloud Development Environments (CDEs) such as GitHub Codespaces or Devcontainers, which allow fully configured workspaces to run on laptops, Kubernetes clusters, or public clouds. Containers and VMs, often managed with tools like KubeVirt and QEMU and wrapped by frameworks like Testcontainers, enable scalable, hardware-aware test setups for HIL testing, firmware validation, and system modeling.

In this workshop, we build a containerized developer environment for a robotics project using the open-source ROS2 stack (C++/Python, CMake, custom build tools, Gazebo, etc.), or another audience-nominated example. Step by step, you will learn to define and customize Dev Containers for your technology stack, adapt IDEs for embedded workflows, and package the full environment for sharing across teams and reuse in CI/CD pipelines.

We also explore how to move these environments beyond the laptop and run them on cloud-based development platforms such as GitHub Codespaces. By the end of the session, participants will understand how to virtualize their IDEs, standardize developer onboarding, and create reusable development environments that connect local workstations, cloud platforms, and automated pipelines.
