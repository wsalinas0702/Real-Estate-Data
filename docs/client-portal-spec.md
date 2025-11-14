# Client Discovery Portal Product Spec

## 1. Vision
Create a Zillow-style discovery experience tailored for agents and clients in Pennsylvania, New Jersey, and Puerto Rico. Anyone can explore listings without an account, while agents can curate client preference profiles that power AI-assisted recommendations and collaborative search.

## 2. Primary Personas
- **Browsing Visitor:** Unauthenticated users exploring inventory by location and property style.
- **Client:** Registered user with saved preferences, mood boards, and collaboration tools.
- **Agent:** Professional who curates client profiles, shares recommendations, and manages engagements.
- **Administrator:** Oversees data ingestion, system settings, and content moderation.

## 3. Initial User Journeys
1. **Open Browse:** Visitor lands on the home page, enters a county/address, selects preferred property style, and instantly sees matching listings.
2. **Preference Setup:** Agent creates or updates a client profile with bullet-style preference tags (style, exterior color, interior vibe, amenities, pet policy, HOA status).
3. **Quick Match:** Agent picks a client and views listings ranked by match score, with explanations highlighting satisfied preferences.
4. **Feedback Loop:** Client reacts to shared listings (thumbs up/down, optional comments), powering the preference engine and generating shareable Google review prompts.
5. **AI Concierge:** User opens the embedded chatbot to clarify filters, ask about amenities, or request similar homes.

## 4. Feature Breakdown
### 4.1 Browsing & Search
- Location search by address, city, or county (initial focus: PA, NJ, PR).
- Style filters (modern, colonial, condo, waterfront, etc.).
- Expanded filters: color palette, interior style, amenities (pool, deck, solar, pet-friendly), HOA acceptance, smart home tech.
- Quick toggle for pets allowed and HOA restrictions.
- Map view with clustering and listing cards showing key attributes.

### 4.2 Client Preference Profiles
- Bullet list of preference tags grouped by category (Style, Exterior, Interior, Amenities, Neighborhood, HOA).
- Weighting model with default emphasis; adjust automatically based on feedback trends.
- Match score calculation with explanation of satisfied/unsatisfied tags.

### 4.3 Collaboration & Feedback
- Shareable collections of listings curated by agents.
- Client reactions (thumbs up/down, optional note) stored per property.
- Automatic Google review CTA once milestones (tour scheduled, offer made) are achieved.
- Mood board upload (stretch goal).

### 4.4 AI Assistance
- Embedded chat widget for filter help, property questions, and onboarding guidance.
- Uses OpenAI function calling to trigger property search, preference updates, and scheduling.

### 4.5 Authentication & Accounts
- Optional browsing without login.
- Account creation via email or OAuth (Google) for clients/agents.
- Role-based dashboard routing.

## 5. Data & Integrations
- **Listings:** Seed with sample datasets; plan ATTOM API integration for production inventory.
- **Embeddings:** Use Pinecone (or pgvector) to store listing embeddings for stylistic similarity.
- **External Reviews:** Integrate Google Business review link generation.
- **Future**: integrate calendar APIs for tour scheduling.

## 6. Technical Architecture
- **Frontend:** React + TypeScript (Vite) with TailwindCSS for rapid UI and responsive design.
- **Backend:** Node.js (NestJS or Express + TypeScript). Provides REST/GraphQL endpoints for listings, clients, preferences, and AI hooks.
- **Database:** PostgreSQL with Prisma ORM. Includes pgvector for semantic search proofs.
- **Search Layer:** Elasticsearch or Postgres full-text for location queries; Pinecone for similarity search (later phase).
- **Hosting:** Vercel/Netlify for frontend, Render/Fly.io for backend, Supabase/Railway for Postgres (TBD).

## 7. Data Model (Initial Draft)
### Listings
- id, mls_id, address, city, county, state, zip
- geo_lat, geo_lng
- price, beds, baths, sqft, lot_size, year_built
- property_style, exterior_color, interior_style
- amenities (JSON array: pool, deck, fireplace, etc.)
- hoa_required (boolean), hoa_details (text)
- pet_policy (enum: allowed, restricted, not_allowed)
- media_urls (JSON array)
- description, neighborhood_highlights

### Clients
- id, name, email, phone
- role (client/agent)
- agency (for agents)
- preference_profile_id (FK)

### Preference Profiles
- id, client_id, tags (JSON grouped by category)
- weighting (JSON map of tag -> weight)
- notes
- updated_at

### Feedback
- id, client_id, listing_id
- reaction (like/dislike)
- comment
- created_at

### Sessions & Reviews
- id, client_id, stage (tour_scheduled, offer_made, closed)
- google_review_url
- sent_at

## 8. Screen Inventory (MVP)
1. **Landing/Search Screen**
   - Hero search with address/county input
   - Quick style filter chips
   - CTA for “Sign Up / Log In”
   - Carousel of featured markets (PA, NJ, PR)
2. **Search Results**
   - Map + list layout
   - Filter drawer (style, color, interior, amenities, pets, HOA)
   - Sorting by price, match score, newest
3. **Listing Detail**
   - Gallery, highlights, match reason explanation
   - Agent notes, neighborhood insights, similar listings
4. **Client Dashboard**
   - Preference summary chips
   - Suggested listings
   - Feedback history and review CTA
5. **Agent Workspace**
   - Client selector
   - Preference editing form
   - AI assistant sidebar

## 9. Roadmap
1. **MVP (4–6 weeks)**
   - Landing/search screen with static dataset
   - User accounts (Supabase Auth or Auth0)
   - Client/agent dashboards with preference tagging
   - Basic matching algorithm with weights
   - AI chatbot MVP (FAQ + filter guidance)
2. **Phase 2**
   - Integrate real API data (ATTOM)
   - Vector search via Pinecone
   - Mood boards & collaboration timeline
   - Automated review request workflow
3. **Phase 3**
   - Advanced analytics (heatmaps, affordability calculators)
   - 3D tours and AR overlays
   - Calendar integrations

## 10. Open Questions
- Finalize branding guidelines and color palette.
- Confirm hosting preferences (self-managed vs managed services).
- Determine chatbot tone and knowledge base source.
- Collect sample datasets for target markets.

