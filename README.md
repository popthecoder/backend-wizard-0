# Backend Wizards - Stage 0
Dynamic Profile Endpoint with Cat Facts API integration.
## 🚀 Quick Start
### Prerequisites
- Python 3.8+
- pip
### Installation
1. Clone the repository:
```bash
git clone <your-repo-url>
cd backend-wizards-stage-0
```
2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your information
```
5. Run migrations:
```bash
python manage.py migrate
```
6. Start server:
```bash
python manage.py runserver
```
7. Test the API:
```
http://localhost:8000/me
```
## 📡 API Endpoints
### GET /me
Returns profile information with a dynamic cat fact.
**Response:**
```json
{
"status": "success",
"user": {
"email": "your.email@example.com",
"name": "Your Full Name",
"stack": "Python/Django"
},
"timestamp": "2025-10-17T15:30:45.123456Z",
"fact": "Cats sleep 70% of their lives."
}
```
## 🧪 Testing
```bash
python test_api.py
```
## 🌐 Deployment
Deployed on: [Your deployment platform]
Live URL: [Your live URL]/me
## 👨‍💻 Author
**Your Name**
- Email: your.email@example.com
- Stack: Python/Django
## 📄 License

# 🧪 LOCAL TESTING {#testing}
## Method 1: Browser Testing
1. Make sure server is running: `python manage.py runserver`
2. Open browser
3. Go to: `http://localhost:8000/me`
4. You should see JSON response
## Method 2: curl Command
```bash
curl http://localhost:8000/me
```
## Method 3: Python Test Script
```bash
python test_api.py
```
## Method 4: Postman/Insomnia
1. Open Postman
2. Create new GET request
3. URL: `http://localhost:8000/me`
4. Click Send
## What to Check:
✅ Status code is 200
✅ Content-Type is application/json
✅ Response has all required fields
✅ Timestamp changes on each request
✅ Cat fact changes on each request