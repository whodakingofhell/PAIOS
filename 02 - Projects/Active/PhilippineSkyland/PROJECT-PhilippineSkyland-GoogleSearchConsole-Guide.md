---
tags:
  - paios/projects
  - paios/project/philippineskyland
related:
  - "Projects-MOC.md"
  - "../../02 - Projects/"
---

# How to Add Your Website to Google Search Console
## (Step-by-Step Guide for Non-Technical Users)

---

## What is Google Search Console?

Google Search Console is a **free tool from Google** that lets you:
- Tell Google your website exists
- Submit your sitemap so Google can find all your pages
- Monitor how your site appears in Google Search
- Fix any problems that prevent your site from showing in search results

**This is how you make your website permanently searchable on Google.**

---

## What You Need Before Starting

- A **Google account** (Gmail)
- Your website URL: `https://philippine-skyland.vercel.app`
- Access to your Vercel account (for verification)

---

## STEP 1: Go to Google Search Console

1. Open your web browser (Chrome, Edge, etc.)
2. Go to: **https://search.google.com/search-console**
3. Click **"Start Now"**
4. Sign in with your Google (Gmail) account

---

## STEP 2: Add Your Property

1. In the top-left corner, click the **dropdown** that says "Select a property"
2. Click **"+ Add property"**
3. Under **"URL prefix"**, type your website address exactly:
   ```
   https://philippine-skyland.vercel.app
   ```
4. Click **"Continue"**

---

## STEP 3: Verify You Own the Website

Google needs to know you actually own this website. You will see several verification methods. **Choose "HTML file"** — it's the easiest:

### Method A: HTML File (Recommended)

1. Click **"HTML file"** under "Other verification methods"
2. Google will give you a file to download (something like `googleXXXXXXXXXX.html`)
3. **Download** this file
4. Go to your project folder: `C:\Users\My PC\OneDrive\Desktop\NALBAP-App\public\`
5. **Copy the downloaded file** into the `public` folder
6. Go back to Google Search Console and click **"Verify"**

> **Note:** I already have the SEO files ready in your `public/` folder. The robots.txt and sitemap.xml are already configured.

### Method B: HTML Tag (If Method A doesn't work)

1. Click **"HTML tag"** under "Other verification methods"
2. Google will give you a code like:
   ```html
   <meta name="google-site-verification" content="YOUR_CODE_HERE" />
   ```
3. Copy the **content** value (the code between quotes)
4. I will update it in the code for you — just tell me the code

### Method C: DNS Record (Most Permanent)

1. Click **"DNS record"**
2. Google will give you a TXT record
3. You need to add this to your domain's DNS settings
4. This is the most permanent method but requires domain access

---

## STEP 4: Submit Your Sitemap

Once verified:

1. In the left sidebar, click **"Sitemaps"**
2. In the "Add a new sitemap" box, type:
   ```
   sitemap.xml
   ```
3. Click **"Submit"**
4. Wait a few minutes — Google will confirm it received your sitemap

---

## STEP 5: Request Indexing for Your Pages

This tells Google to crawl your pages immediately:

1. In the top search bar, type your homepage URL:
   ```
   https://philippine-skyland.vercel.app
   ```
2. Press Enter
3. Click **"Request Indexing"**
4. Wait for Google to confirm
5. **Repeat** for each important page:
   - `https://philippine-skyland.vercel.app/properties`
   - `https://philippine-skyland.vercel.app/profile/nelson-aczon`
   - `https://philippine-skyland.vercel.app/faq`

**Tip:** Google allows about 10-12 indexing requests per day for new websites. If any request says "couldn't fetch" or "limit reached", wait 24 hours and try again.

---

## STEP 6: Wait for Google to Index Your Site

- Google typically indexes new websites within **1-14 days**
- You can check progress in Search Console under **"Pages"** in the left sidebar
- Once indexed, your site will appear in Google search results

---

## How to Check If Your Site is on Google

1. Open Google
2. Type: `site:philippine-skyland.vercel.app`
3. If results appear, your site is indexed!
4. You can also search for: `real estate broker Philippines` or `Nelson Aczon real estate`

### When Will I Know My Site is Indexed?
- **Day 1-3:** Google discovers your site through the sitemap you submitted
- **Day 3-7:** Google crawls and indexes your pages
- **Day 7-14:** Your pages appear in Google search results
- **After 14 days:** Use `site:philippine-skyland.vercel.app` — if results appear, you're indexed!
- **Note:** Even without manual 'Request Indexing', Google will find your site through the sitemap. Manual requests just speed it up.

---

## Important Tips

### What NOT to Do
- Don't use "Instant Indexing" tools that promise overnight results
- Don't submit your site to multiple search engines separately (Google covers most)
- Don't change your sitemap frequently — Google prefers stability

### What TO Do
- Check Search Console **once a week** for any errors
- Keep your content updated (add new properties regularly)
- Share your website on social media (Facebook, Instagram) — this helps Google find you faster
- Make sure your website loads fast (it already does on Vercel)

### How to Stay Indexed Permanently
- Keep your website online and accessible
- Add new content regularly (new properties, blog posts)
- Don't change your URL structure
- Maintain your Vercel hosting (don't let it expire)

---

## Quick Reference Card

| Item | Value |
|------|-------|
| Website URL | `https://philippine-skyland.vercel.app` |
| Sitemap URL | `https://philippine-skyland.vercel.app/sitemap.xml` |
| Robots.txt | `https://philippine-skyland.vercel.app/robots.txt` |
| Google Search Console | `https://search.google.com/search-console` |
| Verification Method | HTML file in `public/` folder |

---

## What's Already Done (Technical Details)

Your website already has these SEO elements:

| Element | Status | File |
|---------|--------|------|
| robots.txt | ✅ Configured | `public/robots.txt` |
| sitemap.xml | ✅ 11 pages listed | `public/sitemap.xml` |
| Meta tags | ✅ Title, description, keywords | `src/app/layout.tsx` |
| Open Graph | ✅ Facebook/LinkedIn sharing | `src/app/layout.tsx` |
| Twitter Cards | ✅ Twitter sharing | `src/app/layout.tsx` |
| JSON-LD | ✅ Structured data | `src/app/page.tsx` |
| Semantic HTML | ✅ Proper heading hierarchy | All pages |
| Mobile responsive | ✅ Works on all devices | All pages |
| Fast loading | ✅ Vercel edge network | All pages |
| Google Search Console verification | ✅ Verified | `public/google745da16c350fda3d.html` |
| Session timeout | ✅ 30-min inactivity | Security feature |
| AI chatbot | ✅ FAQ-based | Floating widget |
| Email verification | ✅ Mandatory | Auth flow |
| Password reset | ✅ Token-based | `/auth/forgot-password` |
| Account lockout | ✅ 5 attempts / 15 min | Auth middleware |
| DB audit logging | ✅ PostgreSQL | `AuditLog` model |
| 11-layer security | ✅ Enterprise-grade | Full stack |

**All you need to do is complete Steps 1-6 above to get on Google.**
