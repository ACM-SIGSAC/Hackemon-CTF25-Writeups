## 🎬 The_Movie

**Category**: OSINT  
**Points**: 100  
**Author**: Ateeb Ali  

---

### 🕵️ Challenge Description

> What is the name and the date the production began of the movie this scene is from?  
>  
> **Flag Format**: `ACM{movie_name_dd_mm_yyyy}`

---

### 💡 Hint

> It was chosen by the National Board of Review as one of the top ten films of 2010.

---

### 🧠 Solution Strategy

1. **Analyze the Image**
   - You're given a single movie frame — nothing else.
   - Use **Google Lens** or **reverse image search** to identify which movie the still is from.

2. **Identify the Movie**
   - Google Lens or visual recognition will reveal that the frame is from the psychological thriller:
     ```
     Shutter Island
     ```

3. **Research the Production Start Date**
   - Once the movie is identified, search:
     > "Shutter Island production start date"
   - Verified sources like:
     - [Fandom.com](https://movies.fandom.com/)
     - [KinoPoisk / KinoRium](https://en.kinorium.com/)

   - You’ll find:
     ```
     Filming began on March 6, 2008
     ```

4. **Construct the Flag**
   - Format as per challenge instruction:
     ```
     ACM{shutter_island_06_03_2008}
     ```

---

### 🎯 Final Flag

ACM{shutter_island_06_03_2008}

---
