---
title: "Mocks as Code. Modeling services in configuration management flows"
description: "Hands-on workshop testing infrastructure code with Testcontainers, LocalStack, WireMock and Pulumi."
layout: talk
template: talk.html
category: workshops
type: workshop
headerImage: false
tag:
  - testing
  - api
  - mocking
  - configuration-management
author: oleg_nenashev
speakerdeckId: 1cf15669584141eca7d664970261fc0c
github: https://github.com/oleg-nenashev/workshop-aws-mocks-as-code
sessionize: https://sessionize.com/s/onenashev/mocks-as-code.-modeling-services-in-configuration-/84022
speakerdeck: https://speakerdeck.com/onenashev/workshop-mocks-as-code-in-cfg-mgmt
references:
  - name: "Workshop repository"
    url: "https://github.com/oleg-nenashev/workshop-aws-mocks-as-code"
  - name: "Workshop slides"
    url: "https://speakerdeck.com/onenashev/workshop-mocks-as-code-in-cfg-mgmt"
  - name: "Sessionize session"
    url: "https://sessionize.com/s/onenashev/mocks-as-code.-modeling-services-in-configuration-/84022"
---

When managing service configurations at scale, we often need to automate testing of these configurations. In software integration testing, we can use Testcontainers - a popular framework for Docker and other container engines. For public cloud environments, there is LocalStack. And for API service providers, we have WireMock. Can we use the same toolchain for configuration management? If you use modern Infrastructure-as-Code tools like Pulumi, yes!

In this edition, we will use Java or Kotlin for EVERYTHING, from the application itself and all the way up to Infrastructure as Code definitions and tests.

In this workshop, we will go through the following topics:

1. Containerizing Spring app development
2. Integration testing with Testcontainers and LocalStack
3. Mocking APIs with WireMock
4. Infrastructure as Code (IaC) with Pulumi and Pulumi for Java
5. Testing IaC locally, with all tools above combined

See the [demo repository](https://github.com/oleg-nenashev/mocks-as-code-demo) used in this workshop. It also contains all the links to the used tools and additional learning materials.

*Gradle®, Develocity®, Build Scan®, and the Gradlephant logo are registered trademarks of Gradle, Inc. "Gradle" means "Gradle Build Tool" and does not reference Gradle, Inc. and/or its subsidiaries.*

Presented at DevOpsDays Geneva 2024.
