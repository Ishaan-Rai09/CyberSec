# 📋 Group 7 — Submission File

> **Instructions:** Every student in this group must fill in their own section below.  
> Do **not** leave any field blank. Replace all placeholder text with real information.  
> This file must be placed inside `student_folder/grp7/group_info.md` before raising your PR.

---

## 🗂️ Project Details

| Field              | Details                          |
|--------------------|----------------------------------|
| **Group Number**   | Group 7                          |
| **Project Name**   | The Vault: Cybersecurity Lab     |
| **Reference Used** | `password_strength` and `minipay`   |
| **Branch Name**    | `grp7-the-vault`                 |

---

## 👥 Student Details

> Each student fills in their own block below. There are 6 blocks — one per member.

---

### 🧑‍💻 Student 1

| Field             | Details                        |
|-------------------|--------------------------------|
| **Full Name**     | Jyoti Dhamija                    |
| **Roll Number**   | [2310991944]                   |
| **GitHub Profile**| @Jyotiiiiiiiii                  |
| **Contribution**  | Implemented the SQL Injection (SQLi) f-string vulnerability and the corresponding Parameterized Query secure patch. |

---

### 🧑‍💻 Student 2

| Field             | Details                        |
|-------------------|--------------------------------|
| **Full Name**     | Kartik Nanda                   |
| **Roll Number**   | [2310991948]                   |
| **GitHub Profile**| @ Kartik941                    |
| **Contribution**  | Designed the AES-256-CFB Encryption Engine (using PyCryptodome) and integrated the data-at-rest protection logic. |

---

### 🧑‍💻 Student 3

| Field             | Details                        |
|-------------------|--------------------------------|
| **Full Name**     | Khushi Panwar                  |
| **Roll Number**   | [2310991956]                   |
| **GitHub Profile**| @[Khushipanwar16]              |
| **Contribution**  | Developed the real-time Password Strength Meter with regex validation.                                    |

---

### 🧑‍💻 Student 4

| Field             | Details                        |
|-------------------|--------------------------------|
| **Full Name**     | Ishaan Rai                     |
| **Roll Number**   | [2310991933]                   |
| **GitHub Profile**| @[Ishaan-Rai09]                |
| **Contribution**  | Created the Cybersecurity Lab Guide tutorial system and the reactive security status badges for the dashboard. |

---

### 🧑‍💻 Student 5

| Field             | Details                        |
|-------------------|--------------------------------|
| **Full Name**     | [Krishiv]                      |
| **Roll Number**   | [2310991961]                   |
| **GitHub Profile**| @[Krishivdawra]                |
| **Contribution**  |Handled user session management, routing logic for security toggles, and final project documentation/README preparation. |

---

### 🧑‍💻 Student 6

| Field             | Details                        |
|-------------------|--------------------------------|
| **Full Name**     | [Manav Taneja]                    |
| **Roll Number**   | [2310991975]                  |
| **GitHub Profile**| @[taneja-manav]               |
| **Contribution**  | Managed the SQLite database schema design and implemented the AuditLog persistence and data retrieval logic.  |

---

## 📝 Project Description

**The Vault** is a high-fidelity cybersecurity demonstration platform designed to teach the "Defense in Depth" principle. Unlike static tutorials, The Vault provides a live environment where users can toggle security layers—such as SQL Injection patching and AES encryption—on and off via a professional dashboard. It focuses on the bridge between data exploitation and the cryptographic defenses required to neutralize data breaches in real-world fintech applications.

---

## 🔐 Security Concepts Implemented

- **SQL Injection (SQLi) & Parameterized Queries:** Demonstrates a login bypass using the payload `admin' --` on an un-sanitized literal f-string query. The secure "Patch" mode replaces this with Parameterized Statements, rendering the input data harmless.
- **AES-256 Symmetric Encryption:** Implements data-at-rest protection using the AES-256-CFB algorithm. This demonstrates how even if a database is breached, the data remains scrambled (ciphertext) and unreadable to the attacker.
- **Forensic Audit Logging:** Implements a permanent database-backed audit trail that records every system action, session state, and user identity (encrypted) to simulate real-world security monitoring.
- **Defense in Depth UI:** Provides a "Cybersecurity Lab Guide" side-by-side with a Data Monitor, allowing users to see exactly how data transforms from "EXPOSED" to "PROTECTED" in real-time.

---

## 📦 Submission Checklist

Before raising your Pull Request, confirm every item below:

- [ ] All group student blocks above are fully filled in
- [x] Project code is structured inside `student_folder/grp7/src/`
- [x] README.md and documentation are present
- [x] Branch name follows format: `grp7-the-vault`
- [x] PR is targeting the `develop` branch — NOT `main`
- [x] No `.env` files or secret keys are committed

---

> 📢 **Reminder:** Only **one person** from the group raises the Pull Request.  
> The branch must be created from `develop` — never from `main`.  
> Branch name format: `grp7-the-vault`
