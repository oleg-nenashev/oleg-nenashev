# MSc Degree - Hardware and Software co-design

* University: [Peter the Great St.Petersburg Polytechnic University (SPbPU)](https://english.spbstu.ru/)
* Department: [Computer systems and program technologies](http://kspt.icc.spbstu.ru/)
* Research Group: Electronic Design Automation Lab
* Major: Automation and Control (Russian classifier - 220200) 
* Thesis: Development of methods and tools for reengineering of digital hardware defined by HDL specifications.

# Files

* [Thesis](./thesis.pdf)
* [Slides from the thesis defence](./defence-slides.pdf)

## Abstract

Reengineering can be used to improve device characteristics (performance, power effectiveness, reliability, etc.), or to add new features.
Modern systems are very complex, and there is a common use case task for reengineering automation.
This work approaches to build an extensible toolkit, based on which can be resolved by custom tasks of reengineering.
Survey of the existing tools shows there are no fully programmable reengineering automation tools.
This area remains very prospective.

This work presents a new model of a device for representation, analysis, and transformation of digital systems described in hardware description languages (HDL).
This model is based on an architecture graph with a limited number of basic node types.
Graphs can be divided into tree-like structural description and links between elements.
Hardware representation includes mechanisms for extension and navigation.
A minimal command set for model transformation was developed.

As a part of the project we designed the architecture of a hardware reengineering toolkit that meets basic requirements (programmable, extensible, embeddable).
This toolkit is built in a modular fashion with a minimal kernel that implements device model, basic operations, and application programming interface (API).
All other features (including HDL’s input-output) should be implemented in extensions that the kernel supports.

Prototype of programmable reengineering toolkit was developed as a part of the research.
Results of conducted experiments confirm applicability of the proposed model and system architecture.
