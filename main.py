import streamlit as st
import mysql.connector
import pandas as pd
import hashlib

# Database setup, adapt it to your database information
def init_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="sidiki1234&",  
            database="utilisateurs"
        )
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users 
                     (id INT AUTO_INCREMENT PRIMARY KEY, 
                      email VARCHAR(255) UNIQUE, 
                      password VARCHAR(255))''')
        conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")

# Hash password for security for security reasons
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create user
def create_user(email, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="sidiki1234&",  # Replace with your MySQL password
            database="utilisateurs"
        )
        c = conn.cursor()
        c.execute("INSERT INTO users (email, password) VALUES (%s, %s)", 
                 (email, hash_password(password)))
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        st.error(f"Error creating user: {err}")
        return False

# Read all users
def read_users():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="sidiki1234&",  # Replace with your MySQL password
            database="utilisateurs"
        )
        c = conn.cursor()
        c.execute("SELECT id, email FROM users")
        users = c.fetchall()
        conn.close()
        return users
    except mysql.connector.Error as err:
        st.error(f"Error reading users: {err}")
        return []

# Update user
def update_user(id, email, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="sidiki1234&",  # Replace with your MySQL password
            database="utilisateurs"
        )
        c = conn.cursor()
        c.execute("UPDATE users SET email = %s, password = %s WHERE id = %s", 
                 (email, hash_password(password), id))
        conn.commit()
        conn.close()
        return c.rowcount > 0
    except mysql.connector.Error as err:
        st.error(f"Error updating user: {err}")
        return False

# Delete user
def delete_user(id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="sidiki1234&",  # Replace with your MySQL password
            database="utilisateurs"
        )
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id = %s", (id,))
        conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        st.error(f"Error deleting user: {err}")

# Streamlit app
def main():
    st.title("User Management Dashboard")
    
    # Initialize database
    init_db()
    
    # Sidebar menu
    menu = ["Create User", "View Users", "Update User", "Delete User"]
    choice = st.sidebar.selectbox("Select Operation", menu)
    
    # Create User Form
    if choice == "Create User":
        st.subheader("Create New User")
        with st.form("create_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Create User")
            
            if submit:
                if email and password:
                    if create_user(email, password):
                        st.success("User created successfully!")
                    else:
                        st.error("Email already exists or database error!")
                else:
                    st.error("Please fill in all fields!")
    
    # View Users
    elif choice == "View Users":
        st.subheader("All Users")
        users = read_users()
        if users:
            df = pd.DataFrame(users, columns=["ID", "Email"])
            st.dataframe(df)
        else:
            st.info("No users found or database error!")
    
    # Update User Form
    elif choice == "Update User":
        st.subheader("Update User")
        user_id = st.number_input("User ID", min_value=1, step=1)
        with st.form("update_form"):
            email = st.text_input("New Email")
            password = st.text_input("New Password", type="password")
            submit = st.form_submit_button("Update User")
            
            if submit:
                if user_id and email and password:
                    if update_user(user_id, email, password):
                        st.success("User updated successfully!")
                    else:
                        st.error("Update failed! Email might already exist or ID not found.")
                else:
                    st.error("Please fill in all fields!")
    
    # Delete User
    elif choice == "Delete User":
        st.subheader("Delete User")
        user_id = st.number_input("User ID to Delete", min_value=1, step=1)
        if st.button("Delete User"):
            delete_user(user_id)
            st.success("User deleted successfully!")

if __name__ == "__main__":
    main()