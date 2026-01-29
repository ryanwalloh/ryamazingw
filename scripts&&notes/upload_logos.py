#!/usr/bin/env python3
"""
Script to upload logo images to Cloudinary
"""

import os
import json
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

def upload_logo(local_path, public_id_name):
    """Upload a logo to Cloudinary"""
    if not os.path.exists(local_path):
        print(f"❌ Error: {local_path} not found!")
        return None
    
    try:
        print(f"📤 Uploading: {local_path} -> logo/{public_id_name}")
        
        # Upload with optimization settings
        result = cloudinary.uploader.upload(
            local_path,
            public_id=f"logo/{public_id_name}",
            overwrite=True,
            resource_type="image",
        )
        
        cloudinary_url = result['secure_url']
        print(f"✅ Uploaded: {cloudinary_url}")
        
        return cloudinary_url
        
    except Exception as e:
        print(f"❌ Error uploading {local_path}: {str(e)}")
        return None

def main():
    """Upload both logo files"""
    mapping_file = 'cloudinary_mapping.json'
    
    # Load existing mapping
    mapping = {}
    if os.path.exists(mapping_file):
        with open(mapping_file, 'r') as f:
            mapping = json.load(f)
    
    # Upload logos
    logos = [
        ('assets/logo/ryamazingwhite.png', 'ryamazingwhite'),
        ('assets/logo/ryamazingwblack.png', 'ryamazingwblack')
    ]
    
    print("🚀 Uploading logos to Cloudinary...\n")
    
    for local_path, public_id_name in logos:
        if local_path in mapping:
            print(f"⏭️  Skipping {local_path} (already uploaded)")
            continue
        
        cloudinary_url = upload_logo(local_path, public_id_name)
        if cloudinary_url:
            mapping[local_path] = cloudinary_url
    
    # Save mapping
    with open(mapping_file, 'w') as f:
        json.dump(mapping, f, indent=2)
    
    print("\n✨ Logo upload complete!")
    print(f"📝 Mapping updated in {mapping_file}")

if __name__ == '__main__':
    main()

