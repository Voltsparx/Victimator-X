#!/usr/bin/env python3
import itertools
import platform
import os
import signal
from pathlib import Path

# --- Global Config ---
ORANGE = "\033[38;5;208m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
BLUE = "\033[94m"
RESET = "\033[0m"
REPO_URL = "https://github.com/voltsparx/Victimator-X"

# --- Graceful Exit Handler ---
def handle_quit(signum=None, frame=None):
    print(f"\n{RED}[!] User requested exit. Terminating safely...{RESET}")
    if 'output_file' in globals() and os.path.exists(output_file):
        os.remove(output_file)  # Cleanup partial files
    exit(0)

signal.signal(signal.SIGINT, handle_quit)  # CTRL+C

# --- Terminal Utilities ---
def clear_terminal():
    os.system("cls" if platform.system() == "Windows" else "clear")

# --- Banner ---
def show_banner():
    clear_terminal()
    print(f"{ORANGE}  ╔═══════════════════════════════════════════════════════════════════╗  ")
    print(f"{ORANGE}  ║   __     ___      _   _                 _                __  __   ║  ")
    print(f"{ORANGE}  ║   \ \   / (_) ___| |_(_)_ __ ___   __ _| |_ ___  _ __    \ \/ /   ║  ")
    print(f"{ORANGE}  ║    \ \ / /| |/ __| __| | '_ ` _ \ / _` | __/ _ \| '__|____\  /    ║  ")
    print(f"{ORANGE}  ║     \ V / | | (__| |_| | | | | | | (_| | || (_) | | |_____/  \    ║  ")
    print(f"{ORANGE}  ║      \_/  |_|\___|\__|_|_| |_| |_|\__,_|\__\___/|_|      /_/\_\   ║  ")
    print(f"{ORANGE}  ║                                                                   ║  ")
    print(f"{ORANGE}  ╚═══════════════════════════════════════════════════════════════════╝  ")
    print(f"{BLUE}     ➤ Author: {ORANGE}voltsparx")
    print(f"{BLUE}     ➤ Repo: {ORANGE}{REPO_URL}")
    print(f"{BLUE}     ➤ Version: {ORANGE}1.0.0")
    print(f"{BLUE}     ➤ License: {ORANGE}MIT")
    print(f"{BLUE}     ➤ Contact: {ORANGE}voltsparx@gmail.com")
    print(f"{BLUE}{"\n\n"}{RESET}")

# --- Input Handler ---
def get_input(prompt, is_multi=False):
    while True:
        try:
            value = input(prompt).strip()
            if value.lower() in ('exit', 'quit', 'stop'):
                handle_quit()
            if not value:
                return None
            if is_multi:
                return [v.strip() for v in value.split(",") if v.strip()]
            return value
        except KeyboardInterrupt:
            handle_quit()

# --- Password Generation Logic ---
LEET_DICT = {
    'a': ['4', '@', '^'], 'e': ['3', '€'], 'i': ['1', '!'], 
    'o': ['0', '°'], 's': ['5', '$'], 't': ['7', '+']
}

def apply_leet(word):
    variations = {word, word.capitalize()}
    for char, replacements in LEET_DICT.items():
        if char in word.lower():
            for r in replacements:
                variations.add(word.lower().replace(char, r))
                variations.add(word.capitalize().replace(char, r))
    return list(variations)

def add_special_chars(word):
    specials = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
    return [f"{word}{c}" for c in specials] + [f"{c}{word}" for c in specials]

# --- Main Execution ---
if __name__ == "__main__":
    print(f"\n{RED}[!] WARNING: For authorized ethical pentesting only.")
    print(f"[!] Misuse is illegal. You are responsible for your actions.{RESET}")
    input("\nPress Enter to continue (or CTRL+C to exit)...")

    show_banner()

    # Data Collection
    data = {
        "first_name": get_input(f"{CYAN}First name: {RESET}"),
        "last_name": get_input(f"{CYAN}Last name: {RESET}"),
        "nickname": get_input(f"{CYAN}Nickname: {RESET}"),
        "birthdate": get_input(f"{CYAN}Birthdate (DDMMYYYY): {RESET}"),
        "phone_prefix": get_input(f"{CYAN}First 4 digits of phone: {RESET}"),
        "phone_suffix": get_input(f"{CYAN}Last 4 digits of phone: {RESET}"),
        "favorite_numbers": get_input(f"{CYAN}Favorite numbers (comma-separated): {RESET}", True),
        "favorite_colors": get_input(f"{CYAN}Favorite colors (comma-separated): {RESET}", True),
        "company": get_input(f"{CYAN}Company: {RESET}"),
        "job_title": get_input(f"{CYAN}Job title: {RESET}"),
        "fav_website": get_input(f"{CYAN}Favorite website (no http://): {RESET}"),
        "gamertag": get_input(f"{CYAN}Gaming username: {RESET}"),
        "hobbies": get_input(f"{CYAN}Hobbies (comma-separated): {RESET}", True),
        "frequent_locations": get_input(f"{CYAN}Locations (comma-separated): {RESET}", True),
    }

    # Show collected data
    print(f"\n{CYAN}=============== Collected Data ==============")
    for key, value in data.items():
        if value:
            print(f"{key:>20}: {', '.join(value) if isinstance(value, list) else value}")
    print("=" * 45 + f"{RESET}\n")

    # Generate wordlist
    wordlist = set()
    all_words = []
    
    # Process all fields
    for key, value in data.items():
        if not value:
            continue
        if isinstance(value, list):
            for item in value:
                all_words.extend(apply_leet(item))
        else:
            all_words.extend(apply_leet(value))

    wordlist.update(all_words)

    # Generate combos
    for word1, word2 in itertools.permutations(all_words, 2):
        if len(word1) + len(word2) <= 25:
            wordlist.update([f"{word1}{word2}", f"{word1}_{word2}", f"{word1}-{word2}"])

    # Add number suffixes
    number_sources = []
    if data["birthdate"]:
        number_sources.extend([data["birthdate"][:2], data["birthdate"][2:4], data["birthdate"][-4:]])
    if data["phone_prefix"]:
        number_sources.append(data["phone_prefix"])
    if data["phone_suffix"]:
        number_sources.append(data["phone_suffix"])
    if data["favorite_numbers"]:
        number_sources.extend(data["favorite_numbers"])

    for word in all_words:
        for num in number_sources:
            wordlist.add(f"{word}{num}")
            wordlist.add(f"{word}_{num}")

    # Add special chars (limit to prevent explosion)
    for word in list(wordlist)[:1000]:
        wordlist.update(add_special_chars(word))

    # Common patterns
    wordlist.update(["123", "1234", "password", "qwerty", "1q2w3e", "!@#$"])

    # Save to file
    output_dir = "wordlists"
    Path(output_dir).mkdir(exist_ok=True)
    victim_name = data["first_name"] or "target"
    output_file = f"{output_dir}/custom_wordlist_{victim_name.lower()}.txt"

    try:
        with open(output_file, 'w') as f:
            f.write('\n'.join(sorted(wordlist, key=lambda x: (len(x), x))))

        print(f"{GREEN}[+] Successfully generated {len(wordlist)} passwords")
        print(f"[+] Saved to: {output_file}{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error saving file: {e}{RESET}")
        handle_quit()
