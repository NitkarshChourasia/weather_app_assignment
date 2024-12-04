
// async function deleteLog(log_id) {
//     // Confirm with the user before proceeding
//     const confirmDelete = confirm("Are you sure you want to delete this log?");
//     if (!confirmDelete) return;

//     try {
//         // Make the DELETE request
//         const response = async fetch(`http://127.0.0.1:5000/delete_log/${log_id}`);

//         // Check if the request was successful
//         if (response.ok) {
//             alert("Log deleted successfully!");
//             location.reload(); // Reload the page only if successful
//         } else {
//             const errorData = async response.json();
//             alert(`Error: ${errorData.message || "Failed to delete the log."}`);
//         }
//     } catch (error) {
//         console.error("Error deleting log:", error);
//         alert("An unexpected error occurred. Please try again.");
//     }
// }
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".btn-delete").forEach((button) => {
        button.addEventListener("click", (event) => {
            let log_id = button.getAttribute("data-log-id");
            deleteLog(log_id);
        });
    });
});


// .then(response => response.json())
// .then(data => {
//     // Handle success or failure
//     location.reload();
// })
// .catch(error => {
//     // Handle error
//     console.error('Error:', error);
// });

function deleteLog(log_id) {
    // Retrieve the CSRF token from the meta tag
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    fetch(`/delete_log/${log_id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken // Include the CSRF token in the headers
        },
        body: JSON.stringify({
            log_id: log_id
        })
    }).then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                // Successfully deleted, refresh the page or remove the log row
                document.getElementById(log_id).remove(); // Remove the log row
                location.reload();
            }
        })
    //         .then(response => response.json())
    //         .then(data => {
    //             if (data.status === "success") {
    //                 // Successfully deleted, refresh the page or remove the log row
    //                 // document.getElementById(log_id).remove(); // Remove the log row
    //                 // location.reload();
    //             } else {
    //                 alert('Error deleting log');
    //             }
    //         })
    //         .catch(error => {
    //             console.error('Error:', error);
    //         });
}


function toggleNightMode() {
    document.body.classList.toggle("night-mode");
}

// http://127.0.0.1:5000/add_log_weather?

document.getElementById("confirm-clear-button").addEventListener("click", () => {
    clearAllLogs(); // Function to clear all logs
    closeModal(); // Hide the modal after confirmation
});

// Event listener for Clear All Logs button
document.getElementById("clear-all-logs-btn").addEventListener("click", () => {
    document.getElementById("confirmation-modal").style.display = "block";
});

// Event listener for confirming clearing all logs
document.getElementById("confirm-clear-button").addEventListener("click", () => {
    clearAllLogs(); // Function to clear all logs
    closeModal(); // Hide the modal after confirmation
});


// Close the modal
function closeModal() {
    document.getElementById("confirmation-modal").style.display = "none";
}


// Function to clear all logs
function clearAllLogs() {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    fetch(`http://127.0.0.1:5000/delete_all_logs`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                location.reload(); // Reload the page after successful deletion of all logs
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}