document.getElementById("sendButton").addEventListener("click", function() {
    // Send an HTTP request to the server to retrieve the random message
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://localhost:5000/get_random_message", true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // Display the random message in the alert dialog
        alert(xhr.responseText);
      }
    };
    xhr.send();
  });
  