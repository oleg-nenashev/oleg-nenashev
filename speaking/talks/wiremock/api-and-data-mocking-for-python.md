---
title: "Want a cup of Java? API and data mocking for Python projects"
description: "Testing Python data pipelines against mocked services and fake data with Testcontainers and WireMock."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - python
  - testing
  - api
  - data
  - wiremock
  - testcontainers
author: oleg_nenashev
speakerdeckId: 102ad20845ae4094b254321263cade61
sessionize: https://sessionize.com/s/onenashev/want-a-cup-of-java-api-and-data-mocking-for-python/93401
speakerdeck: https://speakerdeck.com/onenashev/api-and-data-mocking-for-python
references:
  - name: "Sessionize abstract and outline"
    url: "https://sessionize.com/s/onenashev/want-a-cup-of-java-api-and-data-mocking-for-python/93401"
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/api-and-data-mocking-for-python"
presented:
  - event: "PyData Lausanne"
---

When working in embedded and observability domains, I’ve used Python scripting to retrieve and pre-process data from external sources, and one of the issues I’ve seen is the difficulty to reliably test data pipelines against external services: API limits and pay-per-use costs, service outages, etc, etc. So, can we model (aka “mock”) the services to reliably test our data ingestion pipelines?. Sure we can!

In this talk I will show a few ways to build test services, databases and API providers with the help of Testcontainers and WireMock available on Python, thanks to container tech. Then, we will extend the approach by adding the generation of fake data with help of Faker libraries or Synthesized that can be used for both relational data and data sequences.
