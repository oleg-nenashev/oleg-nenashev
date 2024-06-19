---
title: "Jenkins Remoting. Dealing with agent connectivity issues"
layout: talk
category: talks
headerImage: false
date: 2017-06-01
lastPresented:
    title: Day of Jenkins, Oslo
    url: https://www.code-conf.com/doj/doj-osl/
tag:
- jenkins
- remoting
author: oleg_nenashev
slideSource: speakerdeck
speakerdeckId: 0e7cd3cc33ba495da83a13f02e3ed810
---

Welcome to the Dark side of Jenkins...

Almost all agent types in Jenkins use the Remoting library to communicate with the master, 
including JNLP and SSH agents. 
Although Jenkins’ ability to run tasks on multiple hosts is one of its success factors, 
agent connection stability is known to be a major pain point in large-scale installations. 
In this workshop, The talk is about remoting internals, how to diagnose issues, 
how to configure Jenkins and underlying infrastructure, and the future of this layer in Jenkins.
