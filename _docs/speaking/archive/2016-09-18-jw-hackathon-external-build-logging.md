---
title: "External Build Logging in Jenkins. Prototype Demo"
layout: talk
category: talks
headerImage: false
date: 2016-09-18
lastPresented:
    title: Jenkins World 2016 Hackathon
tag:
- jenkins
author: oleg_nenashev
slideSource: speakerdeck
speakerdeckId: c4f9820a036c48e8b2f24e8aebe751f8
links:
-   title: Design draft
    url: https://docs.google.com/document/d/1_bquSeA_lC7zJhQoWhxlSKJAg6b8duNbyQ15zCz-e4Y/edit
-   title: Jenkins Core patch
    url: https://github.com/oleg-nenashev/jenkins/tree/jw-hackaton-external-logging
-   title: Logstash Plugin patch
    url: https://github.com/oleg-nenashev/logstash-plugin/tree/jw-hackaton-remote-logging
---

This presentation summarizes results of our project from the Jenkins World 2016 hackaton. 
The prototype implements reporting of build logs to Logstash/Elasticsearch instead of the system disk 
and their further visualization within the Jenkins Web UI.

The approach allows to reduce network and IO load on Jenkins master and thus avoid performance bottlenecks on large-scale instances.
