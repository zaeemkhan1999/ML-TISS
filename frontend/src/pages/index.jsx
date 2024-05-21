import Head from "next/head";
import Image from 'next/image'
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <div className="relative min-h-screen bg-no-repeat bg-cover" style={{ backgroundImage: "url('/homebg.png')" }}>
      <Head>
        <title>Secure File Upload</title>
      </Head>

      <div className="absolute inset-0 bg-purple-900 bg-opacity-50 flex items-center">
        <div className="bg-purple-900 bg-opacity-10 p-8 rounded-lg shadow-lg mb-80 mr-12 w-11/12 min-h-[40vh]">
          <h1 className="text-white bg-opacity-90 text-2xl mb-2">Nice to see you!</h1>
          <p className="text-white bg-opacity-90 mb-4">Make the world secure place</p>
          <p className="text-white bg-opacity-90 mb-1">upload</p>
          <div className="inline-block">
            <label className="bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-300 cursor-pointer">
              Upload
              <input type="file" className="hidden" />
            </label>
          </div>
        </div>
      </div>
    </div>
  );
}
