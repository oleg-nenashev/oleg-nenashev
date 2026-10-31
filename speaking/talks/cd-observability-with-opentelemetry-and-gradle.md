---
title: "Modern Java app CI/CD observability with OTel and Quarkus"
description: "Making CI/CD pipelines observable with OpenTelemetry, shown on a Quarkus Java app."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - java
  - gradle
  - quarkus
  - ci-cd
  - observability
  - opentelemetry
author: oleg_nenashev
youtubeId: qyYfcsu99aY
sessionize: https://sessionize.com/s/onenashev/modern-java-app-cicd-observability-with-otel-quark/91831
youtube: https://www.youtube.com/watch?v=qyYfcsu99aY
speakerdeck: https://speakerdeck.com/onenashev/cd-observability-with-opentelemetry-and-gradle
references:
  - name: "Video"
    url: "https://www.youtube.com/watch?v=qyYfcsu99aY"
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/cd-observability-with-opentelemetry-and-gradle"
  - name: "Sessionize abstract"
    url: "https://sessionize.com/s/onenashev/modern-java-app-cicd-observability-with-otel-quark/91831"
---

Well-functioning continuous integration, delivery, and deployment pipelines are
important to the stability of cloud-native applications, including recovery when
things go wrong. CI/CD observability is therefore an important complement to
observability in production environments.

This talk explores a modern Java stack using Quarkus, Java Flight Recorder,
build tools, and delivery systems such as Dagger and Argo CD. It demonstrates
OpenTelemetry, Prometheus, and Jaeger, with approaches that can also be applied
to other OpenTelemetry collectors.
