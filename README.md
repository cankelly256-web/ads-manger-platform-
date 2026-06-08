# Ads Manager Platform

A comprehensive agency tool for managing multiple clients' advertising campaigns across Meta (Facebook/Instagram) and Google Ads with web and mobile dashboards.

## 🎯 Project Overview

This platform enables agencies to:
- Manage multiple client accounts
- Create, manage, and monitor ad campaigns across Meta and Google Ads
- View real-time analytics and performance metrics
- Manage budgets and billing
- Automate campaign optimization
- Access dashboards from web and mobile apps

## 📋 Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **Authentication**: JWT + OAuth 2.0
- **Real-time**: WebSockets
- **ORM**: SQLAlchemy

### Web Frontend
- **Framework**: React 18
- **State Management**: Redux Toolkit
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios

### Mobile App
- **Framework**: React Native with Expo
- **State Management**: Redux Toolkit
- **Navigation**: React Navigation
- **HTTP Client**: Axios

## 📁 Project Structure

```
ads-manager-platform/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── integrations/
│   │   └── middleware/
│   ├── tests/
│   ├── requirements.txt
│   ├── .env.example
│   └── docker-compose.yml
│
├── web/                        # React web dashboard
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── store/
│   │   ├── hooks/
│   │   ├── styles/
│   │   └── App.tsx
│   ├── public/
│   ├── package.json
│   └── .env.example
│
├── mobile/                     # React Native mobile app
│   ├── app/
│   ├── src/
│   │   ├── components/
│   │   ├── screens/
│   │   ├── navigation/
│   │   ├── services/
│   │   ├── store/
│   │   └── utils/
│   ├── app.json
│   ├── package.json
│   └── .env.example
│
└── docs/                       # Documentation
    ├── API.md
    ├── SETUP.md
    └── ARCHITECTURE.md
```

## 🚀 Quick Start

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m alembic upgrade head
uvicorn app.main:app --reload
```

### Web App Setup
```bash
cd web
npm install
npm start
```

### Mobile App Setup
```bash
cd mobile
npm install
npx expo start
```

## 🔑 Key Features

### Phase 1 (MVP)
- [x] User authentication (JWT)
- [x] Client management (CRUD)
- [x] Campaign management (CRUD)
- [x] Database setup with PostgreSQL
- [x] Basic API endpoints
- [x] Meta & Google Ads API integration stubs

### Phase 2
- [ ] Real-time analytics dashboard
- [ ] Campaign performance metrics
- [ ] Budget management & alerts
- [ ] Advanced filtering & search
- [ ] Mobile app full functionality

### Phase 3
- [ ] Automated bid optimization
- [ ] AI-powered recommendations
- [ ] Billing & invoicing system
- [ ] White-label features
- [ ] Advanced reporting

## 📚 Documentation

- [API Documentation](./docs/API.md) - Complete API reference
- [Setup Guide](./docs/SETUP.md) - Detailed setup instructions
- [Architecture](./docs/ARCHITECTURE.md) - System architecture & design patterns

## 🔐 Environment Variables

See `.env.example` files in each directory for required environment variables:
- Database connection strings
- JWT secrets
- Meta Ads API credentials
- Google Ads API credentials
- OAuth configuration

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Web tests
cd web
npm test

# Mobile tests
cd mobile
npm test
```

## 📖 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/refresh` - Refresh token

### Clients
- `GET /api/clients` - List all clients
- `POST /api/clients` - Create new client
- `GET /api/clients/{id}` - Get client details
- `PUT /api/clients/{id}` - Update client
- `DELETE /api/clients/{id}` - Delete client

### Campaigns
- `GET /api/campaigns` - List campaigns
- `POST /api/campaigns` - Create campaign
- `GET /api/campaigns/{id}` - Get campaign details
- `PUT /api/campaigns/{id}` - Update campaign
- `DELETE /api/campaigns/{id}` - Delete campaign

### Analytics
- `GET /api/analytics/campaigns/{id}` - Get campaign analytics
- `GET /api/analytics/clients/{id}` - Get client analytics
- `GET /api/analytics/dashboard` - Get dashboard overview

## 🤝 Contributing

1. Create a feature branch (`git checkout -b feature/amazing-feature`)
2. Commit changes (`git commit -m 'Add amazing feature'`)
3. Push to branch (`git push origin feature/amazing-feature`)
4. Open a Pull Request

## 📝 License

This project is proprietary and confidential.

## 📞 Support

For support or questions, please reach out to the development team.

---

**Last Updated**: June 8, 2026
**Version**: 0.1.0 (MVP Phase)