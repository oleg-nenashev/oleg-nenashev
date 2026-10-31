---
title: "OpenAPI extensibility - the Good, the Bad and the YAMLy"
description: "The limits of OpenAPI 3 extensibility and what OpenAPI 4 could fix."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - openapi
  - api
  - developer-tools
author: oleg_nenashev
speakerdeckId: d1bb279b89104845bb23bcfa225b06f8
sessionize: https://sessionize.com/s/onenashev/openapi-extensibility-the-good-the-bad-and-the-yam/84549
speakerdeck: https://speakerdeck.com/onenashev/openapi-extensibility-the-good-the-bad-and-the-yamly
references:
  - name: "Sessionize abstract and references"
    url: "https://sessionize.com/s/onenashev/openapi-extensibility-the-good-the-bad-and-the-yam/84549"
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/openapi-extensibility-the-good-the-bad-and-the-yamly"
presented:
  - event: "API Days Paris"
    year: 2023
---

Swagger and OpenAPI revolutionized the API landscape and created a thriving ecosystem of developer tools, from IDEs to contract testing and no-code solutions. In our projects (WireMock, Jenkins, Testcontainers and WireMock Cloud) we adopted OpenAPI to provide a great developer, and achieved great results. At the same time, the v3 version of specification has too many limitations, especially when it comes to behavior modeling: limited extensions framework, poor response flexibility limiting complex API options, and weak examples and self documentation capabilities. Good news is that OpenAPI v4 (Project Moonwalk) addresses many of those concerns and, hopefully, could address others before the release. Let’s, wearing our end user hats, discuss the v3 experiences and how we could address them in the upcoming major release!
