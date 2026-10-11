# Frontend Work Log

Who built which part of the frontend (`pos-frontend-vite/`). The commit data below is from the team history up to 10 Oct 2026. Run `python3 reports/04-weekly-progress/make_commit_log.py` for the latest numbers. It writes `frontend_work_log.csv` and `frontend_summary.csv` from Git.

## 1. Modules and owners

| Member | GitHub | Module | Pages | Status |
| --- | --- | --- | --- | --- |
| Vrushay Bohra | bohra0022 | Redux Toolkit part 1, frontend setup, Super Admin module, routing | 11 Redux features, API client, utils, 6 Super Admin pages | Done |
| Subhash Dhaka | subhash8729 | Frontend folder structure, Redux Toolkit part 2 | payment, product, refund, sale, shiftReport, store, storeAnalytics, subscription, subscriptionPlan, transaction, user, `globleState.js` | In progress |
| Vimal Kumar | iamvkb7 | Cashier | Create order (POS), orders, returns, customers, shift summary | Done |
| Vishvas Choubisa | choubisavishvas-web | Branch Manager | Dashboard, orders, refunds, transactions, inventory, employees, customers, reports, settings | Done |
| Tanya Singh | tanyasingh077 | Store (the largest module) and onboarding | Dashboard, branches, categories, employees, products, stores, sales, reports, upgrade, settings, alerts | Done |

The Store module has 11 pages, so it is the largest. Branch Manager has 9, Super Admin has 6, and Cashier has 5.

## 2. Redux Toolkit split

| Part | Owner | Features |
| --- | --- | --- |
| Part 1 | Vrushay Bohra | adminDashboard, auth, branch, branchAnalytics, cart, category, customer, employee, inventory, onboarding, order |
| Part 2 | Subhash Dhaka | payment, product, refund, sale, shiftReport, store, storeAnalytics, subscription, subscriptionPlan, transaction, user, and `globleState.js` (in progress) |

## 3. Commits by member and module (from Git, 10 Oct 2026)

These numbers come from `frontend_summary.csv`, which `make_commit_log.py` builds from the Git history.

| Member | Module | Frontend commits |
| --- | --- | --- |
| Vrushay Bohra | Super Admin | 26 |
| Vrushay Bohra | Redux Toolkit | 12 |
| Vrushay Bohra | Setup and shared | 6 |
| Vrushay Bohra | Routing | 1 |
| Vimal Kumar | Cashier | 40 |
| Vishvas Choubisa | Branch Manager | 35 |
| Tanya Singh | Store | 8 |
| Tanya Singh | Auth and onboarding | 3 |
| Subhash Dhaka | Setup and shared | 2 |
| Subhash Dhaka | Redux Toolkit | 1 |
| **Total** | | **134** |

| Member | Frontend commits |
| --- | --- |
| Vrushay Bohra | 45 |
| Vimal Kumar | 40 |
| Vishvas Choubisa | 35 |
| Tanya Singh | 11 |
| Subhash Dhaka | 3 |

The Super Admin module was committed by Vrushay Bohra (24 files, plus an index fix and a README fix). Redux Toolkit part 2 and `globleState.js` are still to be pushed. For the latest numbers, run the script again.

## 4. Testing log

| Item | Owner | File | Status |
| --- | --- | --- | --- |
| Postman testing report (2 parts) | Vrushay Bohra | `reports/06-testing/POSTMAN_TESTING_API.md` | Done |
| API test case sheet (96 cases) | Vrushay Bohra | `reports/06-testing/POS_Backend_Test_Cases.xlsx` | Written, results to record |
| Run the collection with all role tokens and record results | Whole team | Postman | In progress |
| Negative and security tests | Vrushay Bohra | test case sheet | Written, to run |
| Frontend checks of each module | Module owners | each module's pages | In progress |
