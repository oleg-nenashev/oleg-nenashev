---
title: "Mocks as code: Modeling AWS service providers with Testcontainers, WireMock and Localstack"
description: "Combining LocalStack, WireMock and Testcontainers in a Dev Container to test cloud-based services and deployments."
layout: talk
template: talk.html
category: workshops
type: workshop
headerImage: false
tag:
  - testing
  - mocking
  - testcontainers
  - wiremock
  - configuration-management
author: oleg_nenashev
speakerdeckId: 26d5f28dc6d34e71b182e89c4a5c57c7
speakerdeck: https://speakerdeck.com/onenashev/mocks-as-code-modeling-aws-service-providers-with-testcontainers-wiremock-and-localstack
references:
  - name: "Slides and abstract"
    url: "https://speakerdeck.com/onenashev/mocks-as-code-modeling-aws-service-providers-with-testcontainers-wiremock-and-localstack"
  - name: "Workshop repository"
    url: "https://github.com/oleg-nenashev/workshop-aws-mocks-as-code"
presented:
  - event: "PlatformCon"
    year: 2025
    month: 6
---

When managing services at scale, you need automated testing while mocking (or modeling) the parts provided by public clouds, as well as testing entire deployment processes. This session demonstrates how to combine Localstack (for AWS integration testing), WireMock (for service mocking), and Testcontainers, a popular framework for Docker and other container engines, for comprehensive integration testing - all running in a Dev Container on your local machine.

Using Pulumi and Java as examples, you'll see live coding that demonstrates how these tools work together, with the approach applicable to any tech stack. Expect a hands-on workshop format with minimal tool requirements, showcasing developer experience for modern, containerized developer environments and practical techniques you can apply immediately to your own services.
