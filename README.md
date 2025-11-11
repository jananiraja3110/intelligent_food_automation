# 🍽️ Intelligent Food Automation System  
### **TRANSFORMING FOOD PROCESSING THROUGH INTELLIGENT AUTOMATION**

A secure, intelligent, and role-based automation platform built with **Django** for the food processing industry — featuring **encrypted data transfers**, **workflow automation**, and **team collaboration**.

---

## 🚀 Project Overview
The **Intelligent Food Automation System** is a web-based platform that integrates multiple teams in the food processing pipeline. It ensures **data security**, **workflow transparency**, and **intelligent task automation** using encryption and role-based access management.

---

## ⚙️ Quick Start

### 🧩 Installation & Setup

# Clone and setup environment
git clone https://github.com/jananiraja3110/intelligent_food_automation
cd intelligent_food_automation
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate

# Install dependencies and run the app
pip install -r requirements.txt

**#👤 Default Admin Access**

URL	Email: admin@gmail.com
Password:admin
http://localhost:8000

**#👥 User Roles & Permissions**

**Role	Capabilities**
Vendor Team	Register, upload (Excel/CSV/raw files), submit requests, track status
Purchase Team	Process vendor requests, manage procurement, secure file access
Tech Team	Handle technical requests, system maintenance
Production Team	Manage production data, quality control, monitoring
Admin Team	Approve users, manage system-wide operations
🔐 Security Features

Military-grade AES-256 Encryption for all file transfers

Role-Based Access Control (RBAC) with 5 permission levels

Secure Authentication and admin approval workflows

Encrypted Data Storage (at rest and in transit)

Complete Audit Trails for all activities

##**📁 File Management**
Supported File Formats

Excel (.xlsx, .xls)

CSV (.csv)

Raw material data files

Dataset files

Secure Transfer Workflow
Upload → AES-256 Encryption → Team Routing → Role-based Access → Audit Logging

**#🤖 Workflow Automation**
Request Processing Flow
Vendor Upload → Auto Encryption → Team Notification → 
Request Processing → Status Update → Completion Tracking

Automated Features

Real-time request alerts

Status change notifications

Secure team communication

Automated file handling

**#🧠 Technology Stack**
Category	Tools & Technologies
Backend	Python 3.9+, Django 4.2+, Django REST Framework
Database	PostgreSQL (Production), SQLite (Development)
Frontend	HTML5, CSS3, JavaScript, Bootstrap 5
Encryption	PyCryptodome (AES-256)
Visualization	Chart.js
Security	Django Auth System, Role-based Permissions
Deployment	Docker, Gunicorn, Nginx
Version Control	Git & GitHub


#👩‍💻 Author: Janani Raja

#🌐 GitHub: @jananiraja3110

#📧 Email: jananiraja3110@gmail.com

#RUN

python manage.py migrate

python manage.py runserver
