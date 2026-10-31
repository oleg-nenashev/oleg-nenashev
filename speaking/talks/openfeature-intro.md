---
title: "OpenFeature - making feature flags a commodity"
description: "An introduction to OpenFeature, the open standard for feature flag management."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - openfeature
  - feature-flags
  - cloud-native
  - open-source
author: oleg_nenashev
speakerdeckId: 813beeee00a64f45811c157eeb3417ce
youtubeId: aSJcUB0MuIQ
youtube: https://www.youtube.com/watch?v=aSJcUB0MuIQ
speakerdeck: https://speakerdeck.com/onenashev/openfeature-intro
references:
  - name: "Slides and abstract"
    url: "https://speakerdeck.com/onenashev/openfeature-intro"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=aSJcUB0MuIQ"
presented:
  - event: "Data on Kubernetes Meetup"
  - event: "DevopsDays Zurich BoF"
    year: 2022
---

With the evolution of software delivery methods, feature flags became one of the ways to deliver features and get user feedback. Modern applications may have hundreds of feature flags describing customizations, preview features, and environment specifics. Feature flags are not just a single toggle anymore, their values are often determined at runtime depending on the instance, user context, and inputs from the control plane.

In this session, we will talk about OpenFeature - a new collaboration by many feature flag vendors and end users. OpenFeature, a CNCF sandbox project, is an open standard for feature flag management, created to support a robust feature flag ecosystem using cloud native technologies and to make feature flags a commodity. OpenFeature provides a unified API and SDKs, and a developer-first, cloud-native implementation, with extensibility for open-source and commercial offerings.

We will provide adoption examples from the open-source projects from the Java and Cloud Native ecosystems.
