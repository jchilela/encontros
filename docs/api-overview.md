# API overview

Base URL: `/api/v1/`

## Auth
- `POST /auth/register/`
- `POST /auth/login/`
- `POST /auth/logout/`
- `POST /auth/refresh/`
- `POST /auth/password/forgot/`
- `POST /auth/password/reset/`
- `POST /auth/email/verify/`
- `GET /auth/me/`

## Users
- `GET /users/profile/`
- `PATCH /users/profile/`
- `GET /users/favorites/events/`
- `POST /users/favorites/events/{id}/toggle/`
- `GET /users/payment-methods/`

## Events
- `GET /events/`
- `POST /events/`
- `GET /events/{slug}/`
- `PATCH /events/{slug}/`
- `POST /events/{slug}/publish/`
- `POST /events/{slug}/cancel/`
- `GET /events/{slug}/faqs/`
- `POST /events/{slug}/rsvp/`
- `DELETE /events/{slug}/rsvp/`
- `POST /events/{slug}/waitlist/leave/`
- `POST /events/{slug}/check-in/`
- `GET /events/{slug}/participants/`

## Communities
- `GET /groups/`
- `POST /groups/`
- `GET /groups/{slug}/`
- `PATCH /groups/{slug}/`
- `POST /groups/{slug}/join/`
- `POST /groups/{slug}/approve-member/`
- `POST /groups/{slug}/remove-member/`

## Tickets & Checkout
- `GET /ticket-tiers/`
- `POST /checkout/quote/`
- `POST /checkout/confirm/`
- `GET /orders/`
- `GET /orders/{number}/`
- `POST /orders/{number}/refund-request/`

## Subscriptions
- `GET /plans/`
- `POST /subscriptions/subscribe/`
- `POST /subscriptions/upgrade/`
- `POST /subscriptions/downgrade/`
- `POST /subscriptions/cancel-renewal/`
- `GET /subscriptions/current/`
- `GET /subscriptions/invoices/`

## Payments
- `POST /payments/stripe/webhook/`
- `POST /payments/paypal/webhook/`
- `POST /payments/proprietary/reference/`
- `POST /payments/proprietary/callback/`

## Messaging
- `GET /conversations/`
- `POST /conversations/`
- `GET /conversations/{id}/messages/`
- `POST /conversations/{id}/messages/`

## Notifications
- `GET /notifications/`
- `POST /notifications/mark-read/`
- `GET /notification-preferences/`
- `PATCH /notification-preferences/`

## Moderation
- `POST /reports/`
- `GET /admin/reports/`
- `POST /admin/reports/{id}/resolve/`

## Dashboards
- `GET /dashboards/member/`
- `GET /dashboards/organizer/`
- `GET /dashboards/admin/`
