# WinGo 30S Lottery Data Application

## Overview

This is a Flask-based web application that displays real-time lottery data from the WinGo 30S lottery system. The application fetches data from an external lottery API and presents it in a user-friendly interface, showing current period information, countdown timers, and historical results with color/number predictions.

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes

**December 5, 2025**: Added prediction feature for next period results
- Implemented prediction algorithm that analyzes last 20 draws for pattern detection
- Added "Prediction for Next Period" section showing guessed number, big/small, and color
- Displays confidence level based on pattern analysis
- Uses streak detection (3 consecutive same results triggers opposite prediction)
- Prioritizes "cold" numbers (less frequently appearing) in predictions

## System Architecture

### Frontend Architecture

**Technology Stack**: The frontend uses server-side rendered HTML templates with vanilla JavaScript for dynamic updates.

**Design Pattern**: Traditional MVC pattern where Flask handles routing and renders Jinja2 templates. Real-time updates are achieved through client-side AJAX polling.

**Rationale**: This approach was chosen for simplicity and ease of deployment on Replit. It avoids the complexity of a separate frontend framework while still providing real-time data updates. The gradient purple background and card-based UI provide a modern, lottery-themed aesthetic.

### Backend Architecture

**Framework**: Flask (Python web framework) serves as the lightweight backend.

**API Layer**: The application acts as a proxy/aggregator, fetching data from `https://draw.ar-lottery01.com` and transforming it for frontend consumption.

**Data Processing**: Helper functions (`get_color_list`, `get_big_small`) transform raw lottery numbers into human-readable predictions (colors like Green/Red/Violet, and Big/Small classifications based on number thresholds).

**Rationale**: Flask was chosen for its simplicity and minimal boilerplate. The single-file structure (`app.py`) keeps the codebase manageable for a simple data aggregation service.

### Data Storage Solutions

**Current Implementation**: No persistent data storage. The application operates statelessly, fetching fresh data from the external API on each request.

**Rationale**: Since the application displays real-time lottery data that changes every 30 seconds, there's no need for local persistence. All authoritative data lives in the external API.

**Future Consideration**: If analytics or historical tracking beyond what the API provides becomes necessary, a simple SQLite database or time-series database could be added.

### Authentication and Authorization

**Current Implementation**: No authentication system. The application is publicly accessible.

**Rationale**: This is a read-only data display application consuming public lottery information. No user accounts or protected resources exist.

### API Integration Strategy

**External API**: The application integrates with `https://draw.ar-lottery01.com/WinGo/WinGo_30S.json`

**Headers Configuration**: Custom headers mimic a mobile browser to ensure API compatibility, including User-Agent spoofing and CORS headers that indicate the request originates from `https://dkwin9.com`.

**Error Handling**: The `fetch_current_period()` function includes timeout protection (10 seconds) and exception handling to gracefully handle API failures.

**Data Freshness**: Timestamp parameter (`ts`) is appended to API requests to prevent caching and ensure fresh data.

**Rationale**: The lottery API appears to expect specific headers and referrer information. The current implementation mimics legitimate client behavior to maintain API access.

## External Dependencies

### Third-Party APIs

- **WinGo Lottery API** (`https://draw.ar-lottery01.com`): Primary data source for lottery periods, results, and timing information. Returns JSON data including current period, previous results, and next period details.

### Python Libraries

- **Flask**: Web framework for routing and template rendering
- **requests**: HTTP client for fetching data from external lottery API
- **time**: Standard library for timestamp generation and time calculations

### Frontend Dependencies

- **No external JavaScript libraries**: Uses vanilla JavaScript for AJAX calls and DOM manipulation
- **CSS**: Custom inline styles with gradient backgrounds (no frameworks like Bootstrap or Tailwind)

### Environment Requirements

- Python 3.x runtime
- Network access to external lottery API domain
- No database requirements