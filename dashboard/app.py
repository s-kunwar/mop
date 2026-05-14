"""
MOP Dashboard - Local Wiki for Placement Data
A markdown-based wiki generator with Flask server for exploring placement data
"""

import os
import csv
import json
import time
import threading
from pathlib import Path
from collections import defaultdict, Counter
from flask import Flask, render_template, request, jsonify, send_from_directory, session, redirect, url_for
import re

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'mop-dashboard-secret-key-2026'

# Global data storage
DATA = {
    'companies': defaultdict(lambda: {
        'name': '',
        'experience_data': [],
        'questions': [],
        'packages': [],
        'branches': set(),
        'years': set()
    }),
    'questions_by_company': defaultdict(list),
    'all_questions': [],
    'index': {},
    'loaded': False
}

# Processing state for UI feedback
PROCESSING_STATE = {
    'progress': 0,
    'current_step': '',
    'total_companies': 0,
    'total_questions': 0,
    'is_processing': False,
    'start_time': None
}

def scan_csv_files(base_path='db/cleaned_csv'):
    """Scan all CSV files in cleaned_csv directories"""
    PROCESSING_STATE['is_processing'] = True
    PROCESSING_STATE['progress'] = 5
    PROCESSING_STATE['current_step'] = 'Initializing system...'
    
    print("📂 Scanning CSV files...")
    
    base_path = Path(base_path)
    
    if not base_path.exists():
        print(f"❌ Path does not exist: {base_path}")
        PROCESSING_STATE['is_processing'] = False
        return False
    
    # Load experience data
    PROCESSING_STATE['current_step'] = 'Loading experience data...'
    PROCESSING_STATE['progress'] = 15
    
    exp_path = base_path / 'exp'
    if exp_path.exists():
        for year_dir in exp_path.iterdir():
            if year_dir.is_dir():
                year = year_dir.name
                for company_dir in year_dir.iterdir():
                    if company_dir.is_dir():
                        for exp_subdir in company_dir.iterdir():
                            if exp_subdir.is_dir():
                                for csv_file in exp_subdir.glob('*.csv'):
                                    load_experience_csv(csv_file, year)
    
    PROCESSING_STATE['progress'] = 50
    
    # Load question bank data
    PROCESSING_STATE['current_step'] = 'Loading question banks...'
    
    que_path = base_path / 'que'
    if que_path.exists():
        for branch_dir in que_path.iterdir():
            if branch_dir.is_dir():
                branch = branch_dir.name
                for item in branch_dir.rglob('*.csv'):
                    load_questions_csv(item, branch)
    
    PROCESSING_STATE['progress'] = 80
    PROCESSING_STATE['current_step'] = 'Building search index...'
    
    # Build search index
    build_index()
    
    PROCESSING_STATE['progress'] = 95
    PROCESSING_STATE['current_step'] = 'Finalizing...'
    PROCESSING_STATE['total_companies'] = len(DATA['companies'])
    PROCESSING_STATE['total_questions'] = len(DATA['all_questions'])
    
    time.sleep(1)  # Simulate final processing
    
    PROCESSING_STATE['progress'] = 100
    PROCESSING_STATE['current_step'] = 'Complete!'
    DATA['loaded'] = True
    PROCESSING_STATE['is_processing'] = False
    
    print(f"✅ Loaded {len(DATA['companies'])} companies")
    print(f"✅ Loaded {len(DATA['all_questions'])} question entries")
    
    return True
    que_path = base_path / 'que'
    if que_path.exists():
        for branch_dir in que_path.iterdir():
            if branch_dir.is_dir():
                branch = branch_dir.name
                for item in branch_dir.rglob('*.csv'):
                    load_questions_csv(item, branch)
    
    # Build search index
    build_index()
    print(f"✅ Loaded {len(DATA['companies'])} companies")
    print(f"✅ Loaded {len(DATA['all_questions'])} question entries")

def load_experience_csv(filepath, year):
    """Load experience CSV file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                company = row.get('Company Name', '').strip()
                if company:
                    DATA['companies'][company]['name'] = company
                    DATA['companies'][company]['experience_data'].append(row)
                    DATA['companies'][company]['years'].add(year)
                    
                    # Extract branch from filepath if possible
                    if 'ECE' in str(filepath):
                        DATA['companies'][company]['branches'].add('ECE')
                    elif 'CSE' in str(filepath):
                        DATA['companies'][company]['branches'].add('CSE')
                    elif 'EEE' in str(filepath):
                        DATA['companies'][company]['branches'].add('EEE')
                    
                    # Extract package
                    pkg = row.get('Package', '').strip()
                    if pkg:
                        DATA['companies'][company]['packages'].append(pkg)
    except Exception as e:
        print(f"⚠️ Error loading {filepath}: {e}")

def load_questions_csv(filepath, branch):
    """Load questions CSV file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                company = row.get('company_name', '').strip()
                if company:
                    DATA['companies'][company]['branches'].add(branch)
                    
                    question_entry = {
                        'company': company,
                        'branch': branch,
                        'technical': row.get('technical_questions', '').strip(),
                        'programming': row.get('programming_questions', '').strip(),
                        'personal': row.get('personal_interaction_questions', '').strip()
                    }
                    DATA['all_questions'].append(question_entry)
                    DATA['questions_by_company'][company].append(question_entry)
    except Exception as e:
        print(f"⚠️ Error loading {filepath}: {e}")

def build_index():
    """Build search index"""
    for company_name in DATA['companies'].keys():
        DATA['index'][company_name.lower()] = company_name

def get_company_stats(company):
    """Get statistics for a company"""
    data = DATA['companies'][company]
    packages = data['packages']
    
    stats = {
        'total_placements': len(data['experience_data']),
        'avg_package': None,
        'max_package': None,
        'min_package': None,
        'branches': list(data['branches']),
        'years': sorted(list(data['years']))
    }
    
    # Parse packages
    numeric_packages = []
    for pkg in packages:
        match = re.search(r'(\d+\.?\d*)', pkg)
        if match:
            numeric_packages.append(float(match.group(1)))
    
    if numeric_packages:
        stats['avg_package'] = f"{sum(numeric_packages)/len(numeric_packages):.2f} LPA"
        stats['max_package'] = f"{max(numeric_packages):.2f} LPA"
        stats['min_package'] = f"{min(numeric_packages):.2f} LPA"
    
    return stats

# Routes
@app.route('/')
def landing():
    """Landing page"""
    if DATA['loaded'] and session.get('database_path'):
        return redirect(url_for('index'))
    return render_template('landing.html')

@app.route('/api/start-processing', methods=['POST'])
def start_processing():
    """Start data processing"""
    db_path = request.json.get('database_path', 'db/cleaned_csv').strip()
    
    if not db_path:
        db_path = 'db/cleaned_csv'
    
    session['database_path'] = db_path
    session.permanent = True
    
    # Start processing in background thread
    thread = threading.Thread(target=scan_csv_files, args=(db_path,))
    thread.start()
    
    return jsonify({'status': 'processing'})

@app.route('/processing')
def processing():
    """Processing page"""
    if DATA['loaded']:
        return redirect(url_for('index'))
    return render_template('processing.html')

@app.route('/api/progress')
def get_progress():
    """Get processing progress"""
    return jsonify({
        'progress': PROCESSING_STATE['progress'],
        'current_step': PROCESSING_STATE['current_step'],
        'total_companies': PROCESSING_STATE['total_companies'],
        'total_questions': PROCESSING_STATE['total_questions'],
        'is_complete': DATA['loaded']
    })

@app.route('/dashboard')
def index():
    """Dashboard homepage"""
    if not DATA['loaded']:
        return redirect(url_for('landing'))
    
    companies = sorted(list(DATA['companies'].keys()))
    stats = {
        'total_companies': len(companies),
        'total_questions': len(DATA['all_questions']),
        'total_placements': sum(len(DATA['companies'][c]['experience_data']) for c in companies)
    }
    return render_template('index.html', companies=companies, stats=stats)

@app.route('/api/search')
def search():
    """Search endpoint"""
    query = request.args.get('q', '').lower().strip()
    if not query:
        return jsonify({'results': []})
    
    results = []
    for company in DATA['companies'].keys():
        if query in company.lower():
            stats = get_company_stats(company)
            results.append({
                'name': company,
                'placements': stats['total_placements'],
                'branches': stats['branches']
            })
    
    return jsonify({'results': sorted(results, key=lambda x: x['name'])})

@app.route('/company/<company_name>')
def company_profile(company_name):
    """Company profile page"""
    # Find exact company name (case-insensitive)
    company = None
    for c in DATA['companies'].keys():
        if c.lower() == company_name.lower():
            company = c
            break
    
    if not company:
        return "Company not found", 404
    
    data = DATA['companies'][company]
    stats = get_company_stats(company)
    questions = DATA['questions_by_company'].get(company, [])
    
    return render_template('company_profile.html', 
                         company=company,
                         stats=stats,
                         experiences=data['experience_data'],
                         questions=questions)

@app.route('/interview-insights')
def interview_insights():
    """Interview insights page"""
    # Aggregate interview data
    insights = {
        'common_topics': Counter(),
        'common_questions': [],
        'companies_by_placements': []
    }
    
    # Count common technical topics
    for q in DATA['all_questions']:
        tech = q.get('technical', '')
        if tech:
            # Simple word frequency
            words = set(re.findall(r'\b\w+\b', tech.lower()))
            for word in words:
                if len(word) > 4:  # Filter short words
                    insights['common_topics'][word] += 1
    
    # Sort companies by placement count
    company_placements = [(c, len(DATA['companies'][c]['experience_data'])) 
                         for c in DATA['companies'].keys()]
    insights['companies_by_placements'] = sorted(company_placements, 
                                                 key=lambda x: x[1], 
                                                 reverse=True)[:20]
    
    return render_template('interview_insights.html', 
                         insights=insights,
                         total_companies=len(DATA['companies']),
                         common_topics=insights['common_topics'].most_common(20))

@app.route('/questions/<branch>')
def branch_questions(branch):
    """Questions by branch"""
    questions_by_company = defaultdict(list)
    
    for q in DATA['all_questions']:
        if q.get('branch', '') == branch:
            questions_by_company[q['company']].append(q)
    
    return render_template('branch_questions.html',
                         branch=branch,
                         questions_by_company=dict(questions_by_company))

if __name__ == '__main__':
    # Create necessary directories
    Path('templates').mkdir(exist_ok=True)
    Path('static').mkdir(exist_ok=True)
    
    # Configure session
    app.config['SESSION_PERMANENT'] = True
    app.config['PERMANENT_SESSION_LIFETIME'] = 3600  # 1 hour
    
    # Reset data loading state
    DATA['loaded'] = False
    PROCESSING_STATE['progress'] = 0
    PROCESSING_STATE['is_processing'] = False
    
    print("\n🚀 Starting MOP Dashboard...")
    print("📍 Local URL: http://localhost:5000")
    print("📝 Please provide database path on landing page")
    print("Press Ctrl+C to stop\n")
    
    app.run(debug=True, port=5000, use_reloader=False)
