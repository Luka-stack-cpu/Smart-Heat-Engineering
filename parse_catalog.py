import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's locate the categories
# We have showCat(catId) tabs:
# 'heat-pumps', 'fancoils', 'warm-floor', 'boilers', 'radiators'
# Let's write a python parser using BeautifulSoup if installed, or regex
try:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    catalog = {}
    
    # Let's find all divs with class "cat-section"
    for cat_sec in soup.find_all(class_='cat-section'):
        cat_id = cat_sec.get('id')
        catalog[cat_id] = []
        
        # Find all cards in this section
        for card in cat_sec.find_all(class_='prod-card'):
            title = card.find('h3').get_text(strip=True) if card.find('h3') else ''
            desc = card.find('p').get_text(strip=True) if card.find('p') else ''
            img_tag = card.find('img')
            img = img_tag.get('src') if img_tag else ''
            
            badges = [b.get_text(strip=True) for b in card.find_all(class_='prod-badge')]
            
            # Models select
            models = []
            select = card.find('select', class_='area-select')
            if select:
                for opt in select.find_all('option'):
                    val_str = opt.get('value')
                    try:
                        val = json.loads(val_str)
                        models.append(val)
                    except Exception as e:
                        print(f"Error parsing option value in {title}: {val_str}")
            
            catalog[cat_id].append({
                "title": title,
                "desc": desc,
                "img": img,
                "badges": badges,
                "models": models
            })
            
    print(json.dumps(catalog, ensure_ascii=False, indent=2))
except Exception as e:
    print("Error:", e)
