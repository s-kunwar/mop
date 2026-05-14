# MOP Dashboard - Local Wiki for Placement Data

A beautiful, interactive markdown-based wiki dashboard for exploring placement preparation data from the MOP (Machine for Organizational Processing) system.

## 🎯 Features

- **Company Profiles**: Detailed information about each company including placements, packages, branches, and interview questions
- **Search & Filter**: Quick search across all companies with intelligent filtering
- **Interview Insights**: Analytics on common interview topics, top recruiting companies, and preparation insights
- **Branch-wise Questions**: Browse interview questions organized by engineering branch
- **Student Data**: View student placements, packages, CGPA, and interview feedback
- **Beautiful UI**: Dark-mode dashboard with responsive design and interactive cards

## 📊 Data Included

- **25+ Companies** from placement cycles
- **1,000+ Student Placements** with detailed data
- **500+ Interview Question Sets** organized by branch and company
- **Engineering Branches**: CSE, ECE, EEE, AIML, AInDS, CV, ISE, MBA, MCA, ME
- **Academic Years**: 2020-2021 through 2025-2026

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation & Setup

1. **Navigate to the dashboard directory:**
   ```bash
   cd dashboard
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   - Visit `http://localhost:5000` in your web browser
   - Dashboard will load automatically with all data scanned from CSV files

## 📖 Usage Guide

### Home Page
- View overall statistics (companies, placements, question entries)
- Search for specific companies
- Browse all companies in grid view
- Quick access to main features

### Company Profile
- **View:** Click any company from the home page
- **See:** 
  - Company statistics (total placements, average/max/min packages)
  - Engineering branches offering placements
  - Academic years with data
  - All student placement records with details
  - Interview questions (technical, programming, HR)
  - Recruitment rounds and interview process details

### Interview Insights
- **Top Companies**: See which companies recruited the most students
- **Common Topics**: Visualize frequently asked interview topics
- **Preparation Tips**: Key areas to focus on for interviews
- **Branch Explorer**: Quick links to branch-specific questions

### Branch Questions
- Select any engineering branch (CSE, ECE, etc.)
- View all interview questions organized by company
- Filter questions by type (technical, programming, HR)
- Prepare for specific company interviews

## 🏗️ Architecture

```
dashboard/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── templates/               # HTML templates
│   ├── base.html           # Base layout and styling
│   ├── index.html          # Home page
│   ├── company_profile.html # Company detail page
│   ├── interview_insights.html # Analytics page
│   └── branch_questions.html # Questions by branch
└── README.md               # This file
```

## 🔧 Data Processing

The dashboard automatically:

1. **Scans CSV directories** - Finds all cleaned CSV files in `db/cleaned_csv/`
2. **Parses experience data** - Loads student placement records with company details
3. **Indexes questions** - Collects interview questions from all sources
4. **Builds search index** - Creates searchable company database
5. **Calculates statistics** - Computes packages, placement rates, and metrics
6. **Generates pages** - Creates interactive HTML views on-the-fly

## 📋 API Endpoints

- `GET /` - Home page with company listing
- `GET /company/<company_name>` - Company profile page
- `GET /interview-insights` - Analytics and insights page
- `GET /questions/<branch>` - Branch-specific questions
- `GET /api/search?q=<query>` - Search API (JSON response)

## 💾 Data Schema

### Experience Data Columns
- Name, USN, Aptitude Test, JAM Round, Email, Contact Number, CGPA
- Company Name, Package, Recruitment Rounds
- Interview Questions, Feedback, Offer Letter Link

### Question Bank Columns
- Serial Number, Company Name
- Technical Questions, Programming Questions
- Personal/HR Questions

## 🎨 Customization

### Change Port Number
Edit `app.py` and modify the port in:
```python
app.run(debug=True, port=8080, use_reloader=False)  # Change 8080 to your port
```

### Modify Styling
Edit `templates/base.html` CSS variables:
```css
:root {
    --primary: #2563eb;      /* Main accent color */
    --bg: #0f172a;           /* Background color */
    --text: #f1f5f9;         /* Text color */
    /* ... more colors ... */
}
```

## ⚡ Performance Tips

- Dashboard caches data on startup for fast navigation
- Search is instant thanks to in-memory indexing
- All data loads from local CSV files (no network needed)
- Runs completely offline after startup

## 🐛 Troubleshooting

**Issue: Port 5000 already in use**
```bash
# Use a different port
# Edit app.py and change port number
python app.py
```

**Issue: CSV files not loading**
- Ensure CSV files are in `db/cleaned_csv/` directory
- Check file permissions
- Verify CSV format matches expected structure

**Issue: No companies showing**
- Wait for initial data scan (may take a few seconds)
- Check console output for errors
- Verify file paths in app.py

## 📈 Future Enhancements

- [ ] Export data to PDF/Excel
- [ ] Advanced filtering by package range, CGPA, etc.
- [ ] Interview question recommendations
- [ ] Student success rate analytics
- [ ] Timeline visualization of placement seasons
- [ ] Email notifications for new placements
- [ ] Multi-language support

## 📝 Notes

- Dashboard is read-only (doesn't modify CSV files)
- Search is case-insensitive
- All data is stored in memory during runtime
- Refreshing the page won't lose state (Flask handles it)

## 🤝 Support

For issues or suggestions:
1. Check the troubleshooting section above
2. Review CSV file structure in `db/cleaned_csv/`
3. Check Flask console output for errors
4. Verify Python version (3.8+)

## 📄 License

Part of the MOP (Machine for Organizational Processing) system for placement preparation.

---

**Happy Exploring! 🚀**

Visit `http://localhost:5000` and start discovering placement opportunities!
