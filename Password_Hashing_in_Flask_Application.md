# Password Hashing in Flask Application

## Introduction

In the provided Flask application, password hashing is utilized to store and manage user passwords securely. Rather than storing passwords in plain text, which could be vulnerable to data breaches, hashing ensures that even if the database or JSON file is compromised, the actual passwords are not exposed. This process helps protect user data and adheres to best security practices.

## Why Use Password Hashing?

1. **Security**: Storing passwords as plain text can easily lead to data leaks if someone gains unauthorized access to the database or files. Hashing converts the password into a fixed-length string that is not easily reversible, making it significantly harder for attackers to recover the original password.

2. **Irreversible Process**: Hashing is a one-way process, meaning once a password is hashed, it cannot be converted back into its original form. This makes it secure even if attackers gain access to the hashed values.

3. **Salting for Extra Security**: By adding a salt to the hash (a unique random string), even if two users have the same password, they will have different hashes, further enhancing security.

4. **Compliance with Security Standards**: Password hashing helps ensure that applications meet security standards and guidelines such as those provided by OWASP (Open Web Application Security Project).

## How Password Hashing Works in This Flask Application

In the given application, password hashing is implemented during the user registration process when new users are created. Here's how it works:

### Step-by-Step Process for Hashing the Password

1. **User Registration**:
   - When a user attempts to register, they submit their desired username and password through a form. The password is then validated to ensure it meets strength requirements (including length, uppercase, lowercase, numeric, and special character).
   - If the password passes the validation, it is then hashed using the `bcrypt` hashing algorithm, which is a popular and secure algorithm specifically designed for password storage.

2. **Hashing with bcrypt**:
   - The password is hashed using the `bcrypt.generate_password_hash()` method, which produces a secure hash. The hash is stored in the application's data (in this case, the `users.json` file).
   - The password hash is then stored along with the username in the file. The original password is never saved.

3. **How It is Stored**:
   - The hashed password is saved in a dictionary along with the username, and this data is written to a JSON file using the `write_users_to_json()` function. This ensures that only the hashed password is stored, not the plain text password.

   ```python
   hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
   users.append({"username": username, "password": hashed_password})
   write_users_to_json(users)
   ```

### Why Is This Approach Useful?

1. **Prevents Plaintext Password Storage**:
   - Storing passwords in plaintext would make them easily accessible to anyone who gains access to the application’s data storage (in this case, the `users.json` file). By hashing the passwords, even if an attacker gains access to the file, they won’t be able to retrieve the original passwords.

2. **Secure User Authentication**:
   - When a user logs in, their submitted password is hashed again and compared to the stored hash. This ensures that the password verification process doesn't require storing or transmitting the plaintext password at any point.
   - The following code checks if the provided password matches the stored hash:

   ```python
   if bcrypt.check_password_hash(user["password"], password):
       session["username"] = username
       return redirect("/dashboard")
   ```

3. **Compliance and Best Practices**:
   - Using bcrypt for hashing is an industry-standard approach. bcrypt is a strong hashing algorithm specifically designed to slow down brute-force attacks, making it more resistant to cracking attempts compared to simpler hashing algorithms like MD5 or SHA-1.
   
4. **Mitigates Common Security Threats**:
   - By using bcrypt, the application mitigates threats such as rainbow table attacks (precomputed hash attacks) by automatically adding a salt to each password before hashing, making each password hash unique even for identical passwords.

## Conclusion

In summary, by using password hashing with bcrypt, this Flask application enhances security by ensuring that passwords are stored in a secure, non-reversible format. This method protects user data, even in the event of a database breach, and follows industry-standard security practices to safeguard sensitive information.