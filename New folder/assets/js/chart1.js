const ctx = document.getElementById('lineChart').getContext('2d');
let myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'],
        datasets: [{
            label: '# of appoinments',
            data: [20, 15, 23, 25, 12, 7],
            backgroundColor: [
                'rgba(35,35,228,1.0)'
                // 'rgba(255, 150, 182, 0.2)',
                // 'rgba(54, 202, 255, 0.2)',
                // 'rgba(255, 206, 136, 0.2)',
                // 'rgba(125, 242, 242, 0.2)',
                // 'rgba(253, 152, 255, 0.2)',
                // 'rgba(255, 209, 114, 0.2)'
            ],
            borderColor: [
                'rgb(35, 35, 228)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
       responsive: true,

    }
});


const ctx_1 = document.getElementById('doughnut').getContext('2d');
const myChart_1 = new Chart(ctx_1, {
    type: 'doughnut',
    data: {
        labels: ['OPD', 'Eye Clinic', 'ENT', 'Pediatric', 'Dental Clinic', 'Ward'],
        datasets: [{
            label: '# of patients',
            data: [24, 20, 22, 25, 15, 17],
            backgroundColor: [
                'rgba(35,35,228,1.0)',
                'rgba(255, 150, 182, 0.2)',
                'rgba(80, 150, 255, 0.2)',
                'rgba(255, 180, 136, 0.2)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)'
                // 'rgba(255, 209, 114, 0.2)'
            ],
            borderColor: [
                'rgba(35,35,228,1.0)',
                'rgba(255, 150, 182, 0.2)',
                'rgba(80, 150, 255, 0.2)',
                'rgba(255, 180, 136, 0.2)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)'
                // 'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
       responsive: true,

    }
});