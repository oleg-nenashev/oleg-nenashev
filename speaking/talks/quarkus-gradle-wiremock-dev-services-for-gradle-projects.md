---
title: "Strange Quarks, Mocking Quarks - Modeling API services in Quarkus in high-density environments"
description: "Developing and mocking APIs with Quarkus Dev Services and WireMock in Gradle projects."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - quarkus
  - wiremock
  - testcontainers
  - api
  - testing
author: oleg_nenashev
speakerdeckId: f7da78a5100d459491cc646cceddf7da
youtubeId: Lf15C0Jl3Yk
sessionize: https://sessionize.com/s/onenashev/strange-quarks-mocking-quarks-modeling-api-service/82365
youtube: https://www.youtube.com/watch?v=Lf15C0Jl3Yk
speakerdeck: https://speakerdeck.com/onenashev/quarkus-gradle-wiremock-dev-services-for-gradle-projects
references:
  - name: "Sessionize abstract"
    url: "https://sessionize.com/s/onenashev/strange-quarks-mocking-quarks-modeling-api-service/82365"
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/quarkus-gradle-wiremock-dev-services-for-gradle-projects"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=Lf15C0Jl3Yk"
---

Quarkus offers many local development capabilities, including the recently released Dev Services that usually run with Testcontainers under the hood. We can leverage Dev Services to provide real-time API provider development experiences for Quarkus-based services and client apps.

In this session, I provide an overview of using Quarkus and its Dev Services in Gradle projects. We take WireMock as an example. I will demonstrate how to develop a REST API and a gRPC 3-tier client-service-database application using Quarkus and WireMock. DM for a Testcontainers edition!

- Demo with Apache Maven: [wiremock-quarkus-devservice-demo](https://github.com/wiremock/wiremock-quarkus-devservice-demo)
- Demo with Gradle Build Tool: [gradle-quarkus-plugin-demo](https://github.com/oleg-nenashev/gradle-quarkus-plugin-demo)

NOTE: This presentation was modified on Oct 10, 2025, to exclude the IP of Gradle Inc. Extended introduction, Quarkus Plugin for Gradle Build Tool, and the respective demo details are no longer included in the slides.

*Gradle®, Develocity®, Build Scan®, and the Gradlephant logo are registered trademarks of Gradle, Inc. "Gradle" means "Gradle Build Tool" and does not reference Gradle, Inc. and/or its subsidiaries.*

Presented at the Turkish Java Meetup and Red Hat Engineering Day.
