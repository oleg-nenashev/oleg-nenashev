# PhD Degree - Hardware Design

* University: [St.Petersburg State Polytechnic University (SPbPU)](https://english.spbstu.ru/)
* Department: Computer Systems and Program Technologies
* Research Group: Electronic Design Automation Lab (EDA Lab)
* Thesis: Reengineering of digital hardware, and embedding test modules and interfaces into devices described by multilevel models
* Keywords: hardware representation models, methodologies for the automated synthesis of integrated circuit testing and built-in self-test components, prototyping of automated hardware reengineering toolkits

## Files

* [Extended Abstract (Rus)](./extended-abstract.pdf)
* [Thesis (Rus)](./thesis.pdf)
* [Slides from the thesis defense (Rus)](./defense-slides.pdf)

## Results

New model for hardware representation:

* A multilevel model of the architecture of single-chip digital devices with fixed inter-element connections has been proposed.
  This model differs from existing approaches by combining formalisms for describing architectures at both the physical and semantic levels.
  Such an approach enables the reengineering of devices from arbitrary initial descriptions.
* A universal model of the architecture for embedded subsystems of on-chip testing and self-diagnostics in single-chip digital devices has been developed. Unlike existing models, it is applicable to reengineering tasks, enabling the unification of methods and tools for the analysis and synthesis of digital computing and control systems.

Scientific Contributions of the Dissertation:

* A methodology for developing domain-specific models of single-chip digital devices based on the proposed hybrid metamodel has been created.
  This methodology is distinguished by the combination of applied algorithms, which expands the class of reengineering problems that can be addressed.
* An algorithm for reverse engineering of single-chip digital device architectures has been developed.
  It is distinguished from existing solutions by its use of a combination of descriptions in high-level abstraction languages and physical implementation levels,
  thereby broadening the range of architectures subject to recovery.
* Methods for synthesizing test subsystems for digital systems-on-chip have been developed.
  These methods differ from known approaches by allowing the creation of testing tools based on a set of controllable and observable signals,
  thus reducing the labor intensity of test infrastructure development.
* A methodology for parallel verification of a digital device model and its physical prototype has been introduced.
  It is distinguished by the absence of a requirement for processor cores, enabling verification of non-programmable single-chip digital devices.

Practical Results:

* The proposed models and methods can be applied in the design of new development tools and electronic design automation (EDA) systems
  aimed at diagnostics, analysis, and architectural modification.
  The dissertation provides case studies demonstrating the application of the developed models and methods to specific reengineering tasks.
* The Programmable Hardware Reengineering Toolkit (PHRT toolkit), developed as part of the research,
  have been evaluated by Synopsys SPB LLC (a Synopsys Inc. representative office)
  and SDC LLC for reengineering and on-chip testing tasks during the design of complex digital systems-on-chip.
 This is confirmed by official implementation reports.
* The research results have been integrated into the academic curriculum of the course "Hardware Design of Computing Systems" at the 
  Department of Computer Systems and Software Engineering, Institute of Computer Science and Technology, St. Petersburg State Polytechnic University.
  This is also confirmed by an official implementation report.

## Slides

![PhD Slides](./defense-slides.pdf){ type=application/pdf style="min-height:50vh;width:100%" }

## Publications

1. Nenashev O, Mamoutova O, Filippov A. Automation of the low-level memory failure emulation injection into systems on chip. Proceedings of the universities. Electronics. 2015; 2.
2. Mamoutova OV, Nenashev OV, Filippov AS. In-circuit Emulation of Memory Fault Injection. Recent Advances in Electrical Engineering and Computer Science. 2014:105-107.
3. Nenashev O. Methods of the test infrastructure injection into digital devices based on the automated engineering tools. Problems of Advanced Micro- and Nanoelectronic Systems Development. 2014;2:101-106
4. Nenashev O. An Extensible Framework for Automated Hardware Reengineering of Complex Systems-on-Chip. Humanities and Science University Journal. 2013; 5:194-203
5. Nenashev O. PHRT: a model and programmable tool for hardware reengineering automation. In: Proceeding of 9th European Software Engineering Conference. New York: ACM; 2013:719-722
6. Nenashev O. PHRT: A programmable tool for automated hardware reengineering and verification. In: Proceedings of the International Workshop on Verification of Embedded Systems 2013 (VES2013). Saint Petersburg; 2013:5-13
7. Nenashev O. Automated synthesis of in-circuit testing components with use of programmable hardware reengineering tools. In: Proceedings of the Youth Science Symposium. Vol 1. Saint Petersburg: SPBSTU; 2012:37-42
8. Nenashev O. Automated test instrumentation and BIST insertion with usage of automated reengineering toolkit. In: Proceedings of XIIIth International Conference “Fundamental and Applied Research in Russia". Vol 2. Saint Petersburg: SPBSTU; 2012:46-49
9. Nenashev O. Concepts of programmable tools for automated analysis and transformation of digital device architectures described by VHDL. In: First International Congress of PhD Students. Saint Petersburg: ITMO University; 2012.
10. Nenashev O. Developing an automated reengineering methodologies of digital systems on chip described by HDL specifications. 2011.
12. Nenashev O. Developing a programmable toolkit for automated structural redundancy insertion. In: Proceedings of XXXIX SPBSTU Week of Science. Vol 5. Saint Petersburg: SPBSTU; 2010:46-47.
