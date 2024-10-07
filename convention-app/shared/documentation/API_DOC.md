# API Documentation

## Overview

This document outlines the API endpoints for the Convention App.

### Authentication

- **POST** `/api/auth/register`
  - **Request**: `{ "email": "user@example.com", "password": "yourpassword" }`
  - **Response**: `{ "message": "User created successfully." }`

- **POST** `/api/auth/login`
  - **Request**: `{ "email": "user@example.com", "password": "yourpassword" }`
  - **Response**: `{ "message": "Login successful" }`

### Events

- **GET** `/api/events`
  - **Response**: `[{ "id": 1, "name": "Event Name", ... }]`