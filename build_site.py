import markdown
import re

readme_path = r'c:\Users\ALEX\Downloads\.py\.projects\README.md'
index_path = r'c:\Users\ALEX\Downloads\.py\.projects\alexcj10.github.io\index.html'
project_path = r'c:\Users\ALEX\Downloads\.py\.projects\alexcj10.github.io\project.html'

# --- 1. Rebuild index.html (Summary format) ---
summary_html = """<!-- Projects -->
        <h2>Projects</h2>

        <div class="entry">
            <div class="entry-head">
                <strong>HR Analytics & EDA: Employee Workforce Report</strong>
                <span class="entry-aside">Python · Pandas · Matplotlib</span>
            </div>
            <p>
                A comprehensive exploratory data analysis (EDA) of 1,020 employee records, moving from messy raw data to actionable business intelligence. Handled data quality issues like missing values using grouped median imputation. Analyzed salary distributions, finding a near-perfect 50/50 split around the $85K average. Conducted a deep dive into salary versus performance, revealing a critical compensation misalignment where top performers earn as low as $50K while poor performers earn up to $119K. Built detailed visualizations to highlight retention risks, regional salary patterns, and the impact of remote work on performance. 
            </p>
            
            <div class="gallery-scroll">
                <img src="hr-analytics/Above vs Below Average Salary.png" alt="Salary Distribution" class="screenshot thumb" />
                <img src="hr-analytics/Top 7 high earners (Performance = Poor).png" alt="High Earners, Poor Performance" class="screenshot thumb" />
                <img src="hr-analytics/Top 7 low earners (Performance = Excellent).png" alt="Low Earners, Excellent Performance" class="screenshot thumb" />
                <img src="hr-analytics/Top 7 high salary earners.png" alt="Top 7 Highest Paid" class="screenshot thumb" />
                <img src="hr-analytics/Top 7 low salary earners.png" alt="Top 7 Lowest Paid" class="screenshot thumb" />
            </div>
            <p class="img-hint fade-up" style="margin-bottom: 20px;">Swipe to see more &nbsp;·&nbsp; Tap to expand</p>
            
            <div style="display: flex; gap: 12px; margin-top: 15px;">
                <a href="project.html" style="display: inline-block; font-weight: 500; text-decoration: none; padding: 8px 16px; background: #0969da; color: #fff; border-radius: 6px; font-size: 0.9rem; transition: opacity 0.2s;" onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='1'">View Full Analytics Report →</a>
                <a href="https://github.com/alexcj10/employee-workforce-analytics" target="_blank" style="display: inline-flex; align-items: center; gap: 6px; font-weight: 500; text-decoration: none; padding: 8px 16px; background: #24292f; color: #fff; border-radius: 6px; font-size: 0.9rem; transition: opacity 0.2s;" onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='1'">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.009-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.379.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.161 22 16.418 22 12c0-5.523-4.477-10-10-10z"></path></svg>
                    GitHub ↗
                </a>
            </div>
        </div>
"""

with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

start_marker = "<!-- Projects -->"
end_marker = "<!-- Education -->"
start_idx = index_html.find(start_marker)
end_idx = index_html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    end_idx = index_html.rfind("<hr>", start_idx, end_idx)
    new_index = index_html[:start_idx] + summary_html + "\n        " + index_html[end_idx:]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_index)

# --- 2. Build project.html (Full report) ---
with open(readme_path, 'r', encoding='utf-8') as f:
    md_text = f.read()

html_content = markdown.markdown(md_text, extensions=['tables'])
html_content = re.sub(r'src="(.*?\.png)"', r'src="hr-analytics/\1"', html_content)

project_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HR Analytics & EDA - Alex Joshva</title>
    <link rel="icon" type="image/png" href="favicon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="page" style="max-width: 800px;">
        <a href="index.html" style="display: inline-flex; align-items: center; gap: 6px; font-weight: 500; text-decoration: none; margin-bottom: 30px; color: #555; transition: color 0.2s;" onmouseover="this.style.color='#111'" onmouseout="this.style.color='#555'">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
            Back to Portfolio
        </a>
        
        <div style="margin-bottom: 10px;">
            <a href="https://github.com/alexcj10/employee-workforce-analytics" target="_blank" class="github-btn" style="margin-bottom: 0;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.009-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.379.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.161 22 16.418 22 12c0-5.523-4.477-10-10-10z"></path></svg>
                View Code & Data on GitHub
            </a>
        </div>
        
        <div class="report-content" style="opacity: 1; transform: none; animation: none;">
            {html_content}
        </div>
    </div>
</body>
</html>
"""

with open(project_path, 'w', encoding='utf-8') as f:
    f.write(project_page)

print("Site rebuilt successfully.")
