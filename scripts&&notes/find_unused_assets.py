#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

def get_all_asset_files():
    """Get all files in the assets directory"""
    assets_dir = Path("assets")
    asset_files = []
    for file_path in assets_dir.rglob("*"):
        if file_path.is_file():
            asset_files.append(str(file_path))
    return sorted(asset_files)

def get_code_files():
    """Get all HTML, CSS, and JS files to search"""
    code_files = []
    # Directories to exclude
    exclude_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'transfonter'}
    
    # Get HTML files (excluding transfonter)
    for html_file in Path(".").rglob("*.html"):
        if not any(excluded in html_file.parts for excluded in exclude_dirs):
            code_files.append(str(html_file))
    
    # Get CSS files (excluding transfonter)
    for css_file in Path(".").rglob("*.css"):
        if not any(excluded in css_file.parts for excluded in exclude_dirs):
            code_files.append(str(css_file))
    
    # Get JS files
    for js_file in Path(".").rglob("*.js"):
        if not any(excluded in js_file.parts for excluded in exclude_dirs):
            code_files.append(str(js_file))
    
    return code_files

def search_for_reference(asset_file, code_files):
    """Search for references to an asset file in code files"""
    # Get just the filename and also the relative path
    filename = os.path.basename(asset_file)
    filename_no_ext = os.path.splitext(filename)[0]
    
    # Try multiple search patterns
    search_patterns = [
        asset_file,  # Full relative path
        filename,  # Just filename
        filename_no_ext,  # Filename without extension
    ]
    
    # Also handle path with forward slashes (for web)
    search_patterns.append(asset_file.replace('\\', '/'))
    
    for code_file in code_files:
        try:
            with open(code_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for pattern in search_patterns:
                    if pattern in content:
                        return True
        except Exception as e:
            continue
    
    return False

def main():
    print("Scanning assets and checking for usage...\n")
    
    asset_files = get_all_asset_files()
    code_files = get_code_files()
    
    print(f"Found {len(asset_files)} asset files")
    print(f"Searching in {len(code_files)} code files\n")
    
    unused_assets = []
    used_assets = []
    
    for asset_file in asset_files:
        if search_for_reference(asset_file, code_files):
            used_assets.append(asset_file)
        else:
            unused_assets.append(asset_file)
    
    print(f"\n{'='*60}")
    print(f"RESULTS: {len(unused_assets)} unused assets found")
    print(f"{'='*60}\n")
    
    if unused_assets:
        print("UNUSED ASSETS:")
        print("-" * 60)
        for asset in unused_assets:
            print(asset)
    else:
        print("All assets are being used!")
    
    print(f"\n{'='*60}")
    print(f"Summary: {len(used_assets)} used, {len(unused_assets)} unused")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

