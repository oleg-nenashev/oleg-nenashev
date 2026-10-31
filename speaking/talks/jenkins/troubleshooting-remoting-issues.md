---
title: "Jenkins Remoting. Dealing with agent connectivity issues"
description: "How Jenkins Remoting works, how to diagnose agent connection problems and where this layer is heading."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - remoting
  - troubleshooting
author: oleg_nenashev
speakerdeckId: 0e7cd3cc33ba495da83a13f02e3ed810
speakerdeck: https://speakerdeck.com/onenashev/day-of-jenkins-2017-dealing-with-agent-connectivity-issues
references:
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/day-of-jenkins-2017-dealing-with-agent-connectivity-issues"
  - name: "Simplified version of the slides"
    url: "https://speakerdeck.com/onenashev/day-of-jenkins-2017-dealing-with-agent-connectivity-issues-simplified"
presented:
  - event: "Day of Jenkins Oslo"
    year: 2017
    month: 5
    url: "https://www.code-conf.com/doj/doj-osl/"
---

Welcome to the Dark side of Jenkins...

Almost all agent types in Jenkins use the Remoting library to communicate with the master, including JNLP and SSH agents. Although Jenkins’ ability to run tasks on multiple hosts is one of its success factors, agent connection stability is known to be a major pain point in large-scale installations. In this workshop, the talk is about remoting internals, how to diagnose issues, how to configure Jenkins and underlying infrastructure, and the future of this layer in Jenkins.
