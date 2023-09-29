# Module 6 - Real World Tasks / Examples

The objective with this module is to look at tasks that can be completed with the help of code and automation to expedite completion and dissemination to SecOps team members.

The following code will be executed from the top level directory of the project `/developing-with-attack-workshop/`

## Part 1 - Fast Lookup of Techniques to Cache Locally

1_fast_lookup.py is parsing all the relationships available in the STIX data and building out the appropriate Software + Techniques associated for threat actor Groups. There is no terminal output from running the command, however a group-techniques.yml file is created to store the mappings locally for follow-on analysis.

`$ python 6-Real-World/1_fast_lookup.py`

## Part 2 - Group Lookups to Determine Similarity to a List of Techniques

2_group_lookup.py takes in a list of techniques from an IR event or CTI input and it compares that list of techniques against known techniques for all groups and does a similarity lookup to find the most similar group. The output is a list of the most similar group matchings.

`$ python 6-Real-World/2_group_lookup.py`

## Part 3 - Create a Navigator Layer Based Off of a List of Techniques

3_create_layer.py builds a layer off of the techniques passed in from the yaml file lapsus_ir_scenario.yml.

`$ python 6-Real-World/3_create_layer.py`

## Part 4 - Crosswalk CREF

Data mapped to Techniques is a powerful process that allows us to move from other Frameworks to ATT&CK, vendor detections to ATT&CK, etc. Start with a dataset of all Candidate Mitigations, then invert it into a mappings of mitigations and controls per Technique. This allows us to later crosswalk from a list of Techniques covered by defensive tooling to our NIST posture == crosswalk from one framework to another.

## Part 5 - CrowdStrike Detection Coverage API Analysis

Continuing this theme of data mapped to Techniques; take the CSV export of the CrowdStrike API and build a list of Techniques (eventually a heat map) showing the coverage of the EDR platform.

* Read in CSV export
* Parse into JSON for readability
* Read in all the STIX data
* Match on Technique names in JSON data to build out list of Techniques and detection counts
