---
title: "Fake it until you `make it`. API integration testing with Testcontainers and WireMock"
description: "Choosing between Testcontainers and WireMock for API integration tests, and combining them."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - testing
  - api
  - wiremock
  - testcontainers
author: oleg_nenashev
speakerdeckId:
  - 3c990d297b3046d7b0bad9c0e520b17e
  - b04844ecb9b841cd983996bab7a8116f
youtubeId: eFILbyaMI2A
sessionize: https://sessionize.com/s/onenashev/fake-it-until-you-make-it.-api-integration-testing/67137
youtube: https://www.youtube.com/watch?v=eFILbyaMI2A
speakerdeck:
  - https://speakerdeck.com/onenashev/fake-it-until-you-make-it-its-with-wiremock-testcontainers-and-quarkus
  - https://speakerdeck.com/onenashev/devoxx-be-fake-it-until-you-make-it-with-testcontainers-and-wiremock-spring-boot-edition
references:
  - name: "Sessionize abstract and outline"
    url: "https://sessionize.com/s/onenashev/fake-it-until-you-make-it.-api-integration-testing/67137"
  - name: "Solo slides with Quarkus"
    url: "https://speakerdeck.com/onenashev/fake-it-until-you-make-it-its-with-wiremock-testcontainers-and-quarkus"
  - name: "Pair-talk slides with Spring Boot"
    url: "https://speakerdeck.com/onenashev/devoxx-be-fake-it-until-you-make-it-with-testcontainers-and-wiremock-spring-boot-edition"
  - name: "Devoxx BE video"
    url: "https://www.youtube.com/watch?v=eFILbyaMI2A"
---

Testcontainers has become one of the most popular tools for software integration testing. If you can put your system-under-test into a container, Docker compose cluster or a pod, this is what you're likely to use. If your target isn't ready, not containerizable or just too heavy for testing as is, you can always use mock testing frameworks, e.g. WireMock or MockServer in the JVM ecosystem. Can you combine both approaches? Sure!

In this talk, we will classify integration testing and discuss application areas for WireMock and Testcontainers, and discuss which tool to choose for each use-case. And why not both? We will discuss putting WireMock into Testcontainers, and getting the best from their features thanks to the new WireMock modules for Testcontainers. Last but not least, we will see how to put WireMock in front of the Testcontainers or your real system to do deeper tests or even chaos engineering.

P.S: We will focus on the Java, Golang or Rust examples, but the same approaches can be used everywhere

Presented at Devoxx BE, JCON, API World, JUG.ch, and Java Israel.
