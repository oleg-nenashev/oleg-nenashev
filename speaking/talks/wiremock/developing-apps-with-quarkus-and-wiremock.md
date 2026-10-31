---
title: "Developing subatomic apps with Quarkus and WireMock"
description: "Live coding a REST and gRPC 3-tier app with Quarkus Dev Services, WireMock and Testcontainers."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - wiremock
  - testcontainers
  - mocking
  - api
author: oleg_nenashev
speakerdeckId: 1314ff5029bf4cffb15a7a94bf7effbe
speakerdeck: https://speakerdeck.com/onenashev/developing-apps-with-quarkus-and-wiremock
references:
  - name: "Slides and abstract"
    url: "https://speakerdeck.com/onenashev/developing-apps-with-quarkus-and-wiremock"
presented: []
---

Quarkus has a lot of capabilities for local development, including the recently released Dev Services that usually runs with Testcontainers under the hood. We can leverage Dev Services for providing great real-time API provider development experiences for Quarkus based service and client apps.

In this talk and live coding session I will show how to develop a REST API and gRPC 3-tier client-service-database app with help of WireMock, Quarkus and Testcontainers. We will go through live development and prototyping APIs, mocking data and API providers, and then also using WireMock as a proxy to inject some failures and chaos into the service.
