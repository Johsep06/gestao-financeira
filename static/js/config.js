var year = 2024;

async function getYear() {
    try {
        const response = await fetch('/year');
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        year = data.year;
    } catch (error) {
        console.error('Error fetching variable:', error);
    }
}

function addYear(){
    this.year += 1;
    console.log(this.year);
}

function subYear() {
    year -= 1;
    console.log(year);
}