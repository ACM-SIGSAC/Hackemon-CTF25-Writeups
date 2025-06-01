# 🕵️‍♀️ Decrypting Layers:“ONION” CTF Challenge

**Category:** CRYPTO | **Difficulty:** Easy
**Author:** Rabia Ishtiaq

Let me walk you through how to solve it step-by-step — all using online tools.

## 🔐 Challenge Overview

You’re given a mysterious encrypted message. No clue, no hints — just a note saying:

>Buried beneath layers of secrecy lies the truth. Like peeling an onion, each layer reveals another puzzle, another cipher another barrier between you and the flag. 

Here’s the encrypted message (yes, it’s long — don’t panic):

```
MnkvQ2ZqKk0jKThcJj9PUzJ5JDBoKypNKGFDdDxuT1QtPyQwaDNXXiMpRFQmN1JCMz0kLGZqJ14jJ0RYPGZPVDM7JCxmaldeIydEWDtAT1QzPSQwaDMqTCMnRFgmP1JDMz0uXmZqV04oYURYJjchUjM9L0NoMypNIWNDdDxuT1MzPSQwTzsqXSMpRFg8blIyMnkvQ2ZqV14jJzhcJj9PUzJ5JCxmYipNKGNEWDxmT1QtPyQwaDMqTShhRFQmN1JDMz0kLGgzJ14jKURYPGZPVDM7JCxoMypdKGNEWDtAT1QyeS9DaDMqTCMnRFg8ZlJDMz0uXmZqV04oY0RYPG4hUjJ5L0NmaldOIWNDdDxuT1MzPSQwTzsqXShhQ3Q8ZlIyMnkvR2gzV14jKThcJjdSQjJ5JCxmYipNIydDdDxmUkI=
```

---

## 🧩 Step 1: Base64 Decoding

Our first stop is Base64 — a familiar format used often in encoding text data. Head over to a trusted online tool like:

* 🔗 [https://www.base64decode.org/](https://www.base64decode.org/)
* 🔗 [CyberChef](https://gchq.github.io/CyberChef/)

Paste the message, decode it, and boom — you’ll get a new string filled with strange symbols. Don’t worry — that’s **Base92**.

```
2y/Cfj*M#)8\&?OS2y$0h+*M(aCt<nOT-?$0h3W^#)DT&7RB3=$,fj'^#'DX<fOT3;$,fjW^#'DX;@OT3=$0h3*L#'DX&?RC3=.^...
```

---

## 🧩 Step 2: Base92 Decoding

Now that you've peeled off the Base64 layer, you’ll need to deal with the less common cousin — **Base92**. This one isn't as widely supported, but a quick Google search for *"Base92 decoder online"* should give you a few usable options. Here's one I found useful:

* 🔗 [https://tomeko.net/online\_tools/base92.php](https://tomeko.net/online_tools/base92.php)

Paste the Base64-decoded string here and hit decode.

You should now see a **long binary string** — hundreds of 1s and 0s.

```
01000001 01000011 01001101 01111011 01010000 00110011 00110011 01101100 01011111 01010100 01101000 01100101 01011111 01001100 01000000 01111001 01100101 01110010 01110011 01011111 01010100 01101111 01011111 00100100 01100101 01100101 01111101 00100000 00001010
```

---

## 🧩 Step 3: Binary to Text Conversion

The final layer is plain old binary. To reveal the actual message, head to:

* 🔗 [https://www.convertbinary.com/binary-to-text/](https://www.convertbinary.com/binary-to-text/)

Paste the binary string and hit convert. And just like that — you’ll reveal the hidden **flag**, usually in the format:

```
ACM{P33l_The_L@yers_To_$ee}
```

---

## 🎉 Final Thoughts

What makes this challenge so great is how it tests your awareness of different encoding schemes — not just knowing them, but understanding how to reverse them in sequence. It’s not about deep cryptography — it’s about attention to detail and methodical problem-solving.


If you're new to CTFs, challenges like these are perfect for building confidence and learning how to break things down layer by layer.

