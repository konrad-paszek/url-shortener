# URL Shortener API



## Endpoints

**POST /api/url-shortener/** → Creates a short URL from a long one and returns the shortened version.

**GET /api/<short_hash>/** → Redirects to the original URL.

**GET /api/<short_hash>/?format=json** → Returns the original URL in JSON format.