# WiFi Wordlist Generator

A tool for generating and combining custom wordlists for WiFi password cracking. Supports adding symbols, years, phone numbers, and more.

## Features

- Generate complex wordlists from a base wordlist.
- Add symbols, years, phone numbers.
- Low RAM mode for large wordlists.
- Combine multiple wordlists into one.
## Usage
Generate a wordlist

wifi-wordlist-generator generate --base-wordlist base.txt --output mylist.txt --symbols --years --phone-numbers --low-ram

Combine wordlists

wifi-wordlist-generator combine --input list1.txt --input list2.txt --output combined.txt

## Example

wifi-wordlist-generator generate --base-wordlist base.txt --output wifi_words.txt --symbols --years

Author

FoxVR (Svetlin Minkov)

## Installation

```bash
git clone https://github.com/FoxVR-sudo/wifi-wordlist-generator.git
cd wifi-wordlist-generator
pip install .

