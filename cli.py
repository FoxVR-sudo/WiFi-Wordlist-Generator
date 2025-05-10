import click
from wifi_wordlist.generator import generate_wordlist
from wifi_wordlist.combiner import combine_wordlists


@click.group()
def cli():
    """WiFi Wordlist Generator Tool.

    This is a tool for generating wordlists for WiFi networks. It allows adding base words, numbers, symbols, years, and phone numbers.

    Example of generating a wordlist:
    wifi-wordlist-generator generate --base-wordlist base.txt --output mylist.txt --symbols --years --phone-numbers --low-ram

    Author: FoxVR (Svetlin Minkov)
    """
    pass

@cli.command()
@click.option('--base-wordlist', required=True, help='Path to the base wordlist file')
@click.option('--output', required=True, help='Output file path')
@click.option('--symbols', is_flag=True, help='Include symbols')
@click.option('--years', is_flag=True, help='Include years')
@click.option('--phone-numbers', is_flag=True, help='Include phone numbers')
@click.option('--low-ram', is_flag=True, help='Use low RAM mode')
def generate(base_wordlist, output, symbols, years, phone_numbers, low_ram):
    """Generate a wordlist."""
    generate_wordlist(base_wordlist, output, symbols, years, phone_numbers, low_ram)

@cli.command()
@click.argument('wordlists', nargs=-1)
@click.option('--output', required=True, help='Output file path')
def combine(wordlists, output):
    """Combine multiple wordlists into one."""
    combine_wordlists(wordlists, output)

if __name__ == '__main__':
    cli()
