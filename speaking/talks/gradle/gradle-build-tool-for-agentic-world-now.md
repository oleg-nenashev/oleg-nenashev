---
title: "Gradle Build Tool for Agentic World, NOW!"
description: "Exploring Gradle Build Tool as a build server for interactive, agentic development."
layout: talk
template: talk.html
category: talks
type: talk
headerImage: false
tag:
  - gradle
  - ai
  - developer-tools
author: oleg_nenashev
cancelled:
  - event: "Devoxx Belgium"
    year: 2025
---

The way we build software is changing, and agents are rising! CI systems have already evolved from brittle shell-script runners to highly resilient, feature-rich services that support developers at every step, from a new branch in the IDE to deployment. The same happens with build tools. In five years, we won’t be running `mvn clean package` or `gradle build`. Instead, developers or AI agents will interact with build servers in dialog mode. So, bye-bye “software builds” and welcome “software transforms” powered by build servers?

This talk introduces the great old *Gradle Build Tool* but re-packaged for the new world where developers don’t just write tasks—they collaborate with the build server directly, or let their agentic system do that. We’ll explore how Gradle’s existing capabilities—its Daemon Mode, advanced build and configuration caching, Tooling API, Build Server Protocol integrations, MCP servers & Co make it not just a Build Tool, but a Build Server suitable for iterative agentic development!

You’ll see live examples of agentic workflows in action, including conversational build interactions from within IDEs like Visual Studio Code or IntelliJ IDEA, interactive dependency updates and toolchain management. Everything I present will be open source and ready for tinkering in your projects.
