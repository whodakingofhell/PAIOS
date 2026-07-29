---
tags:
  - paios/knowledge
  - paios/software-development
  - paios/api
related:
  - "04-Engineering.md"
  - "Backend.md"
  - "Database.md"
  - "../DevOps/CI-CD-Pipeline.md"
  - "../Architecture/03-Architecture.md"
---

# API Design

## Design Principles
- Consistency: naming conventions, error format, pagination style
- Statelessness: each request has all info needed (REST constraint)
- Resource-orientation: endpoints map to nouns, not verbs
- Versioning: URL prefix (/v1/, /v2/) or header (Accept: version=2)
- Backward compatibility: additive changes preferred; breaking = new version

## REST Conventions
- GET /resources — list (with pagination, filtering, sorting)
- GET /resources/:id — read one
- POST /resources — create
- PATCH /resources/:id — partial update
- DELETE /resources/:id — delete
- Nested: GET /resources/:id/subresources
- Response envelope: { data, error, meta (pagination) }

## GraphQL (when appropriate)
- Single endpoint, client-driven queries
- Great for complex/nested data requirements
- Requires careful N+1 prevention (DataLoader pattern)
- Authentication and authorization at resolver level
- Schema-first development with Apollo or Relay

## Security
- Authentication: JWT, OAuth2, API keys
- Authorization: per-endpoint role/permission checks
- Rate limiting: per-IP, per-user, per-endpoint tiers
- Input validation: schema validation (JSON Schema, Zod, Pydantic)
- Output sanitization: no sensitive fields in responses
- CORS: restrict to known origins
- HTTPS only, HSTS headers

## Documentation
- OpenAPI/Swagger for REST
- GraphQL introspection + Apollo Studio
- Include: auth method, rate limits, error codes, examples (curl or SDK)

## Error Handling
- Consistent error shape: { error: { code, message, details } }
- Appropriate HTTP status codes (400, 401, 403, 404, 409, 422, 429, 500)
- Meaningful messages (not "An error occurred")

## Pagination
- Cursor-based preferred for real-time/large datasets
- Offset-based acceptable for small/stable datasets
- Always include total count or next cursor
