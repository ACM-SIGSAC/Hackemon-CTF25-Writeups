## 🎧 Disrupted Noises?

**Category**: CRYPTO  
**Points**: 200  
**Author**: Ateeb Ali 

---

### 🕵️ Challenge Description

> What is this noise about?  
> *Make sure to use underscores where necessary.*

**Hint**:  
> Does ROT47 have something to do with this?

---

### 🔍 Challenge Overview

You're given a strange audio file named `audio.wav`. No obvious text or encrypted string, but the title and hint suggest noise and ROT47 — sounds like something hidden in the **sound itself**.

---

### 🧩 Solution Strategy

1. **Analyze the Audio File**  
   The sound in the `audio.wav` file is actually **Morse code**. Use [morsecode.world](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) to decode the audio.

2. **Decoded Output**  
   You'll get the string: "N0HZAGVBNVTZZ@NTO0A1IYT3OCVMY"

3. **ROT47? Not quite…**  
The hint mentioned ROT47, but what if that's a *misleading nudge*?  
Try using **CyberChef** and apply the **ROT13 operation**, but set the key as `-47` instead of 13.

Use this tool: [CyberChef](https://gchq.github.io/CyberChef/)

4. **Decryption Output**  
Applying ROT13 with a shift of `-47` gives you:
S0MEFLAGSAYEE@SYT0F1NDY3THARD

5. **Final Touch: Format the Flag**  
Add the required underscores and wrap it in the flag format: ACM{flag}

---

### 🎯 Final Flag

ACM{S0ME_FLAGS_ARE_E@SY_T0_F1ND_Y3T_HARD}

---
