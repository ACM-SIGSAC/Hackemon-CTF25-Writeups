🔐 THE SECRET PLAN — Writeup

AUTHOR: Ammara Qazi, CATEGORY: Crypto, LEVEL: Medium

**Flag: ACM{Aurangzeb}**

CHALLENGE OVERVIEW:

DESCRIPTION:

The file was recovered from a dead agent’s laptop — the screen still glowing, the tea beside it untouched.
The system had already begun wiping itself, but we were faster.

At 04:17 AM, our cyber surveillance unit intercepted a suspicious data packet embedded within encrypted military chatter.
Hidden inside was a scrambled message — too chaotic to make sense, yet too deliberate to dismiss.

Preliminary analysis suggests the use of an older, manual encryption technique. No characters appear to be missing — just misplaced,
as if someone wanted this message to be unreadable to most… but decipherable to the right eyes.

We believe this communication reveals who the enemy plans to contact — or perhaps, who they’re targeting.


SOLUTION:

The description strongly hints at a Columnar transposition cipher.
“Older, manual encryption technique. No characters appear to be missing — just misplaced."

Columnar transposition works by writing the ciphertext in rows and rearranging the columns based on a keyword.
You can either use a known keyword (e.g., "Secret"), or automate brute-force decryption using tools like CyberChef, dCode, or Python scripts.

In our case, we used brute-force decryption (no keyword needed), and obtained the following plaintext:

amessagehasbeeninterceptedumustactswiftlyandsilentlyretreatisnotanoptionthistimeaerialunitswillsupportthegroundtroopsnavyisreadytoblocktheescaperoutegroundforcesareawaitingthesignalzebrasquadwillenterfirstenemycampsarelightlyguardedatnightbesuretoburnalldecodedmessages

Now, Now recall this line from the challenge description:
(We believe this communication reveals who the enemy plans to contact — or perhaps, who they’re targeting.)

🧠 How to Realize the Hidden Name in the Message

Once the cipher is decrypted and you get a long, continuous message, your first instinct might be to read it normally. However, the challenge description subtly hints at further analysis:

“We believe this communication reveals who the enemy plans to contact — or perhaps, who they’re targeting.”

This sentence clearly indicates that there is a specific name hidden within the decrypted content.

At this point, a participant may ask:
“Where is the name? I just see plain instructions.”

But there’s another clue:

“Too chaotic to make sense, yet too deliberate to dismiss.”

This suggests that even the decrypted message itself is hiding something — it’s meant to look like normal orders, but there’s a deliberate structure buried within.

To find it, participants may:

Notice that the long plaintext appears to contain distinct sentence-like blocks.
Try breaking the message into logical chunks or lines based on grammar or rhythm.

Realize that if they divide the message like this:

a message has been intercepted
u must act swiftly and silently
retreat is not an option this time
aerial units will support the ground troops
navy is ready to block the escape route
ground forces are awaiting the signal
zebra squad will enter first
enemy camps are lightly guarded at night
be sure to burn all decoded messages

So, through careful observation and connecting the hints in the description with the decrypted result, the participant can deduce that the structure of the plaintext holds a hidden message — a classic steganographic twist.
or a real world message hiding strategies in old army times like German war, which suggests that each letter of every line tells the name of target so here it is aurangzeb.
This reveals the target name: Aurangzeb.
Flag: ACM{Aurangzeb}
