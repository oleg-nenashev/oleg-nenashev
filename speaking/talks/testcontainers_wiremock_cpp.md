---
title: "Testcontainers and API mocking with WireMock for C/C++ projects"
description: "Testcontainers for C/C++: an SDK for integration testing native projects with WireMock."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - cpp
  - embedded
  - testing
  - wiremock
  - testcontainers
author: oleg_nenashev
speakerdeckId: e3308989cce84817bf50be0ddf9f12b4
youtubeId: dBjjFDZS5FM
youtube: https://www.youtube.com/watch?v=dBjjFDZS5FM
speakerdeck: https://speakerdeck.com/onenashev/testcontainers_wiremock_cpp
---

Testcontainers has become one of the most popular tools for software integration testing. If you can put your system-under-test into a container, Docker compose cluster or a pod, this is what you're likely to use. If your target isn't ready, not containerizable or just too heavy for testing as is, you can always use API mocking like WireMock to mock your interfaces including REST API, gRPC, etc. But are these tools available to C/C++ developers? And the answer is YES!

In September 2023 I created Testcontainers for C/C++. This is not a standalone Testcontainers engine, but a C-style shared library adapter for native languages like C/C++, and also D, Lua, Swift, etc. It is a MVP SDK that can be later extended for the languages. The project is based on Testcontainers for Go which is one of the most powerful Testcontainers implementations. And yes happy to chat about how it does [and doesn’t] work under the hood.

The objective of this talk is to present the existing solution, find early adopters and get feedback from professional C/C++ developers who use modern C/C++. For me it has been 10 years since I used it professionally for Embedded and SCADA projects, so it would be awesome to get the community feedback on use-cases and priorities!

Presented at the C/C++ Meetup Zurich.

References:

- [Slides and abstract](https://speakerdeck.com/onenashev/testcontainers_wiremock_cpp)
- [Video](https://www.youtube.com/watch?v=dBjjFDZS5FM)
