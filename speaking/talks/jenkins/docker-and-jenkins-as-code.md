---
title: "Docker and Jenkins [as Code]"
description: "Running Jenkins in Docker and managing its configuration as code."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - docker
  - configuration-as-code
  - ci-cd
author: oleg_nenashev
speakerdeckId: 61615b9107bb4d94afbbbc10a45ab030
youtubeId: J0d-CbJKAwU
youtube: https://www.youtube.com/watch?v=J0d-CbJKAwU
speakerdeck: https://speakerdeck.com/onenashev/docker-and-jenkins-as-code
references:
  - name: "Slides and abstract"
    url: "https://speakerdeck.com/onenashev/docker-and-jenkins-as-code"
  - name: "DevOps World | Jenkins World 2019 slides"
    url: "https://speakerdeck.com/onenashev/dw-jw-2019-docker-and-jenkins-as-code"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=J0d-CbJKAwU"
presented:
  - event: "Docker Meetup Geneva"
    year: 2019
    month: 3
  - event: "DevOps World | Jenkins World"
    year: 2019
    month: 12
  - event: "Day of Jenkins Copenhagen"
    year: 2019
  - event: "CloudBees webinars"
---

Docker is everywhere in the CI/CD pipelines and in development tools. Jenkins, one of the most popular automation servers, is actively evolving to improve its support of container technologies and static configurations in images. The Configuration as Code plugin is a new milestone which enables managing Jenkins configurations via YAML. Together with Docker, this plugin offers many ways to produce ready-to-fly Jenkins images for any environments. In our talk, we will describe official master and agent images offered by the Jenkins project. What's inside them? How do you configure images with JCasC and Groovy hooks? How do you use these approaches together? How do CloudBees Jenkins Distribution and CloudBees Assurance program help with plugin management? And what's next for Jenkins Docker packaging and JCasC?

