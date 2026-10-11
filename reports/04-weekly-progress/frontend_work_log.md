# Frontend Work Log

Who built which part of the frontend (`pos-frontend-vite/`). The commit data below is from the team history up to 10 Oct 2026. Run `python3 reports/04-weekly-progress/make_commit_log.py` for the latest numbers. It writes `frontend_work_log.csv` and `frontend_summary.csv` from Git.

## 1. Modules and owners

| Member | GitHub | Module | Pages | Status |
| --- | --- | --- | --- | --- |
| Vrushay Bohra | bohra0022 | Redux Toolkit part 1, frontend setup, Super Admin (with Subhash) | 11 Redux features, API client, utils | Done |
| Subhash Dhaka | subhash8729 | Frontend folder structure, Redux Toolkit part 2, Super Admin (with Vrushay) | Dashboard, stores, store details, pending requests, subscription plans, settings | Done |
| Vimal Kumar | iamvkb7 | Cashier | Create order (POS), orders, returns, customers, shift summary | Done |
| Vishvas Choubisa | choubisavishvas-web | Branch Manager | Dashboard, orders, refunds, transactions, inventory, employees, customers, reports, settings | Done |
| Tanya Singh | tanyasingh077 | Store (the largest module) and onboarding | Dashboard, branches, categories, employees, products, stores, sales, reports, upgrade, settings, alerts | Done |

The Store module has 11 pages, so it is the largest. Branch Manager has 9, Super Admin has 6, and Cashier has 5.

## 2. Redux Toolkit split

| Part | Owner | Features |
| --- | --- | --- |
| Part 1 | Vrushay Bohra | adminDashboard, auth, branch, branchAnalytics, cart, category, customer, employee, inventory, onboarding, order |
| Part 2 | Subhash Dhaka | payment, product, refund, sale, shiftReport, store, storeAnalytics, subscription, subscriptionPlan, transaction, user, and `globleState.js` |

## 3. Commits so far, by member

| Member | Commits | What they added |
| --- | --- | --- |
| Vrushay Bohra | `dbcae3a`, `7ab1196`, `0abb5fc`, `06b282a`, `09a4708`, `26e7b01`, `8d7cd95`, `b04b449`, `ed775da`, `e426064`, `c579b5a`, `9809d35` | Frontend config, API client and utils, and 11 Redux Toolkit features |
| Subhash Dhaka | `ddf392b`, `751e82d` | Frontend folder structure |
| Vimal Kumar | `3d1187e`, `deff443`, `655d718`, `2d48633`, `7974ef5`, `7faddd4`, `76a311a` | Cashier sidebar pages, cart and components |
| Vishvas Choubisa | `3197520`, `bb95311`, `db9c60b` | Branch Manager customer pages, dashboard and cashier performance |
| Tanya Singh | `7307504` | Onboarding owner details page |

Super Admin commits go to the team repo and show up in `frontend_work_log.csv` under the Super Admin module.

## 4. Testing log

| Item | Owner | File | Status |
| --- | --- | --- | --- |
| Postman testing report (2 parts) | Vrushay Bohra | `reports/06-testing/POSTMAN_TESTING_API.md` | Done |
| API test case sheet (96 cases) | Vrushay Bohra | `reports/06-testing/POS_Backend_Test_Cases.xlsx` | Written, results to record |
| Run the collection with all role tokens and record results | Whole team | Postman | In progress |
| Negative and security tests | Vrushay Bohra | test case sheet | Written, to run |
| Frontend checks of each module | Module owners | each module's pages | In progress |
