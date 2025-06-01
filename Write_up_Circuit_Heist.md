
## 🚗 Challenge Write-Up: Circuit Heist

**Category:** Web  
**Difficulty:** Hard  
**Challenge Title:** *Circuit Heist*  

**Description:**  
> Pit Stop Panic! Welcome, Race Engineer! The high-stakes world of Formula 1 finance has hit a snag. Navigate the intricate backchannels of the Grand Prix Banking System, uncover secret team accounts, strategically "adjust" funds between drivers, and exploit any technical loopholes you can find to redistribute the wealth. Your mission starts with a seemingly routine transfer between rivals... Can you pull off the ultimate financial undercut?

---

### 🧠 Initial Recon

Opening the challenge shows a dashboard with the user logged in as **Carloz**, displaying a current balance. Below that are other users (e.g., Rocket, Gamora, etc.) with their own balances. There’s a **hidden field** named `sender` visible only through browser inspection.

There’s also a **receiver** dropdown, and an **amount** field along with a **submit** button.

---

### 🗂️ Step 1: robots.txt

Visiting `/robots.txt` reveals:

```
User-agent: *  
Disallow: /admin
```

This hints at a hidden admin route.

---

### 🔒 Step 2: Accessing /admin

Visiting `/admin` gives:

> “You are not allowed. Only the members who have balance more than 2000 are allowed to get the secret.”

This implies our goal is to **increase Carloz's balance above 2000**.

---

### 🔍 Step 3: Observing the Transfer Mechanism

By using **Burp Suite** and intercepting a transfer, we observe:

```
GET /?sender=Rocket&receiver=Rocket&amount=2000 HTTP/1.1
```

You can manipulate:
- `sender`
- `receiver`
- `amount`

But you **cannot send money to Carloz** directly, and negative/float values are blocked with validation errors.

---

### ⚙️ Step 4: Exploiting Float Precision via Burp Suite

Editing the intercepted request to:

```
GET /?sender=Gamora&receiver=Rocket&amount=0.9999999 HTTP/1.1
```

Successfully transfers the float value, bypassing frontend validation. Repeating this allows accumulating small amounts in Rocket's account.

Still, **Carloz cannot be the receiver directly** — a message appears:

> “You cannot send money to Yourself!!!”

---

### 🧨 Step 5: HTTP Parameter Pollution (HPP)

Here’s the trick: You can bypass the restriction using **duplicate parameters**.

**Original:**

```
GET /?sender=lando&receiver=lewis&amount=1200
```

**Exploited version:**

```
GET /?sender=lando&receiver=lewis&amount=1200&receiver=carloz
```

Using HTTP Parameter Pollution (HPP), the **second `receiver` is processed**, and Carloz receives the funds.

---

### 🧪 Final Step: Accessing /admin

Once Carloz's balance is **greater than 2000**, visiting `/admin` shows:

> 🎉 “Congratulations, here is your flag: ACMCTF{<REDACTED>}”

---

