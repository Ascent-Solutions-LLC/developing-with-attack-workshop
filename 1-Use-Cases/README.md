# Use Cases

Why should we develop against MITRE ATT&CK?

Many of the security tools, systems, and platforms we use, already speak ATTC&K.
Let's explore two straightforward defensive examples.

## 1. Parse Sigma Rules
In this example we parse a Sigma rule and extract the applicable Technique IDs associated to a rule.

## 2. Analyze Azure Sentinel Rule Templates
In this example, we pull back a list of built-in rule templates for Azure Sentinel to demonstrate how MITRE ATT&CK information is provided inside of security tooling.

### Requirements
In order for this to run successfully, you will need to provide Azure details as indicated in the `os.environ` variables in the script.

You will also need to be authenticated to Azure using something like Environment Credentials or an `az login` session.
