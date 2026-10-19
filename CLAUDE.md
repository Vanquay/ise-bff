# CLAUDE.md

**Status:** design phase. There is no application code yet; the repo holds architecture docs only.

- `README.md`: decisions so far, product scope, domain model, scheduling and double-booking design, payment flow, US/Canada specifics, launch cost floor, the code layout shared by all options, the API surface, later features, and items still to confirm.
- `docs/architecture/option-1-ecs-ec2-fastapi.md`: FastAPI on ECS with **EC2 capacity** (recommended).
- `docs/architecture/option-2-lambda-fastapi-mangum.md`: the same FastAPI app on Lambda via Mangum.
- `docs/architecture/option-3-lambda-powertools.md`: Lambda-native with Powertools; no FastAPI or Mangum.

Decisions the owner has made:

- Python on AWS. Containers run on **ECS with EC2 instances, not Fargate**.
- Market: US and Canada. Launch volume: ~100 bookings a day.
- Payment: the customer prepays, and the money is held and released to the mechanic on job completion. The flow is Stripe Connect with separate charges and transfers: authorise on request, capture on acceptance, transfer on release.
- Mechanics confirm every booking; there's no instant book in v1.
- Live tracking and chat are later features.

Not yet decided: which option to build, and the README's "Still to confirm" list (Stripe setup for Canada, sales tax, release and response windows, Quebec).

When code starts: business logic goes in `src/okada/modules/<module>/{service,repository,tables,schemas}.py` and must not import FastAPI, Powertools or boto3. Only `routes.py` and `src/okada/entrypoints/` are allowed to differ between options. Double-booking is enforced by the Postgres exclusion constraint on `allocation`. Keep it there, not in app code.
