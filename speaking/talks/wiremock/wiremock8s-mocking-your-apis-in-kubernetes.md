---
title: "WireMock8s - Mocking your APIs in Kubernetes"
description: "Running WireMock on Kubernetes for API mocking in cloud-native testing and pipelines."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - wiremock
  - kubernetes
  - api
  - testing
author: oleg_nenashev
speakerdeckId: e4f3f75f38e74776afdbd5abb202c70e
youtubeId: 1D-BbC6AQWA
youtube: https://youtu.be/1D-BbC6AQWA
speakerdeck: https://speakerdeck.com/onenashev/wiremock8s-mocking-your-apis-in-kubernetes
references:
  - name: "Video"
    url: "https://youtu.be/1D-BbC6AQWA"
  - name: "Slides and abstract"
    url: "https://speakerdeck.com/onenashev/wiremock8s-mocking-your-apis-in-kubernetes"
presented:
  - event: "CNCF Basel Meetup"
    year: 2023
    month: 6
---

Distributed and microservice architectures are all about APIs these days, whether you use gRPC, REST API, Websockets or any other interface. There are tools for integration testing that involve API providers, including mocking them based on OpenAPI specifications. There are even Kubernetes native tools like Microcks that are scalable and provide valuable features and observability out of the box. More classic tools, including my favorite WireMock, are available on Kubernetes too.

If you’ve ever developed for JVM or .NET stacks, most likely you’ve heard about WireMock. It is a popular open-source tool and framework for API mock testing, with over 5 million downloads per month. It has implementations and adapters for many languages.

In this talk, I will focus on using WireMock for testing Cloud Native applications in Kubernetes, including using it for common continuous delivery and deployment use-cases. We will see how to use WireMock as a standalone deployment, or as a part of Argo CD and Tekton pipelines. I’ll also show how these approaches can be integrated with WireMock Cloud for those who want to do distributed testing and chaos engineering.
