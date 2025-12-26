# Quick Start: Cloudinary Migration

## Step 1: Create .env file

Create a `.env` file in the project root:

```env
CLOUDINARY_CLOUD_NAME=dwqrkobq1
CLOUDINARY_API_KEY=971572751775647
CLOUDINARY_API_SECRET=m9005UklJxpQ53IgE5opAYDU2dc
```

## Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Upload images

```bash
python upload_to_cloudinary.py
```

This will upload all images from `home.html` to Cloudinary and create a `cloudinary_mapping.json` file.

## Step 4: Update HTML

```bash
python update_html_with_cloudinary.py
```

This will replace all local image paths in `home.html` with Cloudinary URLs.

## Done! ✅

Your images are now hosted on Cloudinary and your HTML has been updated with the new URLs.

**Note:** A backup of your original `home.html` will be created as `home.html.backup`.

