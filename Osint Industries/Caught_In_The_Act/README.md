Challenge: Caugh In The Act

Platform: Osint Industries

Solved: Yes

Description:
"""
Challenge:

A photo has been recovered during an investigation.
Your objective is to determine: • The name of the university where the photo was taken • The city in which it is located
Flag format: OSINT{"university_name_city"}
Example: OSINT{"harvard_university_cambridge"}
Good luck.
"""

Solution:

- Check for subtle hints inside the Image, some were found, mediteranian style buildings, star in the middle.
- Clean the Image from the "red doodle" before letting an LLM digest it, using a simple python script with OpenCV.
- LLM returns the location and info, we confirm on Google Maps, and return the flag.

Before doodle removal:

<img width="1652" height="1266" alt="image" src="https://github.com/user-attachments/assets/75511f3f-7ee4-429b-bb71-31c0f948e340" />


After doodle removal:

<img width="1652" height="1266" alt="image" src="https://github.com/user-attachments/assets/aa1b00ae-b32a-4c06-b0c3-06da9e58de11" />

Google Maps Image:

<img width="1425" height="752" alt="caught_in_the_act" src="https://github.com/user-attachments/assets/f67b4c26-0f04-4fdc-8ade-fe43194253a5" />


Flag: OSINT{"bond_university_robina"}

Note:
Robina is a suburb in the city of Gold Coast, queensland in Australia. the challenge did not accept the city name, but did accept the suburb name.
A feedback was submitted to the site.
