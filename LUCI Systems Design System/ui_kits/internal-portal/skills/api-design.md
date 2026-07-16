# API Design Patterns

## REST API Conventions

### URL Structure
```
GET    /resources          # List resources
GET    /resources/:id      # Get single resource
POST   /resources          # Create resource
PUT    /resources/:id      # Update resource (full)
PATCH  /resources/:id      # Update resource (partial)
DELETE /resources/:id      # Delete resource
```

### Naming Guidelines
- Use plural nouns for resources: `/users`, `/orders`
- Use kebab-case for multi-word: `/user-profiles`
- Nest related resources: `/users/:id/orders`
- Keep URLs shallow (max 2-3 levels deep)

### Query Parameters
- Pagination: `?page=1&limit=20` or `?offset=0&limit=20`
- Filtering: `?status=active&category=tech`
- Sorting: `?sort=created_at&order=desc`
- Field selection: `?fields=id,name,email`

## Response Formats

### Success Response
```json
{
  "data": { ... },
  "meta": {
    "page": 1,
    "total": 100
  }
}
```

### Error Response
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable message",
    "details": [
      { "field": "email", "message": "Invalid email format" }
    ]
  }
}
```

## HTTP Status Codes

| Code | Usage |
|------|-------|
| 200 | Success (GET, PUT, PATCH) |
| 201 | Created (POST) |
| 204 | No Content (DELETE) |
| 400 | Bad Request (validation errors) |
| 401 | Unauthorized (missing/invalid auth) |
| 403 | Forbidden (insufficient permissions) |
| 404 | Not Found |
| 409 | Conflict (duplicate, state conflict) |
| 422 | Unprocessable Entity (semantic errors) |
| 500 | Internal Server Error |

## Authentication & Authorization

### Token-Based Auth
- Use Bearer tokens in Authorization header
- Implement token refresh mechanism
- Store tokens securely (httpOnly cookies or secure storage)

### API Keys
- Use for server-to-server communication
- Pass in header: `X-API-Key: <key>`
- Implement rate limiting per key

## Versioning Strategies

1. **URL Path**: `/v1/resources` (most common)
2. **Header**: `Accept: application/vnd.api.v1+json`
3. **Query**: `?version=1` (least preferred)

## Rate Limiting

Include headers in responses:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640000000
```

## Best Practices

- Use consistent casing throughout
- Provide meaningful error messages
- Document all endpoints with examples
- Implement proper CORS for web clients
- Use HTTPS exclusively in production
- Log requests with correlation IDs
