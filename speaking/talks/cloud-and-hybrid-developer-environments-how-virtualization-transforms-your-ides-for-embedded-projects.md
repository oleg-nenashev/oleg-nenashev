---
title: "Cloud and Hybrid Developer Environments - how virtualization transforms your IDEs for embedded projects"
description: "Building hybrid developer environments for embedded QA with Dev Containers, Testcontainers and open source tools."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - embedded
  - devcontainers
  - testing
author: oleg_nenashev
speakerdeckId: ad9509d7988446c4a17b7e09d5eb36a1
speakerdeck: https://speakerdeck.com/onenashev/cloud-and-hybrid-developer-environments-how-virtualization-transforms-your-ides-for-embedded-projects
references:
  - name: "Slides and abstract"
    url: "https://speakerdeck.com/onenashev/cloud-and-hybrid-developer-environments-how-virtualization-transforms-your-ides-for-embedded-projects"
presented: []
---

Back in 2017 at QA&Test Bilbao, I explored how Docker and Jenkins pipelines could transform CI/CD for embedded projects. Fast forward to 2023, containerization has become the norm in embedded software QA. My recent talk focused on tools like Testcontainers and WireMock, now widely used for testing not just backend services but entire embedded systems—from SCADA to IoT—within virtualized environments powered by Kubernetes. These technologies now form the backbone of modern testing infrastructure in software, and now expand to edge and embedded systems to cover full-system virtualization and integration testing. Same happens on the developer machines.

Embedded QA Engineers are entering a new era of development enabled by Cloud Development Environments (CDEs) like GitHub Codespaces or Devcontainers, where fully configured workspaces can run on laptops, Kubernetes clusters or public clouds. Containers and VMs, often managed with tools like KubeVirt and QEMU, and wrapped by frameworks like Testcontainers, enable scalable, hardware-aware test setups that support HIL testing, firmware validation, and system modeling. It might sound like a miracle, but it's actually possible with modern tech stacks!

This talk demonstrates how to build such "hybrid developer environments" entirely with open source tools, combining C++/SystemVerilog development, embedded hardware access, and even AI-driven test automation – showing that the modern IDE for embedded QA is now distributed, intelligent, and platform-agnostic.
