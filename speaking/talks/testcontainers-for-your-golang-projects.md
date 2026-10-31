---
title: "Testcontainers and API mocking for Golang projects"
description: "Using Testcontainers and WireMock for integration testing in Go projects."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - golang
  - testing
  - api
  - wiremock
  - testcontainers
author: oleg_nenashev
speakerdeckId: bf5e39e856a74a7b8f32e3c03d921b90
youtubeId: 9F6hGhmedKk
sessionize: https://sessionize.com/s/onenashev/testcontainers-and-api-mocking-for-golang-projects/93404
youtube: https://www.youtube.com/watch?v=9F6hGhmedKk
speakerdeck: https://speakerdeck.com/onenashev/testcontainers-for-your-golang-projects
references:
  - name: "Sessionize abstract"
    url: "https://sessionize.com/s/onenashev/testcontainers-and-api-mocking-for-golang-projects/93404"
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/testcontainers-for-your-golang-projects"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=9F6hGhmedKk"
---

Testcontainers has become one of the most popular tools for software integration testing. If you can put your system-under-test into a container, Docker Compose cluster, or a pod, this is what you're likely to use. If your target isn't ready, not containerizable, or just too heavy for testing as is, you can always use API mocking like WireMock or Microcks to mock your interfaces including REST API, gRPC, etc.

In this talks, I will focus on using WireMock and Microcks for cloud native projects implemented in Golang, including using it for common continuous delivery and deployment use-cases. We will see how to use Testcontainers and its API mocking modules as a standalone deployment, or as a part of Argo CD and Tekton pipelines. And then, let's see how to seamlessly use the same tools in Golang IDEs!

The Speaker Deck version is a quick overview of Testcontainers for integration testing in Golang projects, with WireMock as an example.

Presented at PlatformCon 2025.
