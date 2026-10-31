---
title: "FOSDEM 2024 - Jenkinsfile Runner Update"
description: "Jenkinsfile Runner status at the Jenkins Contributor Summit and why Testcontainers can replace it for pipeline testing."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - testcontainers
  - testing
author: oleg_nenashev
speakerdeckId: a63ccf396a57428eadc3536a4421294e
speakerdeck: https://speakerdeck.com/onenashev/fosdem-2024-jenkinsfile-runner-update
references:
  - name: "Slides and abstract"
    url: "https://speakerdeck.com/onenashev/fosdem-2024-jenkinsfile-runner-update"
presented:
  - event: "Jenkins Contributor Summit (FOSDEM)"
    year: 2024
    month: 2
---

Jenkinsfile Runner update at the Jenkins Contributor Summit. TL;DR: No big updates, I am still on a break in the Jenkins project, and I have only some time to keep the lights on. I am looking for co-maintainers and tinkerers who are interested in working on the project but it still remains relevant.

One thing to mention is that I no longer consider JFR relevant for integration testing of Jenkins Pipelines. At this stage, it can be totally replaced by the containerized Jenkins instances running inside Testcontainers, because it provides all features of the real Jenkins like classloading, even with an embedded K3s cluster if you need it for testing. Container suspension and caching address performance concerns for tests. Recently Steve Hill created a module for it.
