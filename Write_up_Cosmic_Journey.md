## 🚐 Challenge Write-Up: Cosmic Journey

**Category:** Web  
**Difficulty:** Medium  
**Challenge Title:** *Cosmic Journey*  

**Description:**  
> Embark on an interstellar journey to uncover a hidden secret! Traverse the vastness of space, navigating through a series of cosmic checkpoints. Decipher cryptic clues, bypass celestial obstacles, and prove your worthiness to reach the ultimate destination.

---

### 🧠 Initial Recon

Upon opening the challenge, we’re greeted with the message:

> “Welcome to page one of sanity check in space.”

There’s also an image of a robot on this page — a clear hint toward checking for a common file: `/robots.txt`.

---

### 🗂️ Step 1: robots.txt

Accessing `/robots.txt` gives us:

```
User-agent: *  
Disallow: /humans.txt/
```

This hint nudges us to try `/humans.txt` next.

---

### 👨 Step 2: humans.txt

Navigating to `/humans.txt` reveals:

> “Welcome fellow human to page three of sanity check in space! You look pretty human, but we have to be sure. Go eat something and come back.”

Alongside this message is an image of an astronaut holding cookies — a hint to inspect or manipulate browser cookies.

---

### 🍪 Step 3: Cookie Manipulation

Inspecting the browser’s cookies reveals a value such as:

```
human=false
```

We change this to:

```
human=true
```

After refreshing the page, we’re greeted with:

> “Wow, you really are human, celebrate with us by visiting /arrakis”

---

### 🦐 Step 4: arrakis

Accessing `/arrakis` brings us to page four:

> “Welcome master jedi to page four of sanity check in space. We want to party, but this place is password protected, so we might as well give up.”

There's a password input field. The hint? If you go back to the very first page, you'll spot a small, obscure password at the **bottom-left corner**.

Submitting that password progresses us to the final message:

> “Excellent job. One ultimate challenge awaits you, on /krypton.”

---

### 🧪 Step 5: krypton (Command Injection)

Now at `/krypton`, we see:

> “Welcome to the final page of sanity check in space. This is the ultimate challenge. This is: ping but in space.”

There’s a text field labeled **“Space Ping”**, used to ping websites — but this is where command injection comes in.

Most common payloads such as:

```
; ls  
&& whoami  
| cat flag.txt
```

are blocked.

However, the `dir` command (Windows) is allowed.

Running:

```
dir
```

reveals a file:

```
ACM_ctf.txt
```

Then, we can try:

```
more ACM_ctf.txt
```

This finally displays the **flag**.

---

### 🏋️‍♂️ Flag

```
ACMCTF{<REDACTED>}
```

*(Replace `<REDACTED>` with the actual flag if allowed to share.)*
