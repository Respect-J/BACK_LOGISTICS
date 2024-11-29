# Legacy Authentication and User Management

## Overview

This project implements a comprehensive user authentication and management system for the Legacy project. It includes registration, email verification, role-based access control, password reset, and more.

---

## Features

### 1. **User Registration**
   - Users can register using their email, username, and password.
   - A 5-digit email verification code is sent to the user after registration.
   - Accounts remain inactive until the email is verified.

### 2. **Email Verification**
   - Users verify their accounts by submitting the verification code sent to their email.
   - Upon successful verification:
     - The account is activated.
     - An access token and the user ID are returned for immediate authentication.

### 3. **Login**
   - Users log in using their email and password.
   - Only verified accounts can log in.

### 4. **Password Reset**
   - Users can request a password reset via email.
   - A 5-digit reset code is sent to the user's email.
   - Users submit the reset code and a new password to complete the process.

### 5. **Role-Based Access Control**
   - Roles available:
     - **Client** (default)
     - **Salesperson**
     - **Logistician**
   - Super admin can assign roles to users during creation or editing via the admin panel.
   - Users can be filtered and managed by role in the admin interface.

---

## API Endpoints

### Registration and Verification
| Endpoint              | Method | Description                                  |
|-----------------------|--------|----------------------------------------------|
| `/register/`          | POST   | Register a new user.                        |
| `/verify-email/`      | POST   | Verify email with a 5-digit code.           |

### Authentication
| Endpoint              | Method | Description                                  |
|-----------------------|--------|----------------------------------------------|
| `/login/`             | POST   | Log in with email and password.             |

### Password Reset
| Endpoint                    | Method | Description                             |
|-----------------------------|--------|-----------------------------------------|
| `/password-reset-request/`  | POST   | Request a password reset code.         |
| `/password-reset-confirm/`  | POST   | Confirm the reset code and set a new password. |

---

## Admin Features

- Assign roles during user creation.
- Filter users by roles in the admin panel.
- Edit user roles directly from the user list.

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Configure email settings in `settings.py`:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your_email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your_password'
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

---

## Testing

### Email Verification Flow
1. Register a new user via `/register/`.
2. Check the email for the 5-digit code.
3. Verify the code via `/verify-email/`.

### Password Reset Flow
1. Request a reset code via `/password-reset-request/`.
2. Check the email for the reset code.
3. Submit the code and new password via `/password-reset-confirm/`.

---

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

---

Этот README дает полное представление о проекте и его функциональности, включая API, инструкции по установке и описания ключевых возможностей. Если требуется что-то добавить или изменить, дайте знать!
