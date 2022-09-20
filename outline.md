# Outline for Developing with ATT&CK Workshop

## Introduction and use cases. 
Why should we develop against MITRE ATT&CK?

## Frameworks and protocols.
How is MITRE ATT&CK organized, structured, and communicated?

## Data
Where can we obtain data about MITRE ATT&CK?

## Versioning
How does MITRE handle versions/upgrade and why do we care?

## Existing tools and platforms
What does MITRE provide? What does our community provide?

## Development time!
Design, gather, process, and build a functional processing tool using Python.


* Mental models needed to interact with ATT&CK STIXX data
* STIXX objects
  * Data Sources
  * Mitigations
  * Groups
  * Techniques
  * Software

Gotchas:

* ATT&CK does Group Navigator layers with TTPs __only__ not the Software that they have also used
* Enumerating STIX data can be costly, caching considerations


Nod to MITRE ATT&CK Defender course....although it covers more of the theory than the practical that our course will discuss.


Expand upon https://attack.mitre.org/resources/working-with-attack/

STIX/TAXII server call considerations

ATT&CK Workbench?

ATT&CK pip module?
https://github.com/mitre-attack/mitreattack-python

Navlayers example with pip module?

Nav layer updater that Brian created??? Cool tool!!!