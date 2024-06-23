from PIL import Image, ImageDraw, ImageFont

# Create image for mockup
img = Image.new('RGB', (800, 600), color = (255, 255, 255))
d = ImageDraw.Draw(img)

# Dashboard title and filters
d.rectangle([50, 50, 750, 550], outline="black", width=2)
d.text((60, 60), "Security Incident Analytics Dashboard", fill="black")
d.text((60, 90), "Filters: Time Period | Incident Type | Outcome", fill="black")

# Graphs and charts
d.rectangle([60, 120, 370, 320], outline="black", fill="lightgrey")
d.text((65, 125), "Incident Types Over Time", fill="black")
d.rectangle([380, 120, 740, 320], outline="black", fill="lightgrey")
d.text((385, 125), "Outcomes by Incident Type", fill="black")
d.rectangle([60, 330, 370, 530], outline="black", fill="lightgrey")
d.text((65, 335), "Incidents by Severity", fill="black")
d.rectangle([380, 330, 740, 530], outline="black", fill="lightgrey")
d.text((385, 335), "Monthly Incident Trends", fill="black")

# Save the image
mockup_path = "/mnt/data/Security_Incident_Analytics_Dashboard.png"
img.save(mockup_path)
mockup_path
