# Code Style Guide

## TypeScript

- Always use explicit return types on exported functions
- Prefer `interface` over `type` for object shapes
- Use `unknown` instead of `any` when the type is truly unknown

## React

- Components must be functional (no class components)
- Use hooks for state and side effects
- Always provide `key` props in list renders

## Testing

- Test file naming: `*.test.ts` or `*.test.tsx`
- Use descriptive test names that explain the behavior
- Aim for meaningful assertions, not just "no error"
