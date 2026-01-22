---
______________________________________________________________________
|                            VICTIMATOR-X                            |
|                   Advanced Password Profiling Tool                 |
----------------------------------------------------------------------

=== DESCRIPTION ===
Victimator‑X is an advanced **password profiling & wordlist generation tool** designed for ethical penetration testing and security auditing.

It generates targeted wordlists by combining:

* Personal data (names, birthdates, phone numbers)
* Professional info (company, job titles)
* Digital footprints (websites, gaming usernames)
* Multi‑value fields (hobbies, locations, favorite colors)
* Smart transformations (leet, symbols, number patterns)

Designed for **authorized security assessments ONLY**.

---

=== WARNING ===
❗ THIS TOOL IS FOR LEGAL ETHICAL HACKING / PENTESTING ONLY
❗ UNAUTHORIZED USE IS ILLEGAL
❗ THE AUTHOR IS NOT RESPONSIBLE FOR MISUSE

---

=== INSTALLATION ===

1. REQUIREMENTS

   * Python 3.x
   * Built‑in modules only:
     • itertools
     • platform
     • os
     • signal
     • pathlib
     • argparse

   ✅ No external pip packages required

2. DOWNLOAD

```
git clone https://github.com/voltsparx/Victimator-X.git
cd Victimator-X
```

---

=== USAGE ===

Run the tool:

```
python3 victimator-x.py
```

Optional modes:

```
--hashcat    Optimize output for Hashcat usage
--hydra      Optimize output for Hydra usage
--min N      Minimum password length
--max N      Maximum password length
```

Example:

```
python3 victimator-x.py --hashcat --min 8 --max 16
```

---

=== INPUT FIELDS (All Optional) ===

---
_____________________________________________________________________________________
##| INPUT TYPE            | EXAMPLE VALUES                                            |
|-----------------------------------------------------------------------------------|
| Personal              | John, Doe, 15071990, 55501234                             |
| Professional          | AcmeCorp, Manager                                         |
| Digital               | reddit.com, xXJohnXx                                      |
| Multi‑value (comma)   | gaming,hiking,blue,green                                  |
-------------------------------------------------------------------------------------

---

=== GENERATED OUTPUT ===

Victimator‑X creates:

```
/wordlists/
  ├── weak.txt
  ├── medium.txt
  ├── strong.txt
  └── full.txt
```

Typical output:
➡ 1,000 – 50,000+ targeted password combinations
➡ Categorized by strength
➡ Ready for Hashcat, Hydra, John the Ripper, etc.

---

=== FEATURES ===

✓ Leet Speak Transformations
(e.g., "John" → "J0hn", "J0hN!")

✓ Smart Combinations
(e.g., "JohnDoe", "John_Doe", "DoeJohn")

✓ Special Character & Number Injection
(e.g., "John123", "John!")

✓ Password Strength Classification
(weak / medium / strong)

✓ Hashcat & Hydra Optimized Modes

✓ Length Filtering (--min / --max)

✓ Graceful Exit Handling
(CTRL+C or type 'exit' anytime)

---

=== ETHICAL USES ===

✔ Password strength auditing
✔ CTF competitions
✔ Authorized penetration testing
✔ Red team exercises
✔ Security research & education

---

=== ILLEGAL USES ===

✖ Attacking systems without permission
✖ Brute‑forcing unknown targets
✖ Any activity violating cybercrime laws

---

=== SUPPORT ===

Report issues at:
[https://github.com/voltsparx/Victimator-X/issues](https://github.com/voltsparx/Victimator-X/issues)

---

=== LICENSE ===

MIT License — Use responsibly!

---

=== CREDITS ===

Created by: voltsparx
Contact: [voltsparx@gmail.com](mailto:voltsparx@gmail.com)
GitHub: [https://github.com/voltsparx](https://github.com/voltsparx)

---

=== DISCLAIMER ===

This tool is provided for educational and authorized testing purposes only.
The author disclaims all responsibility for illegal or unethical use.
By using this tool, you agree to test only systems you own or have permission for.
