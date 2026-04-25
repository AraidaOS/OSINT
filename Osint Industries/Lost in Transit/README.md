Description:
***
### 🚉 Lost in Transit

Hello,

a photo was taken, apparently in a train station.

Your mission is to determine:

1. **Which train station** this photo was taken in  
2. **The approximate time window** when it was taken, with a precision of **two hours**

Expected time format:  
- 8am–10am  
- 10am–12pm  
- 12pm–2pm  
- 2pm–4pm  
- etc.

---

### 🎯 Flag format  
`OSINT{station_name_time-range}`

---

### ✅ Example  
`OSINT{example_station_2pm-4pm}`
***

Image: [https://ctf.osint.industries/files/5b8d4917f71e0e88bc815c9a74ff9c01/img.jpg?token=eyJ1c2VyX2lkIjoxODk2LCJ0ZWFtX2lkIjpudWxsLCJmaWxlX2lkIjoxMH0.aeyXdQ.jK9LfEHYrfjoCh-wxEuiuiZrd8s]

Upon opening the Image for first inspection, we catch the train number `93 87 0029`.
Simple google search reveals it is a `Alstom TGV Duplex high-speed trainset operated by SNCF Voyageurs in France`.
(We also notice the french flag).

<img width="810" height="458" alt="Screenshot 2026-04-25 123605" src="https://github.com/user-attachments/assets/11b96cd9-1f62-423c-af17-7296f3a3d40d" />

After some digging and looking in google maps and satelite imagery we finally found a train station that resembles the one in the image.

The sattion: `Marseille Saint-Charles`

<img width="497" height="451" alt="image" src="https://github.com/user-attachments/assets/f479f045-c81e-4afd-ad9e-42854acfc4e9" />



