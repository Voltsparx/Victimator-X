_______________________________________________________________________
|                            VICTIMATOR-X                             |
|                   Advanced Password Profiling Tool.                 |
——————————————————————––——————––——————––——————––——————––——————––——————–


=== DESCRIPTION ===
Victimator-X generates targeted wordlists for ethical penetration testing by combining:
- Personal data (names, birthdates, phone numbers)
- Professional info (company, job titles)
- Digital footprints (websites, gaming usernames)
- Multi-value fields (hobbies, locations, favorite colors)

Designed for authorized security assessments ONLY.

=== WARNING ===
❗ THIS TOOL IS FOR LEGAL ETHICAL HACKING/PENTESTING ONLY.
❗ USING IT FOR UNAUTHORIZED TESTING IS ILLEGAL.
❗ THE AUTHOR IS NOT RESPONSIBLE FOR MISUSE.

=== INSTALLATION ===
1. REQUIRED MODULES:
   - Python 3.x
   - Built-in modules:
     • itertools
     • platform
     • os
     • signal
     • pathlib (from standard library)

   No additional pip packages needed!

2. DOWNLOAD:
   git clone https://github.com/voltsparx/Victimator-X.git
   cd Victimator-X

=== USAGE ===
1. Run the tool:
   python3 victimator-x.py

2. Input Fields (All Optional):
   ---------------------------------------------------------------------------------------
   │          INPUT TYPE         |                    EXAMPLE VALUES                     |
   ---------------------------------------------------------------------------------------
   |     Personal                |            John, Doe, 15071990, 55501234              |
   |     Professional            |            Acme Corp, Manager                         |
   |     Digital                 |            reddit.com, xXJohnXx                       |
   |     Multi-value (comma)     |            gaming,hiking,blue,green                   |
   ---------------------------------------------------------------------------------------

3. Generated Output:
   - Creates /wordlists/custom_wordlist_[targetname].txt
   - Typical output: 1,000-20,000+ password combinations

=== FEATURES ===
✓ Leet Speak Transformations  (e.g., "John" → "J0hn", "J0hN!")
✓ Smart Combinations          (e.g., "John" + "Doe" → "JohnDoe", "John_Doe")
✓ Number/Special Char Appending (e.g., "John" → "John123", "John!")
✓ Keyboard Walk Patterns      (e.g., "qwerty", "1qaz2wsx")
✓ Graceful Exit Handling      (CTRL+C or type 'exit' anytime)

=== ETHICAL USES ===
✔ Password strength audits
✔ CTF competitions
✔ Authorized penetration tests
✔ Educational security research

=== ILLEGAL USES ===
✖ Brute-forcing without permission
✖ Attacking systems you don't own
✖ Any activity violating Computer Misuse Acts

=== SUPPORT ===
Report issues at: https://github.com/voltsparx/Victimator-X/issues

=== LICENSE ===
MIT License - Use responsibly!

=== CREDITS ===
Created by: voltsparx
Contact: voltsparx@gmail.com
GitHub: github.com/voltsparx

=== DISCLAIMER ===
This tool is provided for educational purposes only. The author disclaims 
all responsibility for illegal or unethical use. By using this tool, 
you agree to use it only on systems you have explicit permission to test.
