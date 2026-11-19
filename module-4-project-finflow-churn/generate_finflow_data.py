# Imports
from faker import Faker, VERSION
import random
import csv
from datetime import date, timedelta
from pathlib import Path

# Set seeds for reproducibility.
# The number 42 is conventional. Use the same value every time you want
# the same output. Change it if you want a different "random" run.

SEED = 42
Faker.seed(SEED)
random.seed(SEED)

# Pin the dataset to a fixed "as of" date.
AS_OF = date(2026, 10, 21)
SIGNUP_WINDOW_DAYS = 730
SIGNUP_WINDOW_START = AS_OF - timedelta(days=SIGNUP_WINDOW_DAYS)


# Initialize the Faker instance with US English locale.
# FinFlow's customer base is US-concentrated, so we want US-flavored names,
# addresses, and phone numbers.

fake = Faker('en_US')

print(f"Faker initialized with seed {SEED}") 
print(f"Test draw:{fake.name()}")

# A lookup from plan_tier to monthly_fee.
# These are the locked FinFlow pricing tiers from the kickoff call.abs

PLAN_FEES = {
    'Basic': 9.99,
    'Pro': 29.99,
    'Enterprise': 199.00
}

def build_one_customer_v2(index):
     """Build a single FinFlow customer record, version 2 with correlations.
    Args:
        index: integer counter used to generate sequential customer_id.
    Returns:
        Dictionary with all FinFlow customer fields populated.
    """
     first = fake.first_name()
     last = fake.last_name()
     signup_date = SIGNUP_WINDOW_START + timedelta(
         days = random.triangular(
             low= 0,
             high=SIGNUP_WINDOW_DAYS ,
             mode=SIGNUP_WINDOW_DAYS - 180))
    
      # plan_tier with realistic FinFlow distribution
     plan_tier = random.choices(
        ['Basic', 'Pro', 'Enterprise'],
        weights = [60,30,10],
        k=1)[0]
     monthly_fee = PLAN_FEES[plan_tier]
    
     # churn rate with correlate plan_tier
     churn_rates = {
        "Basic": 25,
        "Pro": 15,
        "Enterprise": 5
     }
     churn_rate = churn_rates[plan_tier]
     is_active = random.choices(
        [True, False],
         weights = [100 - churn_rate,churn_rate],
         k=1)[0]
        
    
      #last_login_date and churn_date depend on active state,
     # measured from the pinned as-of date rather than the clock
     today = AS_OF
     churn_date = None
    
     if is_active:
         # Active customers logged in within the last 30 days
         days_since_login = random.randint(0, 30)
         last_login = today - timedelta(days=days_since_login)
     else:
         # Churned customers haven't logged in for 30 to 180 days
         days_since_login = random.randint(30, 180)
         last_login = today - timedelta(days=days_since_login)

         # Churn date is between last_login and today
         days_since_churn = random.randint(0, days_since_login)
         churn_date = today - timedelta(days=days_since_churn)

     # Engagement metrics: correlate with active state
     if is_active:
         total_sessions = random.randint(20, 400)
         avg_session_duration = round(random.uniform(3.0, 15.0), 1)
         support_tickets = random.randint(0, 4)
     else:
         total_sessions = random.randint(1, 50)
         avg_session_duration = round(random.uniform(1.0, 6.0), 1)
         support_tickets = random.randint(0, 8)
         
     referral_source = random.choices(
         ["Organic Search", "Paid Search", "Social Media", "Word of Mouth", "Affiliate", "Direct"],
         weights = [45, 20, 15,10, 7, 3],
         k =1)[0]

     return {
         "customer_id": f"FF-{index:05d}",
         "first_name": first,
         "last_name": last,
         "email": f"{first.lower()}.{last.lower()}{index}@example.com",
         "city": fake.city(),
         "state": fake.state_abbr(),
         "country": "US",
         "signup_date": signup_date.isoformat(),
         "plan_tier": plan_tier,
         "monthly_fee": monthly_fee,
         "last_login_date": last_login.isoformat(),
         "total_sessions": total_sessions,
         "avg_session_duration_minutes": avg_session_duration,
         "support_tickets_opened": support_tickets,
         "active": is_active,
         "churn_date": churn_date.isoformat() if churn_date else None,
         "referral_source": referral_source
     }

     
  # Build and display a single record
sample = build_one_customer_v2(1)
for field, value in sample.items():
    print(f'{field}: {value}')

import time

# Re-seed so the run is reproducible from this point
Faker.seed(SEED)
random.seed(SEED)

# Generate 1,000 customers
start = time.time()
customers = [build_one_customer_v2(i) for i in range(1,1001)]
elapsed = time.time() - start

print(f'Built {len(customers)} customers in {elapsed:.2f} seconds')
print()
print("First customer:")
for field, value in customers[0].items():
    print(f'{field}: {value}')
print("Last customer:")
for field, value in customers[-1].items():
    print(f'{field}: {value}')

# Plan tier distribution
plan_counts = {}
for c in customers:
    tier = c["plan_tier"]
    plan_counts[tier] = plan_counts.get(tier, 0) + 1

print("Plan tier distribution (expected: ~60/30/10):")
for tier in ['Basic', 'Pro', 'Enterprise']:
    count = plan_counts.get(tier, 0)
    pct = count / len(customers) * 100
    print(f"  {tier}: {count} ({pct:.1f}%)")

# Churn rate for each plan separately
for plan in ["Basic", "Pro", "Enterprise"]:
    plan_customers = [c for c in customers if c["plan_tier"] == plan]

    churned = sum(1 for c in plan_customers if not c["active"])
    churn_rate = churned / len(plan_customers) * 100

    print(f"\n{plan} churn rate (expected: ~{ {'Basic': 25, 'Pro': 15, 'Enterprise': 5}[plan] }%): {churn_rate:.1f}%")

# Monthly fee total
total_mrr = sum(c["monthly_fee"] for c in customers if c["active"])
print(f"\nMonthly recurring revenue from active customers: ${total_mrr:,.2f}")

# Signup date range
signup_dates = [c["signup_date"] for c in customers]
print(f"\nSignup date range: {min(signup_dates)} to {max(signup_dates)}")

# sign up date distribution 
last_12_months = 0
older_12_to_24_months = 0

for c in customers:
    signup = date.fromisoformat(c["signup_date"])

    if date(2025, 10, 21) <= signup <= AS_OF:
        last_12_months += 1
    else:
        older_12_to_24_months += 1
total = len(customers)
print("\nSign up date distribution")
print("Last 12 months:", f"{last_12_months / total:.1%}")
print("12–24 months ago:", f"{older_12_to_24_months / total:.1%}")

#Referral source distribution 
print("\nReferral source distribution (expected: ~45/20/15/10/7/3):")
from collections import Counter

referral_counts = Counter(
    customer["referral_source"] for customer in customers
)
for source, count in referral_counts.items():
    percentage = (count / len(customers)) * 100
   
    print(f"{source}: {count} customers ({percentage:.1f}%)")

# Define the output path. Path() handles Mac/Windows path differences cleanly.
output_path = Path("finflow-customers-1000-extended.csv")

# Get the field names from the first record (Python 3.7+ dicts preserve order)
field_names = list(customers[0].keys())

# Write the CSV
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(customers)

# Verify
print(f"Wrote {len(customers)} customers to {output_path.resolve()}")
print(f"File size: {output_path.stat().st_size:,} bytes")