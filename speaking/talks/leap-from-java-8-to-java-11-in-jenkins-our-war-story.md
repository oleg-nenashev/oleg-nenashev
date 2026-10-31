---
title: "Leap from Java 8 to Java 11 in Jenkins. Our *.war story"
description: "Lessons from adding Java 11 support to Jenkins while keeping Java 8 compatibility."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - jenkins
  - java
  - migration
author: oleg_nenashev
speakerdeckId: 0f986b85ef544ac0ade3f888857a2844
speakerdeck: https://speakerdeck.com/onenashev/leap-from-java-8-to-java-11-in-jenkins-our-war-story
references:
  - name: "Slides"
    url: "https://speakerdeck.com/onenashev/leap-from-java-8-to-java-11-in-jenkins-our-war-story"
presented:
  - event: "JUG Lausanne"
---

Jenkins, one of the leading open-source automation servers, has not been supporting Java 9 and above since its official release. Over the last year Jenkins contributors were working towards the support of Java 11 (Jenkins JEP-211). Jenkins has a huge and sometimes legacy Java/Groovy/native codebase, includes DSL engines, and depends on many upstream libraries and modules (including ones deleted from Java 11). It was a thorny way, but Java 11 support is almost ready to be released.

In this talk I would like to share our experiences and talk about potential obstacles others may hit while implementing Java 11 support in their projects. What issues have we hit while implementing support of Java 11 in the core? Are modules and deprecations that tricky for a web application (spoiler: no)? How have we enabled building and testing with OpenJDK 11 in our Maven-based pipelines? And how have we retained Java 8 compatibility after all these changes?
