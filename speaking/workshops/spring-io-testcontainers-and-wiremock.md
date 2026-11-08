---
title: "API Integration testing for Spring Boot apps, with Testcontainers and WireMock"
description: "Hands-on workshop on testing a Spring Boot app with Testcontainers, Dev Services and WireMock."
layout: talk
template: talk.html
category: workshops
type: workshop
headerImage: false
tag:
  - testing
  - wiremock
  - testcontainers
  - api
  - ai
  - spring
author: oleg_nenashev
github: https://github.com/oleg-nenashev/spring_io_2025-Testcontainers-workshop
speakerdeckId: cd89e51f4c4c4b55b1c298837c30c5ec
speakerdeck: https://speakerdeck.com/onenashev/workshop-api-testing-for-spring-apps-tc-wm
references:
  - name: "Workshop repository"
    url: "https://github.com/oleg-nenashev/spring_io_2025-Testcontainers-workshop"
  - name: "Workshop slides"
    url: "https://speakerdeck.com/onenashev/workshop-api-testing-for-spring-apps-tc-wm"
presented:
  - event: "Spring I/O"
    year: 2025
---

Testcontainers have become one of the most popular tools for software integration testing.
If you can put your system under test into a container, Docker compose cluster, or pod, you’re likely to use this.
If your target isn’t ready, not containerizable, or just too heavy for testing as is, 
you can always use mock testing frameworks, e.g., WireMock or MockServer in the JVM ecosystem.
Can you combine both approaches? Sure!

In this talk, we will classify integration testing of Spring projects and discuss application areas for WireMock and Testcontainers, and discuss which tool to choose for each use-case.
And why not both? We will discuss putting WireMock into Testcontainers, and getting the best from their features thanks to the new WireMock modules for Testcontainers.
Last but not least, we will see how to put WireMock in front of the Testcontainers or your real system to do deeper tests or even chaos engineering.

P.S: We will focus on the Java/Kotlin examples and Spring, but the same approaches can be used everywhere

## Chapters

1. Getting Started and introductions
2. Spring Dev Services
3. Containers for Development
4. Now with WireMock - API mocking in development and tests
5. Let's add some AI? Using Spring AI and SLMs for test purposes

## Requirements

Participants only need Docker Desktop or another Testcontainers-compatible container engine.
