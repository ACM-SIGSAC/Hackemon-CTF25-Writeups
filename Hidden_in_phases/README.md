**🔍 Writeup - Hidden in Phases**

Author: Ammara Qazi,
Category: Crypto,
Difficulty: Medium

**FLAG: ACM{WWZVAZHKPOFX}**

**📜 Challenge Description:**

A classified transmission was intercepted from a long-abandoned lunar research facility.
 The message is inscribed in an ancient lunar script, rumored to be used by a secretive space agency to conceal their most sensitive data.
Experts who attempted to decipher it can only conclude:

 "The answer lies within the phases of the moon."

Yet, the image accompanying the transmission hums with secrets, as though its surface tells only part of the story.
 Hidden clues may lie deeper, like in the stars, waiting to be uncovered.

⏳ With time slipping away and the void threatening to swallow the message, only those who can unravel its secrets will uncover the truth.
Hint: Flag is in encrypted form of the text.

**Step-by-Step Walkthrough:**

**Step 1: Observing the Image**

Upon opening the file lunar_17.png, the participant sees a space background filled with stars and two horizontal bands containing images of the moon in various phases.
The moons seem to resemble glyphs rather than regular photos.
This unusual design hints that the image may be symbolic or encoded, rather than purely illustrative.

**Step 2: Lunar Phases Are Not Just Lunar Phases…**

The challenge hints:
"The message is inscribed in an ancient lunar script…"

This should ring a bell for experienced solvers - the Lunar Alphabet by L. Katz, a cipher system where each lunar phase represents a letter of the alphabet.

**Step 3: Decoding the Lunar Alphabet**

Participants can:
Use tools like dcode.fr's Lunar Alphabet Cipher tool to decode it.
Manually map each lunar glyph from the image to its corresponding letter.

👉 Once the lunar phases are transcribed and decoded, they get the plaintext:
TWILIGHTMOON

**Step 4: But That's Not the Flag!**

Back to the hint:

"Flag is in encrypted form of the text."

This tells the solver the flag is an encryption of TWILIGHTMOON, not the direct result of the lunar glyphs.

**Step 5: Trying Common Ciphers**

In CTF crypto challenges, when something is described as "encrypted" and the encryption isn't specified, solvers usually try common classical ciphers, starting with:

Caesar Cipher

Atbash

Vigenère Cipher

Vigenère is a standard go-to cipher in many CTFs because it's simple, key-based, and produces mixed uppercase outputs,

✨ Q: How to guess the key is Darkstar?

 A: Hints like "stars", "twilight", and the space/moon theme all point to "Darkstar" as a logical poetic keyword.
Trying a Vigenère Cipher with the key DARKSTAR (derived from the challenge theme: space, stars, twilight...) gives:

Plaintext:  TWILIGHTMOON  

Key:        DARKSTAR 

Encrypted:  WWZVAZHKPOFX

✅ Final Flag:
ACM{WWZVAZHKPOFX}
