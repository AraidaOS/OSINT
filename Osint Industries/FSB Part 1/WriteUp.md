Description:
***
Important

The following challenges are provided strictly for OSINT training purposes.
They are based on real-world leaked material and must be handled responsibly.

Participants must remain strictly passive:

    No contact with individuals
    No interaction with real accounts
    No harassment or operational use
    Analysis and reasoning only

CHALLENGE 1 — DATE OF BIRTH IDENTIFICATION
Context

A historical dataset linked to an FSB-related leak contains partial civil information.
Only the individual’s identity is visible. The date of birth is missing.
Known Information

    Full name: КОВЖАРОВА ЕЛЕНА АЛЕКСАНДРОВНА
    Gender: Female

Objective

Using open-source intelligence methods, determine the date of birth of the individual.

No direct access to private databases or accounts is permitted.
Flag format

OSINT{DD/MM/YYYY}
***

After a simple google serach for the name "КОВЖАРОВА ЕЛЕНА АЛЕКСАНДРОВНА" in english,
which is: "KOVZHAROVA ELENA ALEXANDROVNA", we find a website that has the entire database leak.

Website: "https://www.thetechoutlook.com".

full URL: "https://www.thetechoutlook.com/featured/anonymous-has-leaked-personal-data-of-over-600-russian-fsb-officers-operate-in-moscow/"

On kali, we can 'curl' the entire webpage into a file called 'database.txt' and search for our agent.

<img width="937" height="395" alt="grep_database" src="https://github.com/user-attachments/assets/376789ac-c145-45de-9cac-1eaa41edfc38" />

***
The flag: OSINT{11/12/1968}
***
