# CyberSecProject Group 13

## Contributors
 * Sophia Leeseberg
 * Ellie Clark
 * Rogelio Atilano
 * Rodrigo Pandal
 * Gage Buckley

## Description
This code implements a replica of the attack method used in the SainT algorithm from ___. It checks for data leaks using the wikipedia api which can retrieve multiple things including geosearch, date & time, and info on the user.

## How to run

### Requirements
 * [Python 3](https://www.python.org/downloads/)
 * Wikipedia
    * pip install wikipedia
 * Wikipedia api
    * pip install wikipedia-api
 * Requests
    * pip install requests
 * Numpy
    * pip install numpy

### How to run
 * Run Wiki Interact.py

## Research
1st Source: Sensitive Information Tracking in Commodity IoT (https://arxiv.org/pdf/1802.08307v1)
   This source discusses privacy concerns in Iot devices and proposes a solution to address them called Saint. Saint effectively flags sensitive data flows and highlights potential risks for further investigation. Saint provides a systematic approach to identifying sensitive data flows in IoT apps and supporting devolpers and regulators in enhancing privacy safeguards. However, its scope is limited to detecting potentional data leaks and requires manual inspection to assess the real world impact of these leaks.


2nd Source: Real-time Analysis of Privacy-(un)aware IoT Applications (https://arxiv.org/abs/1911.10461)
   This source discusses growing privacy risks in Iot ecosystems and highlights the common challenges in existing solutions. Many solutions inaccurately detect leaks, are too complex, or completely neglect user-defined strings. This paper proposes a solution called IOTWATCH which is a dynamic analysis tool designed to address user privacy concerns through a survery driven understanding of their preferences. IOTWATCH allows users to specify privacy settings during app installation. This source shows an improved version of Saint.
