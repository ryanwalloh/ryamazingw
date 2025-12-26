#!/usr/bin/env python3
"""
Script to update index.html with Cloudinary URLs from the mapping file
"""

import json
import re
from pathlib import Path

def update_html_with_cloudinary(html_file='index.html', mapping_file='cloudinary_mapping_index.json'):
    """Update HTML file with Cloudinary URLs"""
    
    # Load mapping
    if not Path(mapping_file).exists():
        print(f"❌ Error: {mapping_file} not found!")
        print("Please run upload_index_images.py first.")
        return
    
    with open(mapping_file, 'r') as f:
        mapping = json.load(f)
    
    # Read HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace all image paths with Cloudinary URLs
    for local_path, cloudinary_url in mapping.items():
        # Escape special regex characters in the path
        escaped_path = re.escape(local_path)
        # Replace in src attributes
        content = re.sub(
            r'(src=["\'])' + escaped_path + r'(["\'])',
            r'\1' + cloudinary_url + r'\2',
            content
        )
        # Replace in href attributes (for favicon)
        content = re.sub(
            r'(href=["\'])' + escaped_path + r'(["\'])',
            r'\1' + cloudinary_url + r'\2',
            content
        )
        # Replace in meta tags (og:image, twitter:image)
        content = re.sub(
            r'(content=["\'])' + escaped_path + r'(["\'])',
            r'\1' + cloudinary_url + r'\2',
            content
        )
        # Replace in JSON-LD structured data
        content = re.sub(
            r'("image":\s*")([^"]*' + re.escape(local_path) + r'[^"]*)(")',
            r'\1' + cloudinary_url + r'\3',
            content
        )
    
    # Only write if changes were made
    if content != original_content:
        # Create backup
        backup_file = html_file + '.backup'
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(original_content)
        print(f"💾 Backup created: {backup_file}")
        
        # Write updated content
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {html_file} with Cloudinary URLs")
    else:
        print("ℹ️  No changes needed")

if __name__ == '__main__':
    update_html_with_cloudinary()

