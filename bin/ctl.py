#!/usr/bin/env python3

import sys
import os
from pathlib import Path
import argparse
import subprocess

def find_project_root():
    """Find the project root directory."""
    current = Path.cwd()
    while current != current.parent:
        if (current / 'src').exists():
            return current
        current = current.parent
    return None

def run_website(args):
    """Run the website locally."""
    project_root = find_project_root()
    if not project_root:
        print("Error: Could not find project root (directory containing 'src')")
        sys.exit(1)

    src_dir = project_root / 'src'
    os.chdir(src_dir)

    # Import http.server only when needed
    import http.server
    import socketserver

    PORT = 8000
    DIRECTORY = str(src_dir)

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.shutdown()

def deploy_website(args):
    """Deploy the website to production."""
    project_root = find_project_root()
    if not project_root:
        print("Error: Could not find project root (directory containing 'src')")
        sys.exit(1)

    src_dir = project_root / 'src'

    # Confirm with user
    if not args.yes:
        response = input("Are you sure you want to deploy to production? [y/N] ")
        if response.lower() != 'y':
            print("Deployment cancelled.")
            sys.exit(0)

    print("Deploying to production...")
    try:
        subprocess.run(
            ['aws', 's3', 'sync', str(src_dir), 's3://koepkes.us', '--delete'],
            check=True
        )
        print("Deployment successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error deploying to S3: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'aws' command not found. Please install the AWS CLI.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Website control script')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Run command
    run_parser = subparsers.add_parser('run', help='Run the website locally')
    
    # Deploy command
    deploy_parser = subparsers.add_parser('deploy', help='Deploy the website to production')
    deploy_parser.add_argument('-y', '--yes', action='store_true', 
                             help='Skip confirmation prompt')
    
    args = parser.parse_args()
    
    if args.command == 'run':
        run_website(args)
    elif args.command == 'deploy':
        deploy_website(args)
    elif not args.command:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main() 