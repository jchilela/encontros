-- Schema lógico simplificado, alinhado ao backend Django.

CREATE TABLE users_user (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  username VARCHAR(150) UNIQUE NOT NULL,
  first_name VARCHAR(150),
  last_name VARCHAR(150),
  password VARCHAR(255) NOT NULL,
  phone VARCHAR(32),
  role VARCHAR(32) NOT NULL DEFAULT 'member',
  is_email_verified BOOLEAN NOT NULL DEFAULT FALSE,
  is_identity_verified BOOLEAN NOT NULL DEFAULT FALSE,
  preferred_currency VARCHAR(8) NOT NULL DEFAULT 'EUR',
  timezone VARCHAR(64) NOT NULL DEFAULT 'Europe/Lisbon',
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

CREATE TABLE users_profile (
  id UUID PRIMARY KEY,
  user_id UUID UNIQUE NOT NULL REFERENCES users_user(id),
  avatar_url VARCHAR(500),
  bio TEXT,
  city VARCHAR(120),
  language_code VARCHAR(12) DEFAULT 'pt',
  interests JSONB DEFAULT '[]'::jsonb,
  privacy_level VARCHAR(32) DEFAULT 'public'
);

CREATE TABLE taxonomy_category (
  id UUID PRIMARY KEY,
  name VARCHAR(120) UNIQUE NOT NULL,
  slug VARCHAR(140) UNIQUE NOT NULL,
  icon VARCHAR(80),
  is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE taxonomy_city (
  id UUID PRIMARY KEY,
  country_code VARCHAR(8) NOT NULL,
  region VARCHAR(120),
  name VARCHAR(120) NOT NULL,
  slug VARCHAR(140) UNIQUE NOT NULL,
  latitude NUMERIC(9,6),
  longitude NUMERIC(9,6)
);

CREATE TABLE communities_group (
  id UUID PRIMARY KEY,
  owner_id UUID NOT NULL REFERENCES users_user(id),
  category_id UUID REFERENCES taxonomy_category(id),
  city_id UUID REFERENCES taxonomy_city(id),
  name VARCHAR(180) NOT NULL,
  slug VARCHAR(220) UNIQUE NOT NULL,
  description TEXT,
  visibility VARCHAR(32) DEFAULT 'public',
  access_rule VARCHAR(32) DEFAULT 'open',
  required_plan VARCHAR(32) DEFAULT 'none',
  rules TEXT,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

CREATE TABLE communities_group_membership (
  id UUID PRIMARY KEY,
  group_id UUID NOT NULL REFERENCES communities_group(id),
  user_id UUID NOT NULL REFERENCES users_user(id),
  role VARCHAR(32) DEFAULT 'member',
  status VARCHAR(32) DEFAULT 'active',
  joined_at TIMESTAMP NOT NULL,
  UNIQUE (group_id, user_id)
);

CREATE TABLE events_event (
  id UUID PRIMARY KEY,
  organizer_id UUID NOT NULL REFERENCES users_user(id),
  group_id UUID REFERENCES communities_group(id),
  category_id UUID REFERENCES taxonomy_category(id),
  city_id UUID REFERENCES taxonomy_city(id),
  title VARCHAR(220) NOT NULL,
  slug VARCHAR(260) UNIQUE NOT NULL,
  summary VARCHAR(280),
  description TEXT,
  event_format VARCHAR(32) NOT NULL,
  visibility VARCHAR(32) NOT NULL DEFAULT 'public',
  required_plan VARCHAR(32) DEFAULT 'none',
  starts_at TIMESTAMP NOT NULL,
  ends_at TIMESTAMP NOT NULL,
  timezone VARCHAR(64) NOT NULL,
  venue_name VARCHAR(180),
  address_line VARCHAR(255),
  latitude NUMERIC(9,6),
  longitude NUMERIC(9,6),
  online_url VARCHAR(500),
  capacity INTEGER,
  waitlist_enabled BOOLEAN DEFAULT TRUE,
  base_currency VARCHAR(8) NOT NULL DEFAULT 'EUR',
  status VARCHAR(32) DEFAULT 'draft',
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

CREATE TABLE events_rsvp (
  id UUID PRIMARY KEY,
  event_id UUID NOT NULL REFERENCES events_event(id),
  user_id UUID NOT NULL REFERENCES users_user(id),
  status VARCHAR(32) NOT NULL,
  checked_in_at TIMESTAMP,
  created_at TIMESTAMP NOT NULL,
  UNIQUE (event_id, user_id)
);

CREATE TABLE events_waitlist_entry (
  id UUID PRIMARY KEY,
  event_id UUID NOT NULL REFERENCES events_event(id),
  user_id UUID NOT NULL REFERENCES users_user(id),
  priority_score INTEGER NOT NULL DEFAULT 0,
  promoted_at TIMESTAMP,
  created_at TIMESTAMP NOT NULL,
  UNIQUE (event_id, user_id)
);

CREATE TABLE tickets_ticket_tier (
  id UUID PRIMARY KEY,
  event_id UUID NOT NULL REFERENCES events_event(id),
  name VARCHAR(140) NOT NULL,
  tier_type VARCHAR(32) NOT NULL,
  description TEXT,
  price NUMERIC(12,2) NOT NULL,
  currency VARCHAR(8) NOT NULL,
  quantity_total INTEGER,
  quantity_sold INTEGER NOT NULL DEFAULT 0,
  sale_starts_at TIMESTAMP,
  sale_ends_at TIMESTAMP,
  min_plan VARCHAR(32) DEFAULT 'none',
  is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE tickets_order (
  id UUID PRIMARY KEY,
  number VARCHAR(32) UNIQUE NOT NULL,
  buyer_id UUID NOT NULL REFERENCES users_user(id),
  event_id UUID REFERENCES events_event(id),
  order_type VARCHAR(32) NOT NULL,
  status VARCHAR(32) NOT NULL,
  subtotal NUMERIC(12,2) NOT NULL,
  discount_total NUMERIC(12,2) NOT NULL DEFAULT 0,
  fee_total NUMERIC(12,2) NOT NULL DEFAULT 0,
  total NUMERIC(12,2) NOT NULL,
  currency VARCHAR(8) NOT NULL,
  coupon_code VARCHAR(64),
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

CREATE TABLE tickets_order_item (
  id UUID PRIMARY KEY,
  order_id UUID NOT NULL REFERENCES tickets_order(id),
  ticket_tier_id UUID REFERENCES tickets_ticket_tier(id),
  description VARCHAR(255) NOT NULL,
  quantity INTEGER NOT NULL,
  unit_price NUMERIC(12,2) NOT NULL,
  discount_amount NUMERIC(12,2) NOT NULL DEFAULT 0,
  total_amount NUMERIC(12,2) NOT NULL
);

CREATE TABLE subscriptions_membership_plan (
  id UUID PRIMARY KEY,
  code VARCHAR(32) UNIQUE NOT NULL,
  name VARCHAR(120) NOT NULL,
  description TEXT,
  tier_rank INTEGER NOT NULL,
  is_free BOOLEAN DEFAULT FALSE,
  is_active BOOLEAN DEFAULT TRUE,
  features JSONB NOT NULL DEFAULT '[]'::jsonb,
  limits JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE subscriptions_plan_price (
  id UUID PRIMARY KEY,
  plan_id UUID NOT NULL REFERENCES subscriptions_membership_plan(id),
  billing_cycle VARCHAR(32) NOT NULL,
  currency VARCHAR(8) NOT NULL,
  amount NUMERIC(12,2) NOT NULL,
  trial_days INTEGER DEFAULT 0,
  UNIQUE (plan_id, billing_cycle, currency)
);

CREATE TABLE subscriptions_user_subscription (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users_user(id),
  plan_id UUID NOT NULL REFERENCES subscriptions_membership_plan(id),
  billing_cycle VARCHAR(32) NOT NULL,
  currency VARCHAR(8) NOT NULL,
  status VARCHAR(32) NOT NULL,
  auto_renew BOOLEAN DEFAULT TRUE,
  started_at TIMESTAMP NOT NULL,
  current_period_end TIMESTAMP NOT NULL,
  cancel_at_period_end BOOLEAN DEFAULT FALSE,
  scheduled_plan_id UUID REFERENCES subscriptions_membership_plan(id),
  external_reference VARCHAR(120)
);

CREATE TABLE payments_payment_transaction (
  id UUID PRIMARY KEY,
  order_id UUID REFERENCES tickets_order(id),
  subscription_id UUID REFERENCES subscriptions_user_subscription(id),
  provider VARCHAR(32) NOT NULL,
  external_reference VARCHAR(120),
  provider_reference VARCHAR(120),
  status VARCHAR(32) NOT NULL,
  amount NUMERIC(12,2) NOT NULL,
  currency VARCHAR(8) NOT NULL,
  metadata JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

CREATE TABLE messaging_conversation (
  id UUID PRIMARY KEY,
  kind VARCHAR(32) NOT NULL,
  subject VARCHAR(180),
  created_at TIMESTAMP NOT NULL
);

CREATE TABLE messaging_message (
  id UUID PRIMARY KEY,
  conversation_id UUID NOT NULL REFERENCES messaging_conversation(id),
  sender_id UUID NOT NULL REFERENCES users_user(id),
  body TEXT NOT NULL,
  is_system BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL
);

CREATE TABLE notifications_notification (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users_user(id),
  channel VARCHAR(32) NOT NULL,
  kind VARCHAR(64) NOT NULL,
  title VARCHAR(180) NOT NULL,
  body TEXT,
  is_read BOOLEAN DEFAULT FALSE,
  payload JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMP NOT NULL
);

CREATE TABLE moderation_report (
  id UUID PRIMARY KEY,
  reporter_id UUID NOT NULL REFERENCES users_user(id),
  target_type VARCHAR(32) NOT NULL,
  target_id UUID NOT NULL,
  reason VARCHAR(120) NOT NULL,
  details TEXT,
  status VARCHAR(32) DEFAULT 'pending',
  created_at TIMESTAMP NOT NULL
);

CREATE TABLE moderation_audit_log (
  id UUID PRIMARY KEY,
  actor_id UUID REFERENCES users_user(id),
  action VARCHAR(120) NOT NULL,
  resource_type VARCHAR(64),
  resource_id UUID,
  metadata JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMP NOT NULL
);
