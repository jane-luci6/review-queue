# Testing Patterns

## Testing Pyramid

```
        /\
       /  \      E2E Tests (few)
      /----\
     /      \    Integration Tests (some)
    /--------\
   /          \  Unit Tests (many)
  /------------\
```

## Unit Testing

### Structure: Arrange-Act-Assert
```
// Arrange: Set up test data and conditions
// Act: Execute the code under test
// Assert: Verify the expected outcome
```

### Naming Convention
```
test_[unit]_[scenario]_[expected_result]
should_[expected_behavior]_when_[condition]
```

### Best Practices
- Test one behavior per test
- Use descriptive test names
- Avoid testing implementation details
- Keep tests independent and isolated
- Use factories/fixtures for test data

## Integration Testing

### Database Tests
- Use transactions with rollback
- Seed known test data
- Test actual queries, not mocks
- Clean up after each test

### API Tests
- Test full request/response cycle
- Verify status codes and headers
- Test authentication flows
- Test error responses

## Mocking Guidelines

### When to Mock
- External services (APIs, databases)
- Time-dependent operations
- Random/non-deterministic behavior
- Slow operations (network, filesystem)

### When NOT to Mock
- The code under test
- Simple data structures
- Internal collaborators (usually)

## Test Data Management

### Factories
- Create minimal valid objects
- Allow overriding specific fields
- Use realistic but deterministic data

### Fixtures
- Use for complex, reusable scenarios
- Keep fixtures close to tests
- Document fixture purposes

## Code Coverage

### Meaningful Metrics
- Focus on critical path coverage
- Don't chase 100% blindly
- Cover edge cases and error paths
- Branch coverage over line coverage

### Coverage Targets
- Unit tests: 80%+ of business logic
- Integration: Key user flows
- E2E: Critical happy paths

## Test Organization

```
tests/
├── unit/
│   ├── services/
│   └── utils/
├── integration/
│   ├── api/
│   └── database/
├── e2e/
│   └── flows/
├── fixtures/
└── helpers/
```

## Performance Testing

- Establish baseline metrics
- Test under expected load
- Test failure scenarios
- Monitor resource usage

## Continuous Integration

- Run tests on every commit
- Fail fast with parallel execution
- Cache dependencies
- Report coverage trends
