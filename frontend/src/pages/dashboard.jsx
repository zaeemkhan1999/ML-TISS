import React, { useContext, useEffect } from 'react';
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
import { MyContext } from '../../context/MyContext';
import { useRouter } from 'next/navigation';

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement);

function getTopAttackCategories(data) {
  const attackArray = Object.keys(data.attack_categories).map(key => ({
      name: key,
      ...data.attack_categories[key]
  }));

  // Filter out the "Normal" attack strategy
  const filteredAttackArray = attackArray.filter(item => item.name !== 'Normal');

  // Sort the array based on the percentage in descending order
  const sortedAttackArray = filteredAttackArray.sort((a, b) => b.percentage - a.percentage);

  // Get the top 3 attack strategies
  const top3Attacks = sortedAttackArray.slice(0, 3);

  return top3Attacks;
}

const Dashboard = () => {

  const {data} = useContext(MyContext);
  const router = useRouter()

  useEffect(() => {
    if (data === null) {
      router.push('/');
    }
  }, [data, router]);

  if (!data) {
    return <p>Loading...</p>;
  }

  const attackData = [
    parseFloat((data.attack_categories.Analysis.percentage).toFixed(2)),
    parseFloat((data.attack_categories.Backdoor.percentage).toFixed(2)),
    parseFloat((data.attack_categories.DoS.percentage).toFixed(2)),
    parseFloat((data.attack_categories.Exploits.percentage).toFixed(2)),
    parseFloat((data.attack_categories.Fuzzers.percentage).toFixed(2)),
    parseFloat((data.attack_categories.Generic.percentage).toFixed(2)),
    parseFloat((data.attack_categories.Normal.percentage).toFixed(2)),
    parseFloat((data.attack_categories.Reconnaissance.percentage).toFixed(2)),
    parseFloat((data.attack_categories.Shellcode.percentage).toFixed(2)),
    parseFloat((data.attack_categories.Worms.percentage).toFixed(2)),
  ]

  const chartData = [
    parseInt((data.attack_categories.Analysis.count).toFixed(2)),
    parseInt((data.attack_categories.Backdoor.count).toFixed(2)),
    parseInt((data.attack_categories.DoS.count).toFixed(2)),
    parseInt((data.attack_categories.Exploits.count).toFixed(2)),
    parseInt((data.attack_categories.Fuzzers.count).toFixed(2)),
    parseInt((data.attack_categories.Generic.count).toFixed(2)),
    parseInt((data.attack_categories.Normal.count).toFixed(2)),
    parseInt((data.attack_categories.Reconnaissance.count).toFixed(2)),
    parseInt((data.attack_categories.Shellcode.count).toFixed(2)),
    parseInt((data.attack_categories.Worms.count).toFixed(2)),
  ]

  const doughnutData = {
    labels: ['Analysis', 'Backdoor', 'DoS', 'Exploits','Fuzzers','Generic','Normal','Reconnaissance','Shellcode','Worms' ],
    datasets: [
      {
        data: attackData,
        backgroundColor: [
          '#4CAF50', // Green
          '#FFC107', // Amber
          '#FF5722', // Deep Orange
          '#9C27B0', // Purple
          '#2196F3', // Blue
          '#FFEB3B', // Yellow
          '#00BCD4', // Cyan
          '#E91E63', // Pink
          '#8BC34A', // Light Green
          '#FF9800'  // Orange
      ],
      },
    ],
  };

  const barData = {
    labels: ['Analysis', 'Backdoor', 'DoS', 'Exploits','Fuzzers','Generic','Normal','Reconnaissance','Shellcode','Worms' ],
    datasets: [
      {
        label: 'Packet types',
        data: chartData,
        backgroundColor: '#03A9F4',
      },
    ],
  };

  const recommanationArray = getTopAttackCategories(data);

  

  

  return (
    <div className="p-6 bg-custom-gradient">
      <div className="min-h-screen backdrop-blur-3xl border border-white flex flex-col p-8 rounded-lg ">
      <div className="flex items-center justify-between mb-8">
        <button className="text-white" onClick={() => router.push("/")}>&larr; Back</button>
      </div>
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-box-gradient p-4 rounded-lg flex flex-col items-center">
          <h2 className="text-white mb-20 text-4xl">Score</h2>
          <Box position="relative" display="inline-flex">
            <CircularProgress
              variant="determinate"
              value={data.mean_cvss_score / 10 * 100}
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
              <span className="text-white text-4xl">{(data.mean_cvss_score / 10 * 100).toFixed(2)}%</span>
            </Box>
          </Box>
        </div>
        <div className="bg-box-gradient p-4 rounded-lg">
          <h2 className="text-white text-center mb-4 text-4xl">Attack Categories</h2>
          <Doughnut className='text-white' data={doughnutData} />
        </div>
        <div className="bg-box-gradient p-4 rounded-lg">
          <h2 className="text-white text-center mb-4 text-4xl">Packet types</h2>
          <Bar width={50} height={50} data={barData} />
        </div>
      </div>
      <div className="bg-box-gradient p-4 mt-8 rounded-lg">
        <h2 className="text-white mb-4 text-4xl">Recommendations</h2>

        
        {recommanationArray.map((attack, index) => (
          <div key={index} className="bg-innerbox-gradient p-4 rounded-lg mb-2">
            <h3 className="text-white">{attack.name}</h3>
            <p className="text-white">{attack.recommendation}</p>
          </div>
        ))}


            </div>
    </div>
    </div>
    
  );
};

export default Dashboard;
