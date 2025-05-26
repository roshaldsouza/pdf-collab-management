# 🚀 PDF Collab Pro - Your Ultimate PDF Workspace

<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDZ1dG1zZ3J1Z2R4bWQ0bWJ2Z2N6dWx5Z2JtY3BmcGZ6eGZ0eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT5LMHxhOfscxPfIfm/giphy.gif" width="200">
  
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
bash
git clone https://github.com/roshaldsiuza/pdf-collab-pro.git
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

# Collect static files
python manage.py collectstatic

# Set production environment
# PDF Collaboration Project (Django) ✨

## 🚀 Deployment Quickstart


# Collect static files
python manage.py collectstatic

# Set production mode
export DEBUG=False
export SECRET_KEY='your-secret-key-here'
🗂️ Project Structure
pdf-collab-pro/
├── documents/       📂 PDF collaboration core
├── models.py       💾 Database models
├── templates/      🎨 Beautiful UI
├── views.py        ⚙️ Business logic
├── accounts/       🔐 Auth system
├── manage.py       🎛️ Project control
└── requirements.txt 📦 Dependencies

🔮 Built with Django Magic!

⭐ Star if you find this useful!

🤝 PRs welcome!
