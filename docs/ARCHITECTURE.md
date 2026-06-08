# Architecture Documentation

## System Overview

The Ads Manager Platform is built as a distributed system with three main components:

1. **Backend API** - FastAPI server handling business logic and integrations
2. **Web Dashboard** - React SPA for desktop/laptop users
3. **Mobile App** - React Native for iOS and Android

## Backend Architecture

### Technology Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **API Integrations**: Meta Ads API, Google Ads API

### Project Structure

```
backend/
├── app/
│   ├── main.py              # Application entry point
│   ├── config.py            # Configuration and settings
│   ├── database.py          # Database connection and session
│   ├── models/              # SQLAlchemy models
│   │   ├── user.py
│   │   ├── client.py
│   │   ├── campaign.py
│   │   └── analytics.py
│   ├── schemas/             # Pydantic request/response schemas
│   │   ├── user.py
│   │   ├── client.py
│   │   ├── campaign.py
│   │   └── auth.py
│   ├── routes/              # API endpoint handlers
│   │   ├── auth.py
│   │   ├── clients.py
│   │   ├── campaigns.py
│   │   └── analytics.py
│   ├── services/            # Business logic layer
│   │   ├── auth.py
│   │   ├── client.py
│   │   ├── campaign.py
│   │   └── analytics.py
│   ├── integrations/        # External API integrations
│   │   ├── meta.py          # Meta Ads API
│   │   └── google.py        # Google Ads API
│   └── middleware/          # Custom middleware
├── tests/                   # Unit and integration tests
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Docker configuration
└── Dockerfile              # Container image definition
```

### Data Flow

```
Client Request
    ↓
FastAPI Router (auth validation)
    ↓
Service Layer (business logic)
    ↓
Database/External API
    ↓
Schema Response (validation & serialization)
    ↓
JSON Response
```

### Database Schema

#### Users Table
- `id` (UUID): Primary key
- `email` (String): Unique user email
- `username` (String): Unique username
- `hashed_password` (String): Bcrypt hashed password
- `full_name` (String): User's full name
- `is_active` (Boolean): Account status
- `is_superuser` (Boolean): Admin flag
- `created_at` (DateTime): Creation timestamp
- `updated_at` (DateTime): Last update timestamp

#### Clients Table
- `id` (UUID): Primary key
- `user_id` (FK): Reference to user
- `name` (String): Client business name
- `email` (String): Client contact email
- `company_name` (String): Company name
- `phone` (String): Contact phone
- `description` (Text): Client description
- `meta_account_id` (String): Meta business account ID
- `google_account_id` (String): Google Ads customer ID
- `meta_access_token` (String): Encrypted Meta API token
- `google_refresh_token` (String): Encrypted Google refresh token
- `is_active` (Boolean): Client status
- `created_at` (DateTime): Creation timestamp
- `updated_at` (DateTime): Last update timestamp

#### Campaigns Table
- `id` (UUID): Primary key
- `client_id` (FK): Reference to client
- `name` (String): Campaign name
- `description` (Text): Campaign details
- `platform` (Enum): "meta", "google", or "both"
- `status` (Enum): "draft", "active", "paused", "completed", "archived"
- `budget` (Float): Total campaign budget
- `daily_budget` (Float): Daily spending limit
- `start_date` (DateTime): Campaign start date
- `end_date` (DateTime): Campaign end date
- `meta_campaign_id` (String): Meta campaign ID
- `google_campaign_id` (String): Google campaign ID
- `objective` (String): Campaign objective
- `audience_targeting` (JSON): Audience targeting configuration
- `created_at` (DateTime): Creation timestamp
- `updated_at` (DateTime): Last update timestamp

#### CampaignAnalytics Table
- `id` (UUID): Primary key
- `campaign_id` (FK): Reference to campaign
- `date` (DateTime): Analytics date
- `platform` (String): "meta" or "google"
- `impressions` (Integer): Ad impressions
- `clicks` (Integer): Ad clicks
- `conversions` (Integer): Conversions
- `spend` (Float): Amount spent
- `ctr` (Float): Click-through rate
- `cpc` (Float): Cost per click
- `cpa` (Float): Cost per acquisition
- `roas` (Float): Return on ad spend
- `created_at` (DateTime): Creation timestamp

## Frontend Architecture

### Web App (React)

**Technology Stack:**
- React 18
- Redux Toolkit (state management)
- React Router (routing)
- Axios (HTTP client)
- Tailwind CSS (styling)
- Recharts (data visualization)

**Structure:**
```
web/
├── public/              # Static assets
├── src/
│   ├── components/      # Reusable UI components
│   ├── pages/           # Page components
│   ├── services/        # API integration services
│   ├── store/           # Redux store configuration
│   ├── hooks/           # Custom React hooks
│   ├── styles/          # Global and component styles
│   ├── types/           # TypeScript types
│   ├── utils/           # Utility functions
│   └── App.tsx          # Root component
└── package.json
```

**State Management:**
Redux Toolkit manages:
- User authentication state
- Clients list and details
- Campaigns list and details
- Analytics data
- UI state (loading, errors, modals)

### Mobile App (React Native)

**Technology Stack:**
- React Native with Expo
- Redux Toolkit (state management)
- React Navigation (routing)
- Axios (HTTP client)

**Structure:**
```
mobile/
├── assets/              # Images and icons
├── src/
│   ├── components/      # Reusable components
│   ├── screens/         # Screen components
│   ├── navigation/      # Navigation configuration
│   ├── services/        # API integration
│   ├── store/           # Redux store
│   ├── types/           # TypeScript types
│   └── utils/           # Utility functions
└── app.json
```

## API Integration Architecture

### Meta Ads Integration

**Authentication Flow:**
1. User authorizes app via Meta OAuth
2. App receives user access token
3. Token stored securely in database
4. Token used for API calls on behalf of user

**Operations:**
- Create campaigns
- Update campaign settings
- Pause/resume campaigns
- Retrieve performance metrics
- Manage ad sets and ads

### Google Ads Integration

**Authentication Flow:**
1. User authorizes app via Google OAuth
2. App receives refresh token
3. Refresh token stored securely
4. Token used to obtain access tokens for API calls

**Operations:**
- Create campaigns
- Update campaign settings
- Retrieve campaign metrics
- Manage ad groups and ads

## Security Architecture

### Authentication
- JWT tokens for API authentication
- Access tokens (short-lived, 30 minutes)
- Refresh tokens (long-lived, 7 days)
- Password hashing with bcrypt

### Authorization
- Role-based access control (User/Admin)
- Client isolation (users can only access their clients)
- Campaign isolation (users can only access their campaigns)

### Data Protection
- Environment variables for sensitive config
- Encrypted storage of API tokens
- HTTPS for all API communications
- CORS protection
- SQL injection prevention via ORM

## Deployment Architecture

### Backend
- Containerized with Docker
- Deployed to cloud platform (AWS, GCP, Azure)
- PostgreSQL managed database service
- Horizontal scaling via load balancer

### Frontend
- Static hosting (S3, Netlify, Vercel)
- CDN for fast content delivery
- Environment-based API URLs

### Mobile
- iOS App Store
- Google Play Store
- App-specific API endpoints

## Scalability Considerations

1. **Database**: Implement connection pooling, read replicas
2. **API**: Use async operations, caching with Redis
3. **File Storage**: Use S3 or similar for large files
4. **Analytics**: Consider separate analytics database
5. **Queuing**: Implement job queue for background tasks

## Monitoring & Logging

- Application logging (Python logging)
- Error tracking (Sentry)
- Performance monitoring (New Relic, Datadog)
- API analytics (custom logging)
- Database query monitoring
