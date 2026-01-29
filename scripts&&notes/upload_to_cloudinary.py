#!/usr/bin/env python3
"""
Script to upload images from home.html to Cloudinary
Creates a mapping file with local paths -> Cloudinary URLs
"""

import os
import json
import re
from pathlib import Path
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader

# Load environment variables
load_dotenv()

# Initialize Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

def extract_images_from_html(html_file):
    """Extract all image paths from home.html"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all img src attributes
    img_pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
    # Find all href attributes in <a> tags that link to images (for lightbox)
    href_pattern = r'<a[^>]+href=["\']([^"\']+\.(?:webp|jpg|jpeg|png|gif))["\']'
    # Find favicon
    favicon_pattern = r'<link[^>]+href=["\']([^"\']+\.(?:png|ico|svg))["\'][^>]*rel=["\']icon["\']'
    
    images = set()
    
    # Extract img src
    for match in re.finditer(img_pattern, content):
        images.add(match.group(1))
    
    # Extract href images
    for match in re.finditer(href_pattern, content):
        images.add(match.group(1))
    
    # Extract favicon
    for match in re.finditer(favicon_pattern, content):
        images.add(match.group(1))
    
    return sorted(list(images))

def get_cloudinary_folder(path):
    """Determine Cloudinary folder based on local path"""
    if 'favicon' in path:
        return 'favicon'
    elif 'gallery' in path:
        return 'gallery'
    elif 'misc' in path:
        return 'misc'
    elif 'icons' in path:
        return 'icons'
    elif 'mobileicons' in path:
        return 'mobileicons'
    else:
        return 'images'

def upload_image(local_path, base_dir='.'):
    """Upload a single image to Cloudinary"""
    # Normalize path - handle both relative paths from HTML and absolute paths
    if local_path.startswith('../'):
        # Path is relative to pages/ directory, so we need to go up one level
        full_path = os.path.join(base_dir, local_path.replace('../', ''))
    else:
        full_path = os.path.join(base_dir, local_path)
    
    if not os.path.exists(full_path):
        print(f"⚠️  Warning: {full_path} not found, skipping...")
        return None
    
    # Get folder structure for Cloudinary
    folder = get_cloudinary_folder(local_path)
    
    # Create public_id (Cloudinary path)
    # Remove '../assets/' or 'assets/' prefix
    public_id = local_path.replace('../assets/', '').replace('../', '')
    public_id = public_id.replace('assets/', '')
    # Remove extension for public_id (Cloudinary stores without extension)
    public_id = os.path.splitext(public_id)[0]
    # Replace path separators with forward slashes
    public_id = public_id.replace('\\', '/')
    
    # If folder is specified, prepend it to public_id
    if folder:
        public_id = f"{folder}/{public_id}" if public_id else folder
    
    try:
        print(f"📤 Uploading: {local_path} -> {public_id}")
        
        # Upload with optimization settings
        result = cloudinary.uploader.upload(
            full_path,
            public_id=public_id,
            overwrite=True,
            resource_type="image",
            # SEO-friendly settings
            use_filename=False,  # We're providing public_id, so don't use filename
            unique_filename=False,
            # Optimization - these are applied automatically by Cloudinary
            # We'll use transformations in URLs instead
        )
        
        # Get the secure URL with auto optimization
        # Cloudinary automatically applies optimizations, but we can request them explicitly
        cloudinary_url = result['secure_url']
        print(f"✅ Uploaded: {cloudinary_url}")
        
        return cloudinary_url
        
    except Exception as e:
        print(f"❌ Error uploading {local_path}: {str(e)}")
        return None

def main():
    """Main function to upload all images from home.html"""
    html_file = 'pages/home.html'
    mapping_file = 'cloudinary_mapping.json'
    
    if not os.path.exists(html_file):
        print(f"❌ Error: {html_file} not found!")
        return
    
    print("🔍 Extracting images from home.html...")
    image_paths = extract_images_from_html(html_file)
    
    print(f"\n📋 Found {len(image_paths)} images to upload:\n")
    for img in image_paths:
        print(f"  - {img}")
    
    print(f"\n🚀 Starting upload to Cloudinary...\n")
    
    # Load existing mapping if it exists
    mapping = {}
    if os.path.exists(mapping_file):
        with open(mapping_file, 'r') as f:
            mapping = json.load(f)
    
    # Upload each image
    uploaded_count = 0
    for img_path in image_paths:
        if img_path in mapping:
            print(f"⏭️  Skipping {img_path} (already uploaded)")
            continue
        
        cloudinary_url = upload_image(img_path)
        if cloudinary_url:
            mapping[img_path] = cloudinary_url
            uploaded_count += 1
    
    # Save mapping
    with open(mapping_file, 'w') as f:
        json.dump(mapping, f, indent=2)
    
    print(f"\n✨ Upload complete! {uploaded_count} new images uploaded.")
    print(f"📝 Mapping saved to {mapping_file}")

if __name__ == '__main__':
    main()

