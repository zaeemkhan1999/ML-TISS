import React from 'react';
import { CircularProgress, Box } from '@mui/material';
import { Doughnut, Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
} from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement);

const Dashboard = () => {
  const doughnutData = {
    labels: ['Normal', 'Worms', 'DoS', 'Backdoor'],
    datasets: [
      {
        data: [48.8, 24.3, 14.6, 12.3],
        backgroundColor: ['#4CAF50', '#FFC107', '#FF5722', '#9C27B0'],
      },
    ],
  };

  const barData = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    datasets: [
      {
        label: 'Packet types',
        data: [200, 400, 300, 500, 100, 200, 300, 400, 200, 100, 300, 500],
        backgroundColor: '#03A9F4',
      },
    ],
  };

  return (
    <div className="min-h-screen bg-blue-900 flex flex-col p-8">
      <div className="flex items-center justify-between mb-8">
        <button className="text-white">&larr; Back</button>
      </div>
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-blue-800 p-4 rounded-lg flex flex-col items-center">
          <h2 className="text-white mb-20 text-4xl">Score</h2>
          <Box position="relative" display="inline-flex">
            <CircularProgress
              variant="determinate"
              value={68}
              size={300}
              thickness={4}
              sx={{ color: '#4CAF50' }}
            />
            <Box
              top={0}
              left={0}
              bottom={0}
              right={0}
              position="absolute"
              display="flex"
              alignItems="center"
              justifyContent="center"
            >
              <span className="text-white text-4xl">68%</span>
            </Box>
          </Box>
        </div>
        <div className="bg-blue-800 p-4 rounded-lg">
          <h2 className="text-white text-center mb-4 text-4xl">Attack Categories</h2>
          <Doughnut data={doughnutData} />
        </div>
        <div className="bg-blue-800 p-4 rounded-lg">
          <h2 className="text-white text-center mb-4 text-4xl">Packet types</h2>
          <Bar width={50} height={50} data={barData} />
        </div>
      </div>
      <div className="bg-blue-800 p-4 mt-8 rounded-lg">
        <h2 className="text-white mb-4 text-4xl">Recommendations</h2>
        {['Oliver Liam', 'Oliver Liam', 'Oliver Liam'].map((name, index) => (
          <div key={index} className="bg-blue-700 p-4 rounded-lg mb-2">
            <h3 className="text-white">{name}</h3>
            <p className="text-blue-300">
              hadjhfjahfjfhajfhjfhajfhjacjbcvnzbbxzcxjcbzjbcxjcjxzjcj
              kfajflkdfdjfafjhjahjfdjhf
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
