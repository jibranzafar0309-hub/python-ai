# Project M1 Part 2: Sweet Crumbs Front Desk

## Intents

| Intent | Keywords | Reply |
|---|---|---|
| Complaint | refund, complaint, late | Sorry about that. A manager will call you within 1 hour. |
| Greeting | hi, hello, salam (starts with) | Hello! How can I help you? |
| Hours | hours, open, timing | We are open 9 am to 10 pm, every day. |
| Location | location, where, address of shop | We are in Gulberg, Lahore. |
| Delivery | delivery, deliver | Delivery is 200 PKR, free from 3,000 PKR. |
| Fees | fee, charge | Delivery fee is 200 PKR. Free from 3,000 PKR. |

## Business rules

| Rule | Value |
|---|---|
| Item prices | cupcake 250 PKR, brownie 300 PKR, chocolate cake 1,500 PKR |
| Bulk discount | 10% off for 10 or more items |
| Delivery | 200 PKR, free from 3,000 PKR |
| Private words | phone, cnic, my address |
## Rule tests

| You type | Expected | Pass? |
|---|---|---|
| ` WHAT are your hours ` | Hours reply (capitals and spaces handled) | Pass |
| `which cake is best?` | Fallback, not a greeting | Pass |
| `my order is late` | Manager reply (complaint first) | Pass |
| `/quote`, chocolate cake, 1 | Delivery fee charged (total 1,700) | Pass |
| `/quote`, chocolate cake, 3 | Delivery free (total 4,500) | Pass |
| `/quote`, brownie, 10 | Discount applied (total 2,900) | Pass |
| `/quote`, pizza, 2 | "Not on our menu", no crash | Pass |
| `can I change my phone number on the order?` | Local model, cost 0 | Pass |
| Press Enter with no text | Asks again | Pass |
| `BYE` | Goodbye + session report | Pass |
| `do you have chocolate cake?` | Fallback, not complaint ("late" hides in "chocolate") | Pass |