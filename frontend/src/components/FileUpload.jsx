import React, { useContext, useState } from 'react';
import axios from 'axios';
import { useRouter } from 'next/navigation'
import { MyContext } from '../../context/MyContext';
import ProgressBar from "@ramonak/react-progress-bar";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [progress, setProgress] = useState(0);
  const {data, setData} = useContext(MyContext);

  const router = useRouter()

  const onFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const onFileUpload = () => {
    const api = process.env.NEXT_PUBLIC_API_URL;

    console.log(api);
    const formData = new FormData();
    formData.append('file', file);

    axios.post(`${process.env.NEXT_PUBLIC_API_URL}/upload`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress: (progressEvent) => {
        setProgress(Math.round((progressEvent.loaded * 100) / progressEvent.total));
      },
    })
    .then((response) => {
      
      setData(response.data);
      
      router.push("/dashboard")
    })
    .catch((error) => {
      console.error('Error uploading file:', error);
    });
  };

  return (
    <div className='flex flex-col gap-5'>
      <h2 className='font-bold'>Upload your CSV</h2>
      <input className='bg-white text-black p-4 rounded-lg mr-2' type="file" onChange={onFileChange} />
      <button disabled={!file} className='bg-white text-black px-5 py-3 rounded-lg' onClick={onFileUpload}>Upload!</button>
      
      {
        file && (
          <div>
        <p>Progress: {progress}%</p>
      <ProgressBar completed={progress} />
      </div>
        )
      }
    </div>
  );
};

export default FileUpload;
