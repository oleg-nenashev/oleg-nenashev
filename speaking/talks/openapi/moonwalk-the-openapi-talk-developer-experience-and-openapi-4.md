---
title: "Moonwalk the OpenAPI talk. Developer experience and OpenAPI 4"
description: "Using OpenAPI for service modeling and mocking, its limits in v3, and what OpenAPI 4 (Moonwalk) brings."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - openapi
  - api
  - developer-experience
author: oleg_nenashev
speakerdeck: https://speakerdeck.com/onenashev/moonwalk-the-openapi-talk-developer-experience-and-openapi-4
references:
  - name: "Speaker Deck"
    url: "https://speakerdeck.com/onenashev/moonwalk-the-openapi-talk-developer-experience-and-openapi-4"
presented:
  - event: "API Days Paris"
    year: 2024
---

Swagger and OpenAPI revolutionized the API landscape and created a thriving ecosystem of developer tools, from IDEs to contract testing and no-code solutions. In our projects (WireMock, Jenkins, Testcontainers, and WireMock Cloud) we adopted OpenAPI to provide a great developer experience including automated generation of plugins, pipeline integrations, and the creation of Mock APIs directly from OpenAPI definitions. Not everything went well. OpenAPI excels at documentation but not so much for machine processing. We had to craft our own tooling, apply some AI magic to reverse engineer specifications, and build behavioral models. Most of it could have been prevented if OpenAPI v3 was more flexible and extensible.

In this talk we will discuss using OpenAPI for service modeling, also known as "mocking" and its impact on developer experience. Then, we will discuss the current limitations of OpenAPI 3 and offer a glimpse into the anticipated enhancements in OpenAPI v4 "Moonwalk," which are to be released soon.
