#!/usr/bin/env python3
import os

SERVERS = {
    '1': {
        'name': 'My New AWS Server',
        'command': 'ssh -i /app/my-aws-key.pem ec2-user@98.81.219.188'
    },
}

os.system('clear')
print("===================================")
print("     QuickConnect SSH Gateway")
print("===================================")

for key, server in SERVERS.items():
    print(f"  [{key}] {server['name']}")

print("\n[q] Quit")
print("-----------------------------------")

try:
    choice = input("Enter your choice: ")
    if choice.lower() == 'q':
        print("Exiting.")
    elif choice in SERVERS:
        print(f"\n---> Connecting to {SERVERS[choice]['name']}...")
        os.system(SERVERS[choice]['command'])
    else:
        print("\nInvalid choice.")
except KeyboardInterrupt:
    print("\n\nOperation cancelled. Exiting.")
