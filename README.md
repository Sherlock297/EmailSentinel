# EmailSentinel
EmailSentinel: The Guardian of Email Best Practices.

A Python tool for checking and improving email configuration and security.

```python EmailSentinel.py -h
  ____  _     _ _ _ _ ____ _  _ ____ 
  |__| |     | | | | | __ |_/  | __ |
  |  | |_____| |_|_| |__| | \_ |__| |

GitHub : Sherlock297

usage: EmailSentinel.py [-h] [-d DOMAIN] [-l LIST_FILE]

Email Best Practices Checker

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Single domain to check
  -l LIST_FILE, --list-file LIST_FILE
                        Text file containing a list of domains to check
```                                                                                              

## Introduction

Email is a critical component of communication for businesses and individuals alike. However, ensuring the security and effectiveness of email services is of paramount importance. Email security vulnerabilities can lead to phishing attacks, spamming, and other malicious activities. To address these concerns, it's essential to implement best practices for email configuration. The Email Best Practices Checker is designed to help you assess your email setup and enhance its security.

## Features

- Check for SPF, DKIM, and DMARC records
- Verify MX records for email delivery
- Validate additional DNS records (A, AAAA, CNAME)
- Monitor the expiration dates of DNS records
- Provides suggestions for improving email configuration

## Getting Started

To get started with the Email Best Practices Checker, follow these steps:

### Installation

- Download the files/folder:

  **```git clone https://github.com/Sherlock297/EmailSentinel.git```**

- Change directory:

  **```cd EmailSentinel```**

- Install the required Python packages using pip:

  **```pip install -r requirements.txt```**

- Set the execute permission on the script file:

  **```chmod +x EmailSentinel.py```**

- To access globally, copy it to bin folder:

  **```sudo cp EmailSentinel.py /bin```**

- Access:

  **```EmailSentinel.py```**

### Usage
- Run the Email Best Practices Checker for a single domain:

  **```python EmailSentinel.py -d example.com```**

  OR
  
  **```EmailSentinel.py -d example.com```**

- For multiple domains, create a text file with one domain per line and use the -l flag:

  **```python EmailSentinel.py -l domain_list.txt```**

  OR
  
  **```EmailSentinel.py -l domain_list.txt```**

## Contribution Guidelines
We welcome contributions from the community.

## License
This project is licensed under the MIT Licens.

## Acknowledgments
We'd like to acknowledge the following libraries and tools that helped make this project possible:
* [Python](https://www.python.org/)
* [dnspython](https://pypi.org/project/dnspython/)
* [colorama](https://pypi.org/project/colorama/)

## Release Notes

### Version 1.0.0 (Initial Release)
Initial release of the Email Best Practices Checker

### Version 1.1.0
Added support for multiple record types
Improved error handling

## About the Author
👋 Hi, I’m Ravindra Dagale | Information Security | Security Researcher

📫 How to reach us [Instagram](https://www.instagram.com/Infosec97/) | [YouTube](https://www.youtube.com/c/RavindraDagale)
