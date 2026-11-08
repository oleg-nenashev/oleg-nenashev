---
title: "Introduction to Testcontainers and WireMock"
description: "Hands-on introduction to integration testing and API mocking with Testcontainers and WireMock for the tech stack of your choice."
layout: talk
template: talk.html
category: workshops
type: workshop
headerImage: false
tag:
  - testing
  - api
  - mocking
  - testcontainers
  - wiremock
author: oleg_nenashev
speakerdeckId: b04844ecb9b841cd983996bab7a8116f
speakerdeck: https://speakerdeck.com/onenashev/devoxx-be-fake-it-until-you-make-it-with-testcontainers-and-wiremock-spring-boot-edition
references:
  - name: "Fake it until you make it: API integration testing talk"
    url: "https://oleg.swiss/speaking/talks/wiremock/fake-it-until-you-make-it-its-with-wiremock-testcontainers-and-quarkus/"
  - name: "Fake it until you make it: Spring Boot talk slides"
    url: "https://speakerdeck.com/onenashev/devoxx-be-fake-it-until-you-make-it-with-testcontainers-and-wiremock-spring-boot-edition"
  - name: "Fake it until you make it: Quarkus talk slides"
    url: "https://speakerdeck.com/onenashev/fake-it-until-you-make-it-its-with-wiremock-testcontainers-and-quarkus"
  - name: "Testcontainers and API mocking for Go projects"
    url: "https://oleg.swiss/speaking/talks/testcontainers/testcontainers-for-your-golang-projects/"
  - name: "API and data mocking for Python projects"
    url: "https://oleg.swiss/speaking/talks/wiremock/api-and-data-mocking-for-python/"
  - name: "Testcontainers documentation"
    url: "https://testcontainers.com/"
  - name: "WireMock documentation"
    url: "https://wiremock.org/docs/"
---

Integration tests often depend on databases, APIs, and other services that are
slow to set up, unreliable, expensive, or unavailable during development.
Testcontainers helps run real dependencies in disposable containers, while
WireMock lets us model HTTP APIs when a real service is impractical to use.
When should we use each approach, and how can we combine them?

This hands-on workshop introduces container-based integration testing and API mocking.
Participants work with an example in the technology stack(s), selected for the audience.
We build test environments with Testcontainers, configure WireMock to simulate API
responses, and bring them together to test an application's interactions with
external services.

By the end of the session, participants will understand how to choose between
real and mocked dependencies, create repeatable integration tests, and exercise
both successful responses and failure scenarios without relying on a live API.

## Possible technology stacks

Java (Spring or Quarkus), Kotlin, Golang, Python, C/C++

## Workshop Structure

### Getting started

1. Discussion of the audience's use-cases
2. Environment Setup
3. Optional - Integration testing fundamentals

### Main parts

1. Getting started with Testcontainers, in a Dev Container
  - Introduction to the key features
  - Testcontainers Modules
  - Demo for a database project
  - Demo for an AI project with Ollama and a local SLM
2. API mocking with WireMock
  - Model HTTP endpoints and configure responses
  - Exercise successful responses, errors, and delays
  - Verify requests sent by the application
3.  Combining Testcontainers and WireMock
  - Run WireMock in a container as part of the test
  - Test an application against real and mocked dependencies

### Optional parts parts

The following parts can be selected by participants:

- Testcontainers with Docker Compose and Podman Compose
- Data modeling and mocking with Testcontainers, WireMock and data libraries
- Using the technologies for CI/CD
- For Spring and Quarkus frameworks, Dev Services

## Requirements

Participants need a laptop with a Testcontainers-compatible container engine
and the development tools for the selected stack.
