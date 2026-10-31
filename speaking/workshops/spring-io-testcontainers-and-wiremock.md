---
title: "Spring I/O - Testcontainers and WireMock Workshop"
description: "Hands-on workshop on testing a Spring Boot app with Testcontainers, Dev Services and WireMock."
layout: talk
template: talk.html
category: workshops
type: workshop
headerImage: false
tag:
  - testing
  - mocking
  - api
author: oleg_nenashev
github: https://github.com/oleg-nenashev/spring_io_2025-Testcontainers-workshop
---

In this workshop, we work with a Spring Boot TODO list application that can also load top stories from Hacker News for reading, either from the public API or from a [WireMock](https://wiremock.org/) mock API running in [Testcontainers](https://www.testcontainers.org/).

In the first part, we use containers for development: running Postgres in a container, using Spring Boot Dev Services, and writing tests with Testcontainers, including verifying database migrations. In the second part, we add WireMock to mock the Hacker News API, using the WireMock Spring Boot integration and the WireMock Testcontainers module.

Participants only need Docker Desktop or another Testcontainers-compatible container engine.

Presented at Spring I/O 2025.

References:

- [Workshop repository](https://github.com/oleg-nenashev/spring_io_2025-Testcontainers-workshop)
