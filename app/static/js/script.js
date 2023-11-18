document.addEventListener('DOMContentLoaded', function () {
    const presidentialTable = document.getElementById("presidential-table");
    const partyTotals = {
        Democrat: 0,
        Republican: 0,
        Independent: 0
    };

    // Add event listener for party selection
    presidentialTable.addEventListener('change', function (e) {
        if (e.target.classList.contains('party-select')) {
            console.log("Party selected:", e.target.value);
            updateTableColorsAndTotals(e.target.parentElement.parentElement);
            updateTotalVotes();
        }
    });

   // Function to update table cell colors
function updateTableColorsAndTotals(row) {
    const selectedParty = row.querySelector('.party-select').value;
    // Remove the existing class on the row
    row.classList.remove('party-Democrat', 'party-Republican', 'party-Independent');
    // Add the selected party class to change the color
    row.classList.add(`party-${selectedParty}`);
    
    // Set the data-party attribute on the row
    row.setAttribute('data-party', selectedParty);
}

    // Function to update total votes for each party
function updateTotalVotes() {
    console.log("Updating total votes");

    // Initialize partyTotals
    const partyTotals = {
        Democrat: 0,
        Republican: 0,
        Independent: 0
    };

    // Loop through rows to calculate total votes
    const rows = presidentialTable.querySelectorAll('tbody tr');
    rows.forEach(row => {
        const selectedParty = row.getAttribute('data-party');
        const electoralVotes = parseInt(row.querySelector('td[data-electoral-votes]').textContent);
        partyTotals[selectedParty] += electoralVotes;
    });

    // Update total vote elements and hidden field
    const hiddenField = document.querySelector('input[name="results"]');
    if (hiddenField) {
        // Initialize the results string
        let totalResults = 'Total Election Results:\n\nPresidential\n\n';

        // Update total vote elements and add to the results string
        for (const party in partyTotals) {
            const totalElement = document.getElementById(`presidential-total-${party}`);
            if (totalElement) {
                totalElement.textContent = partyTotals[party];
                totalResults += `Total (${party}): ${partyTotals[party]}\n`;
            } else {
                console.error(`Total element not found for party: ${party}`);
            }
        }

        // Update the hidden field with the total results
        hiddenField.value = totalResults.trim();
    } else {
        console.error('Hidden field not found.');
    }
}


    // Function to update the hidden field with the total results
    function updateHiddenField() {
        const democratTotal = document.getElementById("presidential-total-Democrat").textContent;
        const independentTotal = document.getElementById("presidential-total-Independent").textContent;
        const republicanTotal = document.getElementById("presidential-total-Republican").textContent;

        const totalResults = `Total Election Results:\n\nPresidential\n\nTotal (Democrat): ${democratTotal}\nTotal (Independent): ${independentTotal}\nTotal (Republican): ${republicanTotal}`;

        // Update the hidden field with the total results
        document.querySelector('input[name="results"]').value = totalResults;
    }

    console.log("Democrat Total Element:", document.getElementById("presidential-total-Democrat"));
    console.log("Independent Total Element:", document.getElementById("presidential-total-Independent"));
    console.log("Republican Total Element:", document.getElementById("presidential-total-Republican"));
});
