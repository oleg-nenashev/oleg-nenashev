# MSc - Hardware and Software co-design

* Department: Computer systems and program technologies
* Major: Automation and Control (Russian classifier - 220200) 
* Thesis: Development of methods and tools for reengineering of digital hardware defined by HDL specifications.

## Abstract

Reengineering is used to improve device characteristics (performance, power effectiveness, reliability, etc) or to add new features.
Modern systems are very complex and there's an actual task of reengineering automation.
This work approaches to build an extensible toolkit, based on which can be resolved by custom tasks of reengineering.
Survey of the existing tools shows that there’s no fully programmable reengineering automation tools and this area remains very prospective.

This work presents a new model of device for representation, analysis and transformation of digital systems that are described in hardware description languages (HDL).
This model is based on an architecture graph with a limited number of basic node types.
Graphs can be divided into tree-like structural description and links between elements.
Hardware representation includes mechanisms for extension and navigation.
A minimal command set for model transformation was developed.

In the work was designed architecture of hardware reengineering toolkit that meets basic requirements (programmable, extensible, embeddable).
Toolkit is built in a modular fashion with a minimal kernel that implements device model, basic operations and application programming interface (API).
All other features (including HDL’s input-output) should be implemented in extensions that the kernel supports.

Prototype of programmable reengineering toolkit was developed as a part of research.
Results of conducted experiments confirm applicability of proposed model and system architecture.
