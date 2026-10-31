---
title: "Under the hood of serverless Jenkins. Jenkinsfile Runner"
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - ci-cd
  - cloud-native
author: oleg_nenashev
speakerdeckId: 4e9f5d4982884ba196b9b0a021992350
speakerdeck: https://speakerdeck.com/onenashev/under-the-hood-of-serverless-jenkins-jenkinsfile-runner
---

There were significant changes in the Jenkins project over last year. It is still one of the most popular automation servers in the world, but it is not just a “server” anymore. In 2019 Jenkins is a universal automation engine, which actively evolves towards the new Cloud Native architecture and which can be used in any CI/CD flows. It can be used not only as a server, but also as a “serverless” single-shot execution. And it is not only about Jenkins X, but also about more classic usages.

In my talk I will present Jenkinsfile Runner - an engine which allows running Jenkins Pipelines in a single-shot container. I will show how it is used in Jenkins X, GitHub Actions and other services. And, finally, I will show how to package your own Jenkinsfile Runner images and run it in any environments, CI systems and Cloud providers.

NOTE: This slidedeck will be periodically updated to reflect the latest version of the talk

Presented at DevopsDays Zurich 2019 and DevOops 2019.

References:

- [Slides and abstract](https://speakerdeck.com/onenashev/under-the-hood-of-serverless-jenkins-jenkinsfile-runner)
