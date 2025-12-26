# Cloudinary Image Migration Setup Guide

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
CLOUDINARY_CLOUD_NAME=your_cloud_name_here
CLOUDINARY_API_KEY=your_api_key_here
CLOUDINARY_API_SECRET=your_api_secret_here
```

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

Or if you prefer pip3:
```bash
pip3 install -r requirements.txt
```

## Usage

### Step 1: Upload Images to Cloudinary

Run the upload script to migrate all images from `home.html` to Cloudinary:

```bash
python upload_to_cloudinary.py
```

Or:
```bash
python3 upload_to_cloudinary.py
```

This script will:
- Extract all image paths from `pages/home.html`
- Upload each image to Cloudinary with optimization settings
- Create a `cloudinary_mapping.json` file mapping local paths to Cloudinary URLs
- Skip images that have already been uploaded (based on the mapping file)

### Step 2: Update HTML with Cloudinary URLs

After uploading, update the HTML file with Cloudinary URLs:

```bash
python update_html_with_cloudinary.py
```

Or:
```bash
python3 update_html_with_cloudinary.py
```

This script will:
- Read the `cloudinary_mapping.json` file
- Replace all local image paths in `home.html` with Cloudinary URLs
- Create a backup file (`home.html.backup`) before making changes

## SEO Improvements Already Implemented

The following SEO improvements have been added to `home.html`:

1. **Enhanced Meta Tags**
   - Improved meta description with keywords
   - Added keywords meta tag
   - Added author meta tag
   - Added robots meta tag

2. **Open Graph Tags** (for Facebook/LinkedIn sharing)
   - og:type, og:url, og:title, og:description, og:image, og:site_name

3. **Twitter Card Tags** (for Twitter sharing)
   - twitter:card, twitter:url, twitter:title, twitter:description, twitter:image, twitter:creator

4. **Structured Data (JSON-LD)**
   - Person schema with social media links
   - WebSite schema
   - ImageGallery schema

5. **Improved Alt Text**
   - All gallery images now have descriptive alt text
   - Social media icons have proper alt attributes
   - Better accessibility and SEO

6. **Canonical URL**
   - Added canonical link to prevent duplicate content issues

## Additional SEO Recommendations

1. **Update Domain URLs**: Replace `https://ryamazingw.com` in the meta tags with your actual domain when deployed

2. **Sitemap**: Create a `sitemap.xml` file listing all your pages

3. **robots.txt**: Create a `robots.txt` file to guide search engine crawlers

4. **Page Speed**: Cloudinary automatically optimizes images, but you can also:
   - Enable lazy loading for images below the fold
   - Use Cloudinary's responsive image transformations

5. **Analytics**: Consider adding Google Analytics or similar tracking

6. **Social Media Verification**: Verify your website with:
   - Google Search Console
   - Facebook Business Manager
   - Twitter Developer Portal

7. **Content**: Ensure your content includes relevant keywords naturally:
   - "Ryan Walloh" and "ryamazingw" appear in headings and content
   - Location-based keywords (Mindanao, Philippines)
   - Photography-related keywords

## Notes

- The upload script creates a mapping file to avoid re-uploading images
- Cloudinary URLs are automatically optimized (auto quality, auto format)
- Images are organized in folders on Cloudinary (gallery, misc, icons, etc.)
- The backup file allows you to revert changes if needed

