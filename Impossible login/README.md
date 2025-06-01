## 🧩 Challenge Writeup – "IMPOSSIBLE LOGIN" (Beginner-Friendly)
---
## DESCRIPTION:
Not every doorway is meant to be opened.
Not every path leads to light.
Beyond the veil of simplicity lies a domain built on misdirection, patience, and the silence of unanswered questions.
Here, every step you take may either bring you closer to clarity — or bury you deeper in confusion.
Choices matter, but appearances lie.
You are free to roam, but you are not free from doubt.

This challenge was crafted for those who do not trust what they see —
for those who question everything and expect nothing in return.

There is no guidance.
There are no breadcrumbs.
Only the void... and the possibility of triumph.

This CTF (Capture The Flag) challenge is based on:

* **Login flow tricks**
* **Session management**
* **Finding hidden pages (endpoints)**

---

## 🔍 Step-by-Step Guide

### 1. **Starting Point – `/login`**

* When you open the main page ( `/` ), it **automatically redirects** you to `/login`.
* The **login form asks for a token**, but you don’t know where to get that token yet.

---

### 2. **Getting the Token – `/pre-auth`**

* Try checking if there are **other hidden pages**.
* If you go to `/pre-auth`, you will see something like:

  ```
  Your pre-auth token: abc123xyz
  ```
* This is the **token you need to log in**.
* ⚠️ **Important:** This token is **only valid for 20 seconds**! So be quick.

---

### 3. **Logging In**

* Go back to the `/login` page.
* Paste the token from `/pre-auth` into the login form.
* If the token is still valid, you’ll successfully log in.
* Behind the scenes, this happens:

  ```python
  session['logged_in'] = True
  session['visited_race'] = False
  ```

  This means you're now logged in, but you haven't completed everything yet.

---

### 4. **Exploring After Login – `/dashboard`**

* After logging in, you’re sent to `/dashboard`.
* This page doesn’t show anything useful — it's just a **distraction**.

---

### 5. **Looking for Clues – `/about`**

* There's no real `/about` page, but the **hint "race"** may appear in a clue or description.
* That word leads us to **try `/race`**, a **hidden endpoint**.

---

### 6. **The Hidden Page – `/race`**

* When you visit `/race`, you see:

  ```
  You feel like you are on the right track...
  ```
* More importantly, it updates your session:

  ```python
  session['visited_race'] = True
  ```
* This means your account now **remembers** that you visited `/race`.

---

### 7. **Getting the Flag – `/get-flag`**

* Now try going to `/get-flag`.

#### Two possible results:

* ❌ If you didn’t visit `/race` first:

  ```
  You haven't explored enough.
  ```
* ✅ If you **did** visit `/race`:

  ```
  ACM{you_found_it}
  ```

---

## ⚠️ Tricks & Distractions to Watch Out For:

### 1. **Token Time Limit**

* The token only works for **20 seconds**.
* If you’re too slow, you’ll need to go back to `/pre-auth` and get a new one.

### 2. **Fake Flag – `/fake-flag`**

* This page shows:

  ```
  ACM{this_is_a_trap}
  ```
* It’s a **decoy**, not the real flag!

### 3. **Forbidden Page – `/debug`**

* If you try `/debug`, you get a **403 Forbidden** error.
* It's just there to **distract you**.

### 4. **Robots.txt File**

* If you check `/robots.txt`, you see:

  ```
  Disallow: /race
  Disallow: /debug
  ```
* This file is meant for search engines, but **you can use it to find hidden paths!**

---

## ✅ Final Summary

To solve the challenge:

1. Go to `/pre-auth` → copy the token.
2. Use it at `/login` quickly.
3. Visit `/race` to set the right session variable.
4. Now go to `/get-flag` → 🎉 Flag revealed: `ACM{you_found_it}`

---
