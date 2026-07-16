# Docker Workflows

## Dockerfile Best Practices

### Multi-Stage Builds
```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Layer Optimization
- Order commands from least to most frequently changing
- Combine RUN commands to reduce layers
- Use `.dockerignore` to exclude unnecessary files
- Copy dependency files before source code

### Security
- Use non-root users
- Scan images for vulnerabilities
- Use specific version tags, not `latest`
- Minimize installed packages

## Docker Compose

### Development Environment
```yaml
version: '3.8'
services:
  app:
    build:
      context: .
      target: development
    volumes:
      - .:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
    depends_on:
      - db
      
  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=app_dev
      - POSTGRES_USER=dev
      - POSTGRES_PASSWORD=dev_password

volumes:
  postgres_data:
```

### Production Considerations
- Use secrets management for credentials
- Configure health checks
- Set resource limits
- Use restart policies

## Common Commands

### Build & Run
```bash
# Build image
docker build -t app:latest .

# Build with specific target
docker build --target production -t app:prod .

# Run container
docker run -d -p 3000:3000 --name app app:latest

# Run with environment file
docker run --env-file .env app:latest
```

### Compose Operations
```bash
# Start services
docker-compose up -d

# Rebuild and start
docker-compose up -d --build

# View logs
docker-compose logs -f [service]

# Stop and remove
docker-compose down

# Stop and remove with volumes
docker-compose down -v
```

### Debugging
```bash
# Execute command in running container
docker exec -it <container> sh

# View container logs
docker logs -f <container>

# Inspect container
docker inspect <container>

# Check resource usage
docker stats
```

## Volume Management

### Development Volumes
- Mount source code for hot reload
- Exclude node_modules via anonymous volume
- Use named volumes for data persistence

### Production Volumes
- Use named volumes for persistent data
- Backup strategies for critical data
- Consider external volume drivers

## Networking

### Service Discovery
- Services can reference each other by name
- Use internal networks for security
- Expose only necessary ports

### Network Modes
```yaml
networks:
  frontend:
  backend:
    internal: true  # No external access
```

## Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1
```

## CI/CD Integration

### Build Pipeline
1. Build image with commit SHA tag
2. Run tests in container
3. Push to registry
4. Deploy to environment

### Image Tagging Strategy
```bash
# Commit-based
app:abc1234

# Environment-based  
app:staging
app:production

# Semantic versioning
app:1.2.3
app:1.2
app:1
```
