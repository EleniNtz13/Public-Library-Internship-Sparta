$(document).ready(function () { // Execute the function when the DOM is fully loaded
    $("#id_titlos").on("keyup", function () { // Attach a keyup event listener to the title input field
        let query = $(this).val(); // Get the current value of the input field
        if (query.length < 2) return; // Exit early if the query is shorter than 2 characters

        $.ajax({ // Perform an AJAX request
            url: "/ajax/autocomplete/title/", // Define the server endpoint for autocomplete
            data: { q: query }, // Send the query parameter to the server
            success: function (data) { // Execute this function if the request is successful
                let box = $("#title-suggestions"); // Select the suggestion container element
                box.empty(); // Clear any existing suggestions
                data.results.forEach(item => { // Loop through each result returned from the server
                    box.append(`<div class="suggestion-item">${item}</div>`); // Add each suggestion as a div element
                });

                $(".suggestion-item").click(function () { // Attach a click handler to each suggestion item
                    $("#id_titlos").val($(this).text()); // Set the input value to the clicked suggestion text
                    box.empty(); // Clear the suggestion box after selection
                });
            }
        });
    });
});
