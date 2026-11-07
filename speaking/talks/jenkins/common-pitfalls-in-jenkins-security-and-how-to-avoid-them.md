---
title: "Common Pitfalls in Jenkins Security and How to Avoid Them"
description: "The most common Jenkins security mistakes and how to avoid them."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - security
author: oleg_nenashev
speakerdeckId: 39e7f7b97b504a919440e7ebfd1a7419
speakerdeck: https://speakerdeck.com/onenashev/common-pitfalls-in-jenkins-security
youtubeId: YufZHjO0hd4
youtube: https://www.youtube.com/watch?v=YufZHjO0hd4
references:
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/common-pitfalls-in-jenkins-security"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=YufZHjO0hd4"
presented:
  - event: "Jenkins World"
    year: 2018
  - event: "Jenkins User Conference Oslo"
    year: 2017
  - event: "Jenkins User Conference Gothenburg"
    year: 2017
---

It is 2025, and Jenkins, an open source automation server with 20 years of history, still dominates the CI/CD market and remains a mission-critical part of the worldwide software supply chain. In 2025, it even won the "The most innovative DevOps open source project" award from DevOps Dozen, and got security grants from Alpha Omega. But Jenkins still has quite an old architecture, and one can consider it a remote execution engine which has access to project data… by design. So, how secure is your instance and supply chain when using Jenkins?

When it comes to Jenkins instances with thousands of users, it is hard to retain status quo between security itself and its impact on user experience due to the restrictions and performance degradation. I will talk about Jenkins security model, best practices and common non-newbie configuration mistakes which we often see on production instances. In particular we will discuss Groovy scripting, controller-to-agent communications and resource isolation. We will also review a few supply chain attack cases that happened through Jenkins, and how one could prevent them.

Target audience for this talk: experienced Jenkins administrators and users interested in Security. The learnings are applicable to other CI/CD tools, especially the self-hosted ones
