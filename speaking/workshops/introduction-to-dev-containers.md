---
title: "Introduction to Dev Containers"
description: "Hands-on introduction to reproducible developer environments with Dev Containers, including AI tools, CDEs and CI for your favorite stack."
layout: talk
template: talk.html
category: workshops
type: workshop
headerImage: false
tag:
  - devcontainers
  - cloud-development-environments
  - developer-tools
  - ai
  - ci-cd
author: oleg_nenashev
references:
  - name: "Related embedded developer environments workshop"
    url: "https://oleg.swiss/speaking/workshops/container-developer-environments-for-embedded/"
  - name: "Development Containers documentation"
    url: "https://containers.dev/"
  - name: "GitHub Codespaces documentation"
    url: "https://docs.github.com/en/codespaces"
---

**TL;DR: Works in your IDE? Now you can ship it to your team, your PM and your CI system!**

Setting up a development environment can be time-consuming and difficult to reproduce across a team.
Dev Containers let you describe the base images, tools, dependencies,
and editor configuration for a project as code, so developers can work in a
consistent environment on their laptops or in the cloud.
The same container configuration can also support automated workflows.

In this hands-on workshop, we build and customize a Dev Container for a project
using a technology stack selected by the audience, such as Go, Python, Java,
C/C++, or .NET.
We explore how to package development tools, use AI assistants and agents, and share the resulting environment across a team.
We then take the environment to the cloud with GitHub Codespaces and explore how to reuse it in CI.

By the end of the session, participants will understand how to define a reproducible development environment,
adapt it to their project's tooling, and
use it across in local developer environment, cloud developer environments, and CI/CD pipelines.

## Workshop Structure

### I. Getting started

* Environment Setup

### II. Key sections

1. Dev Container basics:
  - Dev Containers 101
  - Define and run a development environment in a Dev Container
  - Key features
  - Demos for the selected tech stack(s)
2. **AI and agents in Dev Containers:
  - Using coding agents in a Dev Container,
  - Model Context Protocol (MCP) integrations
  - Using SLMs and Ollama in a Dev Container.
3. Custom images:
  - Using a custom image with the dependencies and  tools needed for the selected stack.
  - Multi-container systems with Docker Compose or Podman Compose
4. Cloud development environments:
  - Move the environment to the cloud using GitHub Codespaces as an example.
5. Dev Containers in CI:
  - Explore how to reuse the development environment configuration in CI/CD pipelines with GitHub Actions as an example

### III. Optional parts

Depending on the audience and available time, we can also explore:

- Integration testing with Testcontainers in a Dev Container
- Using Nix in Dev Containers
- Custom cloud development environments (CDEs): building your own IDEs at scale
