import urllib.request
import os

username = "Rizky-kanata"
url = f"https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={username}&theme=transparent"

def generate_activity_graph():
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')
            
            # Replace colors
            svg_data = svg_data.replace('fill: #ffffff;', 'fill: #00D4FF;')
            svg_data = svg_data.replace('color="#ffffff"', 'color="#00D4FF"')
            
            svg_data = svg_data.replace('#006AFF', '#c4001a')
            svg_data = svg_data.replace('fill="#0579C3"', 'fill="#00D4FF"')

            if not os.path.exists('assets'):
                os.makedirs('assets')
                
            with open('assets/activity-graph.svg', 'w', encoding='utf-8') as f:
                f.write(svg_data)
            print("Saved assets/activity-graph.svg")
    except Exception as e:
        print(f"Error fetching graph: {e}")

if __name__ == "__main__":
    generate_activity_graph()