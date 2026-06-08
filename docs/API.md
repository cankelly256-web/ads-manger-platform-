# API Documentation

## Base URL

```
http://localhost:8000/api
```

## Authentication

All protected endpoints require a Bearer token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## Endpoints

### Authentication

#### Register User

```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "username",
  "password": "password123",
  "full_name": "John Doe"
}

Response 200:
{
  "id": "uuid",
  "email": "user@example.com",
  "username": "username",
  "full_name": "John Doe",
  "is_active": true,
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### Login User

```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}

Response 200:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

### Clients

#### List Clients

```http
GET /clients?skip=0&limit=100
Authorization: Bearer <access_token>

Response 200:
[
  {
    "id": "uuid",
    "name": "Client Name",
    "email": "client@example.com",
    "company_name": "Company",
    "phone": "+1234567890",
    "description": "Client description",
    "is_active": true,
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
]
```

#### Create Client

```http
POST /clients
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "name": "Client Name",
  "email": "client@example.com",
  "company_name": "Company",
  "phone": "+1234567890",
  "description": "Client description"
}

Response 201:
{
  "id": "uuid",
  "name": "Client Name",
  "email": "client@example.com",
  "company_name": "Company",
  "phone": "+1234567890",
  "description": "Client description",
  "is_active": true,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### Get Client

```http
GET /clients/{client_id}
Authorization: Bearer <access_token>

Response 200:
{
  "id": "uuid",
  "name": "Client Name",
  "email": "client@example.com",
  "company_name": "Company",
  "phone": "+1234567890",
  "description": "Client description",
  "is_active": true,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### Update Client

```http
PUT /clients/{client_id}
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "name": "Updated Client Name",
  "email": "updated@example.com"
}

Response 200:
{
  "id": "uuid",
  "name": "Updated Client Name",
  "email": "updated@example.com",
  "company_name": "Company",
  "phone": "+1234567890",
  "description": "Client description",
  "is_active": true,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### Delete Client

```http
DELETE /clients/{client_id}
Authorization: Bearer <access_token>

Response 200:
{
  "message": "Client deleted successfully"
}
```

### Campaigns

#### List Campaigns

```http
GET /campaigns?skip=0&limit=100
Authorization: Bearer <access_token>

Response 200:
[
  {
    "id": "uuid",
    "client_id": "uuid",
    "name": "Campaign Name",
    "description": "Campaign description",
    "platform": "meta",
    "status": "active",
    "budget": 1000.00,
    "daily_budget": 50.00,
    "start_date": "2024-01-01T00:00:00Z",
    "end_date": "2024-12-31T00:00:00Z",
    "objective": "conversions",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
]
```

#### Create Campaign

```http
POST /campaigns
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "client_id": "uuid",
  "name": "Campaign Name",
  "description": "Campaign description",
  "platform": "meta",
  "budget": 1000.00,
  "daily_budget": 50.00,
  "start_date": "2024-01-01T00:00:00Z",
  "end_date": "2024-12-31T00:00:00Z",
  "objective": "conversions",
  "audience_targeting": "{\"age\": \"18-65\"}"
}

Response 201:
{
  "id": "uuid",
  "client_id": "uuid",
  "name": "Campaign Name",
  "description": "Campaign description",
  "platform": "meta",
  "status": "draft",
  "budget": 1000.00,
  "daily_budget": 50.00,
  "start_date": "2024-01-01T00:00:00Z",
  "end_date": "2024-12-31T00:00:00Z",
  "objective": "conversions",
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

### Analytics

#### Get Campaign Analytics

```http
GET /analytics/campaigns/{campaign_id}
Authorization: Bearer <access_token>

Response 200:
{
  "campaign_id": "uuid",
  "campaign_name": "Campaign Name",
  "data": [
    {
      "date": "2024-01-01T00:00:00Z",
      "platform": "meta",
      "impressions": 10000,
      "clicks": 500,
      "conversions": 50,
      "spend": 250.00,
      "ctr": 5.0,
      "cpc": 0.50,
      "cpa": 5.00,
      "roas": 4.0
    }
  ]
}
```

#### Get Dashboard Overview

```http
GET /analytics/dashboard
Authorization: Bearer <access_token>

Response 200:
{
  "total_spend": 10000.00,
  "total_impressions": 500000,
  "total_clicks": 25000,
  "total_conversions": 2500,
  "average_ctr": 5.0
}
```

## Error Responses

### 400 Bad Request

```json
{
  "detail": "Invalid request parameters"
}
```

### 401 Unauthorized

```json
{
  "detail": "Not authenticated"
}
```

### 404 Not Found

```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error

```json
{
  "detail": "Internal server error"
}
```