# Week 5 Update: Redux Toolkit Complete, All Modules Complete

**Week:** 5 (planned 3 to 9 Aug 2026)
**Focus:** wrap-up of the frontend: Redux Toolkit and the Super Admin, Store, Branch Manager and Cashier modules
**Status:** Done

## 1. What was completed in weeks 1 to 5

| Item | At the Week 1 report | Now (Week 5) |
| --- | --- | --- |
| Redux Toolkit part 1 (11 features) | Done by Vrushay | Done |
| Redux Toolkit part 2 (11 features) and `globleState.js` | In progress | **Done by Subhash** |
| Super Admin module | In progress | **Done by Vrushay** |
| Store module and onboarding | In progress | **Done by Tanya** |
| Branch Manager module | In progress | **Done by Vishvas** |
| Cashier module | In progress | **Done by Vimal** |
| UML, ER and architecture diagrams | Made | Committed to `reports/03-design/` |

Redux Toolkit is now fully done by Subhash and Vrushay together, with 22 features and the global store.

## 2. Redux Toolkit split

| Part | Owner | Features |
| --- | --- | --- |
| Part 1 | Vrushay Bohra | adminDashboard, auth, branch, branchAnalytics, cart, category, customer, employee, inventory, onboarding, order |
| Part 2 | Subhash Dhaka | payment, product, refund, sale, shiftReport, store, storeAnalytics, subscription, subscriptionPlan, transaction, user, and `globleState.js` |

## 3. Frontend modules

| Module | Owner | Pages |
| --- | --- | --- |
| Super Admin | Vrushay Bohra | 6 |
| Store and onboarding | Tanya Singh | 11 |
| Branch Manager | Vishvas Choubisa | 9 |
| Cashier | Vimal Kumar | 5 |

Exact commit counts per member and module are in `frontend_summary.csv`. Run `python3 reports/04-weekly-progress/make_commit_log.py` to refresh them.

## 4. Testing

The Postman testing report (2 parts) and the 96-case test sheet are in `reports/06-testing/`. Running the collection with every role token and recording the results is still in progress.

## 5. What is next

- **A new assignment is coming soon.** The plan for the following weeks will be updated once it is announced.
- Record the Postman results and fix any bugs they show.
- Write the SRS in IEEE format.
- Clean up the known issues listed in the main README.
