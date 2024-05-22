import FileUpload from "@/components/FileUpload";
import Head from "next/head";

export default function Home() {
  return (
    <div className="relative min-h-screen bg-no-repeat bg-cover" style={{ backgroundImage: "url('/homebg.png')"}}>
      <Head>
        <title>Secure File Upload</title>
      </Head>

      <div className="absolute inset-0 bg-purple-900 bg-opacity-50 flex items-center">
        <div className="bg-purple-900 bg-opacity-10 p-8 rounded-lg shadow-lg mb-80 mr-12 w-11/12 min-h-[40vh]">
          <h1 className="text-white bg-opacity-90 text-2xl mb-2">Nice to see you!</h1>
          <p className="text-white bg-opacity-90 mb-4">Make the world secure place</p>
          <FileUpload />
        </div>
      </div>
    </div>
  );
}
