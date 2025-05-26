
# 🚀 PDF Collab Pro - Your Ultimate PDF Workspace

<div align="center">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDV5dG10b2VwNjQ3Zm95dHdxNmJsNHdlOHQ1YnowYXc2ajFzc2g3eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7jtU9sxHNLZuv8HZCa/giphy.gif" width="200">
  
  [![Django](https://img.shields.io/badge/Django-3.2.18-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
  [![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
  [![SQLite](https://img.shields.io/badge/SQLite-3.0-lightgrey?style=for-the-badge&logo=sqlite)](https://sqlite.org/)
</div>

## ✨ **Features That Spark Joy**
| Feature | Emoji | Description |
|---------|-------|-------------|
| **Secure Auth** | 🔐 | Login/Signup with password protection |
| **PDF Magic** | 📄 | Upload, view & manage PDFs effortlessly |
| **Share with Ease** | 🔗 | One-click document sharing |
| **Blazing Search** | 🔍 | Find documents in milliseconds |
| **Responsive UI** | 📱 | Works perfectly on all devices |

## 🎯 **Quick Start Guide**

### 1. **Clone & Enter** 🏠
```bash
git clone https://github.com/yourusername/pdf-collab-pro.git
cd pdf-collab-pro
2. Setup Virtual Environment 🐍
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
3. Install Dependencies 📦
bash
pip install -r requirements.txt
4. Database Setup 💾
bash
python manage.py migrate
python manage.py createsuperuser  # Create admin account
5. Launch! 🚀
bash
python manage.py runserver
👉 Visit http://localhost:8000

🛠 Developer Cheat Sheet
🔄 Database Operations
bash
# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (careful!)
rm db.sqlite3 && python manage.py migrate
👥 User Management
bash
# Create superuser
python manage.py createsuperuser

# List all users
python manage.py shell -c "from django.contrib.auth.models import User; print(list(User.objects.all()))"
⚙️ Production Setup
bash
# Collect static files
python manage.py collectstatic

# Set production environment
export DEBUG=False
export SECRET_KEY='your-secret-key-here'
🎨 Project Structure
📦 pdf-collab-pro
├── 📂 documents        # PDF management core
│   ├── 📜 models.py    # Database models
│   ├── 🎨 templates/   # Beautiful UI templates
│   └── 🎭 views.py     # Business logic
├── 🔐 accounts        # Authentication system
├── 🎮 manage.py       # Project control center
└── 📜 requirements.txt # Dependencies list
💖 Made with Django Magic
License
PRs Welcome


