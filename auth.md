# Authentication and Registration for RNMH Agents

Welcome! We support automated agents accessing our APIs.

## Registration

To register your agent, please contact `admin@rnmh.in` with your use case. We do not support Dynamic Client Registration (RFC 7591) at this time.

## Authentication

Once registered, you will be issued a Client ID and Client Secret. 
We support OAuth 2.0 `client_credentials` grant for machine-to-machine authentication.

See `/.well-known/oauth-authorization-server` for our OAuth endpoints.
