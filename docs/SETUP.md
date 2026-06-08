# Setup Guide

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Git

## Backend Setup

### 1. Clone the Repository

```bash
git clone https://github.com/cankelly256-web/ads-manager-platform.git
cd ads-manager-platform/backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and update:
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Your JWT secret key
- `META_APP_ID`, `META_APP_SECRET`, `META_ACCESS_TOKEN`: Meta Ads API credentials
- `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_DEVELOPER_TOKEN`: Google Ads API credentials

### 5. Run Database Migrations

```bash
python -m alembic upgrade head
```

### 6. Start the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## Web App Setup

### 1. Navigate to Web Directory

```bash
cd ../web
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment Variables

```bash
cp .env.example .env.local
```

Edit `.env.local` and update:
- `REACT_APP_API_URL`: Backend API URL (default: `http://localhost:8000`)

### 4. Start Development Server

```bash
npm start
```

The app will be available at `http://localhost:3000`

## Mobile App Setup

### 1. Navigate to Mobile Directory

```bash
cd ../mobile
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and update:
- `EXPO_PUBLIC_API_URL`: Backend API URL

### 4. Start Expo

```bash
npm start
```

Then:
- Press `i` for iOS simulator
- Press `a` for Android emulator
- Scan QR code with Expo app on your phone

## Docker Setup (Optional)

If you prefer using Docker:

```bash
cd backend
docker-compose up
```

This will start PostgreSQL and the FastAPI backend.

## Troubleshooting

### Database Connection Error

Ensure PostgreSQL is running and the connection string in `.env` is correct.

### Port Already in Use

If port 8000 is in use:

```bash
uvicorn app.main:app --port 8001 --reload
```

### Module Not Found

Make sure your virtual environment is activated and all dependencies are installed:

```bash
pip install -r requirements.txt
```

## Next Steps

- Read the [API Documentation](./API.md)
- Review the [Architecture](./ARCHITECTURE.md)
- Check GitHub Issues for feature implementation tasks