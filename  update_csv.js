const fs = require('fs');
const csv = require('csv-parser');
const { parse } = require('json2csv');

// Path to the CSV file
const csvFilePath = './data.csv';

// Function to read the CSV file
function readCsv(filePath) {
    return new Promise((resolve, reject) => {
        const results = [];
        fs.createReadStream(filePath)
            .pipe(csv())
            .on('data', (data) => results.push(data))
            .on('end', () => resolve(results))
            .on('error', (err) => reject(err));
    });
}

// Function to add a new item to the CSV file
async function addNewItem(newItem) {
    try {
        // Read the existing data
        const data = await readCsv(csvFilePath);
        data.push(newItem); // Add the new item

        // Convert data back to CSV format
        const updatedCsv = parse(data);

        // Write updated data back to the CSV file
        fs.writeFileSync(csvFilePath, updatedCsv);
        console.log('New item added to the CSV file!');
    } catch (error) {
        console.error('Error updating the CSV file:', error);
    }
}

// Example usage
const newItem = { Time: 11, ItemsAdded: 10000 };
addNewItem(newItem);
