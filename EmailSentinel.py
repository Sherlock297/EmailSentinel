#!/usr/bin/env python

import dns.resolver
from datetime import datetime
import argparse
from colorama import Fore, Style


# ASCII art for an email
email_art = """
  ____  _     _ _ _ _ ____ _  _ ____ 
  |__| |     | | | | | __ |_/  | __ |
  |  | |_____| |_|_| |__| | \_ |__| |
"""

# Your GitHub username
github_username = "Sherlock297"

# Print the stylized email art and username
print("\033[1m\033[35m" + email_art + "\033[0m")
print(f"GitHub : \033[1m\033[34m{github_username}\033[0m\n")


def validate_spf(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                if "v=spf1" in txt_string.decode('utf-8'):
                    return True
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    return False

def validate_dkim(domain):
    try:
        answers = dns.resolver.resolve(f"_domainkey.{domain}", 'TXT')
        for rdata in answers:
            return True
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    return False

def validate_dmarc(domain):
    try:
        answers = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                if "v=DMARC1" in txt_string.decode('utf-8'):
                    return True
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    return False

def check_mx_records(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return [str(mx.exchange) for mx in answers]
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    return []

def check_record_expiration(domain, record_type):
    try:
        dns.resolver.resolve(domain, record_type)
        return True
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    return False

def print_bold(text):
    return Style.BRIGHT + text + Style.RESET_ALL

def print_colored(text, color):
    return color + text + Style.RESET_ALL

def main():
    parser = argparse.ArgumentParser(description="Email Best Practices Checker")
    parser.add_argument("-d", "--domain", help="Single domain to check")
    parser.add_argument("-l", "--list-file", help="Text file containing a list of domains to check")
    args = parser.parse_args()

    if not args.domain and not args.list_file:
        print("Please specify a domain using the -d flag or a list of domains using the -l flag.")
        return

    if args.domain:
        domains = [args.domain]
    else:
        try:
            with open(args.list_file, 'r') as file:
                domains = [line.strip() for line in file]
        except FileNotFoundError:
            print(f"File '{args.list_file}' not found.")
            return

    for domain in domains:
        print(f"Checking email best practices for: {print_bold(domain)}\n")

        missing_spf = not validate_spf(domain)
        missing_dkim = not validate_dkim(domain)
        missing_dmarc = not validate_dmarc(domain)

        print("Email Best Practices Checks:")
        print(f"SPF record: {print_colored('Missing', Fore.RED) if missing_spf else print_colored('Found', Fore.GREEN)} - {'Add SPF record to enhance email security.' if missing_spf else 'Good job, SPF record is in place.'}")
        print(f"DKIM record: {print_colored('Missing', Fore.RED) if missing_dkim else print_colored('Found', Fore.GREEN)} - {'Implement DKIM to validate email authenticity.' if missing_dkim else 'Good job, DKIM record is implemented.'}")
        print(f"DMARC record: {print_colored('Missing', Fore.RED) if missing_dmarc else print_colored('Found', Fore.GREEN)} - {'Set up DMARC to protect against spoofing.' if missing_dmarc else 'Great, DMARC is set up.'}")

        mx_records = check_mx_records(domain)
        if mx_records:
            print("\nMX Records:")
            for mx in mx_records:
                print(f"MX Record: {mx}")
        else:
            print(f"{Fore.RED}MX Records: No MX records found - {Fore.CYAN}Configure MX records for email delivery.{Style.RESET_ALL}")

        record_types_to_check = ["A", "AAAA", "CNAME"]
        print("\nAdditional DNS Records:")
        for record_type in record_types_to_check:
            found = check_record_expiration(domain, record_type)
            if found:
                print(f"{record_type} Record: {print_colored('Found', Fore.GREEN)} - {'Good job, the record is already in place.'}")
            else:
                if record_type == "AAAA":
                    print(f"{record_type} Record: {Fore.RED}Missing - {Fore.CYAN}Consider adding an IPv6 (AAAA) record for broader internet access.{Style.RESET_ALL}")
                elif record_type == "CNAME":
                    print(f"{record_type} Record: {Fore.RED}Missing - {Fore.CYAN}Configure CNAME records for aliasing or domain redirection.{Style.RESET_ALL}")
                else:
                    print(f"{record_type} Record: {Fore.RED}Missing - {Fore.CYAN}Add this record to enhance email delivery and accessibility.{Style.RESET_ALL}")

        print("\n---\n")

if __name__ == "__main__":
    main()
