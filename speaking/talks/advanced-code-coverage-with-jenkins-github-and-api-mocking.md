---
title: "Advanced Code Coverage with Jenkins and API Mocking"
description: "Improving code coverage reporting in Jenkins and GitHub, with API mocking to test the hard-to-reach paths."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - testing
  - code-coverage
  - wiremock
  - testcontainers
author: oleg_nenashev
speakerdeckId: 8ec9ea263fab42ea989104bc04432ea1
youtubeId: ZBaQ71CI_lI
sessionize: https://sessionize.com/s/onenashev/advanced-code-coverage-with-jenkins-and-api-mockin/70786
youtube: https://www.youtube.com/watch?v=ZBaQ71CI_lI
speakerdeck: https://speakerdeck.com/onenashev/advanced-code-coverage-with-jenkins-github-and-api-mocking
references:
  - name: "Sessionize abstract and outline"
    url: "https://sessionize.com/s/onenashev/advanced-code-coverage-with-jenkins-and-api-mockin/70786"
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/advanced-code-coverage-with-jenkins-github-and-api-mocking"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=ZBaQ71CI_lI"
  - name: "Talk summary"
    url: "https://github.com/MichaelCade/90DaysOfDevOps/blob/main/2024/day26.md"
---

In 2015-2018, I talked about how to use the Jenkins Pipeline and custom libraries to do advanced integration tests and analyze code coverage. Coverage plugins were rather weak, and one needed some scripts and hacks to make it work, and to DIY for distributed testing. In 2021 the situation has changed significantly thanks to the Coverage and Checks API plugins. Distributed integration testing also became easier thanks to better coverage collectors and integrations with API mocking tools. So, good time to be alive… and use Jenkins!

We will talk about how modern Jenkins allows you to improve and analyze code coverage. We will talk about unit and integration testing with WireMock, the new Coverage Plugin, support for standard formats (Cobertura, JaCoCo, gcov, JUnit, etc.), parallelization for heavy integration tests and API mocking, and integration with GitHub Checks API. How can you analyze code coverage in Jenkins and when do you need to create your own libraries? And what’s the fuzz about Testcontainers and WireMock for integration testing?

Presented at 90 Days of DevOps 2024.
