from openpyxl import Workbook

# Create a new workbook
wb = Workbook()

# Select the active worksheet
ws = wb.active

# Add the provided data to the worksheet
data = [
    "You brighten my darkest days.",
    "Your smile lights up my life.",
    "Thinking of you makes my heart sing.",
    "You're my sunshine on a cloudy day.",
    "Your laughter is my favorite melody.",
    "Every moment with you is precious.",
    "You're the reason for my happiness.",
    "Your love makes my soul soar.",
    "You're my anchor in a storm.",
    "You're my favorite hello and hardest goodbye.",
    "Your kindness knows no bounds.",
    "You're the epitome of grace.",
    "Your presence makes everything better.",
    "You make my heart skip a beat.",
    "You're a treasure beyond compare.",
    "Your warmth fills my soul.",
    "You're the best thing in my life.",
    "Your love is my greatest blessing.",
    "You're my ray of hope.",
    "You're my rock, always there for me.",
    "You're my forever and always.",
    "You're my heart's desire.",
    "Your love is my guiding light.",
    "You're my knight in shining armor.",
    "You make every day brighter.",
    "Your love is like a gentle breeze.",
    "You're my sweet escape.",
    "Your touch sets my soul on fire.",
    "You're my safe haven.",
    "Your love is my sanctuary.",
    "You're my soulmate, my everything.",
    "Your love is my greatest gift.",
    "You're my dream come true.",
    "Your laughter is infectious.",
    "You're my beacon of hope.",
    "Your love fills my heart with joy.",
    "You're my partner in crime.",
    "You're my best friend and lover.",
    "Your presence is a gift.",
    "You're my guiding star.",
    "Your love completes me.",
    "You're my everything and more.",
    "You're my missing puzzle piece.",
    "Your love is my strength.",
    "You're my happily ever after.",
    "You're my sweet serenade.",
    "Your love is my sanctuary.",
    "You're my inspiration.",
    "You're my constant in a changing world.",
    "Your love is my anchor.",
    "You're my true north.",
    "You're the center of my universe.",
    "Your love is my solace.",
    "You're my reason to smile.",
    "Your love is my lifeline.",
    "You're my silver lining.",
    "You're my heart's keeper.",
    "Your love is my treasure.",
    "You're my light in the darkness.",
    "You're my guiding light.",
    "Your love is my sanctuary.",
    "You're my true love.",
    "You're my forever and always.",
    "Your love is my anchor.",
    "You're my reason to believe.",
    "You're my heart's delight.",
    "Your love is my refuge.",
    "You're my soulmate.",
    "You're my shining star.",
    "Your love is my strength.",
    "You're my ray of sunshine.",
    "You're my heart's keeper.",
    "Your love is my salvation.",
    "You're my guiding light.",
    "You're my forever love.",
    "Your love is my compass.",
    "You're my heart's desire.",
    "You're my sweet serenade.",
    "Your love is my sanctuary.",
    "You're my true north.",
    "You're my reason to smile.",
    "Your love is my lifeline.",
    "You're my silver lining.",
    "You're my heart's delight.",
    "Your love is my treasure.",
    "You're my soulmate.",
    "You're my shining star.",
    "Your love is my refuge.",
    "You're my guiding light.",
    "You're my forever love.",
    "Your love is my strength.",
    "You're my ray of sunshine.",
    "You're my heart's keeper.",
    "Your love is my salvation.",
    "You're my guiding light.",
    "You're my forever love.",
    "Your love is my compass.",
    "You're my heart's desire.",
    "You're my sweet serenade."
]

for idx, item in enumerate(data, start=1):
    ws.cell(row=idx, column=1, value=item)

# Save the workbook
wb.save("quotes.xlsx")
