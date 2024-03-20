document.addEventListener("DOMContentLoaded", function() {
    // Select the Send button element
    const sendButton = document.getElementById("sendButton");
  
    // Add an event listener to the Send button
    sendButton.addEventListener("click", function() {
      // Make an HTTP GET request to the server to get a random message
      fetch("/get_random_message")
        .then(response => response.text())
        .then(message => {
          // Display the random message
          alert(message);
        })
        .catch(error => {
          console.error("Error fetching random message:", error);
        });
    });
  });
  