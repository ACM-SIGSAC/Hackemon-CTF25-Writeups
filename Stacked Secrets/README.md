## 🧩 Decrypting Secrets: “Stacked Secrets” CTF Challenge

**Category**: CRYPTO | **Points**: 200  
**Author**: Ateeb Ali

---

### 🔐 Challenge Overview

You're given an RSA-encrypted message Secure enough or should we double the security?
Hint: which cipher requires Ps & Qs?

---

### 🔍 Challenge Analysis
We are given three blocks:

An RSA public key
An RSA private key
An encrypted message

The title and hint suggest we’re dealing with a standard RSA encryption. The mention of “Ps & Qs” hints towards RSA, where P and Q are the two large primes used to generate the key.

### 🛠️ Solution Steps
1- Recognize the format:
This is a classic RSA encryption challenge.
Since both the private key and the ciphertext are provided, all that’s left is to decrypt the message.

2- Use a tool to decrypt RSA:
Visit [AnyCript](https://anycript.com/) or any RSA decryption tool that allows importing a private key.
Paste the private key and the encrypted message.
The tool will decrypt the message and give you a hex string output.

3- Hex output from decryption:
41 43 4d 7b 52 53 41 5f 44 33 43 30 64 33 44 5f 53 75 63 63 33 24 24 46 75 31 31 59 7d

4- Convert Hex to ASCII:
Open [CyberChef](https://gchq.github.io/CyberChef/)
Use the "From Hex" operation to convert the hex string to plaintext.

---

### 🎯 Final Flag

ACM{RSA_D3C0d3D_Succ3$$Fu11Y}

---

### 🧠 Key Concepts Covered

- RSA encryption/decryption
- Online decryption tools
- Hex to ASCII conversion

