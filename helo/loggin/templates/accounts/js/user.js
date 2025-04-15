// Example create user
function createUser(data) {
    axios.post('/api/create/', data)
      .then(response => {
        console.log(response.status); // 201
        alert('User created successfully!');
        window.location.reload();
      })
      .catch(error => {
        console.error(error.response.data);
        alert('Error: ' + JSON.stringify(error.response.data));
      });
  }
  
  // Example update user
  function updateUser(pk, data) {
    axios.put(`/api/update/${pk}/`, data)
      .then(response => {
        console.log(response.status); // 200
        alert('User updated!');
      })
      .catch(error => {
        console.error(error.response.data);
        alert('Error: ' + JSON.stringify(error.response.data));
      });
  }
  
  // Example delete user
  function deleteUser(pk) {
    axios.delete(`/api/delete/${pk}/`)
      .then(response => {
        console.log(response.status); // 200
        alert('User deleted!');
        window.location.reload();
      })
      .catch(error => {
        console.error(error);
        alert('Error deleting user');
      });
  }
  