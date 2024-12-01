# CyberSecProject Group 13

## **Contributors**
 * Sophia Leeseberg
 * Ellie Clark
 * Rogelio Atilano
 * Rodrigo Pandal
 * Gage Buckley

## **Description**
This code implements a replica of the attack method used in the SainT algorithm from the paper "Sensitive Information Tracking in Commodity IoT". It checks for data leaks using the Wikipedia API, which can retrieve multiple types of information, including:
- Geolocation (via geosearch)
- Date & time
- Other user-specific data
- Other page-specific data

The aim is to simulate a potential privacy issue within IoT ecosystems by checking for the leakage of sensitive data through these API calls. The Tester program calls the algorithm to run and listen for these
types of information and outputs instances where there could be a potential data leak. For our case, we define a data leak as the transfer of sensitive user information such as their name, location, spoken language,
and other information. When this information is picked up by the program, the testing algorithm flags this in the report for all the test cases. When run on its own, the WikiInteract file will become an interface where
the user can see the types of information that is trasnfered through wikipedia and the form in which it can captured.

## **How to run**

### **Requirements**
 * [Python 3](https://www.python.org/downloads/)
 * Wikipedia
    * `pip install wikipedia`
 * Wikipedia API
    * `pip install wikipedia-api`
 * Requests
    * `pip install requests`
 * Numpy
    * `pip install numpy`

### **How to run**
 * Clone the repository on your local machine, code can be run from the 'main' branch
 * Run `WikiInteract.py`
 * Input one of the listed types of data (case sensitive)

## **Running Testcases** 
 * Run 'Tester.py'

## **Research**

### **1st Source:** [Sensitive Information Tracking in Commodity IoT](https://arxiv.org/pdf/1802.08307v1)
This source discusses privacy concerns in IoT devices and proposes a solution to address them in the form of an algorithm called Saint. Saint effectively flags sensitive data flows and highlights potential risks for further investigation. Saint provides a systematic approach to identifying sensitive data flows in IoT apps and supports developers and regulators in enhancing privacy safeguards. However, its scope is limited to detecting potential data leaks and requires manual inspection to assess the real-world impact of these leaks.

### **2nd Source:** [Real-time Analysis of Privacy-(un)aware IoT Applications](https://arxiv.org/abs/1911.10461)
This source discusses growing privacy risks in IoT ecosystems and highlights the common challenges in existing solutions. Many solutions inaccurately detect leaks, are too complex, or completely neglect user-defined strings. This paper proposes a solution called IOTWATCH, which is a dynamic analysis tool designed to address user privacy concerns through a survey-driven understanding of their preferences. IOTWATCH allows users to specify privacy settings during app installation. This source shows an improved version of Saint.

## **Known Issues**
- The current version of this tool only interacts with the Wikipedia API.
- Manual inspection is still required to assess the impact of detected leaks in real-world scenarios. The tester only identifies what was previously described as a "data leak", different interpretations of this can exist.
