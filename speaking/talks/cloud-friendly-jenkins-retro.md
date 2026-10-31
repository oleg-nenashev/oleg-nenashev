---
title: "Cloud Friendly(?) Jenkins. How we failed to make Jenkins cloud native and what we learned"
description: "What worked and what failed when making Jenkins cloud native, and why cloud friendly is enough."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - cloud-native
  - architecture
  - ci-cd
author: oleg_nenashev
speakerdeckId: 922fbcd99b444e4e94b9f143ad68d851
sessionize: https://sessionize.com/s/onenashev/cloud-friendly-jenkins.-how-we-failed-to-make-jenk/80447
speakerdeck: https://speakerdeck.com/onenashev/cloud-friendly-jenkins-retro
references:
  - name: "Sessionize abstract"
    url: "https://sessionize.com/s/onenashev/cloud-friendly-jenkins.-how-we-failed-to-make-jenk/80447"
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/cloud-friendly-jenkins-retro"
---

Key takeaway: Being Cloud Friendly is a must, Cloud Native is optional. Likely YAGNI in your projects

Jenkins has been one of the most popular automation servers in the world. It is widely used for CI/CD purposes in cloud environments. You may have heard that Jenkins is not cloud native, and of course it is true. You may have heard that Jenkins controllers are a legacy monolith from the 2000s. That is not true, it is quite **cloud friendly** if used right. And yes we tried to make Jenkins cloud native, but it didn’t quite work. Why?

I have been involved in Jenkins architecture projects for more than ten years, including pluggable storage, multi-tenant Jenkins, cloud-native agents, breaking down the controller monolith, Kubernetes integrations, etc. Some of these efforts worked, some didn’t. But it was a great learning experience that can be used by developers and maintainers of other projects that consider re-platforming them to make cloud- and Kubernetes-native. I'll talk about the technical assumptions and mistakes we made in Jenkins, and how it worked. What to keep in mind when doing the re-platforming? And do you even need it?

Presented at CNCF Bilbao 2023 and Cloud Native Rejekts EU 2024.
