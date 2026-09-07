#!/usr/bin/env python3
"""
send_outreach_email.py — Commercial Outbound Email Dispatcher via Gmail SMTP

Features:
- Connects securely to Google Gmail SMTP (smtp.gmail.com:587 TLS) using Google App Passwords.
- Multipart MIME (text/plain + text/html + inline CID image attachment).
- Auto-embeds the mobile animated GIF / iPhone mockup directly into the email body so it auto-plays on phone.
- Includes safety guardrails:
    --dry-run: Renders and inspects email without sending.
    --test-to <your_email>: Sends test email to yourself so you can preview on your own phone.
    --target <id>: Specifies target business (goodroots | amatttree | dapco).
    --force-send: Explicit flag required to dispatch to real business.
"""

import os
import sys
import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path

# Fix Windows console UTF-8 output
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent

# Business Outbound Profiles
TARGET_PROFILES = {
    "goodroots": {
        "name": "Good Roots Roofing & Construction",
        "city": "Fort Worth / Saginaw, TX",
        "recipient_name": "Good Roots Roofing Team",
        "recipient_email": "info@goodrootsroofing.com", # Target business address
        "phone": "(817) 781-6811",
        "current_url": "https://goodrootsroofing.com",
        "demo_url": "https://cakteam.github.io/texas-contractor-demos/goodroots/",
        "visual_hook": BASE_DIR / "04_PREVIEWS" / "visual_hooks" / "01_good_roots_scroll.gif",
        "subject": "Quick heads-up about a formatting glitch on goodrootsroofing.com (+ live concept for you)",
        "pain_points": [
            "GoDaddy header error repeating 'Good Roots Roofing' 9 times on the homepage",
            "Project photos appearing as broken 1x1 blank placeholders",
            "No interactive hail damage deductible estimator or 24/7 drone inspection booking"
        ]
    },
    "amatttree": {
        "name": "A. Matt Tree Service",
        "city": "Fort Worth & Keller, TX",
        "recipient_name": "Allen Matthews",
        "recipient_email": "info@amatt-treeservice.com",
        "phone": "(817) 391-8899",
        "current_url": "https://amatt-treeservice.com",
        "demo_url": "https://cakteam.github.io/texas-contractor-demos/amatttree/",
        "visual_hook": BASE_DIR / "04_PREVIEWS" / "visual_hooks" / "02_a_matt_scroll.gif",
        "subject": "Quick question about A. Matt Tree Service website (+ mobile concept for Allen)",
        "pain_points": [
            "Older 2013 WordPress theme with blog post displaying 'Comments are closed'",
            "Promoting northern 'Snow Plowing' & firewood instead of high-value heavy crane removals",
            "No mobile photo-upload estimator for homeowners with fallen storm branches"
        ]
    },
    "dapco": {
        "name": "DAPco Garage Door Service",
        "city": "Grand Prairie & Arlington, TX",
        "recipient_name": "DAPco Garage Door Team",
        "recipient_email": "service@dapcodoor.com",
        "phone": "(817) 681-8186",
        "current_url": "https://dapcodoor.com",
        "demo_url": "https://cakteam.github.io/texas-contractor-demos/dapcodoor/",
        "visual_hook": BASE_DIR / "04_PREVIEWS" / "visual_hooks" / "03_dapco_scroll.gif",
        "subject": "Broken link on dapcodoor.com navigation (+ fresh 5.0★ mobile redesign for DAPco)",
        "pain_points": [
            "Top navigation 'Reviews' button throws a broken 404 Not Found error on mobile",
            "Homepage displays a raw red Facebook OAuth API error message",
            "Lacks a 3-second symptom diagnoser (broken spring vs cable) for emergency callers"
        ]
    },
    "duckac": {
        "name": "Duck AC & Heating",
        "city": "Arlington, Mansfield, Grand Prairie, TX",
        "recipient_name": "Duck AC & Heating Team",
        "recipient_email": "info@duckacandheating.com",
        "phone": "(817) 631-8281",
        "current_url": "https://www.duckacandheating.com/",
        "demo_url": "https://cakteam.github.io/texas-contractor-demos/duckac/",
        "visual_hook": BASE_DIR / "04_PREVIEWS" / "visual_hooks" / "04_duck_ac_mockup.png",
        "subject": "Quick heads-up about a mobile calling issue on duckacandheating.com (+ live concept)",
        "pain_points": [
            "Mobile site phone number (817) 631-8281 lacks clickable 'tap-to-call' link during emergency summer breakdowns",
            "Leftover Wix default placeholder text (example@mysite.com) appearing in live source",
            "No 60-second emergency triage dispatch selector for frantic homeowners with broken AC"
        ]
    },
    "ameritex": {
        "name": "AmeriTex Foundation Repair",
        "city": "Keller, Fort Worth, Dallas, TX",
        "recipient_name": "AmeriTex Foundation Repair Team",
        "recipient_email": "AmeriTexFoundationRepair@gmail.com",
        "phone": "(817) 703-9111",
        "current_url": "https://ameritexfoundationrepair.com/",
        "demo_url": "https://cakteam.github.io/texas-contractor-demos/ameritex/",
        "visual_hook": BASE_DIR / "04_PREVIEWS" / "visual_hooks" / "05_ameritex_mockup.png",
        "subject": "Quick note on your mobile site + built a custom steel pier prototype for AmeriTex",
        "pain_points": [
            "Mobile view compresses your heavy equipment and Silverado Lone Star job site photos",
            "Lacks a 3-step foundation symptom self-assessment funnel for high-ticket ($8k-$25k) inquiries",
            "No 1-tap direct dialing button on mobile headers for exterior brick crack emergency calls"
        ]
    },
    "calldadac": {
        "name": "D.A.D. Home Services",
        "city": "Dallas, Arlington, DFW, TX",
        "recipient_name": "David",
        "recipient_email": "david@calldadac.com",
        "phone": "(682) 328-3700",
        "current_url": "https://calldadac.com/",
        "demo_url": "https://cakteam.github.io/texas-contractor-demos/calldadac/",
        "visual_hook": BASE_DIR / "04_PREVIEWS" / "visual_hooks" / "06_dad_mockup.png",
        "subject": "David — quick thought on calldadac.com mobile speed (+ live prototype for you)",
        "pain_points": [
            "Older WordPress theme and plugins causing 3-4 second load delay on mobile connections",
            "Buried dispatch form costs emergency calls during peak North Texas heatwaves",
            "Doesn't prominently highlight TACLA 116949C state license & Generac certified generator capabilities on mobile"
        ]
    },
    "bourdonfence": {
        "name": "Bourdon Fence Co. LLC",
        "city": "Fort Worth & DFW, TX",
        "recipient_name": "Ryan & Brittany Bourdon",
        "recipient_email": "Bourdonfenceco@gmail.com",
        "phone": "(682) 368-9172",
        "current_url": "https://bourdonfenceco.com/",
        "demo_url": "https://cakteam.github.io/texas-contractor-demos/bourdonfence/",
        "visual_hook": BASE_DIR / "04_PREVIEWS" / "visual_hooks" / "07_bourdon_mockup.png",
        "subject": "Ryan & Brittany — quick idea on your mobile site (+ live concept for Bourdon Fence)",
        "pain_points": [
            "Heavy WordPress styling plugins slowing down mobile load times on cellular connections",
            "No interactive 60-second fence footage and style pricing estimator for storm callers",
            "Lacks an interactive Before/After slider highlighting rotten pine vs heavy-post Western Red Cedar"
        ]
    },
    "rockwater": {
        "name": "Rockwater Plumbing",
        "city": "Fort Worth & Arlington, TX",
        "recipient_name": "Rockwater Plumbing Team",
        "recipient_email": "rockwaterplumbing@gmail.com",
        "phone": "(817) 383-8782",
        "current_url": "https://callrockwaterplumbing.com/",
        "demo_url": "https://cakteam.github.io/texas-contractor-demos/rockwater/",
        "visual_hook": BASE_DIR / "04_PREVIEWS" / "visual_hooks" / "08_rockwater_mockup.png",
        "subject": "Quick observation on callrockwaterplumbing.com (+ live mobile concept for you)",
        "pain_points": [
            "Extensive text paragraphs bury emergency dispatch options during urgent burst pipe situations",
            "Lacks a 30-second emergency triage selector (Slab Leak / Pipe Burst / Sewer Backup) for immediate technician routing",
            "Doesn't visually showcase non-invasive pipe relining vs breaking foundation concrete"
        ]
    },
    "elevatedpool": {
        "name": "Elevated Pool Remodeling",
        "city": "Southlake, Keller, Fort Worth, TX",
        "recipient_name": "Elevated Pool Remodeling Team",
        "recipient_email": "Elevatedpoolremodeling@gmail.com",
        "phone": "(817) 350-3519",
        "current_url": "https://elevatedpoolremodel.com/",
        "demo_url": "https://cakteam.github.io/texas-contractor-demos/elevatedpool/",
        "visual_hook": BASE_DIR / "04_PREVIEWS" / "visual_hooks" / "09_elevated_mockup.png",
        "subject": "Critical technical note on elevatedpoolremodeling.com (+ built a luxury pool concept for you)",
        "pain_points": [
            "Primary domain elevatedpoolremodeling.com failing to connect with an SSL/server certificate error",
            "Alternate site is a client-side JavaScript shell that can experience delays on mobile devices",
            "Lacks an interactive luxury transformation slider comparing aged plaster to Midnight Pebble and travertine"
        ]
    }
}

def load_env():
    """Load credentials from .env if present."""
    env_path = BASE_DIR / ".env"
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

def build_email_content(target_key, sender_name, sender_email):
    target = TARGET_PROFILES[target_key]
    
    # 1. Plain Text Version (Vital for Spam Deliverability)
    text_body = f"""Hi {target['recipient_name']},

I was looking at {target['name']} ({target['current_url']}) while researching reputable home service contractors around {target['city']}, and wanted to quickly share a couple of observations:

Current conversion roadblocks on your live site:
• {target['pain_points'][0]}
• {target['pain_points'][1]}
• {target['pain_points'][2]}

Because you have great local reputation and reviews, I built a fast, modern mobile concept page specifically tailored for {target['name']} to show what's possible:

👉 Live Mobile Demo: {target['demo_url']}

(I've also attached a short 5-second mobile preview showing the interactive booking experience)

No cost, no pushy sales pitch. If you like how it presents your business and want to put it to work to capture more high-value inquiries, I'd be happy to help you get it live. If you're happy with your current setup, no problem at all—you're free to keep any of the ideas or copy!

Either way, hope this heads-up helps you fix the issue on your current site.

Best regards,

{sender_name}
{sender_email}

---
Opt-out: If this isn't relevant to you, simply reply with "pass" or "stop" and I will never contact you again.
"""

    # 2. Rich HTML Version with Inline Embedded Visual Hook
    html_body = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; margin: 0; padding: 20px; background-color: #f8fafc; }}
    .container {{ max-width: 600px; margin: 0 auto; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 28px; }}
    .badge {{ display: inline-block; padding: 4px 10px; border-radius: 9999px; font-size: 11px; font-weight: bold; background: #ecfdf5; color: #059669; margin-bottom: 16px; }}
    h2 {{ font-size: 18px; color: #0f172a; margin-top: 0; }}
    ul {{ padding-left: 20px; margin: 14px 0; }}
    li {{ margin-bottom: 6px; font-size: 14px; color: #475569; }}
    .btn {{ display: inline-block; padding: 12px 24px; background: #059669; color: #ffffff !important; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 14px; margin: 18px 0; }}
    .preview-box {{ text-align: center; margin: 24px 0; background: #f1f5f9; padding: 16px; border-radius: 12px; }}
    .preview-box img {{ max-width: 320px; width: 100%; height: auto; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.15); }}
    .footer {{ font-size: 12px; color: #94a3b8; border-top: 1px solid #f1f5f9; padding-top: 16px; margin-top: 24px; }}
  </style>
</head>
<body>
  <div class="container">
    <span class="badge">TAILORED CONCEPT • {target['city']}</span>
    <p>Hi <strong>{target['recipient_name']}</strong>,</p>
    
    <p>I was looking over <strong>{target['name']}</strong> while researching top-rated local contractors in your area, and wanted to quickly flag a couple of technical items on your current website (<code>{target['current_url']}</code>):</p>
    
    <ul>
      <li><strong style="color: #dc2626;">Item 1:</strong> {target['pain_points'][0]}</li>
      <li><strong style="color: #dc2626;">Item 2:</strong> {target['pain_points'][1]}</li>
      <li><strong style="color: #059669;">Opportunity:</strong> {target['pain_points'][2]}</li>
    </ul>

    <p>Because your customer reviews are so strong, I took the initiative to design an interactive, lightning-fast mobile prototype specifically for {target['name']}:</p>

    <!-- Visual Hook Embedded Directly in Email Body -->
    <div class="preview-box">
      <div style="font-size: 12px; color: #64748b; font-weight: bold; margin-bottom: 8px;">Interactive Mobile Prototype Preview:</div>
      <a href="{target['demo_url']}" target="_blank">
        <img src="cid:visual_hook" alt="{target['name']} Mobile Demo Preview">
      </a>
      <div style="font-size: 11px; color: #94a3b8; margin-top: 8px;">Tap image above or click the button below to test live on mobile</div>
    </div>

    <div style="text-align: center;">
      <a href="{target['demo_url']}" target="_blank" class="btn">👉 Test Live Prototype on Your Phone</a>
    </div>

    <p style="font-size: 14px; color: #475569;">No charge, no high-pressure pitch. If you like how it elevates your brand and want to use it to capture more jobs, I'd be happy to help you get it connected to your domain. If you prefer to stick with what you have, no worries at all!</p>

    <p style="font-size: 14px; color: #475569;">Best regards,<br>
    <strong>{sender_name}</strong><br>
    <span style="font-size: 12px; color: #64748b;">{sender_email}</span></p>

    <div class="footer">
      <p>P.S. If this was not relevant, reply "pass" and I will never email you again.</p>
    </div>
  </div>
</body>
</html>
"""
    return text_body, html_body, target

def send_email(target_key, test_recipient=None, dry_run=True, force_send=False):
    load_env()
    
    gmail_user = os.getenv("GMAIL_USER")
    gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")
    sender_name = os.getenv("SENDER_NAME", "Web Design Specialist")
    
    if target_key not in TARGET_PROFILES:
        print(f"Error: Target '{target_key}' not recognized. Choices: {list(TARGET_PROFILES.keys())}")
        return False

    target = TARGET_PROFILES[target_key]
    recipient = test_recipient if test_recipient else target["recipient_email"]
    subject = target["subject"]

    if not test_recipient and not force_send and not dry_run:
        print("\n[SAFETY ALERT] You are attempting to send to a real business recipient without --force-send!")
        print(f"Recipient: {recipient}")
        print("To protect your domain and prevent accidental outreach, add --force-send to execute.")
        return False

    text_body, html_body, profile = build_email_content(target_key, sender_name, gmail_user or "your-email@gmail.com")
    
    # Construct MIME Message
    msg_root = MIMEMultipart("related")
    msg_root["Subject"] = subject
    msg_root["From"] = f"{sender_name} <{gmail_user}>" if gmail_user else f"{sender_name} <demo@localbiz.com>"
    msg_root["To"] = recipient

    # Alternative part (plain text + html)
    msg_alt = MIMEMultipart("alternative")
    msg_root.attach(msg_alt)
    msg_alt.attach(MIMEText(text_body, "plain", "utf-8"))
    msg_alt.attach(MIMEText(html_body, "html", "utf-8"))

    # Attach Visual Hook as CID
    visual_hook_path = profile["visual_hook"]
    if visual_hook_path.exists():
        with open(visual_hook_path, "rb") as f:
            img_data = f.read()
        msg_img = MIMEImage(img_data)
        msg_img.add_header("Content-ID", "<visual_hook>")
        msg_img.add_header("Content-Disposition", "inline", filename=visual_hook_path.name)
        msg_root.attach(msg_img)
        visual_hook_status = f"Attached ({len(img_data)//1024} KB) as CID: <visual_hook>"
    else:
        visual_hook_status = f"Warning: {visual_hook_path} not found!"

    print("=" * 70)
    print("OUTREACH EMAIL DISPATCH SUMMARY")
    print("=" * 70)
    print(f"Target Business   : {profile['name']} ({target_key})")
    print(f"Sender            : {msg_root['From']}")
    print(f"Recipient         : {recipient} {'[TEST MODE TO SELF]' if test_recipient else '[LIVE CONTRACTOR]'}")
    print(f"Subject           : {subject}")
    print(f"Live Demo URL     : {profile['demo_url']}")
    print(f"Visual Hook       : {visual_hook_status}")
    print("=" * 70)

    if dry_run:
        print("\n[DRY RUN MODE ENABLED - No email was sent over the network]")
        print("\n--- PLAIN TEXT BODY PREVIEW ---")
        print(text_body[:500] + "...\n[truncated]")
        print("\n--- HTML BODY PREVIEW ---")
        print("HTML rendered with responsive container and CID image hook.")
        print("\nTo send a live test to your own inbox, run:")
        print(f"  python scripts/send_outreach_email.py --target {target_key} --test-to YOUR_GMAIL@gmail.com")
        return True

    # Real SMTP Dispatch
    if not gmail_user or not gmail_app_password:
        print("\n[CONFIG ERROR] Missing Gmail Credentials!")
        print("Please set GMAIL_USER and GMAIL_APP_PASSWORD in your environment or in .env file.")
        print("\nHow to get a Gmail App Password (Takes 60 seconds):")
        print("1. Turn ON '2-Step Verification' on your Google Account: https://myaccount.google.com/security")
        print("2. Visit https://myaccount.google.com/apppasswords")
        print("3. Enter app name 'TexasOutreach' -> Google generates a 16-character password.")
        print("4. Add to .env: GMAIL_USER=yourname@gmail.com, GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx")
        return False

    print(f"\nConnecting to smtp.gmail.com:587 for {gmail_user}...")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.send_message(msg_root)
        server.quit()
        print(f"✅ SUCCESS! Email successfully dispatched to {recipient}")
        return True
    except Exception as e:
        print(f"❌ SMTP Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Commercial Outreach Email Dispatcher via Gmail")
    parser.add_argument("--target", choices=["goodroots", "amatttree", "dapco", "duckac", "ameritex", "calldadac", "bourdonfence", "rockwater", "elevatedpool"], default="goodroots",
                        help="Target business profile to send")
    parser.add_argument("--test-to", type=str, default=None,
                        help="Send a live test to your own inbox to preview on your phone")
    parser.add_argument("--dry-run", action="store_true", default=False,
                        help="Simulate and inspect email without network dispatch")
    parser.add_argument("--force-send", action="store_true", default=False,
                        help="Explicit confirmation to send to real business recipient")

    args = parser.parse_args()
    
    # If neither test-to nor force-send is provided, default to dry-run
    is_dry_run = args.dry_run or (not args.test_to and not args.force_send)
    
    send_email(
        target_key=args.target,
        test_recipient=args.test_to,
        dry_run=is_dry_run,
        force_send=args.force_send
    )

if __name__ == "__main__":
    main()
