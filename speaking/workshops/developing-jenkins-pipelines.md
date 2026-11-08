---
title: "Developing Jenkins Pipelines"
description: "Hands-on development and testing of Jenkins Pipelines and shared libraries."
layout: talk
template: talk.html
category: workshops
type: workshop
headerImage: false
tag:
  - jenkins
  - pipeline
  - testing
  - ci-cd
author: oleg_nenashev
speakerdeckId: 2294554f39c8471ca20f0ab87040b221
speakerdeck: https://speakerdeck.com/onenashev/cph-jenkins-meetup-developing-jenkins-pipeline
references:
  - name: "CPH Jenkins Meetup: Developing Jenkins Pipeline slides"
    url: "https://speakerdeck.com/onenashev/cph-jenkins-meetup-developing-jenkins-pipeline"
  - name: "Developing Jenkins Pipeline libraries locally"
    url: "https://speakerdeck.com/onenashev/jenkins-world-2017-developing-pipeline-libraries-locally"
  - name: "Jenkins Pipeline library example"
    url: "https://github.com/jenkins-infra/pipeline-library/"
---

Developing a Jenkins Pipeline should not mean pushing every change to a shared
server and waiting for a build to find the next mistake. In this hands-on
workshop, we explore developer tools and practices for writing, reviewing, and
testing Pipelines with a faster feedback loop.

Participants work with Jenkinsfiles and shared Pipeline libraries, extract reusable
automation, and explore ways to validate and test changes locally. We compare
testing approaches, from unit testing Pipeline code and mocking Jenkins steps to
integration testing against a containerized Jenkins instance with Testcontainers.
Along the way, we discuss maintainability, versioning, and common pitfalls when
sharing Pipeline code across projects.

## Workshop chapters

1. **Pipeline fundamentals and practices:** Develop Jenkinsfiles and discuss
   readability, maintainability, and common pitfalls.
2. **Pipeline developer tools:** Use local editing and validation workflows to
   shorten the feedback loop before committing changes.
3. **Shared Pipeline libraries:** Managing Jenkins pipelines at scale.
   - Extract reusable automation, organize and version libraries, and use them across projects.
4. **Unit testing:** Explore testing frameworks for Pipeline code, including
   mocking Jenkins steps and testing shared library behavior.
5. **Integration testing:** Run and test Pipelines against a containerized
   Jenkins instance using Testcontainers, and compare integration and unit tests.
