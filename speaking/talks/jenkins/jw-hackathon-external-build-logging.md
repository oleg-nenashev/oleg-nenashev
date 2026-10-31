---
title: "External Build Logging in Jenkins. Prototype Demo"
description: "Hackathon prototype that sends Jenkins build logs to Logstash and Elasticsearch instead of the disk."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - observability
  - ci-cd
author: oleg_nenashev
speakerdeckId: c4f9820a036c48e8b2f24e8aebe751f8
speakerdeck: https://speakerdeck.com/onenashev/jw2016-hackathon-external-build-logging-prototype-demo
references:
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/jw2016-hackathon-external-build-logging-prototype-demo"
  - name: "Design draft"
    url: "https://docs.google.com/document/d/1_bquSeA_lC7zJhQoWhxlSKJAg6b8duNbyQ15zCz-e4Y/edit"
  - name: "Jenkins Core patch"
    url: "https://github.com/oleg-nenashev/jenkins/tree/jw-hackaton-external-logging"
  - name: "Logstash Plugin patch"
    url: "https://github.com/oleg-nenashev/logstash-plugin/tree/jw-hackaton-remote-logging"
presented:
  - event: "Jenkins World Hackathon"
    year: 2016
    month: 9
---

This presentation summarizes results of our project from the Jenkins World 2016 hackathon. The prototype implements reporting of build logs to Logstash/Elasticsearch instead of the system disk and their further visualization within the Jenkins Web UI.

The approach allows to reduce network and IO load on Jenkins master and thus avoid performance bottlenecks on large-scale instances.
