function createUser(userData) {
    fetch('/create/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken') // if CSRF is enabled
      },
      body: JSON.stringify(userData)
    })
    .then(async (response) => {
      const data = await response.json();
  
      if (!response.ok) {
        // Show validation or server-side errors
        console.error('Error:', data.errors || data.message);
        alert('Error: ' + JSON.stringify(data.errors || data.message));
      } else {
        // Success
        console.log('Success:', data);
        alert('User created successfully!');
      }
    })
    .catch((error) => {
      console.error('Fetch error:', error);
      alert('Network or server error: ' + error.message);
    });
  }
  
  // Example user data
  const userData = {
    user_role: "Employee",
    user_name: "John Doe",
    department: "Tech",
    email_id: "john@example.com",
    is_active: true,
    is_locked: false,
    employee_id: "EMP123",
    designation: "Developer",
    mobile_number: "1234567890",
    remarks1: "Testing",
    remarks2: "Optional"
  };
  
  createUser(userData);
  