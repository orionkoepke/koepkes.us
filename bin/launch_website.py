#!/usr/bin/env python3

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def find_project_root():
    """Find the project root directory (where index.html is located)"""
    current_dir = Path(__file__).parent.parent  # Go up one level from bin/
    src_path = current_dir / 'src'
    index_path = src_path / 'index.html'
    
    if index_path.exists():
        return src_path
    else:
        print("Error: Could not find index.html in the src directory")
        sys.exit(1)

def main():
    # Set port for the server
    PORT = 8000
    
    # Change to the project root directory
    os.chdir(find_project_root())
    
    # Create handler for serving files
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        # Create server
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving website at http://localhost:{PORT}")
            print("Press Ctrl+C to stop the server")
            
            # Open the website in the default browser
            webbrowser.open(f"http://localhost:{PORT}")
            
            # Keep the server running
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 